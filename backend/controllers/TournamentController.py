from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.PlayerModel import PlayerModel
from models.DeckModel import DeckModel
from models.GameFormatModel import GameFormatModel
from models.TournamentModel import TournamentModel
from models.SeasonModel import SeasonModel

from helpers import *

TOURNAMENT_LENGTH_CONFIG = {
    'date': {'min':8, 'max':10},
    'observation': {'min': 0, 'max': 200}
}

REQUIRED_FIELDS = ['date', 'format', 'participants', 'observation', 'pot']

tournamentController = Blueprint('tournament', __name__)

def GetConnection():
    connection = getattr(tournamentController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Tournament')
    
    return connection

@tournamentController.route('/tournaments', methods=['POST'])
def CreateTournament():
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
        cleanData = ValidateTournamentData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Torneos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        tournamentDate = StringToDatetime(cleanData['date'])
        if tournamentDate is False:
            error = 'Fecha inválida'
            statusCode = 400
        else:
            now = datetime.now()
            if tournamentDate >= now:
                error = 'La fecha de inicio del torneo no puede ser posterior a la fecha actual'
                statusCode = 400

    if error == '':
        validation = ValidateFloatNumber(cleanData['pot'])
        if type(validation) is str:
            error = validation    
            statusCode = 400

    if error == '':
        gameFormatModel = GameFormatModel(connection)
        if gameFormatModel.GetFormatByName(cleanData['format']) is None:
            error = 'Formato no encontrado'
            statusCode = 404

    if error == '':
        deckModel = DeckModel(connection)
        playerModel = PlayerModel(connection)
        for participant in cleanData['participants']:
            if deckModel.GetDeckById(participant['deck']) is None:
                error = 'El deck de id "{0}" no fue encontrado'.format(participant['deck'])
                statusCode = 404

            if playerModel.GetPlayerById(participant['player']) is None:
                error = 'El jugador de id "{0}" no fue encontrado'.format(participant['player'])
                statusCode = 404
    
    if error == '':
        seasonModel = SeasonModel(connection)
        currentSeason = seasonModel.GetCurrentSeason()
        if currentSeason is None or currentSeason is False:
            error = 'Temporada no encontrada'
            statusCode = 404
    
    if error == '':
        cleanData['season'] = currentSeason['id']
        tournamentModel = TournamentModel(connection)
        created = tournamentModel.CreateTournament(cleanData)
        if created is False:
            error = "Hubo un error al crear el torneo"
            statusCode = 500
        else:
            action = 'Creó el torneo del día {0}'.format(cleanData['date'])
            tournamentModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Torneo creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@tournamentController.route('/tournaments', methods=['GET'])
def GetCurrentTournaments():
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    tournaments = tournamentModel.GetCurrentTournaments()
    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/all', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/tournaments/all/<int:seasonId>', methods=['GET'])
def GetAllTournaments(seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    if seasonId is None:
        tournaments = tournamentModel.GetAllTournaments()
    else:
        tournaments = tournamentModel.GetAllTournamentsOfSeason(seasonId)
    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/inactive', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/tournaments/inactive/<int:seasonId>', methods=['GET'])
def GetInactiveTournaments(seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    if seasonId is None:
        tournaments = tournamentModel.GetInactiveTournaments()
    else:
        tournaments = tournamentModel.GetInactiveTournamentsOfSeason(seasonId)

    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/player/<int:playerId>', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/tournaments/player/<int:playerId>/<int:seasonId>', methods=['GET'])
def GetActiveTournamentsOfPlayer(playerId, seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    
    tournaments = tournamentModel.GetActiveTournamentsOfPlayer(playerId, seasonId)

    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/active', methods=['GET'])
def GetActiveTournaments():
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    tournaments = tournamentModel.GetActiveTournaments()
    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/season/<int:seasonId>', methods=['GET'])
def GetTournamentsOfSeason(seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    tournaments = tournamentModel.GetTournamentsOfSeason(seasonId)
    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/last', methods=['GET'])
def GetLastTournament():
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    tournament = tournamentModel.GetLastTournament()
    response = {
        'success': True,
        'tournament': tournament
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/count', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/tournaments/count/<int:seasonId>', methods=['GET'])
def GetTournamentAndParticipantsCountOfSeason(seasonId):
    ''' If the seasonId is none, returns all tournaments and participants '''
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    count = tournamentModel.GetTournamentsAndParticipantsCountOfSeason(seasonId)
    response = {
        'success': True,
        'count': count
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/<int:tournamentId>', methods=['GET'])
def GetTournamentById(tournamentId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetTournament = tournamentModel.GetTournamentById(tournamentId)
        if type(targetTournament) is str:
            error = targetTournament
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['tournament'] = targetTournament
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/ranking/<int:seasonId>/<int:formatId>', methods=['GET'])
def GetTournamentsRankingOfSeason(seasonId, formatId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200
    error = ''

    seasonModel = SeasonModel(connection)
    targetSeason = seasonModel.GetSeasonById(seasonId)
    if targetSeason is None:
        error = 'Temporada no encontrada'
        statusCode = 404

    if error == '':
        formatModel = GameFormatModel(connection)
        targetFormat = formatModel.GetFormatById(formatId)
        if targetFormat is None:
            error = 'Formato no encontrado'
            statusCode = 404

    if error == '':
        ranking = tournamentModel.GetTournamentsRankingOfSeasonAndFormat(seasonId, targetFormat)
        if type(ranking) is str:
            error = ranking
            statusCode = 500

    response['success'] = error == ''

    if error == '':
        response['ranking'] = ranking
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/statistics/<int:seasonId>', methods=['GET'])
def GetSeasonStatistics(seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200
    error = ''

    seasonModel = SeasonModel(connection)
    targetSeason = seasonModel.GetSeasonById(seasonId)
    if targetSeason is None:
        error = 'Temporada no encontrada'
        statusCode = 404

    if error == '':
        statistics = tournamentModel.GetSeasonStatistics(seasonId)
        if type(statistics) is str:
            error = statistics
            statusCode = 500

    response['success'] = error == ''

    if error == '':
        response['statistics'] = statistics
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/pot/<int:seasonId>/<int:formatId>', methods=['GET'])
def GetPotOfSeason(seasonId, formatId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200
    error = ''

    seasonModel = SeasonModel(connection)
    targetSeason = seasonModel.GetSeasonById(seasonId)
    if targetSeason is None:
        error = 'Temporada no encontrada'
        statusCode = 404

    if error == '':
        formatModel = GameFormatModel(connection)
        targetFormat = formatModel.GetFormatById(formatId)
        if targetFormat is None:
            error = 'Formato no encontrado'
            statusCode = 404

    if error == '':
        potTotal = tournamentModel.GetTotalPotOfSeason(seasonId, formatId)
        if type(potTotal) is str:
            error = potTotal
            statusCode = 500

    response['success'] = error == ''

    if error == '':
        response['pot'] = potTotal
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/individual_players/<int:seasonId>', methods=['GET'])
def GetIndividualPlayersOfSeason(seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200
    error = ''

    seasonModel = SeasonModel(connection)
    targetSeason = seasonModel.GetSeasonById(seasonId)
    if targetSeason is None:
        error = 'Temporada no encontrada'
        statusCode = 404

    if error == '':
        players = tournamentModel.GetTournamentsIndividualPlayersOfSeason(seasonId)
        if type(players) is str:
            error = players
            statusCode = 500

    response['success'] = error == ''

    if error == '':
        response['count'] = players
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/results/player/<int:playerId>', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/results/player/<int:playerId>/<int:seasonId>', methods=['GET'])
def GetTournamentResultsOfPlayer(playerId, seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    results = tournamentModel.GetTournamentResultsOfPlayer(playerId, seasonId)
    response['success'] = results != False

    if results is False:
        response['message'] = 'Ocurrió un error al consultar los resultados de torneos del jugador solicitado'
    else:
        response['results'] = results

    return jsonify(response), statusCode


@tournamentController.route('/results/deck/<int:deckId>', defaults={'seasonId': None}, methods=['GET'])
@tournamentController.route('/results/deck/<int:deckId>/<int:seasonId>', methods=['GET'])
def GetTournamentResultsOfDeck(deckId, seasonId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    results = tournamentModel.GetTournamentResultsOfDeck(deckId, seasonId)
    response['success'] = results != False

    if results is False:
        response['message'] = 'Ocurrió un error al consultar los resultados de torneos del deck solicitado'
    else:
        response['results'] = results

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/<int:tournamentId>', methods=['DELETE'])
def DeactivateTournament(tournamentId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Torneos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        tournamentModel = TournamentModel(connection)
        targetTournament = tournamentModel.GetTournamentById(tournamentId)
        if targetTournament is None:
            error = 'Torneo no encontrado'
            statusCode = 404  # Not found

    if error == '':
        deleted = tournamentModel.DeactivateTournament(tournamentId)
        if deleted is False:
            error = "Hubo un error al desactivar el torneo"
            statusCode = 500
        else:
            action = 'Desactivó el torneo de id "{0}"'.format(tournamentId)
            tournamentModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Tourneo desactivado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateTournamentData(recievedData, exactData = True):
    ''' 
    With exactData = True, the required fields will be obligatory
    With exactData = False, only the existing data will be validated
    '''
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(TOURNAMENT_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error