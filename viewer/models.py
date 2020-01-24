from datetime import datetime
from werkzeug import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

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
