from random import randint,choice as rc
import random
from faker import Faker

from app import app
from models import db,Restaurant,RestaurantPizza,Pizza

fake=Faker()

with app.app_context():
    #clearing the existing data
    RestaurantPizza.query.delete()
    Pizza.query.delete()
    Restaurant.query.delete()

#seeding the restaurants
    restaurants=[] #empty list to store the restaurant 
    for i in range(20):
        b=Restaurant(name=fake.company(),
                     address=fake.address())
        restaurants.append(b)
    
    db.session.add_all(restaurants)
 

#seeding the pizzas
    pizzas = []
    pizza_names = [
    'Margherita', 'Pepperoni', 'Hawaiian', 'Vegetarian', 'Supreme',
    'Mushroom', 'BBQ Chicken', 'Sausage', 'Seafood', 'Pesto',
    'Buffalo Chicken', 'Veggie Deluxe', 'Four Cheese', 'Meat Lovers',
    'Vegan Delight', 'White Pizza', 'Taco Pizza', 'Greek Pizza', 'Hawaiian BBQ',
    'Bacon Cheeseburger', 'Spinach and Feta'
]
    
#  selecting  unique pizza names
    unique_pizza_names = random.sample(pizza_names, 20)

    for name in unique_pizza_names:
        ingredients = fake.sentence(nb_words=6)
        newdata = Pizza(name=name, ingredients=ingredients)
        pizzas.append(newdata)

    db.session.add_all(pizzas)
    db.session.commit()

#seeding restaurant pizzas
    restaurant_pizzas=[]
    for j in range(20):
        price=randint(1,30)
        pizza=rc(pizzas)
        restaurant=rc(restaurants)
        randompizza=RestaurantPizza(price=price,pizza=pizza,restaurant=restaurant)
        restaurant_pizzas.append(randompizza)

    db.session.add_all(restaurant_pizzas)
    db.session.commit()

    print('seeding completed ')
