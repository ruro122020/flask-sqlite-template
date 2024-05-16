#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random
# Remote library imports
from faker import Faker

# Local imports
from app import app
from models.models import User
from config import db

if __name__ == '__main__':
  fake = Faker()

  with app.app_context():
    print("Starting seed...")
    # Seed code goes here!
    print('Deleting all records...')
    User.query.delete()


    users = []
    usernames = []
    for i in range(5):
      username = fake.first_name()
      email = f'{fake.last_name()}@{fake.domain_name()}'
      #this while is to check if a username already exist
      while username in usernames:
          username = fake.first_name()
      usernames.append(username)
      
      user = User(
          name=fake.name(),
          username=username,
          email=email
          )
      
      user.password_hash = user.username + 'password'

      users.append(user)
    
    db.session.add_all(users)
    db.session.commit()



print('Complete.')