from flask import Blueprint

authentication = Blueprint('authentication',__name__,template_folder='template')

from app.auth import routes