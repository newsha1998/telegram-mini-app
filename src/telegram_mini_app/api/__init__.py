from flask import Blueprint

bp = Blueprint('api', __name__)

from telegram_mini_app.api import routes 