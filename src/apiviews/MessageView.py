#/src/views/ProjectView

from flask import request, json, Response, Blueprint, g
from ..models.MessageModel import MessageModel, MessageSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

log_api = Blueprint('log_api', __name__)
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

@log_api.route('/', methods=['POST'])
def create():
  """
  Create new message
  """
  req_data = request.get_json(force=True)
  data, error = message_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  log = MessageModel(data)
  log.save()
  log_data = message_schema.dump(log).data
  return custom_response(log_data, 201)


@log_api.route('/<string:log_id>', methods=['GET'])
def get(log_id):
  """Get project Log"""
  log = MessageSchema.get(log_id)
  if not log:
      return custom_response({'error': 'Project Log not found'}, 404)
  log_data = message_schema.dump(log).data
  return custom_response(log_data, 200)