from App.database import database

class CompetitionHost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey(competition.id), nullable=False)
    host_id =  db.Column(db.Integer, db.ForeignKey(host.id), nullable=False)

    competition = db.relationship("Competition", lazy=True)
    host = db.relationship("Host", lazy-True)