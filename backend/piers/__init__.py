from flask import Blueprint

piers_bp = Blueprint('piers', __name__)

from . import routes

