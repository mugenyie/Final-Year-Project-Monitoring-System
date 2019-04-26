# src/models/ProjectModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class ProjectModel(db.Model):

    """ Project Model """
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    git_url = db.Column(db.String(128), nullable=True)
    web_url = db.Column(db.String(128), nullable=True)
    score = db.Column(db.Integer, nullable=False, default=0)
    proposal_file = db.Column(db.Integer, nullable=True)
    documentation_file = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.git_url = data.get('git_url')
        self.web_url = data.get('web_url')
        self.score = data.get('score')
        self.proposal_file = data.get('proposal_file')
        self.documentation_file = data.get('documentation_file')
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get(id):
        return ProjectModel.query.get(id)
    
    @staticmethod
    def get_by_supervisor(supervisor_id):
        return ProjectModel.query.filter_by(id=supervisor_id).order_by(ProjectModel.created_at.desc())

    @staticmethod
    def get_all():
        return ProjectModel.query.all()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class ProjectSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    git_url = fields.Str(required=False)
    web_url = fields.Str(required=False)
    score = fields.Int(required=False)
    proposal_file = fields.Str(required=False)
    documentation_file = fields.Str(required=False)
    supervisor_id = fields.Int(required=False)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)



    