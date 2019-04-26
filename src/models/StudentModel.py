# src/models/StudentModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class StudentModel(db.Model):

    """ Student Model """
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    student_number = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    phonenumber = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.student_number = data.get('student_number')
        self.name = data.get('name')
        self.email = data.get('email')
        self.phonenumber = data.get('phonenumber')
        self.password = self.__generate_hash(data.get('password'))
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
        return StudentModel.query.get(id)
    
    @staticmethod
    def get_by_email(value):
        return StudentModel.query.filter_by(email=value).order_by(StudentModel.created_at.desc()).first()

    @staticmethod
    def get_student_by_student_number(value):
        return StudentModel.query.filter_by(email=value).first()

    @staticmethod
    def get_all():
        return StudentModel.query.all()

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


class StudentSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    student_number = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    supervisor_id = fields.Int(required=True)
    group_id = fields.Int(required=True)
    project_id = fields.Int(required=True)


    