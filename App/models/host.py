from App.database import db

class Host(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    website = db.Column(db.String, nullable=True)
    