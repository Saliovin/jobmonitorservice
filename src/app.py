from flask import Flask
from .config import app_config
from .models import db
from .views.job_view import job_api as job_blueprint
from .views.state_view import state_api as state_blueprint


def create_app(env_name):
    app = Flask(__name__)
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    app.register_blueprint(job_blueprint, url_prefix='/modulelogs/')
    app.register_blueprint(state_blueprint, url_prefix='/modulelogs/<job_id>/')

    return app
