from functools import wraps
from flask_jwt_extended import jwt_required, current_user
from flask import jsonify, make_response, Blueprint, Flask
from flask_restful import Api
from .auth import *
from .competition import * 
from .UserCompetition import *

def ensure_admin(u):
    @wraps(u)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user = current_user
        if user and user.type == 'admin':
            return u(*args, **kwargs)
        return make_response(jsonify(error="Unauthorized"), 401)
    return decorated_function

def register_admin_blueprint(app: Flask) -> Blueprint:

    from .competition import CompetitionController
    from .competitions import CompetitionsController

    # The main blueprint for the admin APIs. All admin endpoints will be of the form /admin/<endpoint>
    admin_blueprint = Blueprint('admin', __name__, url_prefix='/admin')

    admin_api = Api(admin_blueprint)

    admin_api.add_resource(CompetitionController, '/competition')
    admin_api.add_resource(CompetitionsController, '/competitions')

    app.register_blueprint(admin_blueprint)


