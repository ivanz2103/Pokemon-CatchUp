from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship("Post", backref='Author', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    img_url = db.Column(db.String(), nullable=False)
    caption = db.Column(db.String(50), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, title, img_url, caption, user_id):
        self.title = title
        self.img_url = img_url
        self.caption = caption
        self.user_id = user_id

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.Column(db.String(50), nullable=False)
    baseExp =db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(), nullable=False)
    attackExp = db.Column(db.Integer, nullable=False)
    hpExp = db.Column(db.Integer, nullable=False)
    defenseExp = db.Column(db.Integer, nullable=False)

    def __init__(self, name, ability, baseExp, image, attackExp, hpExp, defenseExp):
        self.name = name
        self.ability = ability
        self.baseExp = baseExp
        self.image = image
        self.attackExp = attackExp
        self.hpExp = hpExp
        self.defenseExp = defenseExp
    