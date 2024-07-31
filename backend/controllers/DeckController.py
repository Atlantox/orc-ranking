from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.DeckModel import DeckModel
from models.TornamentModel import TournamentModel

from helpers import *

DECK_LENGTH_CONFIG = {
    'name': {'min': 1, 'max':100}
}

REQUIRED_FIELDS = ['name', 'colors']

deckController = Blueprint('deck', __name__)

def GetConnection():
    connection = getattr(deckController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Deck')
    
    return connection

@deckController.route('/decks', methods=['POST'])
def CreateDeck():
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
        if userModel.UserHasPermisson(targetUser['id'], 'Mazos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        deckModel = DeckModel(connection)
        if deckModel.GetDeckByName(cleanData['name']) is not None:
            error = 'El nombre del deck ya está registrado'
            statusCode = 400
    
    if error == '':
        created = deckModel.CreateDeck(cleanData)
        if created is False:
            error = "Hubo un error al crear el deck"
            statusCode = 500
        else:
            action = 'Creó el deck {0}'.format(cleanData['name'])
            deckModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Deck creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@deckController.route('/decks', methods=['GET'])
def GetDecks():
    connection = GetConnection()
    deckModel = DeckModel(connection)
    response = {}
    statusCode = 200

    decks = deckModel.GetDecks()
    response = {
        'success': True,
        'decks': decks
    }

    return jsonify(response), statusCode


@deckController.route('/decks/<int:deckId>', methods=['GET'])
def GetDeckById(deckId):
    connection = GetConnection()
    deckModel = DeckModel(connection)
    error = ''
    statusCode = 200

    if error == '':
        targetDeck = deckModel.GetDeckById(deckId)
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


@deckController.route('/decks/<int:deckId>', methods=['PUT'])
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
        if userModel.UserHasPermisson(targetUser['id'], 'Mazos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        deckModel = DeckModel(connection)
        targetDeck = deckModel.GetDeckById(deckId)
        if targetDeck is None:
            error = 'Deck no encontrado'
            statusCode = 404  # Not found

    if error == '':
        if deckModel.GetDeckByName(cleanData['name']) is not None:
            error = 'Ya existe un deck con ese nombre'
            statusCode = 400

    if error == '':
        updated = deckModel.UpdateDeck(deckId, cleanData)
        if updated is False:
            error = "Hubo un error al modificar el deck"
            statusCode = 500
        else:
            action = 'Modificó el deck "{0}"'.format(targetDeck['id'])
            deckModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
            message = 'Deck modificado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@deckController.route('/decks/<int:deckId>', methods=['DELETE'])
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
        if userModel.UserHasPermisson(targetUser['id'], 'Mazos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        deckModel = DeckModel(connection)
        targetDeck = deckModel.GetDeckById(deckId)
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
        deleted = deckModel.DeleteDeck(deckId)
        if deleted is False:
            error = "Hubo un error al eliminar el deck"
            statusCode = 500
        else:
            action = 'Eliminó el deck "{0}"'.format(targetDeck['name'])
            deckModel.CreateBinnacle(targetUser['id'], action, request.remote_addr)
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