from datetime import datetime

from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.BookModel import BookModel
from backend.models.TornamentModel import ReaderModel
from models.LoanModel import LoanModel

from helpers import *

LOAN_LENGTH_CONFIG = {
    'observation': {'min': 0, 'max':1000, 'optional': True},
    'deliver_date': {'min': 8, 'max':10}
}

REQUIRED_FIELDS = [
    'book',
    'reader',
    'observation',
    'deliver_date'
]

loanController = Blueprint('loan', __name__)

def GetConnection():
    connection = getattr(loanController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Loan')
    
    return connection

@loanController.route('/loans', methods=['POST'])
def CreateLoan():
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
        cleanData = ValidateLoanData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        readerModel = ReaderModel(connection)
        if readerModel.GetReaderById(cleanData['reader']) is None:
            error = 'Lector no encontrado'
            statusCode = 404

    if error == '':
        bookModel = BookModel(connection)
        targetBook = bookModel.GetBookById(cleanData['book'])
        if targetBook is None:
            error = 'Libro no encontrado'
            statusCode = 404
    
    if error == '':
        deliverDate = StringToDatetime(cleanData['deliver_date'])
        if deliverDate is False:
            error = 'Fecha inválida'
            statusCode = 400
        else:
            now = datetime.now()
            if deliverDate > now:
                error = 'La fecha de entrega no puede superar el día actual'
                statusCode = 400
    
    if error == '':
        if targetBook['state'] != 'En biblioteca':
            error = 'El libro a prestar debe encontrarse en biblioteca'
            statusCode = 400
    
    if error == '':
        loanModel = LoanModel(connection)
        created = loanModel.CreateLoan(cleanData)
        if created is False:
            error = 'Hubo un error al intentar crear el préstamo'
            statusCode = 500
        else:
            bookModel.UpdateBook(cleanData['book'], {'state': 'Prestado'})
            action = 'Creó un préstamo {0} al lector {1} y el libro {2}'.format(created, cleanData['reader'], cleanData['book'])
            readerModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Préstamo creado correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@loanController.route('/loans', methods=['GET'])
def GetActiveLoans():
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetActiveLoans()

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/inactive', methods=['GET'])
def GetInactiveLoans():
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetInactiveLoans()

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error

    return jsonify(response), statusCode

@loanController.route('/loans/pendings', methods=['GET'])
def GetPendingLoans():
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetPendingLoans()

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/finished', methods=['GET'])
def GetFinishedLoans():
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetFinishedLoans()

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/reader/<int:readerId>', methods=['GET'])
def GetLoansOfReader(readerId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        readerModel = ReaderModel(connection)
        if readerModel.GetReaderById(readerId) is False:
            error = 'Lector no encontrado'
            statusCode = 404

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetLoansOfReader(readerId)

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error
        
    return jsonify(response), statusCode


@loanController.route('/loans/book/<int:bookId>', methods=['GET'])
def GetLoansOfBook(bookId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        bookModel = BookModel(connection)
        if bookModel.GetBookById(bookId) is None:
            error = 'Libro no encontrado'
            statusCode = 404

    if error == '':
       loanModel = LoanModel(connection)
       loans = loanModel.GetLoansOfBook(bookId)

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error
        
    return jsonify(response), statusCode


@loanController.route('/loans/<int:loanId>', methods=['GET'])
def GetLoanById(loanId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        targetLoan = loanModel.GetLoanById(loanId)
        if targetLoan is None:
            error = 'Préstamo no encontrado'
            statusCode = 404

    response['success'] = error == ''

    if error == '':
        response['loan'] = targetLoan
    else:
        response['message'] = error

    return jsonify(response), statusCode
    

@loanController.route('/loans/return/<int:loanId>', methods=['POST'])
def ReturnLoan(loanId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        targetLoan = loanModel.GetLoanById(loanId)
        if targetLoan is None:
            error = 'Préstamo no encontrado'
            statusCode = 404
    
    if error == '':
        returned = loanModel.ReturnLoan(loanId)
        if returned is False:
            error = 'Hubo un error al registrar la devolución del libro'
            statusCode = 500
        else:
            bookModel = BookModel(connection)
            bookModel.UpdateBook(targetLoan['book_id'], {'state': 'En biblioteca'})
            action = 'Se devolvió el libro {0} del lector {1} del préstamo {2}'.format(targetLoan['book_id'], targetLoan['reader_id'], loanId)
            bookModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Devolución de préstamo creada correctamente'

        response['success'] = error == ''

        if error != '':
            message = error

        response['message'] = message

        return jsonify(response), statusCode
    

@loanController.route('/loans/<int:loanId>', methods=['PUT'])
def UpdateLoanObservation(loanId):
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized
    
    if error == '':
        if 'observation' not in recievedData:
            error = 'Observación no encontrada'
            statusCode = 400
        
    if error == '':
        if len(recievedData['observation']) > 1000:
            error = 'El campo Observación supera el límite de caracteres'
            statusCode = 400    

    if error == '':
        loanModel = LoanModel(connection)
        targetLoan = loanModel.GetLoanById(loanId)
        if targetLoan is None:
            error = 'Préstamo no encontrado'
            statusCode = 404

    if error == '':
        updated = loanModel.UpdateLoanObservation(loanId, recievedData['observation'])
        if updated is False:
            error = 'Ocurrió un error al actualizar el préstamo'
            statusCode = 500

    response['success'] = error == ''

    if error == '':
        response['message'] = 'Observación del préstamo actualizada correctamente'
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/<int:loanId>', methods=['DELETE'])
def DeactivateLoan(loanId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        targetLoan = loanModel.GetLoanById(loanId)
        if targetLoan is None:
            error = 'Préstamo no encontrado'
            statusCode = 404

    if error == '':
        deactivated = loanModel.DeactivateLoan(loanId)
        if deactivated is False:
            error = 'Hubo un error al intentar desactivar el préstamo'
            statusCode = 400
    
    if error == '':
        bookModel = BookModel(connection)
        bookUpdate = {'state': 'En biblioteca'}
        updated = bookModel.UpdateBook(targetLoan['book_id'], bookUpdate)
        if updated:
            message = 'Préstamo desactivado correctamente'
        else:
            error = 'Hubo un error al cambiar el estado del libro del préstamo a "En biblioteca"'


    response['success'] = error == ''

    if error == '':
        response['message'] = message
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/latest/<int:days>', methods=['GET'])
def GetLoansBetweenDaysAndNow(days):
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
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
        loanModel = LoanModel(connection)
        loans = loanModel.GetLoansBetweenDaysAndToday(days)

    response['success'] = error == ''

    if error == '':
        response['loans'] = loans
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/latest_count/<int:days>', methods=['GET'])
def GetLoansCountBetweenDaysAndNow(days):
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
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
        loanModel = LoanModel(connection)
        counts = loanModel.GetLoansDeliveredAndReturnedCountBetweenDaysAndToday(days)


    response['success'] = error == ''

    if error == '':
        response['counts'] = counts
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/between_dates', methods=['POST'])
def GetLoansCountsBetweenDates():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    error = ''
    statusCode = 200
    
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
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400    

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        loansByDate = loanModel.GetLoansDeliveredAndReturnedCountBetweenDates(cleanData['initial_date'], cleanData['final_date'])

    response['success'] = error == ''

    if error == '':
        response['counts'] = loansByDate
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/by_gender', methods=['POST'])
def GetLoansByGender():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    error = ''
    statusCode = 200

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
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400    

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        loansByGender = loanModel.GetLoansQuantityByGenderBetweenDates(cleanData['initial_date'], cleanData['final_date'])

    response['success'] = error == ''

    if error == '':
        response['loans'] = loansByGender
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/by_teacher', methods=['POST'])
def GetLoansByTeacher():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}
    error = ''
    statusCode = 200

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
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400    

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        loansByGender = loanModel.GetLoansQuantityByTeacherBetweenDates(cleanData['initial_date'], cleanData['final_date'])

    response['success'] = error == ''

    if error == '':
        response['loans'] = loansByGender
    else:
        response['message'] = error

    return jsonify(response), statusCode


@loanController.route('/loans/by_categories', methods=['POST'])
def GetLoansByCategories():
    connection = GetConnection()
    userModel = UserModel(connection)
    response = {}

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
        cleanData = ValidateInitialAndFinalDate(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400    

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Préstamos') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        loanModel = LoanModel(connection)
        loansByCategories = loanModel.GetLoansQuantityByCategoriesBetweenDates(cleanData['initial_date'], cleanData['final_date'])


    response['success'] = error == ''

    if error == '':
        response['loans'] = loansByCategories
    else:
        response['message'] = error

    return jsonify(response), statusCode

def ValidateLoanData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(LOAN_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error