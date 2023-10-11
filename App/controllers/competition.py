from . import ensure_admin
from flask_restful import Resource
from flask import jsonify, request, make_response
from flask_jwt_extended import current_user
from App.models import Competition,User, UserCompetition
from App.database import db

class CompetitionController(Resource):
    decorators = [ensure_admin]

    def post(self):
        json_data=request.get_json(force=True)
        name=json_data['name']
        location=json_data['location']
        newcomp = Competition(name = name, location = location)
        db.session.add(newcomp)
        db.session.commit()
        return jsonify(newcomp=Competition.toDict())

    def get_all_competitions():
        return Competition.query.all()

    def get_all_competitions_json():
        competition = Competition.query.all()

        if not competition:
            return []
        else:
            return [comp.toDict() for comp in competition]


    def get(self):
        json_data=request.get_json(force=True)
        id=json_data['id']
        competition = Competition.query.get(id)
        return competition


def add_results(comp_id, user_id):
    Comp = get_competition_by_id(comp_id)

    if Comp:
        user = User.query.get(user_id)
        if user:

            compParticipant = UserCompetition(user_id = user.id, comp_id = Comp.id)
            db.session.add(compParticipant)
            db.session.commit 
            print("successfully added user to comp")



def get_competition_users(comp_id):
    Comp = get_competition_by_id(comp_id)
    

    if Comp:
        compUsers = Comp.participants
        Participants = [User.query.get(part.user_id) for part in compUsers]
        print(Participants)
