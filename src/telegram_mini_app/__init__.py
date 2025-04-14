from flask import Flask, send_from_directory
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

    # MongoDB connection with error handling
    try:
        mongodb_uri = os.getenv('MONGODB_URI')
        if not mongodb_uri:
            raise ValueError("MONGODB_URI environment variable is not set")
        
        client = MongoClient(mongodb_uri)
        app.db = client['telegram-mini-app']
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        # You might want to handle this differently in production
        raise

    # Register blueprints
    from telegram_mini_app.web import bp as web_bp
    from telegram_mini_app.api import bp as api_bp
    
    app.register_blueprint(web_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Serve static files
    @app.route('/static/<path:path>')
    def serve_static(path):
        return send_from_directory('web/static', path)

    return app 