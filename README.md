# Flask Code Challenge - Pizza Restaurants

Welcome to the Flask Code Challenge for Pizza Restaurants! This challenge involves  building a Flask API to manage pizza restaurants. This README provides an overview of the challenge, instructions for setting up the project, and details on how to use the API.

## Introduction

 Pizza Restaurant domain, developing a Flask API with the following functionalities:

- Creation of models and relationships for Restaurants, Pizzas, and RestaurantPizzas.
- Implementing validations for RestaurantPizza and Restaurant models.
- Setting up routes to manage restaurants and pizzas, including listing, retrieving, deleting, and creating associations between existing pizzas and restaurants.

## Getting Started

Follow these steps to get started with the project:

1. Clone this repository to your local machine.
2. Ensure you have Python and Flask installed on your system.
3. Navigate to the project directory:
   cd pizzarestaurants
4. Set up a virtual environment:

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate` <br>
5. Install the required dependencies:

6. Run the Flask server:
    python app.py

Now, your Flask server is up and running, ready to handle API requests.
## Usage

You can use Postman or any API testing tool to interact with the API endpoints. Here are the available routes and their functionalities:
# GET /restaurants

    Description: Retrieve a list of all restaurants.
    Response Format:

    json

    [
      {
        "id": 1,
        "name": "Dominion Pizza",
        "address": "Good Italian, Ngong Road, 5th Avenue"
      },
      {
        "id": 2,
        "name": "Pizza Hut",
        "address": "Westgate Mall, Mwanzi Road, Nrb 100"
      }
    ]

# GET /restaurants/:id

    Description: Retrieve a restaurant by its ID along with its pizzas.
    Response Format:
        If the restaurant exists:

        json

{
  "id": 1,
  "name": "Dominion Pizza",
  "address": "Good Italian, Ngong Road, 5th Avenue",
  "pizzas": [
    {
      "id": 1,
      "name": "Cheese",
      "ingredients": "Dough, Tomato Sauce, Cheese"
    },
    {
      "id": 2,
      "name": "Pepperoni",
      "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
    }
  ]
}

# If the restaurant does not exist, return:

json

        {
          "error": "Restaurant not found"
        }

# DELETE /restaurants/:id

    Description: Delete a restaurant by its ID along with associated RestaurantPizzas.
    Response Format:
        If the restaurant is deleted successfully:
            HTTP Status Code: 204 (No Content)
        If the restaurant does not exist, return:

        json

        {
          "error": "Restaurant not found"
        }

# GET /pizzas

    Description: Retrieve a list of all pizzas.
    Response Format:

    json

    [
      {
        "id": 1,
        "name": "Cheese",
        "ingredients": "Dough, Tomato Sauce, Cheese"
      },
      {
        "id": 2,
        "name": "Pepperoni",
        "ingredients": "Dough, Tomato Sauce, Cheese, Pepperoni"
      }
    ]

# POST /restaurant_pizzas

    Description: Create a new RestaurantPizza associated with an existing Pizza and Restaurant.
    Request Body Format:

    json

{
  "price": 5,
  "pizza_id": 1,
  "restaurant_id": 3
}

# Response Format (If successful):

json

{
  "id": 1,
  "name": "Cheese",
  "ingredients": "Dough, Tomato Sauce, Cheese"
}

# Response Format (If not successful - validation errors):

json

    {
      "errors": ["validation errors"]
    }

## Author

    Author: Judy Chelangat
  
## License

This project is licensed under the MIT License.