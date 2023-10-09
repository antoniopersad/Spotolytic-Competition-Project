from App.models import Competition
from App.database import db


def create_competition(name, location):
    newcomp = Competition(name = name,location = location)
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
