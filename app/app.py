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

#getting all the restaurants
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

#getting a single restaurant
@app.route('/restaurants/<int:id>',methods=['GET'])
def one_restaurant(id):
  restaurant=Restaurant.query.filter_by(id=id).first()

  if restaurant == None:
        response_body={
              "error": "Restaurant not found"
        }
        response = make_response(jsonify(response_body),404)
        return response
  else:
            if request.method == 'GET':
                 #getting the pizzas for that restaurant
                pizzas=RestaurantPizza.query.filter_by(restaurant_id=id).all()
                pizza_details=[]

                for pizza in pizzas:
                    pizza_info={
                        "id": pizza.pizza.id,
                        "name": pizza.pizza.name,
                        "ingredients": pizza.pizza.ingredients
                    }
                    pizza_details.append(pizza_info)

                restaurant_details={
                "id": restaurant.id,
                    "name": restaurant.name,
                    "address": restaurant.address,
                    "pizzas": pizza_details
                }
                response =make_response(jsonify(restaurant_details),200)
                return response
          
  #deleting a restaurant
@app.route('/restaurants/<int:id>',methods=['DELETE'])
def delete_restaurant(id):
    restaurant=Restaurant.query.filter_by(id=id).first()
    #if no restaurant is found

    if restaurant is None:
        response_body={
             "error": "Restaurant not found" 
        }
        response = make_response(jsonify(response_body), 404)
        return response
    #deleting the associated restaurant pizza first
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()

    #deleting the restaurant
    db.session.delete(restaurant)
    db.session.commit()

    return '',204
#getting all the pizzas
@app.route('/pizzas',methods=['GET'])
def pizzas():
  pizzas=Pizza.query.all()
  pizza_data=[] #list to store the data

  for pizza in pizzas:
    pizza_details={
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients,
    }
    pizza_data.append(pizza_details)

  response=make_response(jsonify(pizza_data),200)
  return response

#posting a restaurant pizza 
@app.route('/restaurant_pizzas/',methods=['POST'])
def create_restuarantpizza():
    #extrating data from the form
    price=int(request.form.get('price'))
    pizza_id=int(request.form.get('pizza_id'))
    restaurant_id=int(request.form.get('restaurant_id'))
   
   #validating the price
    if price <1 or price >30:
        response_body = {
            "errors": ["Price must be between 1 and 30"]
        }
        response = make_response(jsonify(response_body), 400)
        return response
    #checking if the pizza and restaurant exist
    pizza=Pizza.query.get(pizza_id)
    restaurant=Restaurant.query.get(restaurant_id)

    if not (pizza and restaurant):
            response_body = {
                "errors": ["Pizza or Restaurant not found"]
            }
            response = make_response(jsonify(response_body), 404)
            return response
     
     #creating the new restaurant
    new_restaurantpizza=RestaurantPizza(
        price=price,
        pizza_id=pizza_id,
        restaurant_id=restaurant_id
    )
    db.session.add(new_restaurantpizza)
    db.session.commit()
    
    #response data
    response={
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
    }
    response_data=make_response(jsonify(response),201)
    return response_data
if __name__=='__main__':
  app.run(port=5555,debug=True)
