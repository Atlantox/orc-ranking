from flask import Blueprint, request, jsonify

from models.UserModel import UserModel
from models.CategoryModel import CategoryModel

from helpers import *

CATEGORY_LENGTH_CONFIG = {
    'name': {'min': 1, 'max':50}
}

REQUIRED_FIELDS = ['name']

categoryController = Blueprint('category', __name__)

def GetConnection():
    connection = getattr(categoryController, 'connection', None)
    if connection is None:
        raise Exception('No se pudo obtener la conexión desde el Blueprint Category')
    
    return connection

@categoryController.route('/categories', methods=['POST'])
def CreateCategory():
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
        cleanData = ValidateCategoryData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Categorías') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        categoryModel = CategoryModel(connection)
        if categoryModel.GetCategoryByName(cleanData['name']) is not None:
            error = 'La categoría ya está registrada'
            statusCode = 400
    
    if error == '':
        created = categoryModel.CreateCategory(cleanData)
        if created is False:
            error = "Hubo un error al crear la categoría"
            statusCode = 500
        else:
            action = 'Creó la categoría {0}'.format(cleanData['name'])
            categoryModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Categoría creada correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@categoryController.route('/categories', methods=['GET'])
def GetCategories():
    connection = GetConnection()
    categoryModel = CategoryModel(connection)
    response = {}
    statusCode = 200

    categories = categoryModel.GetCategories()

    response = {
        'success': True,
        'categories': categories
    }

    return jsonify(response), statusCode


@categoryController.route('/categories/<int:categoryId>', methods=['GET'])
def GetCategoryById(categoryId):
    connection = GetConnection()
    categoryModel = CategoryModel(connection)
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
        if userModel.UserHasPermisson(targetUser['id'], 'Categorías') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        targetCategory = categoryModel.GetCategoryById(categoryId)
        if targetCategory is None:
            error = 'Categoría no encontrada'
            statusCode = 404  # Not found
    
    success = error == ''
    response = {'success': success}

    if error == '':
        response['category'] = targetCategory
    else:
        response['message'] = error

    return jsonify(response), statusCode


@categoryController.route('/categories/<int:categoryId>', methods=['PUT'])
def UpdateCategory(categoryId):
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
        cleanData = ValidateCategoryData(recievedData)
        if type(cleanData) is str:
            error = cleanData
            statusCode = 400

    if error == '':
        if userModel.UserHasPermisson(targetUser['id'], 'Categorías') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        categoryModel = CategoryModel(connection)
        targetCategory = categoryModel.GetCategoryById(categoryId)
        if targetCategory is None:
            error = 'Categoría no encontrada'
            statusCode = 404  # Not found

    if error == '':
        if categoryModel.GetCategoryByName(cleanData['name']) is not None:
            error = 'Ya existe una categoría con ese nombre'
            statusCode = 400

    if error == '':
        updated = categoryModel.UpdateCategory(categoryId, cleanData)
        if updated is False:
            error = "Hubo un error al renombrar la categoría"
            statusCode = 500
        else:
            action = 'Renombró la categoría "{0}" por "{1}" '.format(targetCategory['name'], cleanData['name'])
            categoryModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Categoría renombrada correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


@categoryController.route('/categories/<int:categoryId>', methods=['DELETE'])
def DeleteCategory(categoryId):
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
        if userModel.UserHasPermisson(targetUser['id'], 'Categorías') is False:
            error = 'Acción denegada'
            statusCode = 401  # Unauthorized

    if error == '':
        categoryModel = CategoryModel(connection)
        targetCategory = categoryModel.GetCategoryById(categoryId)
        if targetCategory is None:
            error = 'Categoría no encontrada'
            statusCode = 404  # Not found

    if error == '':
        deleted = categoryModel.DeleteCategory(categoryId)
        if deleted is False:
            error = "Hubo un error al eliminar la categoría"
            statusCode = 500
        else:
            action = 'Eliminó la categoría "{0}"'.format(targetCategory['name'])
            categoryModel.CreateBinnacle(targetUser['id'],action, request.remote_addr)
            message = 'Categoría eliminada correctamente'

    if error != '':
        message = error
        
    success = error == ''
    return jsonify({'success': success, 'message': message}), statusCode


def ValidateCategoryData(recievedData, exactData = True):
    error = ''

    cleanData = HasEmptyFields(REQUIRED_FIELDS, recievedData, exactData)
    if type(cleanData) is str:
        error = cleanData

    if error == '':
        lengthOK = ValidateLength(CATEGORY_LENGTH_CONFIG, cleanData)
        if lengthOK is not True:
            error = lengthOK
    
    return cleanData if error == '' else error