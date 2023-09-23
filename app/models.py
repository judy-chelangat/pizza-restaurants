from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin


db=SQLAlchemy() #Setting up the db 

class Restaurant(db.Model): #creating the restaurant model 
    __tablename__='restaurant'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    address=db.Column(db.String)
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'
    


class RestaurantPizza(db.Model):
    __tablename__='restaurant-pizzas'

    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id'))
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

    restaurant=db.relationship('Restaurant',backref='restaurantpizza')
    pizza=db.relationship('Pizza',backref='restaurantpizza')

    def __repr__(self):
        return f'<RestaurantPizza {self.price}>'
    
class Pizza(db.Model):
    __tablename__='pizzas'


    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True)
    ingredients=db.Column(db.String)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())


    def __repr__(self):
        return f'<Pizza {self.name},{self.ingredients}>'
    