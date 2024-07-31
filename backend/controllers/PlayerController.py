from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.PlayerModel import PlayerModel
from models.TournamentModel import TournamentModel

from helpers import *

PLAYER_LENGTH_CONFIG = {
    'name': {'min': 1, 'max':50}
}

REQUIRED_FIELDS = ['name']

playerController = Blueprint('player', __name__)

def GetConnection():
    connection = getattr(playerController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Player')
    
    return connection

@playerController.route('/players', methods=['POST'])
def CreatePlayer():
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
        cleanData = ValidatePlayerData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Jugadores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        playerModel = PlayerModel(connection)
        if playerModel.GetPlayerByName(cleanData['name']) is not None:
            error = 'El jugador ya está registrado'
            statusCode = 400
    
    if error == '':
        created = playerModel.CreatePlayer(cleanData)
        if created is False:
            error = "Hubo un error al crear al jugador"
            statusCode = 500
        else:
            action = 'Creó al jugador {0}'.format(cleanData['name'])
            playerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Jugador creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@playerController.route('/players', methods=['GET'])
def GetPlayers():
    connection = GetConnection()
    playerModel = PlayerModel(connection)
    response = {}
    statusCode = 200

    players = playerModel.GetPlayers()
    response = {
        'success': True,
        'players': players
    }

    return jsonify(response), statusCode


@playerController.route('/players/<int:playerId>', methods=['GET'])
def GetPlayerById(playerId):
    connection = GetConnection()
    playerModel = PlayerModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetPlayer = playerModel.GetPlayerById(playerId)
        if targetPlayer is None:
            error = 'Jugador no encontrado'
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['player'] = targetPlayer
    else:
        response['message'] = error

    return jsonify(response), statusCode


@playerController.route('/players/<int:playerId>', methods=['PUT'])
def UpdatePlayer(playerId):
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
        cleanData = ValidatePlayerData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Jugadores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        playerModel = PlayerModel(connection)
        targetPlayer = playerModel.GetPlayerById(playerId)
        if targetPlayer is None:
            error = 'Jugador no encontrado'
            statusCode = 404  # Not found

    if error == '':
        if playerModel.GetPlayerByName(cleanData['name']) is not None:
            error = 'Ya existe un jugador con ese nombre'
            statusCode = 400

    if error == '':
        updated = playerModel.UpdatePlayer(playerId, cleanData)
        if updated is False:
            error = "Hubo un error al renombrar al jugador"
            statusCode = 500
        else:
            action = 'Renombró al jugador "{0}" por "{1}" '.format(targetPlayer['name'], cleanData['name'])
            playerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Jugador renombrado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@playerController.route('/players/<int:playerId>', methods=['DELETE'])
def DeletePlayer(playerId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Jugadores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        playerModel = PlayerModel(connection)
        targetPlayer = playerModel.GetPlayerById(playerId)
        if targetPlayer is None:
            error = 'Jugador no encontrado'
            statusCode = 404  # Not found

    if error == '':
        tournamentModel = TournamentModel(connection)
        playerTournaments = tournamentModel.GetTournamentsOfPlayer(playerId)
        if len(playerTournaments) > 0:
            # The player is registered in almost one tournament, then, it can't be deleted
            error = 'No se pueden borrar jugadores que hayan participado en un torneo'
            statusCode = 400

    if error == '':
        deleted = playerModel.DeletePlayer(playerId)
        if deleted is False:
            error = "Hubo un error al eliminar al jugador"
            statusCode = 500
        else:
            action = 'Eliminó al jugador "{0}"'.format(targetPlayer['name'])
            playerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Jugador eliminado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidatePlayerData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(PLAYER_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error