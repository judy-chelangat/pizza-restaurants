from flask import Flask,request,make_response,jsonify
from flask_migrate import Migrate

from models import db,Restaurant,RestaurantPizza,Pizza

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

app.json.compact=False

migrate=Migrate(app,db)

db.init_app(app)

#creating the routes 
#home route
@app.route('/')
def home():
  return '<h1>Welcome to restaurants</h1>'

@app.route('/restaurants',methods=['GET'])
def restaurants():
  restaurants=Restaurant.query.all()
  restaurants_data=[] #list to store the data

  for restaurant in restaurants:
    restaurant_details={
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
    }
    restaurants_data.append(restaurant_details)
    response=make_response(jsonify(restaurants_data),200)
  return response

if __name__=='__main__':
  app.run(port=5555,debug=True)
