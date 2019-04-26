# src/models/MessageModel.py
import datetime
from marshmallow import fields, Schema
from . import db


class MessageModel(db.Model):

    """ Message Model """
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(128), nullable=False)
    from_id = db.Column(db.Integer, nullable=False)
    to_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        self.message = data.get('message')
        self.from_id = data.get('from_id')
        self.to_id = data.get('to_id')
        self.created_at = datetime.datetime.utcnow()

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get(id):
        return MessageModel.query.get(id)
    
    @staticmethod
    def get_message_from(id):
        return MessageModel.query.filter_by(from_id=id).order_by(MessageModel.created_at.desc())

    @staticmethod
    def get_message_to(id):
        return MessageModel.query.filter_by(to_id=id).order_by(MessageModel.created_at.desc())

    @staticmethod
    def get_all():
        return GroupModel.query.all()


class MessageSchema(Schema):
    id = fields.Int(dump_only=True)
    message = fields.Str(required=True)
    from_id = fields.Int(required=True)
    to_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)



    