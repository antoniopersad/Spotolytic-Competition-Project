from App.controllers import ensure_admin
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_jwt_extended import current_user
from App.models import Competition
from App.database import db

class CompetitionsController(Resource):
    decorators = [ensure_admin]

    def get(self):
        competition = Competition.query.all()

        if not competition:
            return []
        else:
            return jsonify(competitions=[comp.toDict() for comp in competition])