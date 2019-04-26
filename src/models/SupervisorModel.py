# src/models/SupervisorModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class SupervisorModel(db.Model):

    """ Supervisor Model """
    __tablename__ = 'supervisors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phonenumber = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    department = db.Column(db.String(128), nullable=True)
    title = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.email = data.get('email')
        self.phonenumber = data.get('phonenumber')
        self.password = self.__generate_hash(data.get('password'))
        self.department = data.get('department')
        self.title = data.get('title')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __generate_hash(self, password):
        return bcrypt.generate_password_hash(password, rounds=10).decode("utf-8")
    
    def check_hash(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get(id):
        return SupervisorModel.query.get(id)
    
    @staticmethod
    def get_by_email(value):
        return SupervisorModel.query.filter_by(email=value).order_by(SupervisorModel.created_at.desc()).first()

    @staticmethod
    def get_all():
        return SupervisorModel.query.all()

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


class SupervisorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    department = fields.Str(required=True)
    title = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


    