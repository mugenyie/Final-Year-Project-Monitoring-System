#/src/views/SupervisorView

from flask import request, json, Response, Blueprint, g, jsonify
from ..models import SupervisorModel, SupervisorSchema
from ..services.AuthorizationService import Auth
from . import custom_response


supervisor_api = Blueprint("supervisor_api", __name__)
supervisor_schema = SupervisorSchema()
supervisors_schema = SupervisorSchema(many=True)


@supervisor_api.route('/', methods=['POST'])
def create():
    """Create new supervisor"""
    req_data = request.get_json()
    data, error = supervisor_schema.load(req_data)
    if error:
        return custom_response(error, 400)
    try:
        supervisor = SupervisorModel(data).save()
        data,error = supervisor_schema.dump(supervisor)
        return custom_response({data, error}, 201)
    except Exception:
        return custom_response({"message":"User with email or phone already registered"}, 400)

@Auth.auth_required
@supervisor_api.route('/', methods=['GET'])
def get():
    supervisors = SupervisorModel.get_all()
    return custom_response(supervisors_schema.dump(supervisors).data, 200)

@supervisor_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
    """
    Get me
    """
    user = SupervisorModel.get(g.user.get('id'))
    ser_user = supervisor_schema.dump(user).data
    return custom_response(ser_user, 200)
  
@Auth.auth_required
@supervisor_api.route('/<int:pk>/', methods=['GET'])
def get_supervisor(pk):
    try:
        supervisor = SupervisorModel.get(pk)
    except Exception:
        return jsonify({'message': 'Supervisor not be found.'}), 400
    result = supervisor_schema.dump(supervisor).data
    return custom_response(result, 200)

@Auth.auth_required
@supervisor_api.route('/<int:pk>/', methods=['DELETE'])
def delete(pk):
    supervisor = SupervisorModel.get(pk)
    if supervisor is None:
        return custom_response({"message":"User does not exist"}, 400)
    supervisor.delete()
    return custom_response({"message":"deleted {}".format(supervisor)}, 204)

@Auth.auth_required
@supervisor_api.route('/<int:pk>/', methods=['PUT'])
def update(pk):
    req_data = request.get_json()
    data, error = supervisor_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    supervisor = SupervisorModel.get(pk)
    supervisor.update(data)
    return custom_response(supervisor_schema.dump(supervisor),200)

@Auth.auth_required
@supervisor_api.route('/login', methods=['POST'])
def login():
  """
  Supervisor Login Function
  """
  req_data = request.get_json()

  data, error = supervisor_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  user = SupervisorModel.get_by_email(data.get('email'))
  if not user:
    return custom_response({'error': 'invalid credentials'}, 400)
  if not user.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  user_data = supervisor_schema.dump(user).data
  token = Auth.generate_token(user_data.get('id'), user_data.get('user_role_value'))
  return custom_response({'api_token': token, 'user':user_data}, 200)