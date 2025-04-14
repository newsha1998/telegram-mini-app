from telegram_mini_app import create_app
from flask import Flask
import os

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=3001)

# For Vercel
handler = app 