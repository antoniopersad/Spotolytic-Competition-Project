from App.models import Competition,User, UserCompetition
from App.database import db

def create_competition(name, location):
    newcomp = Competition(name = name, location = location)
    db.session.add(newcomp)
    db.session.commit()
    return newcomp

def get_all_competitions():
    return Competition.query.all()

def get_all_competitions_json():
    competition = Competition.query.all()

    if not competition:
        return []
    else:
        return [comp.toDict() for comp in competition]


def get_competition_by_id(id):
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
