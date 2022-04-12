import os
import json
from datetime import datetime

import crud
import model
import server

os.system("dropdb tastings")
os.system('createdb tastings')

model.connect_to_db(server.app)
model.db.create_all()

user_data = [
    {"username": "user1",
    "email": "user1@email.com",
    "fname": "Adele",
    "lname":"Applebottom"},
    {"username": "user2",
    "email": "user2@email.com",
    "fname": "Benny",
    "lname":"Beeboop"},
    {"username": "user3",
    "email": "user3@email.com",
    "fname": "Chester",
    "lname":"Chancey"}]

users_in_db = []

for user in user_data:
    username = user["username"]
    email = user["email"]
    fname = user["fname"]
    lname = user["lname"]

    created_user = crud.create_user(username, email, fname, lname)
    users_in_db.append(created_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()