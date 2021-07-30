from flask import Blueprint

location_share_bp = Blueprint('locationShareBP', __name__)

from . import location_share_views