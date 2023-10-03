from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String, nullable=False, unique=True)
    year = 
    level = 
    host 
    location = db.Column(db.String(120), nullable=False)