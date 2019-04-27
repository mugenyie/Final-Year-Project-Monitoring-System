# src/models/SupervisorModel.py
import datetime
from marshmallow import fields, Schema
from . import db
from . import UserModel


class SupervisorModel(UserModel):

    """ Supervisor Model """
    __tablename__ = 'supervisors'
    department = db.Column(db.String(128), nullable=True)

    # class constructor
    def __init__(self, data):
        UserModel.__init__(self, data)
        self.department = data.get("department")


class SupervisorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    department = fields.Str(required=True)
    title = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    modified_at = fields.DateTime(dump_only=True)


    