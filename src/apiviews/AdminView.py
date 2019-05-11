#/src/views/AdminView

from flask import request, json, Response, Blueprint, g
from ..models.AdminModel import AdminModel, AdminSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

admin_api = Blueprint('admin_api', __name__)
admin_schema = AdminSchema()


@admin_api.route('/', methods=['POST'])
def create():
  """
  Create new Admin
  """
  req_data = request.get_json()
  data, error = admin_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = AdminModel.get_by_email(data.get('email'))
  if user_in_db:
    message = {'error': 'User with Email {} already exists'.format(data.get('email'))}
    return custom_response(message, 400)
  
  user = AdminModel(data)
  user.save()
  user_data = admin_schema.dump(user).data
  token = Auth.generate_token(user_data.get('id'), user_data.get('user_role_value'))
  return custom_response({'token': token, 'data': user_data}, 201)

@admin_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
  """
  Get all admins
  """
  admins = AdminModel.get_all()
  return custom_response(admin_schema.dump(admins).data, 200)

@admin_api.route('/<string:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
  """
  Get a single student
  """
  user = AdminModel.get(user_id)
  if not user:
    return custom_response({'error': 'student not found'}, 404)
  
  user_data = admin_schema.dump(user).data
  return custom_response(user_data, 200)

@admin_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
    """
    Update me
    """
    req_data = request.get_json()
    data, error = admin_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    user = AdminModel.get(g.user.get('id'))
    user.update(data)
    user_data = admin_schema.dump(user).data
    return custom_response(user_data, 200)

@admin_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
  """
  Delete me
  """
  user = AdminModel.get(g.user.get('id'))
  user.delete()
  return custom_response({'message': 'deleted'}, 204)

@admin_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  user = AdminModel.get(g.user.get('id'))
  user_data = admin_schema.dump(user).data
  return custom_response(user_data, 200)

@admin_api.route('/login', methods=['POST'])
def login():
  """
  Admin Login Api
  """
  req_data = request.get_json()

  data, error = admin_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  user = AdminModel.get_by_email(data.get('email'))
  if not user:
    return custom_response({'error': 'invalid credentials'}, 400)
  if not user.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  user_data = admin_schema.dump(user).data
  token = Auth.generate_token(user_data.get('id'), user_data.get('user_role_value'))
  return custom_response({'api-token': token, 'data':'user_data'}, 200)