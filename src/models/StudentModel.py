# src/models/StudentModel.py
import datetime, uuid
from marshmallow import fields, Schema
from collections import OrderedDict
from . import db, UserModel, BaseModel
from ..enums.UserRoleEnum import UserRoleEnum


class StudentModel(UserModel, BaseModel):
    
    """ Student Model """
    __tablename__ = 'students'
    student_number = db.Column(db.String(128), unique=True, nullable=False)
    course = db.Column(db.String(128), nullable=False)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=True)
    project_id = db.Column(db.String, db.ForeignKey('projects.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        BaseModel.__init__(self, data)
        UserModel.__init__(self, data)
        self.id=data.get('id')
        self.user_role_name = UserRoleEnum.STUDENT.name
        self.user_role_value = UserRoleEnum.STUDENT.value
        self.student_number = data.get('student_number')
        self.course = data.get('course')
        self.supervisor_id = data.get('supervisor_id')
        self.group_id = data.get('group_id')
        self.project_id = data.get('project_id')

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    @staticmethod
    def get(id):
        return StudentModel.query.get(id)
    
    @staticmethod
    def get_all():
        return StudentModel.query.all()

    @staticmethod
    def get_by_email(value):
        return StudentModel.query.filter_by(email=value).first()

    @staticmethod
    def view_group_members(group_id): 
        return StudentModel.query.filter_by(group_id=group_id) 

    @staticmethod
    def get_by_supervisor(supervisor_id):
        return StudentModel.query.filter_by(supervisor_id=supervisor_id)

    @staticmethod
    def get_by_student_number(value):
        return StudentModel.query.filter_by(student_number=value).first()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class StudentSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    email = fields.Email(required=True, error_messages={'invalid': 'Invalid Email Address'})
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    student_number = fields.Str(required=True)
    course = fields.Function(lambda obj: obj.course.upper(), required=True)
    created_at = fields.DateTime(dump_only=True)
    user_role_value = fields.Int()
    user_role_name = fields.Str()
    modified_at = fields.DateTime(dump_only=True)
    supervisor_id = fields.Int(required=False)
    group_id = fields.Str(required=False)
    project_id = fields.Int(required=False)


    