from flask import Blueprint, render_template, jsonify, request, send_from_directory, flash, redirect, url_for
from flask_jwt_extended import jwt_required, current_user as jwt_current_user
from flask_login import current_user, login_required

from.index import index_views

from App.controllers import (
    # create_user,
    # jwt_authenticate, 
    # get_all_users,
    # get_all_users_json,
    jwt_required,
    create_competition


)


comp_views = Blueprint('comp_views', __name__, template_folder='../templates')


##return the json list of competitions fetched from the db
@comp_views.route('/competitions', methods=['GET'])
def get_competitons():
    competitions = get_all_competitions_json()
    return jsonify(competitions) 

##add new competition to the db
@comp_views.route('/competitions', methods=['POST'])
def add_new_comp():
    data = request.json
    create_competition(data['name'], data['location'])
    return jsonify({'message': f"competition {data['name']} created"})


@comp_views.route('/competitions/user', methods=['POST'])
def add_comp_user():
    data = request.json
    add_new_user()
    return ('customer added to competition')






