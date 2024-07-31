from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.SeasonModel import SeasonModel
from models.TornamentModel import TournamentModel

from helpers import *

SEASON_LENGTH_CONFIG = {
    'date': {'min':8, 'max':10}
}

REQUIRED_FIELDS = ['date']

seasonController = Blueprint('season', __name__)

def GetConnection():
    connection = getattr(seasonController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Season')
    
    return connection

@seasonController.route('/seasons', methods=['POST'])
def CreateSeason():
    connection = GetConnection()
    userModel = UserModel(connection)
    seasonModel = SeasonModel(connection)
    
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
        cleanData = ValidateSeasonData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Temporadas') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        seasonDate = StringToDatetime(cleanData['date'])
        if seasonDate is False:
            error = 'Fecha inválida'
            statusCode = 400
        else:
            now = datetime.now()
            if seasonDate >= now:
                error = 'La fecha de inicio de la temporada no puede ser posterior a la fecha actual'
                statusCode = 400
    
    if error == '':
        created = seasonModel.CreateSeason(cleanData)
        if type(created) is str:
            error = created
            statusCode = 500
        else:
            action = 'Creó la temporada del {0}'.format(cleanData['date'])
            seasonModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Temporada creada correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@seasonController.route('/seasons', methods=['GET'])
def GetSeasons():
    connection = GetConnection()
    seasonModel = SeasonModel(connection)
    response = {}
    statusCode = 200

    seasons = seasonModel.GetSeasons()
    response = {
        'success': True,
        'seasons': seasons
    }

    return jsonify(response), statusCode


@seasonController.route('/seasons/<int:seasonId>', methods=['GET'])
def GetSeasonById(seasonId):
    connection = GetConnection()
    seasonModel = SeasonModel(connection)
    error = ''
    statusCode = 200

    targetSeason = seasonModel.GetSeasonById(seasonId)
    if targetSeason is None:
        error = 'Temporada no encontrada'
        statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['season'] = targetSeason
    else:
        response['message'] = error

    return jsonify(response), statusCode


@seasonController.route('/seasons/current', methods=['GET'])
def GetCurrentSeason():
    connection = GetConnection()
    seasonModel = SeasonModel(connection)
    error = ''
    statusCode = 200

    targetSeason = seasonModel.GetCurrentSeason()
    if targetSeason is None:
        error = 'No hay temporadas actuales'
        statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['season'] = targetSeason
    else:
        response['message'] = error

    return jsonify(response), statusCode


def ValidateSeasonData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(SEASON_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error