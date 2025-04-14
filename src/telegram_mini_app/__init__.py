from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os

def create_app():
    # Load environment variables
    load_dotenv()

    app = Flask(__name__,
                template_folder='web/templates',
                static_folder='web/static')
    CORS(app)

    # MongoDB connection
    client = MongoClient(os.getenv('MONGODB_URI'))
    app.db = client['telegram-mini-app']

    # Register blueprints
    from telegram_mini_app.web import bp as web_bp
    from telegram_mini_app.api import bp as api_bp
    
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    return app 