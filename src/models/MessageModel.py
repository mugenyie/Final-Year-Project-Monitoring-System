# src/models/MessageModel.py
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel


class MessageModel(BaseModel):

    """ Message Model """
    __tablename__ = 'messages'

    message = db.Column(db.String(128), nullable=False)
    from_id = db.Column(db.String, nullable=False)
    to_id = db.Column(db.String, nullable=False)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.message = data.get('message')
        self.from_id = data.get('from_id')
        self.to_id = data.get('to_id')

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    @staticmethod
    def get_message_from(id):
        return MessageModel.query.filter_by(from_id=id).order_by(MessageModel.created_at.desc())

    @staticmethod
    def get_message_to(id):
        return MessageModel.query.filter_by(to_id=id).order_by(MessageModel.created_at.desc())

class MessageSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    message = fields.Str(required=True)
    from_id = fields.Int(required=True)
    to_id = fields.Int(required=True)
    created_on = fields.DateTime(dump_only=True)



    