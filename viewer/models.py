from datetime import datetime

from werkzeug import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, backref


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    password = db.Column(db.String(300))
    created_at = db.Column(db.DateTime)
    level = db.Column(db.Integer)

    def __init__(self, name, email, password, level=0):
        self.name = name
        self.created_at = datetime.now()
        self.password = password
        self.level = level


class SemaStore(db.Model):
    __tablename__ = 'sema_store'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), index=True)
    wave_file_id = db.Column(db.Integer)
    created_at = db.Column(db.DateTime)

    user = relationship('User')

    def __init__(self, user_id, wave_file_id):
        self.wave_file_id = wave_file_id
        self.user_id = user_id
        self.created_at = datetime.now()
