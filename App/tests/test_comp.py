import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Competition
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,

    create_competition,
    get_all_competitions,
    get_all_competitions_json,
    get_competition_by_id,

    add_results,
    get_competition_users


)


LOGGER = logging.getLogger(__name__)



'''
   Unit Tests
'''

class CompUnitTests(unittest.TestCase):

    def test_new_comp(self):
        testComp = Competition("Walktime", "Port of Spain")
        assert testComp.name


    def test_comp_json(self):
        testComp = Competition("Walktime", "Port of Spain")
        testComp_json = testComp.get_json()
        self.assertDictEqual(testComp_json, {"id":None, "name":"Walktime", "location": "Port of Spain"})


# class CompIntegrationTests()

#     # def test_new_user(self):
#     #     user = User("bob", "bobpass")
#     #     assert user.username == "bob"

