#/src/views/StatView

from flask import request, json, Response, Blueprint, g, jsonify
from flask_cors import CORS, cross_origin
from ..models import SupervisorModel, StudentModel, AdminModel, GroupModel
from ..services.AuthorizationService import Auth
from . import custom_response

stat_api = Blueprint("stat_api", __name__)

@stat_api.route('/', methods=['GET'])
def get():
    """Get site statistics"""
    student_stat = StudentModel.query.count()
    group_stat = GroupModel.query.count()
    supervisor_stat = SupervisorModel.query.count()
    admin_stat = AdminModel.query.count()
    return custom_response({'student':student_stat,'group':group_stat,'supervisor':supervisor_stat, 'admin':admin_stat}, 200)