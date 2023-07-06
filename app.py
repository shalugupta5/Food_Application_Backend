from flask import Flask
from flask_login import LoginManager
from models import db, User
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from auth import auth_bp
from flask_cors import CORS
from api import api_bp
from config import DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

# Load the user from the user_id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:shalu@localhost/food'
db.init_app(app)
migrate = Migrate(app, db)

# CORS configuration
CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

# Register the API blueprint
app.register_blueprint(api_bp, url_prefix='/api')

app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run()
