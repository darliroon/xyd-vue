from flask import Blueprint

main_objects_bp = Blueprint('mainObjectBP', __name__)

from . import main_objects_views