# src/models/AdminModel.py
import datetime, uuid
from marshmallow import fields, Schema
from collections import OrderedDict
from . import db, UserModel, BaseModel
from ..enums.UserRoleEnum import UserRoleEnum


class AdminModel(UserModel, BaseModel):
    """Admin Model"""
    __tablename__ = 'admins'

    def __init__(self, data):
        BaseModel.__init__(self, data)
        UserModel.__init__(self, data)
        self.id = data.get('id')
        self.user_role_name = UserRoleEnum.ADMIN.name
        self.user_role_value = UserRoleEnum.ADMIN.value

    @staticmethod
    def get_all():
        return AdminModel.query.all()
    
    @staticmethod
    def get(id):
        return AdminModel.query.get(id)

    @staticmethod
    def get_by_email(value):
        return AdminModel.query.filter_by(email=value).first()

    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class AdminSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    email = fields.Email(required=True, error_messages={'invalid': 'Invalid Email Address'})
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    created_at = fields.DateTime(dump_only=True)
    user_role_value = fields.Int()
    user_role_name = fields.Str()
    modified_at = fields.DateTime(dump_only=True)