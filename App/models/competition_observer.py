
from App.models.admin import Admin
from App.models.user import User
from observer import Observer

class CompetitionObserver(Observer):
    def __init__(self, observer_id, name, location, date, rank):
        self.id = observer_id
        self.name = name
        self.location = location
        self.date = date
        self.rank = rank

    def update(self, subject):
        if isinstance(subject, User): 
            print(f"User {subject.username} participated in competition {self.name} and achieved rank {self.rank}.")

        elif isinstance(subject, Admin):
            print(f"Admin {subject.username} received an update about competition {self.name} with rank {self.rank}.")