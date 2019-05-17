#/src/views/ProjectView

from flask import request, json, Response, Blueprint, g
from flask_cors import CORS, cross_origin
from ..models.ProjectModel import ProjectModel, ProjectSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

project_api = Blueprint('project_api', __name__)
project_schema = ProjectSchema()
projects_schema = ProjectSchema(many=True)

@project_api.route('/', methods=['POST'])
@cross_origin()
def create():
  """
  Create new project
  """
  req_data = request.get_json(force=True)
  data, error = project_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  project = ProjectModel(data)
  project.save()
  project_data = project_schema.dump(project).data
  return custom_response(project_data, 201)

@project_api.route('/<string:project_id>', methods=['PUT'])
def update(project_id):
  """Update Project"""
  req_data = request.get_json()
  data, error = project_schema.load(req_data, partial=True)
  if error:
      return custom_response(error, 400)

  project = ProjectModel.get_project(project_id)
  if not project:
      return custom_response({'error': 'Project not found'}, 404)
  project.update(data)
  project_data = project_schema.dump(project).data
  return custom_response(project_data, 202)

@project_api.route('/<string:project_id>', methods=['GET'])
def get(project_id):
  """Get project"""
  project = ProjectModel.get_project(project_id)
  if not project:
      return custom_response({'error': 'Project not found'}, 404)
  project = ProjectModel.get_project(project_id)
  project_data = project_schema.dump(project).data
  return custom_response(project_data, 200)

@project_api.route('/', methods=['GET'])
def get_all():
  """Get project"""
  projects = ProjectModel.view_all_projects()
  project_data = projects_schema.dump(projects).data
  return custom_response(project_data, 200)

@project_api.route('/<string:supervisor_id>/supervisor', methods=['GET'])
def get_by_supervisor():
  """Get Projects under supervisor"""
  projects = ProjectModel.view_all_projects()
  project_data = projects_schema.dump(projects).data
  return custom_response(project_data, 200)

@project_api.route('/<string:created_by>/createdby', methods=['GET'])
def get_by_created_by(created_by):
  """Get project by who created it"""
  project = ProjectModel.get_by_createdby(created_by)
  project_data = project_schema.dump(project).data
  return custom_response(project_data, 200)