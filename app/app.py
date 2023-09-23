from flask import Flask,request,make_response,jsonify
from flask_migrate import Migrate

from models import db,Restaurant,RestaurantPizza,Pizza

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.json.compact=False

migrate=Migrate(app,db)

db.init_app(app)
