#/src/views/ProjectView

from flask import request, json, Response, Blueprint, g
from ..models.ProjectLogModel import ProjectLogModel, ProjectLogSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

log_api = Blueprint('log_api', __name__)
log_schema = ProjectLogSchema()
logs_schema = ProjectLogSchema(many=True)

@log_api.route('/', methods=['POST'])
def create():
  """
  Create new project log
  """
  req_data = request.get_json(force=True)
  data, error = log_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  log = ProjectLogModel(data)
  log.save()
  log_data = log_schema.dump(log).data
  return custom_response(log_data, 201)

@log_api.route('/<string:log_id>', methods=['PATCH'])
def update(log_id):
  """Update Project Log"""
  req_data = request.get_json()
  data, error = log_schema.load(req_data, partial=True)
  if error:
      return custom_response(error, 400)

  log = ProjectLogModel.get(log_id)
  if not log:
      return custom_response({'error': 'Project not found'}, 404)
  log.update(data)
  log_data = log_schema.dump(log).data
  return custom_response(log_data, 202)

@log_api.route('/<string:log_id>', methods=['GET'])
def get(log_id):
  """Get project Log"""
  log = ProjectLogModel.get(log_id)
  if not log:
      return custom_response({'error': 'Project Log not found'}, 404)
  log_data = log_schema.dump(log).data
  return custom_response(log_data, 200)

@log_api.route('/', methods=['GET'])
def get_all():
  """Get project log"""
  logs = ProjectLogModel.view_all_projects()
  log_data = logs_schema.dump(logs).data
  return custom_response(log_data, 200)

@log_api.route('/<string:supervisor_id>/supervisor', methods=['GET'])
def get_by_supervisor():
  """Get Projects under supervisor"""
  logs = ProjectLogModel.view_all_projects()
  log_data = logs_schema.dump(logs).data
  return custom_response(log_data, 200)

@log_api.route('/<string:student_id>/student', methods=['GET'])
def get_by_created_by(student_id):
  """Get project by who created it"""
  log = ProjectLogModel.get_by_student(student_id)
  log_data = logs_schema.dump(log).data
  return custom_response(log_data, 200)

@log_api.route('/<string:group_id>/group', methods=['GET'])
def get_by_groupid(group_id):
  """Get project by who created it"""
  log = ProjectLogModel.get_by_groupid(group_id)
  log_data = logs_schema.dump(log).data
  return custom_response(log_data, 200)