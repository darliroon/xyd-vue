from flask import Blueprint

new_finger_table_bp = Blueprint('fingerTableBP', __name__)

from . import new_finger_table_views