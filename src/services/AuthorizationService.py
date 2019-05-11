#src/services/Authorization
import jwt
import os
import datetime
from flask import json, Response, request, g
from functools import wraps
from ..models.UserModel import UserModel
from ..models.StudentModel import StudentModel
from ..models.SupervisorModel import SupervisorModel
from ..models.AdminModel import AdminModel
from ..apiviews import custom_response
from ..enums.UserRoleEnum import UserRoleEnum

class Auth:
  """
  AuthorizationService Class
  """
  @staticmethod
  def generate_token(user_id, user_role):
    """
    Generate Token Method
    """
    try:
      payload = {
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow(),
        'user_id': user_id,
        'user_role': user_role
      }
      return jwt.encode(
        payload,
        os.getenv('JWT_SECRET_KEY'),
        'HS256'
      ).decode("utf-8")
    except Exception as e:
      return str(e)
      # return custom_response({'error': 'error in generating user token'}, 400)

  @staticmethod
  def decode_token(token):
    """
    Decode token method
    """
    re = {'data': {}, 'error': {}}
    try:
      payload = jwt.decode(token, os.getenv('JWT_SECRET_KEY'))
      re['data'] = {'user_id': payload['user_id'], 'user_role': payload['user_role']}
      return re
    except jwt.ExpiredSignatureError as e1:
      re['error'] = {'message': 'token expired, please login again'}
      return re
    except jwt.InvalidTokenError:
      re['error'] = {'message': 'Invalid token, please try again with a new token'}
      return re

  # decorator
  @staticmethod
  def auth_required(func):
    """
    Auth decorator
    """
    @wraps(func)
    def decorated_auth(*args, **kwargs):
      if 'api-token' not in request.headers:
        return custom_response({'error': 'Authentication token is not available, please login to get one'}, 400)
      token = request.headers.get('api-token')
      data = Auth.decode_token(token)
      if data['error']:
          return custom_response(data['error'], 400)
          
      user_id = data['data']['user_id']
      user_role = data['data']['user_role']

      check_student = StudentModel.get(user_id)
      check_supervisor = SupervisorModel.get(user_id)
      check_admin = AdminModel.get(user_id)
      
      if not (check_student or check_supervisor or check_admin):
        return custom_response({'error': 'user does not exist, invalid token'}, 400)
      g.user = {'id': user_id, 'user_role': user_role}
      return func(*args, **kwargs)
    return decorated_auth