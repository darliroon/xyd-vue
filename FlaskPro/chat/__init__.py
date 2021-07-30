from flask import Blueprint

chat_bp = Blueprint('chatBP', __name__)

from . import chat_views