from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from helpers import *

REGISTER_USER_LENGTH_CONFIG = {
    'nickname': {'max': 50, 'min':4},
    'username': {'max': 50, 'min':6},
    'password': {'max': 50, 'min':8}
}

CREATE_USER_LENGTH_CONFIG = {
    'username': REGISTER_USER_LENGTH_CONFIG['username'],
    'password': REGISTER_USER_LENGTH_CONFIG['password'],
}

REQUIRED_FIELDS = [
    'nickname',
    'username',
    'password',
    'level',
    'active'
]

userController = Blueprint('users', __name__)

def GetConnection():
    connection = getattr(userController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint User')
    
    return connection


@userController.route('/users', methods=['GET'])
def GetAllUsers():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    statusCode = 200
    error = ''
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        currentUser = userModel.GetUserByToken(token)
        if type(currentUser) is str:
            error = currentUser
            statusCode = 400

    if error == '':
        if currentUser['level'] not in ['Admin', 'Super', 'Editor']:
            error = 'Tipo de usuario inválido'
            statusCode = 400

    if error == '':
        if currentUser['level'] == 'Editor':
            error = 'Acceso denegado'
            statusCode = 401

    if error == '':
        users = userModel.GetUsersPublicData(currentUser['level'])
        if users is not None:
            response = {'success': True, 'users': users}
        else:
            error = 'Ocurrió un error al cargar los usuarios'
    
    if error != '':
        response = {'success': False, 'message': error}


    return jsonify(response), statusCode


@userController.route('/my_user', methods=['GET'])
def GetUserData():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    statusCode = 200
    error = ''
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
        publicData = userModel.GetUserPublicData(token)
        response = {'success': True, 'data': publicData}
    else:
        response = {'success': False, 'message': error}
    return jsonify(response), statusCode


@userController.route('/users/<int:userId>', methods=['GET'])
def GetUserById(userId):
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    statusCode = 200
    error = ''
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401
    
    if error == '':
        currentUser = userModel.GetUserByToken(token)
        if type(currentUser) is str:
            error = currentUser
            statusCode = 400

    if error == '':
        if currentUser['level'] not in ['Admin', 'Super']:
            error = 'Tipo de usuario inválido'
            statusCode = 400
    
    if error == '':
        targetUser = userModel.GetUserById(userId)
        if targetUser is None:
            error = "Usuario solicitado no encontrado"
            statusCode = 400
    
    if error == '':
        response = {'success': True, 'data': targetUser}
    else:
        response = {'success': False, 'message': error}

    return jsonify(response), statusCode


@userController.route('/users', methods=['POST'])
def RegisterUser():
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
        cleanData = ValidateUserData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if cleanData['level'] not in ['Admin', 'Editor']:
            error = 'Tipo de usuario inválido'
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], cleanData['level']) is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        if userModel.UsernameExists(cleanData['username']) is True:
            error = 'Usuario ya registrado'
            statusCode = 400

    if error == '':
        if userModel.NicknameExists(cleanData['nickname']) is True:
            error = 'Nick ya registrado'
            statusCode = 400

    if error == '':
        if cleanData['active'] not in ['1', '0']:
            error = 'El campo activo es inválido'
            statusCode = 400
    
    if error == '':
        created = userModel.CreateUser(cleanData)
        if created:
            message = 'Usuario creado correctamente'
            action = '{0} ha creado al usuario {1}'.format(targetUser['nickname'], cleanData['nickname'])
            userModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
        else:
            error = 'Hubo un error al crear al usuario'
            statusCode = 500

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@userController.route('/login', methods=['POST'])
def TryLogin():
    connection = GetConnection()
    userModel = UserModel(connection)
    recievedData, error, statusCode = JsonExists(request)

    if error == '':
        token = GetTokenOfRequest(request)
        if token is not None:
            error = 'Usted ya está autenticado'
            statusCode = 401  # Unauthorized

    if error == '':
        requiredFields = [
            'username',
            'password'
        ]
        dataOK = HasEmptyFields(requiredFields, recievedData)
        if type(dataOK) is str:
            error = dataOK
            statusCode = 400  # Bad request

    if error == '':
        lengthOK = ValidateLength(CREATE_USER_LENGTH_CONFIG, recievedData)
        if lengthOK is not True:
            error = lengthOK
            statusCode = 400
    
    if error == '':
        loginResult = userModel.TryLogin(recievedData['username'], recievedData['password'])
        if loginResult is False:
            error = 'Credenciales inválidas'
        else:
            token = loginResult
            userData = userModel.GetUserPublicData(token)
            message = token
            action = '{0} ha ingresado al sistema'.format(userData['nickname'])
            userModel.CreateBinnacle(userData['id'],action, request.remote_addr)
            
    if error != '':
        message = error
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['token'] = message
        response['userData'] = userData
    else:
        response['message'] = message
    
    return jsonify(response), statusCode


@userController.route('/users/<int:userId>', methods=['PUT'])
def UpdateUser(userId):
    connection = GetConnection()
    userModel = UserModel(connection)
    
    recievedData, error, statusCode = JsonExists(request)
    token = GetTokenOfRequest(request)
    if token is None:
        error = 'Acceso denegado. Autenticación requerida'
        statusCode = 401

    if error == '':
        currentUser = userModel.GetUserByToken(token)
        if type(currentUser) is str:
            error = currentUser
            statusCode = 400
    
    if error == '':
        targetUser = userModel.GetUserById(userId)
        if targetUser is None:
            error = 'Usuario a modificar no encontrado'
            statusCode = 400

    if error == '':
        cleanData = ValidateUserData(recievedData, False)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '' and 'level' in cleanData:
        if cleanData['level'] not in ['Editor', 'Admin']:
            error = 'Tipo de usuario no encontrado'
        else:
            if userModel.UserHasPermisson(targetUser['id'], cleanData['level']) is False:
                error = 'Acción denegada'
                statusCode = 401  # Unauthorized

    if error == '' and 'username' in cleanData:
        if userModel.UsernameExists(cleanData['username']) is True:
            error = 'Usuario ya registrado'
            statusCode = 400

    if error == '' and 'nickname' in cleanData:
        if userModel.NicknameExists(cleanData['nickname']) is True:
            error = 'Nick ya registrado'
            statusCode = 400

    if error == '' and 'active' in cleanData:
        if cleanData['active'] not in ['1', '0']:
            error = 'El campo activo es inválido'
            statusCode = 400

    if error == '':
        if cleanData == {}:
            error = 'Información recibida vacía'
            statusCode = 400
    
    if error == '':
        updated = userModel.UpdateUser(userId, cleanData)
        if updated is False:
            error = 'Hubo un error al intentar actualizar al usuario'
            statusCode = 500
        else:
            alteredColumns = ''
            for key in cleanData.keys():
                alteredColumns += '{0}, '.format(key)
            alteredColumns = alteredColumns[0:-2]

            action = 'Editó los campos {0} del usuario de id {1}'.format(alteredColumns, userId)
            userModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Usuario actualizado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode

def ValidateUserData(recievedData, exactData = True):
    '''
    Recieves userData and validate them
    If the data has no issues, return the data cleaned
    '''
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(CREATE_USER_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error