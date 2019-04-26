# src/models/GroupModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class GroupModel(db.Model):

    """ Group Model """
    __tablename__ = 'groups'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    number = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)
    supervisor_id = db.Column(db.Integer, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.name = data.get('name')
        self.number = data.get('number')
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
        return GroupModel.query.get(id)
    
    @staticmethod
    def get_by_supervisor(supervisor_id):
        return GroupModel.query.filter_by(supervisor_id=supervisor_id).order_by(GroupModel.created_at.desc())

    @staticmethod
    def get_by_group_number(number):
        return GroupModel.query.filter_by(number=number).first()    

    @staticmethod
    def get_all():
        return GroupModel.query.all()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()


class GroupSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    number = fields.Str(required=False)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)
    project_id = fields.Int(dump_only=True)
    supervisor_id = fields.Int(dump_only=True)



    