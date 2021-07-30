from flask import Blueprint

get_developer_new_bp = Blueprint('getDeveloperNewBP', __name__)

from . import get_developer_new_views