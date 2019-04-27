# src/models/GroupModel.py
import datetime
from marshmallow import fields, Schema
from . import db, BaseModel


class GroupModel(BaseModel):

    """ Group Model """
    __tablename__ = 'groups'

    name = db.Column(db.String(128), nullable=False)
    number = db.Column(db.String(128), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get('name')
        self.number = data.get('number')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

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
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    number = fields.Str(required=False)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)
    project_id = fields.Int(dump_only=True)
    supervisor_id = fields.Int(dump_only=True)



    