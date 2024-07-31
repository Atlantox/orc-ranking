
from flask import Blueprint, request, jsonify

from models.BinnacleModel import BinnacleModel
from models.UserModel import UserModel
from helpers import *

binnacleController = Blueprint('binnacle', __name__)

def GetConnection():
    connection = getattr(binnacleController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Binnacle')
    
    return connection


@binnacleController.route('/binnacle', methods=['GET'])
def GetBinnacle():
    connection = GetConnection()
    response = {}
    statusCode = 200
    error = ''
    token = GetTokenOfRequest(request)

    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        userModel = UserModel(connection)
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Bitácora') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized
    
    if error == '':
        binacleModel = BinnacleModel(connection)
        binnacles = binacleModel.GetBinnacle()
    
    response['success'] = error == ''
    if error == '':
        response['binnacle'] = binnacles
    else:
        response['message'] = error

    return jsonify(response), statusCode


@binnacleController.route('/binnacle/user/<int:userId>', methods=['GET'])
def GetBinnacleOfUser(userId):
    connection = GetConnection()
    response = {}
    statusCode = 200
    error = ''
    token = GetTokenOfRequest(request)

    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        userModel = UserModel(connection)
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Bitácora') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        targetUser = userModel.GetUserById(userId)
        if targetUser is None:
            error = "Usuario solicitado no encontrado"
            statusCode = 404
    
    if error == '':
        binacleModel = BinnacleModel(connection)
        binnacles = binacleModel.GetBinnacleOfUser(userId)
    
    response['success'] = error == ''
    if error == '':
        response['binnacle'] = binnacles
    else:
        response['message'] = error

    return jsonify(response), statusCode

@binnacleController.route('/binnacle/between_dates', methods=['POST'])
def GetBinnacleBetweenDates():
    connection = GetConnection()
    response = {}

    recievedData, error, statusCode = JsonExists(request)
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        userModel = UserModel(connection)
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Bitácora') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400   
    
    if error == '':
        binacleModel = BinnacleModel(connection)
        binnacles = binacleModel.GetBinnacleBetweenDates(cleanData['initial_date'], cleanData['final_date'])
    
    response['success'] = error == ''
    if error == '':
        response['binnacle'] = binnacles
    else:
        response['message'] = error

    return jsonify(response), statusCode

@binnacleController.route('/binnacle/between_dates/<int:userId>', methods=['POST'])
def GetBinnacleOfUserBetweenDates(userId):
    connection = GetConnection()
    response = {}

    recievedData, error, statusCode = JsonExists(request)
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        userModel = UserModel(connection)
        targetUser = userModel.GetUserByToken(token)
        if type(targetUser) is str:
            error = targetUser
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Bitácora') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        targetUser = userModel.GetUserById(userId)
        if targetUser is None:
            error = "Usuario solicitado no encontrado"
            statusCode = 404

    if error == '':
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400   
    
    if error == '':
        binacleModel = BinnacleModel(connection)
        binnacles = binacleModel.GetBinnacleOfUserBetweenDates(userId, cleanData['initial_date'], cleanData['final_date'])
    
    response['success'] = error == ''
    if error == '':
        response['binnacle'] = binnacles
    else:
        response['message'] = error

    return jsonify(response), statusCode