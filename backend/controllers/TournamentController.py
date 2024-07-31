from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.PlayerModel import PlayerModel
from models.DeckModel import DeckModel
from models.GameFormatModel import GameFormatModel
from models.TournamentModel import TournamentModel
from models.SeasonModel import SeasonModel

from helpers import *

DECK_LENGTH_CONFIG = {
    'date': {'min':8, 'max':10}
}

REQUIRED_FIELDS = ['date', 'format', 'participants']

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
        cleanData = ValidateDeckData(recievedData)
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
def GetTournaments():
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    response = {}
    statusCode = 200

    tournaments = tournamentModel.GetTournaments()
    response = {
        'success': True,
        'tournaments': tournaments
    }

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/<int:deckId>', methods=['GET'])
def GetDeckById(deckId):
    connection = GetConnection()
    tournamentModel = TournamentModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetDeck = tournamentModel.GetDeckById(deckId)
        if targetDeck is None:
            error = 'Deck no encontrado'
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['deck'] = targetDeck
    else:
        response['message'] = error

    return jsonify(response), statusCode


@tournamentController.route('/tournaments/<int:deckId>', methods=['PUT'])
def UpdateDeck(deckId):
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
        cleanData = ValidateDeckData(recievedData, False)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Torneos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        tournamentModel = TournamentModel(connection)
        targetDeck = tournamentModel.GetDeckById(deckId)
        if targetDeck is None:
            error = 'Deck no encontrado'
            statusCode = 404  # Not found

    if error == '':
        if tournamentModel.GetDeckByName(cleanData['name']) is not None:
            error = 'Ya existe un deck con ese nombre'
            statusCode = 400

    if error == '':
        updated = tournamentModel.UpdateDeck(deckId, cleanData)
        if updated is False:
            error = "Hubo un error al modificar el deck"
            statusCode = 500
        else:
            action = 'Modificó el deck "{0}"'.format(targetDeck['id'])
            tournamentModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Deck modificado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@tournamentController.route('/tournaments/<int:deckId>', methods=['DELETE'])
def DeleteDeck(deckId):
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
        targetDeck = tournamentModel.GetDeckById(deckId)
        if targetDeck is None:
            error = 'Deck no encontrado'
            statusCode = 404  # Not found

    if error == '':
        tournamentModel = TournamentModel(connection)
        deckTournaments = tournamentModel.GetTournamentsOfDeck(deckId)
        if len(deckTournaments) > 0:
            # The deck is registered in almost one tournament, then, it can't be deleted
            error = 'No se pueden borrar decks que hayan participado en un torneo'
            statusCode = 400

    if error == '':
        deleted = tournamentModel.DeleteDeck(deckId)
        if deleted is False:
            error = "Hubo un error al eliminar el deck"
            statusCode = 500
        else:
            action = 'Eliminó el deck "{0}"'.format(targetDeck['name'])
            tournamentModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Deck eliminado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateDeckData(recievedData, exactData = True):
    ''' 
    With exactData = True, the required fields will be obligatory
    With exactData = False, only the existing data will be validated
    '''
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(DECK_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error