from telegram_mini_app import create_app
from flask import Flask, request
import os

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=3001)

# For Vercel
def handler(event, context):
    with app.app_context():
        response = app.handle_request()
        return {
            'statusCode': response.status_code,
            'headers': dict(response.headers),
            'body': response.get_data().decode('utf-8')
        } 