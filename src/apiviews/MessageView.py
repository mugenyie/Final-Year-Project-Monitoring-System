#/src/views/ProjectView

from flask import request, json, Response, Blueprint, g
from ..models.MessageModel import MessageModel, MessageSchema
from ..services.AuthorizationService import Auth
from ..apiviews import custom_response

message_api = Blueprint('message_api', __name__)
message_schema = MessageSchema()
messages_schema = MessageSchema(many=True)

@message_api.route('/', methods=['POST'])
def create():
  """
  Create new message
  """
  req_data = request.get_json(force=True)
  data, error = message_schema.load(req_data)

  if error:
    return custom_response(error, 400)
  
  message = MessageModel(data)
  message.save()
  message_data = message_schema.dump(message).data
  return custom_response(message_data, 201)


@message_api.route('to/<string:to_id>', methods=['GET'])
def get(to_id):
  """Get project Log"""
  messages = MessageModel.get_message_to(to_id)
  log_data = messages_schema.dump(messages).data
  return custom_response(log_data, 200)