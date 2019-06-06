# src/models/SupervisorModel.py
import datetime, uuid
from marshmallow import fields, Schema
from . import db, UserModel, BaseModel
from ..enums.UserRoleEnum import UserRoleEnum


class SupervisorModel(UserModel, BaseModel):

    """ Supervisor Model """
    __tablename__ = 'supervisors'
    department = db.Column(db.String(128), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        UserModel.__init__(self, data)
        self.id = data.get('id')
        self.name = data.get('name')
        self.user_role_name = UserRoleEnum.SUPERVISOR.name
        self.user_role_value = UserRoleEnum.SUPERVISOR.value
        self.department = data.get("department")

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get(id):
        return SupervisorModel.query.get(id)

    @staticmethod
    def get_all():
        return SupervisorModel.query.all()

    @staticmethod
    def get_by_email(value):
        return SupervisorModel.query.filter_by(email=value).first()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class SupervisorSchema(Schema):
    id = fields.Str(missing=str(uuid.uuid4))
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    phonenumber = fields.Str(required=True)
    password = fields.Str(required=True, load_only=True)
    department = fields.Str(required=True)
    title = fields.Str(required=True)
    user_role_name = fields.Str()
    user_role_value = fields.Integer()
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)


    