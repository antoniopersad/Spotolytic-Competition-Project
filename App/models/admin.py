from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
#from competition_observer import Observer
from observer import Observer

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    # Observer list to hold registered observers
    observers = []

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def add_observer(self, observer):
        """Add an observer to the list."""
        self.observers.append(observer)

    def remove_observer(self, observer):
        """Remove an observer from the list."""
        self.observers.remove(observer)

    def notify_observers(self):
        """Notify all observers."""
        for observer in self.observers:
            observer.update(self)
