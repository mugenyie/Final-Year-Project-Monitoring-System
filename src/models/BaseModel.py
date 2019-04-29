import datetime, uuid
from . import db


class BaseModel(db.Model):

    """Base Model"""
    __abstract__ = True

    id = db.Column(db.String, primary_key=True, default=str(uuid.uuid4()))
    created_on = db.Column(db.DateTime)
    modified_on = db.Column(db.DateTime)

    def __init__(self, data):
        self.created_on = datetime.datetime.utcnow()
        self.modified_on= datetime.datetime.utcnow()


