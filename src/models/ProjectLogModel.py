# src/models/ProjectLogModel.py
import datetime, uuid
from marshmallow import fields, Schema
from . import db, BaseModel


class ProjectLogModel(BaseModel):

    """ Project Log Model """
    __tablename__ = 'projectslog'

    title = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    supervisor_remarks = db.Column(db.String(128), nullable=True)
    files = db.Column(db.String(128), nullable=True)
    score = db.Column(db.Integer, nullable=False, default=0)
    source_link = db.Column(db.String(128), nullable=True)
    student_id = db.Column(db.String, db.ForeignKey('students.id'), nullable=False)
    project_id = db.Column(db.String(128), nullable=True)
    group_id = db.Column(db.String, db.ForeignKey('groups.id'), nullable=True)
    supervisor_id = db.Column(db.String, db.ForeignKey('supervisors.id'), nullable=True)

    # class constructor
    def __init__(self, data):
        BaseModel.__init__(self, data)
        self.id = data.get('id')
        self.title = data.get('title')
        self.description = data.get('description')
        self.files = data.get('files')
        self.score = data.get('score')
        self.supervisor_remarks = data.get('supervisor_remarks')
        self.source_link = data.get('source_link')
        self.project_id = data.get('project_id')
        self.student_id = data.get('student_id')
        self.group_id = data.get('group_id')
        self.supervisor_id = data.get('supervisor_id')

    def __str__(self):
        return "<id: {}>".format(self.id)

    #CRUD Operations
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self,data):
        for key, item in data.items():
            setattr(self, key, item)
        self.modified_at = datetime.datetime.utcnow()
        db.session.commit()

    @staticmethod
    def get_by_student(student_id):
        return ProjectLogModel.query.filter_by(student_id=student_id).order_by(ProjectLogModel.created_on.desc())

    @staticmethod
    def get(log_id):
        return ProjectLogModel.query.get(log_id)
    
    @staticmethod
    def get_by_groupid(group_id):
        return ProjectLogModel.query.filter_by(group_id=group_id).order_by(ProjectLogModel.created_on.desc())


class ProjectLogSchema(Schema):
    id = fields.Str(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    files = fields.Str(required=False)
    score = fields.Int(required=False)
    supervisor_remarks = fields.Str(required=False)
    source_link = fields.Str(required=False)
    student_id = fields.Str(required=False)
    project_id = fields.Str(required=False)
    group_id = fields.Str(required=False)
    supervisor_id = fields.Str(required=False)
    created_on = fields.DateTime(dump_only=True)
    modified_on = fields.DateTime(dump_only=True)



    