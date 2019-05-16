# src/models/GroupModel.py
from flask import g
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel
from .StudentModel import StudentSchema, StudentModel


class GroupModel(BaseModel):

    """ Group Model """
    __tablename__ = 'groups'

    name = db.Column(db.String(128), nullable=False)
    number = db.Column(db.String(128),unique=True, nullable=True)
    created_by = db.Column(db.String(128),unique=True, nullable=True)
    project_id = db.Column(db.String, db.ForeignKey('projects.id'), nullable=True)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get('name')
        self.number = data.get('number')
        self.created_by = data.get('created_by')

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def view_members(group_id):
        return StudentModel.view_group_members(group_id)

    @staticmethod
    def get_by_group_number(value):
        return GroupModel.query.filter_by(number=value).first()

    @staticmethod
    def get_by_supervisor(supervisor_id):
        return GroupModel.query.filter_by(supervisor_id=supervisor_id).order_by(GroupModel.created_at.desc())

    @staticmethod
    def get_by_id(group_id):
        return GroupModel.query.get(group_id)  

class GroupSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    number = fields.Str(required=True)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)
    created_by = fields.Str(required=True)
    project_id = fields.Str()
    supervisor_id = fields.Str()
    members = fields.Nested(StudentSchema, many=True)



    