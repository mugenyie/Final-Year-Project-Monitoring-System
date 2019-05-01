# src/models/GroupModel.py
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel
from .StudentModel import StudentSchema


class GroupModel(BaseModel):

    """ Group Model """
    __tablename__ = 'groups'

    name = db.Column(db.String(128), nullable=False)
    number = db.Column(db.String(128),unique=True, nullable=True)
    password = db.Column(db.String(128), nullable=False)
    project_id = db.Column(db.String, db.ForeignKey('projects.id'), nullable=True)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get('name')
        self.number = data.get('number')

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    @staticmethod
    def get_by_supervisor(supervisor_id):
        return GroupModel.query.filter_by(supervisor_id=supervisor_id).order_by(GroupModel.created_at.desc())

    @staticmethod
    def get_by_group_number(number):
        return GroupModel.query.filter_by(number=number).first()    

class GroupSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=False)
    password = fields.Str(required=False)
    number = fields.Str(required=False)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)
    project_id = fields.Int(dump_only=True)
    supervisor_id = fields.Int(dump_only=True)
    members = fields.Nested(StudentSchema, many=True)



    