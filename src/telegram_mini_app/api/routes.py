from flask import request, jsonify, current_app
from datetime import datetime
from telegram_mini_app.api import bp

@bp.route('/users', methods=['GET', 'POST'])
def handle_users():
    if request.method == 'POST':
        try:
            user = request.json
            result = current_app.db.users.update_one(
                {'telegramId': user['id']},
                {'$set': {
                    'first_name': user.get('first_name'),
                    'last_name': user.get('last_name'),
                    'username': user.get('username'),
                    'photo_url': user.get('photo_url'),
                    'last_seen': datetime.utcnow().isoformat()
                }},
                upsert=True
            )
            return jsonify({'success': True, 'result': str(result.upserted_id)})
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    elif request.method == 'GET':
        try:
            telegram_id = request.args.get('telegramId')
            user = current_app.db.users.find_one({'telegramId': telegram_id})
            if user:
                user['_id'] = str(user['_id'])  # Convert ObjectId to string
            return jsonify(user or {})
        except Exception as e:
            return jsonify({'error': str(e)}), 500 