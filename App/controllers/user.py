from App.models import User, Competition, UserCompetition
from App.database import db
import json 

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None
    
def get_ranked_users():
    return User.query.order_by(User.rank.asc()).all()


# def compute_overall_rank():
#     competitions = 

def add_user_to_comp(user_id, comp_id, rank):
    # user_id = request.form['user_id']
    # comp_id = request.form['comp_id']

    user = User.query.get(user_id)
    comp = Competition.query.get(comp_id)

    
    if user and comp:
        user_comp = UserCompetition(user_id=user.id, comp_id=comp.id, rank = rank)
        db.session.add(user_comp)
        db.session.commit()
        print("success")
        

    return 'Error adding user to competition'


def get_user_competitions(user_id):
    user = User.query.get(user_id)
    userComps = user.competitions
    
    competitions = [Competition.query.get(inst.comp_id) for inst in userComps]
    print(competitions)
    print( [c.toDict() for c in competitions] )
    return competitions





def update_ranks():
  users = User.query.order_by(User.rank.asc()).limit(20).all()
  
  # Store current ranks
  ranks = {u.id: u.rank for u in users}
  
  # Update ranks
  db.session.query(User).update({User.rank: User.rank + 1})  
  db.session.commit()

  # Check if ranks changed
  for u in users:
    if u.rank != ranks[u.id]:
      send_notification(u, f"Your rank changed from {ranks[u.id]} to {u.rank}")
    

def get_user_rankings(user_id):
    users = User.query.get(user_id)
    userComps = users.competitions
    return userComps
    