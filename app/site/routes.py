from flask import Blueprint

mod = Blueprint('site', __name__)

@mod.route('/homepage')
def homepage():
    return '<h1> You are in the site home page <h1>'
