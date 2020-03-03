from flask import Blueprint

mod = Blueprint('api', __name__)

@mod.route('/getData')
def getData():
    return '{"result": "You are in the api"}'
