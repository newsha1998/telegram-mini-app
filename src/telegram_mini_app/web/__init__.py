from flask import Blueprint

bp = Blueprint('web', __name__)

from telegram_mini_app.web import routes 