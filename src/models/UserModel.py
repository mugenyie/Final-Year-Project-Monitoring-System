# src/models/UserModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class UserModel(db.Model):

    """ Student Model """
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    title = db.Column(db.String(128), nullable=True) 
    email = db.Column(db.String(128), unique=True, nullable=False)
    phonenumber = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_role_name = db.Column(db.Integer, nullable=False)
    user_role_value = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def __init__(self, data):
        self.name = data.get("name")
        self.title = data.get("title")
        self.email = data.get("email")
        self.phonenumber = data.get("phonenumber")
        self.user_role_name = data.get("user_role_name")
        self.user_role_value = data.get("user_role_value")
        self.password = self.__generate_hash(data.get('password'))
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<id: {}>".format(self.id)

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")

    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get(id):
        return UserModel.query.get(id)
    
    @staticmethod
    def get_by_email(value):
        return UserModel.query.filter_by(email=value).order_by(UserModel.created_at.desc()).first()

    @staticmethod
    def get_all():
        return UserModel.query.all()

    def update(self, data):
        for key, item in data.items():
            if key == 'password':
                self.password = self.__generate_hash(value)
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()