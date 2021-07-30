from flask import Blueprint

positional_info_bp = Blueprint('positionBP', __name__)

from . import positional_info_views