from App.database import db

class UserCompetition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comp_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    user_id =  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)