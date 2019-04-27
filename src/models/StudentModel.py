# src/models/StudentModel.py
import datetime
from marshmallow import fields, Schema
from . import db, UserModel


class StudentModel(UserModel):
    
    """ Student Model """
    __tablename__ = 'students'
    student_number = db.Column(db.String(128), nullable=False)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        UserModel.__init__(self, data)
        self.student_number = data.get('student_number')

    #CRUD Operations
    @staticmethod
    def get_student_by_student_number(value):
        return StudentModel.query.filter_by(email=value).first()

   
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


    