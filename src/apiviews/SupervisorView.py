#/src/views/SupervisorView

from flask import request, json, Response, Blueprint, g, jsonify
from ..models import SupervisorModel, SupervisorSchema
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
    
@supervisor_api.route('/', methods=['GET'])
def get():
    supervisors = SupervisorModel.get_all()
    return custom_response(supervisors_schema.dump(supervisors).data, 200)

@supervisor_api.route('/<int:pk>/', methods=['GET'])
def get_supervisor(pk):
    try:
        supervisor = SupervisorModel.get(pk)
    except Exception:
        return jsonify({'message': 'Supervisor not be found.'}), 400
    result = supervisor_schema.dump(supervisor).data
    return custom_response(result, 200)

@supervisor_api.route('/<int:pk>/', methods=['DELETE'])
def delete(pk):
    supervisor = SupervisorModel.get(pk)
    if supervisor is None:
        return custom_response({"message":"User does not exist"}, 400)
    supervisor.delete()
    return custom_response({"message":"deleted {}".format(supervisor)}, 204)

@supervisor_api.route('/<int:pk>/', methods=['PUT'])
def update(pk):
    req_data = request.get_json()
    data, error = supervisor_schema.load(req_data, partial=True)
    if error:
        return custom_response(error, 400)
    supervisor = SupervisorModel.get(pk)
    supervisor.update(data)
    return custom_response(supervisor_schema.dump(supervisor),200)
