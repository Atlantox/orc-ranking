from datetime import datetime

from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from backend.models.TornamentModel import ReaderModel
from models.LoanModel import LoanModel

from helpers import *

READER_LENGTH_CONFIG = {
    'cedula': {'min': 7, 'max':11},
    'names': {'min': 2, 'max':60},
    'surnames': {'min': 2, 'max':60},
    'gender': {'min': 1, 'max':1},
    'birthdate': {'min':8, 'max':10},
    'phone': {'min': 7, 'max':15},
    'is_teacher': {'min': 1, 'max':1}
}

REQUIRED_FIELDS = [
    'cedula',
    'names',
    'surnames',
    'gender',
    'birthdate',
    'phone',
    'is_teacher'
]

readerController = Blueprint('reader', __name__)

def GetConnection():
    connection = getattr(readerController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Reader')
    
    return connection

@readerController.route('/readers', methods=['POST'])
def CreateReader():
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
        cleanData = ValidateReaderData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Lectores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        readerModel = ReaderModel(connection)
        if readerModel.GetReaderByCedula(cleanData['cedula']) is not None:
            error = 'La cédula del lector ya está registrada'
            statusCode = 400

    if error == '':
        if cleanData['gender'] not in ['M', 'F']:
            error = 'Género inválido'
            statusCode = 400

    if error == '':
        if cleanData['is_teacher'] not in ['1', '0']:
            error = 'El campo "es profesor" es inválido'
            statusCode = 400
    
    if error == '':
        birthdate = StringToDatetime(cleanData['birthdate'])
        if birthdate is False:
            error = 'Fecha inválida'
            statusCode = 400
        else:
            now = datetime.now()
            if birthdate >= now:
                error = 'La fecha de nacimiento no puede ser posterior a la fecha actual'
                statusCode = 400
    
    if error == '':
        diff = abs((now - birthdate).days)
        if diff < 365 * 10:
            error = 'El lector no cumple con la edad mínima para realizar el préstamo (10 años)'
            statusCode = 400

    if error == '':
        created = readerModel.CreateReader(cleanData)
        if created is False:
            error = 'Hubo un error al intentar crear al lector'
            statusCode = 500
        else:
            action = 'Creó al lector {0} de cédula {1}'.format(cleanData['names'], cleanData['cedula'])
            readerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Lector creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@readerController.route('/readers', methods=['GET'])
def GetReaders():
    connection = GetConnection()
    userModel = UserModel(connection)
    error = ''
    response = {}
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
        if userModel.UserHasPermisson(targetUser['id'], 'Lectores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        readerModel = ReaderModel(connection)
        readers = readerModel.GetReaders()
    else:
        readers = []

    response['success'] = error == ''

    if error == '':
        response['readers'] = readers
    else:
        response['message'] = error

    return jsonify(response), statusCode


@readerController.route('/readers/<int:categoryId>', methods=['GET'])
def GetReaderById(categoryId):
    connection = GetConnection()
    userModel = UserModel(connection)
    error = ''
    response = {}
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
        if userModel.UserHasPermisson(targetUser['id'], 'Lectores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        readerModel = ReaderModel(connection)
        targetReader = readerModel.GetReaderById(categoryId)
        if targetReader is None:
            error = 'Lector no encontrado'
            statusCode = 404
    
    response['success'] = error == ''
    if error == '':
        response['reader'] = targetReader
    else:
        response['message'] = error

    return jsonify(response), statusCode


@readerController.route('/readers/<int:readerId>', methods=['PUT'])
def UpdateReader(readerId):
    connection = GetConnection()
    userModel = UserModel(connection)
    readerModel = ReaderModel(connection)
    
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
        cleanData = ValidateReaderData(recievedData, False)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400
    
    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Lectores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        targetReader = readerModel.GetReaderById(readerId)
        if targetReader is None:
            error = 'Lector no encontrado'
            statusCode = 404

    if error == '' and 'cedula' in cleanData:
        if readerModel.GetReaderByCedula(cleanData['cedula']) is not None:
            error = 'La cédula a actualizar está repetida en el sistema'
            statusCode = 400

    if error == '' and 'gender' in cleanData:
        if cleanData['gender'] not in ['M', 'F']:
            error = 'Género inválido'
            statusCode = 400

    if error == '' and 'is_teacher' in cleanData:
        if cleanData['is_teacher'] not in ['1', '0']:
            error = 'El campo "es profesor" es inválido'
            statusCode = 400

    if error == '':
        if cleanData == {}:
            error = 'Información recibida vacía'
            statusCode = 400
    
    if error == '':
        updated = readerModel.UpdateReader(readerId, cleanData)
        if updated is False:
            error = 'Hubo un error al intentar actualizar al lector'
            statusCode = 500
        else:
            alteredColumns = ''
            for key in cleanData.keys():
                alteredColumns += '{0}, '.format(key)
            alteredColumns = alteredColumns[0:-2]

            action = 'Editó los campos {0} del lector de id {1}'.format(alteredColumns, readerId)
            readerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Lector actualizado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@readerController.route('/readers/<int:readerId>', methods=['DELETE'])
def DeleteReader(readerId):
    connection = GetConnection()
    userModel = UserModel(connection)
    readerModel = ReaderModel(connection)
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
        if userModel.UserHasPermisson(targetUser['id'], 'Lectores') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        targetReader = readerModel.GetReaderById(readerId)
        if targetReader is None:
            error = 'Lector no encontrado'
            statusCode = 404

    if error == '':
        loanModel = LoanModel(connection)
        loansOfReader = loanModel.GetLoansOfReader(readerId)
        if loansOfReader != []:
            error = 'No se puede borrar el lector porque este tiene préstamos registrados.'
            statusCode = 400
    
    if error == '':
        deleted = readerModel.DeleteReader(readerId)
        if deleted is False:
            error = 'Hubo un error al intentar eliminar al lector'
            statusCode = 500
        else:
            action = 'Borró al lector {0} de cédula {1} y id {2}'.format(targetReader['names'], targetReader['cedula'], targetReader['id'])
            readerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Lector eliminado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateReaderData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(READER_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error