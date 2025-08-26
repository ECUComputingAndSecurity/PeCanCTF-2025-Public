from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
import bcrypt
from datetime import datetime
from settings import *
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI  # Use SQLite database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save memory
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

# User model
class Users(db.Model):

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100), nullable=False, unique=True)
    display_name = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False, unique=True) # No brucy forcy pls :D
    profile_pic = db.Column(db.String(1000), default='/static/imgs/defaulticon.png')
    btcaddr = db.Column(db.String(1000), default='')

    def setPassword(self, passwd):
        # Easily set the password for the user
        self.password = bcrypt.hashpw(passwd.encode('utf-8'),bcrypt.gensalt())
        return self
    
    def checkPassword(self, passwd):
        # Easily checkk whether the supplied password is valid
        return bcrypt.checkpw(passwd.encode('utf-8'), self.password)

    # Back references to all posts that this author has
    posts = db.relationship('Products', backref='authors', lazy=True)
    
    def __repr__(self):
        return f'<Users {self.name}>'

class Products(db.Model):
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(100), nullable=False, unique=True)
    content = db.Column(db.String(200), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    brief = db.Column(db.String(200), nullable=False)    
    picture = db.Column(db.String(1000), default='')
    bestFame = db.Column(db.Boolean, default=False)

    # Foreign relationships to another users
    author = db.Column(db.UUID(as_uuid=True), db.ForeignKey('users.id'), nullable=False) 

    def __repr__(self):
        return f'<Products {self.title}>'