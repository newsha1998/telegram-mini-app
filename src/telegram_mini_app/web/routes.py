from flask import render_template
from telegram_mini_app.web import bp

@bp.route('/')
def index():
    return render_template('index.html') 