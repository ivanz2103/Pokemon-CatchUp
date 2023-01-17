from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50),nullable=False, unique=True)
    first = db.Column(db.String(50),nullable=False, unique=True)
    last = db.Column(db.String(50),nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    pokemon = db.relationship('Pokemon', backref='Author', lazy=True)

    def __init__(self, username, first, last, email, password):
        self.username = username
        self.first = first
        self.last = last
        self.email = email
        self.password = generate_password_hash(password)
    
    def update_db(self, p):
        db.session.append(p)
        db.session.commit()

    def pokeballs(self):
        return len(self.p) <= 5

    def delete_from_db(self, p):
        db.session.delete(p)
        db.session.commit()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.Column(db.String(50), nullable=False)
    base_experience =db.Column(db.Integer, nullable=False)
    sprite_url = db.Column(db.String(), nullable=False)
    attack_base = db.Column(db.Integer, nullable=False)
    hp_base = db.Column(db.Integer, nullable=False)
    defense_base = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


    def __init__(self, name, ability, base_experience, sprite_url, attack_base, hp_base, defense_base, user_id):
        self.name = name
        self.ability = ability
        self.base_experience = base_experience
        self.sprite_url = sprite_url
        self.attack_base = attack_base
        self.hp_base = hp_base
        self.defense_base = defense_base
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

class Pokeballs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ability = db.Column(db.String(50), nullable=False)
    base_experience =db.Column(db.Integer, nullable=False)
    sprite_url = db.Column(db.String(), nullable=False)
    attack_base = db.Column(db.Integer, nullable=False)
    hp_base = db.Column(db.Integer, nullable=False)
    defense_base = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)


    def __init__(self, name, ability, base_experience, sprite_url, attack_base, hp_base, defense_base, user_id):
        self.name = name
        self.ability = ability
        self.base_experience = base_experience
        self.sprite_url = sprite_url
        self.attack_base = attack_base
        self.hp_base = hp_base
        self.defense_base = defense_base
        self.user_id = user_id
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()