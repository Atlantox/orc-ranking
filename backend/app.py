from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

from config import config

# Controllers / Blueprints
from controllers.BinnacleController import binnacleController
from controllers.UserController import userController
from controllers.TournamentController import tournamentController
from controllers.DeckController import deckController
from controllers.PlayerController import playerController
from controllers.SeasonController import seasonController
from controllers.GameFormatController import gameFormatController

app = Flask(__name__)
app.config.from_object(config['development'])
CORS(app)
connection = MySQL(app)

CONTROLLERS = [
    binnacleController,
    userController,
    deckController,
    playerController,
    seasonController,
    gameFormatController,
    tournamentController
]

# Le pasamos la conexión de la base de datos a los blueprints / controladores
for controller in CONTROLLERS:
    controller.connection = connection

def NotFound(error):
    return jsonify({'success': False, 'message': 'Ruta no encontrada'}), 404


if __name__ == '__main__':    
    app.register_error_handler(404, NotFound)
    #Registrar los controladores / blueprints
    for controller in CONTROLLERS:
        app.register_blueprint(controller)

    app.run()