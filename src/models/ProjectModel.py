# src/models/ProjectModel.py
import datetime
from marshmallow import fields, Schema
from . import db, BaseModel


class ProjectModel(BaseModel):

    """ Project Model """
    __tablename__ = 'projects'

    name = db.Column(db.String(128), nullable=False)
    git_url = db.Column(db.String(128), nullable=True)
    web_url = db.Column(db.String(128), nullable=True)
    score = db.Column(db.Integer, nullable=False, default=0)
    proposal_file = db.Column(db.Integer, nullable=True)
    documentation_file = db.Column(db.Integer, nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.name = data.get('name')
        self.git_url = data.get('git_url')
        self.web_url = data.get('web_url')
        self.score = data.get('score')
        self.proposal_file = data.get('proposal_file')
        self.documentation_file = data.get('documentation_file')

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    @staticmethod
    def get_by_supervisor(supervisor_id):
        return ProjectModel.query.filter_by(id=supervisor_id).order_by(ProjectModel.created_at.desc())


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    git_url = fields.Str(required=False)
    web_url = fields.Str(required=False)
    score = fields.Int(required=False)
    proposal_file = fields.Str(required=False)
    documentation_file = fields.Str(required=False)
    supervisor_id = fields.Int(required=False)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)



    