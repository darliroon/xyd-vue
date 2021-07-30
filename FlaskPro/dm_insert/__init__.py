from flask import Blueprint

dm_insert_views_bp = Blueprint('dmInsertBP', __name__)

from . import dm_insert_views