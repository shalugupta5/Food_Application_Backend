
from flask import Flask, request
from flask_login import LoginManager
from models import db, User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth import auth_bp
from flask_cors import CORS
from api import api_bp
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME
from flask_socketio import SocketIO, emit
from flask_cors import CORS
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'gfhfjhhgjkhkjhgfjhg87y6u'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Load the user from the user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://DATABASE_USER:DATABASE_PASSWORD@localhost/DATABASE_NAME'
db.init_app(app)
migrate = Migrate(app, db)

# CORS configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# SocketIO configuration
socketio = SocketIO(app, cors_allowed_origins="http://localhost:4200")  # Set the CORS allowed origins for socket.io

# Register the API blueprint
app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/auth')

# SocketIO event handlers
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('order_update')
def handle_order_update(order_id, status):
    # Update the order status in your database
    # Emit an event to all connected clients with the updated order status
    emit('order_status_update', {'order_id': order_id, 'status': status}, broadcast=True)

@app.route('/sendotp', methods=['POST'])
def send_otp():
    email = request.json['email']  # Get the email address from the request body
    otp = generate_otp()  # Generate the OTP (implement this function)
    print(otp)
    # Set up the email content
    msg = MIMEMultipart()
    msg['From'] = 'yourfood743@gmail.com'  # Replace with your email address
    msg['To'] = email
    msg['Subject'] = 'OTP Verification'
    body = f'Your OTP is: {otp}'
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP('your server', 587) as server:  # Replace with your SMTP server details
        server.starttls()
        server.login('yourfood743@gmail.com', 'yourkey')  # Replace with your email and password
        server.send_message(msg)

    return    {'otp': otp}



def generate_otp():
    """Generates a random OTP."""
    otp_digits = random.sample(range(10), 4)
    otp = ''.join([str(digit) for digit in otp_digits])
    return otp



if __name__ == '__main__':
    socketio.run(app)



