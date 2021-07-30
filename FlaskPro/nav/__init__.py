from flask import Blueprint

nav_bp = Blueprint('navBP', __name__)

from . import nav_views