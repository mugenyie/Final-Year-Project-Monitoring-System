#src/app.py

from flask import Flask

from .config import app_config
from .models import db, bcrypt
from .apiviews.SupervisorView import supervisor_api
from .apiviews.StudentView import student_api
from .apiviews.AdminView import admin_api

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
  app.register_blueprint(supervisor_api, url_prefix='{}supervisors'.format(api_version))
  app.register_blueprint(student_api, url_prefix='{}students'.format(api_version))
  app.register_blueprint(admin_api, url_prefix='{}admin'.format(api_version))

  @app.route('/', methods=['GET'])
  def index():
    """
    initial endpoint
    """
    return 'Hello world! this is the future home of FYPMS'
  
  return app