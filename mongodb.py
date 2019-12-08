from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo
import os

app = Flask(__name__)

app.config['MONGO_DBNAME'] = os.environ.get('MONGO_DBNAME', 'test')
app.config['MONGO_URI'] = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/test')


mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Sample CRUD operations in MongoDB...'

@app.route('/tenants', methods=['GET'])
def get_all_tenants():
  tenants = mongo.db.tenants
  print(tenants)
  #return jsonify(tenants)
  output = []
  for tenant in tenants.find():
    output.append({ 'name' : tenant['name'], 'email' : tenant['email']})
  return jsonify({'tenants' : output})

@app.route('/tenants/<name>', methods=['GET'])
def get_one_tenant(name):
  print("get one tenant {}".format(name))
  tenants = mongo.db.tenants
  
  tenant = tenants.find_one({'name' : name})
  if tenant:
    output = {'name' : tenant['name'], 'email' : tenant['email']}
  else:
    output = "No tenant found"
  return jsonify({'result' : output})

@app.route('/tenants', methods=['POST'])
def add_tenant():
  tenants = mongo.db.tenants
  name = request.json['name']
  email = request.json['email']
  tenant_id = tenants.insert_one({'name': name, 'email': email})
  new_tenant = tenants.find_one({'name': name })
  output = {'name' : new_tenant['name'], 'email' : new_tenant['email']}
  return jsonify({'result' : output})

if __name__ == '__main__':
    app.run(
        debug="true",
        host="0.0.0.0",
        port=5000
    )

