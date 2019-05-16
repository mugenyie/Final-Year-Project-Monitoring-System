#/src/views/GroupView

from flask import request, json, Response, Blueprint, g
from ..models.GroupModel import GroupModel, GroupSchema
from ..models.StudentModel import StudentModel, StudentSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

group_api = Blueprint('group_api', __name__)
group_schema = GroupSchema()

@group_api.route('/', methods=['POST'])
def create():
  """
  Create new group
  """
  req_data = request.get_json()
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

