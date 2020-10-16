from flask_sqlalchemy import SQLAlchemy
from app import app_instance

db = SQLAlchemy(app_instance)


class User(db.Model):
    """
    Модель пользователя
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    nickname = db.Column(db.String(24), nullable=False, unique=True)
    phone = db.Column(db.String(16), nullable=True)
    socket = db.relationship('UserSockets', backref='user')

class Messenger(object):
    """
    Справочник мессенджеров
    """
    __tablename__ = 'messengers'
    id = db.Column(db.Integer(), primary_key=True)
    messenger_name = db.Column(db.String(32), nullable=False)
    socket = db.relationship('UserSockets', backref='messenger')

class UserSocket(db.Model):
    """
    Привязки юзеров к ботам (chat_id, token, etc.)
    """
    __tablename__ = 'user_sockets'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    messenger_id = db.Column(db.Integer(), db.ForeignKey('messengers.id'))
    chat_token = db.Column(db.Text(), nullable=False)