from flask import Blueprint

new_img_table_bp = Blueprint('imgTableBP', __name__)

from . import new_img_table_views