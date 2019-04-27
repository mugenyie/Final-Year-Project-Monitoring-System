import datetime
from . import db


class BaseModel(db.Model):

    """Base Model"""
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def __init__(self, data):
        self.created_on = datetime.datetime.utcnow()
        self.modified_on= datetime.datetime.utcnow()

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get(id):
        return BaseModel.query.get(id)

    @staticmethod
    def get_all():
        return BaseModel.query.all()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
