from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db=SQLAlchemy() #Setting up the db 

class Restaurant(db.Model): #creating the restaurant model 
    __tablename__='restaurant'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    address=db.Column(db.String,nullable=False)
    

    #name validation
    @validates('name')
    def validate_name(self,key,name):
        if len(name)>50:
            raise ValueError('Name must be less than 50 characters ')
        return name
    
    def __repr__(self):
        return f'<Restaurant {self.name}>'
    


class RestaurantPizza(db.Model):
    __tablename__='restaurant-pizzas'

    id=db.Column(db.Integer,primary_key=True)
    price=db.Column(db.Integer,nullable=False)
    pizza_id=db.Column(db.Integer,db.ForeignKey('pizzas.id'))
    restaurant_id=db.Column(db.Integer,db.ForeignKey('restaurant.id'))
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())

    restaurant=db.relationship('Restaurant',backref='restaurantpizza')
    pizza=db.relationship('Pizza',backref='restaurantpizza')


   #Adding validations
    @validates('price')
    def validate_price(self,key,price):
        if price <1 or price >30:
            raise ValueError('Price must be between 1 and 30')
        return price
    
    def __repr__(self):
        return f'<RestaurantPizza {self.price}>'
    
class Pizza(db.Model):
    __tablename__='pizzas'


    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=True,nullable=False)
    ingredients=db.Column(db.String,nullable=False)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,onupdate=db.func.now())


    def __repr__(self):
        return f'<Pizza {self.name},{self.ingredients}>'
    