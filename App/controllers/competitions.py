from functools import wraps
from flask_jwt_extended import jwt_required, current_user
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_jwt_extended import current_user
from App.models import Competition
from App.database import db

def ensure_admin(u):
    @wraps(u)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user = current_user
        if user and user.type == 'admin':
            return u(*args, **kwargs)
        return make_response(jsonify(error="Unauthorized"), 401)
    return decorated_function

class CompetitionsController(Resource):
    decorators = [ensure_admin]

    def get(self):
        competition = Competition.query.all()

        if not competition:
            return []
        else:
            return jsonify(competitions=[comp.toDict() for comp in competition])