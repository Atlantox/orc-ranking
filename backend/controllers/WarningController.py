from flask import Blueprint, request, jsonify

from models.SeasonModel import SeasonModel
from models.WarningModel import WarningModel
from models.PlayerModel import PlayerModel
from models.UserModel import UserModel

from helpers import *

WARNING_LENGTH_CONFIG = {
    'reason': {'min':5, 'max':255},
    'date': {'min':8, 'max':10},
}

REQUIRED_FIELDS = ['reason', 'season', 'date', 'player']

warningController = Blueprint('warning', __name__)

def GetConnection():
    connection = getattr(warningController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Warning')
    
    return connection

@warningController.route('/warnings', methods=['POST'])
def CreateWarning():
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
        cleanData = ValidateWarningData(recievedData)        
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Warnings') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        playerModel = PlayerModel(connection)
        targetPlayer = playerModel.GetPlayerById(cleanData['player'])
        if targetPlayer is None:
            error = 'El jugador escogido no existe'
            statusCode = 400

    if error == '':
        seasonModel = SeasonModel(connection)
        if seasonModel.GetSeasonById(cleanData['season']) is None:
            error = 'La temporada escogida no existe'
            statusCode = 400
    
    if error == '':
        warningModel = WarningModel(connection)
        created = warningModel.CreateWarning(cleanData)
        if created is False:
            error = "Hubo un error al crear el warning"
            statusCode = 500
        else:
            action = 'Creó el warning al jugador {0} por motivo {1}'.format(targetPlayer['name'], cleanData['reason'])
            warningModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Warning creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@warningController.route('/warnings', methods=['GET'])
def GetWarnings():
    connection = GetConnection()
    warningModel = WarningModel(connection)
    response = {}
    statusCode = 200

    warnings = warningModel.GetWarnings()
    response = {
        'success': True,
        'warnings': warnings
    }

    return jsonify(response), statusCode

@warningController.route('/warnings/current', methods=['GET'])
def GetCurrentWarnings():
    connection = GetConnection()
    warningModel = WarningModel(connection)
    seasonModel = SeasonModel(connection)

    currentSeason = seasonModel.GetCurrentSeason()
    response = {}
    statusCode = 200
    warnings = warningModel.GetWarningBySeason(currentSeason['id'])
    response = {
        'success': True,
        'warnings': warnings
    }

    return jsonify(response), statusCode

@warningController.route('/warnings/season/<int:seasonId>', methods=['GET'])
def GetWarningBySeason(seasonId):
    connection = GetConnection()
    warningModel = WarningModel(connection)
    seasonModel = SeasonModel(connection)

    targetSeason = seasonModel.GetSeasonById(seasonId)
    response = {}
    statusCode = 200
    warnings = warningModel.GetWarningBySeason(targetSeason['id'])
    response = {
        'success': True,
        'warnings': warnings
    }

    return jsonify(response), statusCode

@warningController.route('/warnings/<int:warningId>', methods=['GET'])
def GetWarningById(warningId):
    connection = GetConnection()
    warningModel = WarningModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetWarning = warningModel.GetWarningById(warningId)
        if targetWarning is None:
            error = 'Warning no encontrado'
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['data'] = targetWarning
    else:
        response['message'] = error

    return jsonify(response), statusCode


@warningController.route('/warnings/<int:warningId>', methods=['DELETE'])
def DeleteWarning(warningId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Warnings') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        warningModel = WarningModel(connection)
        targetWarning = warningModel.GetWarningById(warningId)
        if targetWarning is None:
            error = 'Warning no encontrado'
            statusCode = 404  # Not found

    if error == '':
        deleted = warningModel.DeleteWarning(warningId)
        if deleted is False:
            error = "Hubo un error al eliminar el warning"
            statusCode = 500
        else:
            action = 'Eliminó el warning de {0} de razón {1}'.format(targetWarning['player_name'], targetWarning['reason'])
            warningModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Warning eliminado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateWarningData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(WARNING_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error