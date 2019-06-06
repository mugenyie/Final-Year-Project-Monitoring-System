# src/models/GroupModel.py
from flask import g
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel
from .StudentModel import StudentSchema, StudentModel
from .SupervisorModel import SupervisorModel, SupervisorSchema
from .ProjectModel import ProjectModel


class GroupModel(BaseModel):

    """ Group Model """
    __tablename__ = 'groups'

    name = db.Column(db.String(128), nullable=False)
    number = db.Column(db.String(128),unique=True, nullable=True)
    created_by = db.Column(db.String(128), nullable=True)
    project_id = db.Column(db.String, db.ForeignKey('projects.id'), nullable=True)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get('name')
        self.number = data.get('number')
        self.created_by = data.get('created_by')
        self.project_id = data.get('project_id')
        self.supervisor_id = data.get('supervisor_id')

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
        return GroupModel.query.filter_by(supervisor_id=supervisor_id).order_by(GroupModel.created_on.desc()
        ).join(SupervisorModel, GroupModel.supervisor_id == SupervisorModel.id
        ).join(ProjectModel, GroupModel.project_id == ProjectModel.id
        ).values(GroupModel.id, GroupModel.name, GroupModel.number,
    GroupModel.created_on, GroupModel.modified_on ,GroupModel.created_by,
    GroupModel.project_id, GroupModel.supervisor_id, SupervisorModel.name.label('supervisor_name'), ProjectModel.name.label('project_name'))
    
    @staticmethod
    def get_groups_assigned():
        return GroupModel.query.filter(GroupModel.supervisor_id.isnot(None)
        ).join(SupervisorModel, GroupModel.supervisor_id == SupervisorModel.id
        ).join(ProjectModel, GroupModel.project_id == ProjectModel.id
        ).values(GroupModel.id, GroupModel.name, GroupModel.number,
    GroupModel.created_on, GroupModel.modified_on ,GroupModel.created_by,
    GroupModel.project_id, GroupModel.supervisor_id, SupervisorModel.name.label('supervisor_name'), ProjectModel.name.label('project_name'))
    
    @staticmethod
    def get_groups_unassigned():
        return GroupModel.query.filter(GroupModel.supervisor_id == None
        ).join(SupervisorModel, GroupModel.supervisor_id == SupervisorModel.id
        ).join(ProjectModel, GroupModel.project_id == ProjectModel.id
        ).values(GroupModel.id, GroupModel.name, GroupModel.number,
    GroupModel.created_on, GroupModel.modified_on ,GroupModel.created_by,
    GroupModel.project_id, GroupModel.supervisor_id, SupervisorModel.name.label('supervisor_name'), ProjectModel.name.label('project_name'))
        
    @staticmethod
    def get_by_id(group_id):
        return GroupModel.query.get(group_id)  
    
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

class GroupSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    number = fields.Str(required=True)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)
    created_by = fields.Str(required=True)
    project_id = fields.Str()
    supervisor_id = fields.Str()
    supervisor_name = fields.Str()
    project_name = fields.Str()
    members = fields.Nested(StudentSchema, many=True)



    