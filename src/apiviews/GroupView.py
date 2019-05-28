#/src/views/GroupView

from flask import request, json, Response, Blueprint, g
from flask_cors import CORS, cross_origin
from ..models.GroupModel import GroupModel, GroupSchema
from ..models.StudentModel import StudentModel, StudentSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

group_api = Blueprint('group_api', __name__)
groups_api = Blueprint('groups_api', __name__, url_prefix='/api/v1/groups')
group_schema = GroupSchema()
groups_schema = GroupSchema(many=True)

@group_api.route('/', methods=['POST'])
@cross_origin()
def create():
  """
  Create new group
  """
  req_data = request.get_json(force=True)
  data, error = group_schema.load(req_data)
  if error:
    return custom_response(error, 400)

  existing_group = GroupModel.get_by_group_number(data.get('number'))
  if existing_group:
    message = {'error': 'Group with number "{}" already exists'.format(data.get('number'))}
    return custom_response(message, 400)
  
  group = GroupModel(data)
  group.save()
  group_data = group_schema.dump(group).data
  return custom_response(group_data, 201)

@group_api.route('/<string:group_id>', methods=['GET'])
@Auth.auth_required
def get_a_group(group_id):
  """
  Get a single group
  """
  group = GroupModel.get_by_id(group_id)
  if not group:
    return custom_response({'error': 'Group not found'}, 404)
  
  group_data = group_schema.dump(group).data
  return custom_response(group_data, 200)

@group_api.route('/<string:group_id>/members', methods=['GET'])
@Auth.auth_required
def view_group_members(group_id):
  """
  View group members
  """
  users = GroupModel.view_members(group_id)
  if not users:
    return custom_response({'error': 'Group not found'}, 404)
  
  users = StudentSchema().dump(users).data
  return custom_response(users, 200)

@groups_api.route('/assigned', methods=['GET'])
@Auth.auth_required
def view_groups_assigned():
  """
  Get a assigned groups
  """
  groups = GroupModel.get_groups_assigned()
  group_data =  groups_schema.dump(groups).data
  return custom_response(group_data, 200)

@groups_api.route('<string:supervisor_id>/assigned', methods=['GET'])
@Auth.auth_required
def view_groups_assigned_to_supervisor(supervisor_id):
  """
  Get groups assigned to supervisor
  """
  groups = GroupModel.get_by_supervisor(supervisor_id)
  group_data =  groups_schema.dump(groups).data
  return custom_response(group_data, 200)

@groups_api.route('/unassigned', methods=['GET'])
@Auth.auth_required
def view_groups_unassigned():
  """
  Get a unassigned groups
  """
  groups = GroupModel.get_groups_unassigned()
  group_data =  groups_schema.dump(groups).data
  return custom_response(group_data, 200)

@groups_api.route('<string:group_id>/update', methods=['PATCH'])
@Auth.auth_required
def update_group(group_id):
  """Update group"""
  req_data = request.get_json(force=True)
  data, error = group_schema.load(req_data, partial=True)
  if error:
      return custom_response(error, 400)
  group = GroupModel.get_by_id(group_id)
  group.update_group(data)
  group_data =  group_schema.dump(group).data
  return custom_response(204)