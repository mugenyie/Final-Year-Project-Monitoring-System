#src/app.py

from flask import Flask, render_template
from .config import app_config
from .models import db, bcrypt
from .apiviews.SupervisorView import supervisor_api
from .apiviews.StudentView import student_api
from .apiviews.AdminView import admin_api
from .apiviews.GroupView import group_api, groups_api
from .apiviews.ProjectView import project_api
from .apiviews.StatView import stat_api
from .apiviews.ProjectLogView import log_api
from .apiviews.MessageView import message_api

def create_app(env_name):
  """
  Create app
  """
  
  # app initiliazation
  app = Flask(__name__)
  
  app.config.from_object(app_config[env_name])

  # initializing bcrypt and db
  bcrypt.init_app(app)
  db.init_app(app)

  api_version = "/api/v1/"
  app.register_blueprint(supervisor_api, url_prefix='{}supervisor'.format(api_version))
  app.register_blueprint(student_api, url_prefix='{}student'.format(api_version))
  app.register_blueprint(admin_api, url_prefix='{}admin'.format(api_version))
  app.register_blueprint(group_api, url_prefix='{}group'.format(api_version))
  app.register_blueprint(groups_api)
  app.register_blueprint(project_api, url_prefix='{}project'.format(api_version))
  app.register_blueprint(log_api, url_prefix='{}projectlog'.format(api_version))
  app.register_blueprint(stat_api, url_prefix='{}statistics'.format(api_version))
  app.register_blueprint(message_api, url_prefix='{}message'.format(api_version))

  @app.route('/', methods=['GET'])
  def index():
    return render_template('index.html')

  @app.route('/student', methods=['GET'])
  def student():
    return render_template('student_.html')

  @app.route('/admin', methods=['GET'])
  def admin():
    return render_template('admin_.html')

  @app.route('/supervisor', methods=['GET'])
  def supervisor():
    return render_template('supervisor_.html')

  @app.route('/create_project', methods=['GET'])
  def create_project():
    return render_template('create_project.html')

  @app.route('/create_group', methods=['GET'])
  def create_group():
    return render_template('create_group.html')

  @app.route('/group_members', methods=['GET'])
  def group_members():
    return render_template('group_members.html')

  @app.route('/groups_assigned', methods=['GET'])
  def groups_assigned():
    return render_template('groups_assigned.html')

  @app.route('/groups_unassigned', methods=['GET'])
  def groups_unassigned():
    return render_template('groups_unassigned.html')

  @app.route('/edit_group', methods=['GET'])
  def edit_group():
    return render_template('edit_group.html')

  @app.route('/supervisors', methods=['GET'])
  def supervisors():
    return render_template('supervisors.html')

  @app.route('/students', methods=['GET'])
  def students():
    return render_template('students.html')

  @app.route('/select', methods=['GET'])
  def select():
    return render_template('select.html')

  @app.route('/new-student', methods=['GET'])
  def new_student():
    return render_template('new-student.html')

  @app.route('/new-admin', methods=['GET'])
  def new_admin():
    return render_template('new-admin.html')

  @app.route('/new-supervisor', methods=['GET'])
  def new_supervisor():
    return render_template('new-supervisor.html')

  @app.route('/project_log', methods=['GET'])
  def project_log():
    return render_template('project_log.html')

  @app.route('/view_logs', methods=['GET'])
  def view_logs():
    return render_template('view_logs.html')

  @app.route('/view_group', methods=['GET'])
  def view_group():
    return render_template('view_group.html')

  @app.route('/award_project', methods=['GET'])
  def award_project():
    return render_template('award_project.html')

  @app.route('/group_log', methods=['GET'])
  def group_log():
    return render_template('group_log.html')

  @app.route('/supervisor_message', methods=['GET'])
  def supervisor_message():
    return render_template('supervisor_message.html')

  @app.route('/score_log', methods=['GET'])
  def score_log():
    return render_template('score_log.html')

  @app.route('/report', methods=['GET'])
  def report():
    return render_template('report.html')

  @app.route('/group_messages', methods=['GET'])
  def group_messages():
    return render_template('group_messages.html')

  @app.route('/reply', methods=['GET'])
  def reply():
    return render_template('reply.html')

  @app.route('/all_group_messages', methods=['GET'])
  def all_group_messages():
    return render_template('all_group_messages.html')

  
  return app