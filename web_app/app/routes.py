from flask import render_template, request, jsonify
from app import app, db
from app.models import User
import traceback
from sqlalchemy import text

@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        print('Error in index route:', str(e))
        traceback.print_exc()
        return 'Internal Server Error', 500

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([user.to_dict() for user in users])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        new_user = User(
            username=data['username'],
            email=data['email']
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/test-connection')
def test_connection():
    try:
        # Test the database connection
        db.session.execute(text('SELECT 1'))
        return jsonify({'status': 'success', 'message': 'Database connection successful'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500
