from flask import Blueprint

maps_bp = Blueprint('maps', __name__)

from . import routes

