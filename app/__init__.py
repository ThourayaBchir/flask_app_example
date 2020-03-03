from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.api.routes import mod
from app.site.routes import mod
from app import api
from app import site

app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')

# we put this import in the end because in views.py we import the app variable above
from app import views
