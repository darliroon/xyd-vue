from flask import Blueprint

new_nav_table_bp = Blueprint('navTableBP', __name__)

from . import new_nav_table_views