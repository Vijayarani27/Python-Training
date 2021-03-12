from flask import Flask,jsonify

from Demo import app
#from Connect import view
from microservice.model import User
from microservice.schema import UserSchema
from Demo.auth import token_required,get_user


schema=UserSchema(many=True)
schemaone=UserSchema()


@app.route("/")
def index():
    user=get_user()
    print(user)
    return "Hello world"

@app.route("/hello")
def index1():
    all_users=User.query.all()
    result=schema.dump(all_users)
    
    return result