from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.GameFormatModel import GameFormatModel
from models.TournamentModel import TournamentModel

from helpers import *

GAME_FORMAT_LENGTH_CONFIG = {
    'name': {'min': 1, 'max':50}
}

REQUIRED_FIELDS = ['name']

gameFormatController = Blueprint('format', __name__)

def GetConnection():
    connection = getattr(gameFormatController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Player')
    
    return connection

@gameFormatController.route('/formats', methods=['POST'])
def CreateFormat():
    connection = GetConnection()
    userModel = UserModel(connection)
    
    recievedData, error, statusCode = JsonExists(request)
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401

    if error == '':
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400
    
    if error == '':
        cleanData = ValidateGameFormatData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Formatos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        gameFormatModel = GameFormatModel(connection)
        if gameFormatModel.GetFormatByName(cleanData['name']) is not None:
            error = 'El formato ya está registrado'
            statusCode = 400
    
    if error == '':
        created = gameFormatModel.CreateFormat(cleanData)
        if created is False:
            error = "Hubo un error al crear el formato"
            statusCode = 500
        else:
            action = 'Creó el formato {0}'.format(cleanData['name'])
            gameFormatModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Formato creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@gameFormatController.route('/formats', methods=['GET'])
def GetFormats():
    connection = GetConnection()
    gameFormatModel = GameFormatModel(connection)
    response = {}
    statusCode = 200

    formats = gameFormatModel.GetFormats()
    response = {
        'success': True,
        'formats': formats
    }

    return jsonify(response), statusCode


@gameFormatController.route('/formats/<int:formatId>', methods=['GET'])
def GetGameFormatById(formatId):
    connection = GetConnection()
    gameFormatModel = GameFormatModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetFormat = gameFormatModel.GetFormatById(formatId)
        if targetFormat is None:
            error = 'Formato no encontrado'
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['format'] = targetFormat
    else:
        response['message'] = error

    return jsonify(response), statusCode


@gameFormatController.route('/formats/<int:formatId>', methods=['PUT'])
def UpdateFormat(formatId):
    connection = GetConnection()
    userModel = UserModel(connection)
    
    recievedData, error, statusCode = JsonExists(request)
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401

    if error == '':
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400
    
    if error == '':
        cleanData = ValidateGameFormatData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Formatos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        gameFormatModel = GameFormatModel(connection)
        targetFormat = gameFormatModel.GetFormatById(formatId)
        if targetFormat is None:
            error = 'Formato no encontrado'
            statusCode = 404  # Not found

    if error == '':
        if gameFormatModel.GetFormatByName(cleanData['name']) is not None:
            error = 'Ya existe un formato con ese nombre'
            statusCode = 400

    if error == '':
        updated = gameFormatModel.UpdateFormat(formatId, cleanData)
        if updated is False:
            error = "Hubo un error al renombrar el formato"
            statusCode = 500
        else:
            action = 'Renombró el formato "{0}" por "{1}" '.format(targetFormat['name'], cleanData['name'])
            gameFormatModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Formato renombrado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@gameFormatController.route('/formats/<int:formatId>', methods=['DELETE'])
def DeleteFormat(formatId):
    connection = GetConnection()
    userModel = UserModel(connection)
    error = ''
    statusCode = 200
    
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401

    if error == '':
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Formatos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        gameFormatModel = GameFormatModel(connection)
        targetFormat = gameFormatModel.GetFormatById(formatId)
        if targetFormat is None:
            error = 'Formato no encontrado'
            statusCode = 404  # Not found

    if error == '':
        tournamentModel = TournamentModel(connection)
        formatTournaments = tournamentModel.GetTournamentsOfFormat(formatId)
        if len(formatTournaments) > 0:
            # The format is registered in almost one tournament, then, it can't be deleted
            error = 'No se pueden borrar formatos si se hizo al menos un torneo sobre este'
            statusCode = 400

    if error == '':
        deleted = gameFormatModel.DeleteFormat(formatId)
        if deleted is False:
            error = "Hubo un error al eliminar el formato"
            statusCode = 500
        else:
            action = 'Eliminó el formato "{0}"'.format(targetFormat['name'])
            gameFormatModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Formato eliminado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateGameFormatData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(GAME_FORMAT_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error