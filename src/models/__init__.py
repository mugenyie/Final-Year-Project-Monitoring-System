#src/models/src/__init__.py

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# initialize our db
db = SQLAlchemy()
bcrypt = Bcrypt()

from .BaseModel import BaseModel
from .UserModel import UserModel
from .GroupModel import GroupModel, GroupSchema
from .MessageModel import MessageModel, MessageSchema
from .ProjectLogModel import ProjectLogModel, ProjectLogSchema
from .ProjectModel import ProjectModel, ProjectSchema
from .StudentModel import StudentModel, StudentSchema
from .SupervisorModel import SupervisorModel, SupervisorSchema
