from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from random import seed
from random import randint
import random
import string
app = Flask(__name__)
CORS(app)

seed(1)

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'name' : 'Charlie',
         'job': 'Janitor',
      },
      {
         'id' : 'abc123', 
         'name': 'Mac',
         'job': 'Bouncer',
      },
      {
         'id' : 'ppp222', 
         'name': 'Mac',
         'job': 'Professor',
      }, 
      {
         'id' : 'yat999', 
         'name': 'Dee',
         'job': 'Aspring actress',
      },
      {
         'id' : 'zap555', 
         'name': 'Dennis',
         'job': 'Bartender',
      }
   ]
}

@app.route('/')
def hello_world():
    return 'Hello, World!'
    
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('name') 
      search_job = request.args.get('job')
      if search_job:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username: 
               if user['job'] == search_job:
                    subdict['users_list'].append(user)
         return subdict
      elif search_username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['name'] == search_username: 
                subdict['users_list'].append(user)          
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      userToAdd['id'] = randID()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd)
      resp.status_code = 201
      return resp
   elif request.method == 'DELETE':
      userToDelete = request.get_json()
      users['users_list'].remove(userToDelete)
      resp = jsonify(success=True)
      resp.status_code = 200
      return resp
   
@app.route('/users/<id>')
def get_user(id):
   if id :
      for user in users['users_list']:
        if user['id'] == id:
           return user
      return ({})
   return users
   
def randID():
    letters = string.ascii_lowercase
    rand_str = ''.join(random.choice(letters) for i in range(3))
    rand_nums = randint(0, 1024)
    return rand_str + str(rand_nums)