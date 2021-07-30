from flask import Blueprint

new_object_table_bp = Blueprint('objectTableBP', __name__)

from . import new_object_table_views