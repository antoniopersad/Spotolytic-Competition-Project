from App.models import Competition
from App.database import db


def create_competition(name, location):
    newcomp = Competition(name = name,location = location)
    db.session.add(newcomp)
    db.session.commit()
    return newcomp


