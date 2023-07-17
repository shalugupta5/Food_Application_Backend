

from flask import Blueprint, request, jsonify
from flask_login import login_user
from werkzeug.security import check_password_hash
from models import User
from flask_login import login_required
import bcrypt
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib
from flask import Blueprint, redirect, url_for
from flask_login import logout_user

auth_bp = Blueprint('auth', __name__)

from werkzeug.security import check_password_hash, generate_password_hash

# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get('username')
#     password = data.get('password')
#     remember = data.get('remember', False)

#     if not username or not password:
#         return jsonify({'error': 'Invalid data'})

#     user = User.query.filter_by(username=username).first()

#     if not user or not verify_password(password, user.password):
#         return jsonify({'error': 'Invalid username or password'})

#     login_user(user, remember=remember)
#     return jsonify({'message': 'Logged in successfully',
#     'role':user.role})

# def verify_password(password, hashed_password):
#     # Hash the input password using SHA-256
#     hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

#     # Compare the hashed input password with the stored hashed password
#     return hashed_input_password == hashed_password


###############################

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    remember = data.get('remember', False)

    if not username or not password:
        return jsonify({'error': 'Invalid data'})

    user = User.query.filter_by(username=username).first()

    if not user or not verify_password(password, user.password):
        return jsonify({'error': 'Invalid username or password'})

    login_user(user, remember=remember)
    return jsonify({'message': 'Logged in successfully', 'role': user.role})

def verify_password(password, hashed_password):
    # Hash the input password using SHA-256
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

    # Compare the hashed input password with the stored hashed password
    return hashed_input_password == hashed_password




##################################

@auth_bp.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

