#/src/views/StudentView

from flask import request, json, Response, Blueprint, g
from ..models.StudentModel import StudentModel, StudentSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

student_api = Blueprint('student_api', __name__)
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)

@student_api.route('/', methods=['POST'])
def create():
  """
  Create new student
  """
  req_data = request.get_json()
  data, error = student_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  # check if user already exist in the db
  user_in_db = StudentModel.get_by_student_number(data.get('student_number'))
  if user_in_db:
    message = {'error': 'User with student number {} already exists'.format(data.get('student_number'))}
    return custom_response(message, 400)
  
  student = StudentModel(data)
  student.save()
  student_data = student_schema.dump(student).data
  token = Auth.generate_token(student_data.get('id'), student_data.get('user_role_value'))
  return custom_response({'api_token': token, 'user':student_data}, 201)

@student_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
  """
  Get all students
  """
  students = StudentModel.get_all()
  return custom_response(students_schema.dump(students).data, 200)

@student_api.route('/group/<string:group_id>/members', methods=['GET'])
@Auth.auth_required
def get_group_members(group_id):
  students = StudentModel.view_group_members(group_id)
  return custom_response(students_schema.dump(students).data, 200)

@student_api.route('/<string:user_id>', methods=['GET'])
@Auth.auth_required
def get_a_user(user_id):
  """
  Get a single student
  """
  student = StudentModel.get(user_id)
  if not student:
    return custom_response({'error': 'student not found'}, 404)
  
  student_data = student_schema.dump(student).data
  return custom_response(student_data, 200)

@student_api.route('/me', methods=['PUT'])
@Auth.auth_required
def update():
    """
    Update me
    """
    req_data = request.get_json()
    data, error = student_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)

    student = StudentModel.get(g.user.get('id'))
    student.update(data)
    student_data = student_schema.dump(student).data
    return custom_response(student_data, 200)

@student_api.route('/me', methods=['DELETE'])
@Auth.auth_required
def delete():
  """
  Delete a user
  """
  student = StudentModel.get(g.user.get('id'))
  student.delete()
  return custom_response({'message': 'deleted'}, 204)

@student_api.route('/me', methods=['GET'])
@Auth.auth_required
def get_me():
  """
  Get me
  """
  user = StudentModel.get(g.user.get('id'))
  ser_user = student_schema.dump(user).data
  return custom_response(ser_user, 200)


@student_api.route('/login', methods=['POST'])
def login():
  """
  User Login Function
  """
  req_data = request.get_json()

  data, error = student_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  if not data.get('email') or not data.get('password'):
    return custom_response({'error': 'you need email and password to sign in'}, 400)
  user = StudentModel.get_by_email(data.get('email'))
  if not user:
    return custom_response({'error': 'invalid credentials'}, 400)
  if not user.check_hash(data.get('password')):
    return custom_response({'error': 'invalid credentials'}, 400)
  ser_data = student_schema.dump(user).data
  token = Auth.generate_token(ser_data.get('id'), ser_data.get('user_role_value'))
  return custom_response({'api_token': token, 'user':ser_data}, 200)