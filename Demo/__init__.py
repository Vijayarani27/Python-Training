from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api


app = Flask(__name__)
#HOST='0.0.0.0'
#PORT=3200

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\USER\\VSworkspace\\CaseStudy\\Bank.sqlite3'
app.config['SECRET_KEY'] = 'your secret key'
#track_modifications = app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db =SQLAlchemy(app)
ma = Marshmallow(app)
api=Api(app)

from Demo import view
from Demo import auth
from microservice import model
from microservice import schema

if __name__ == "__main__":
    app.run()