# Import the Flask library
from flask import Flask

# Import the request library from Flask
from flask import request

# Import the library to deal with JSON objects
import json

# Create an application 'app', that is a Flask object
app = Flask(__name__)

# Create a varible to store a list of the different fruits, in a dictionary
fruitList = {
    "fruits": [
        "apple",
        "pear",
        "orange",
        "mango",
        "kiwi",
        "strawberry"
    ]
}

# Bind a URI to the function
# GET request - retrieve the full 'fruits' list
@app.route("/myshop.com/fruits", methods=['GET'])
def get_fruits():
    # Return the 'fruits' list in JSON
    return json.dumps(fruitList)

# POST request - add a fruit to the 'fruits' list
@app.route("/myshop.com/fruits", methods=['POST'])
def post_fruits():
    # Add the request data to the end of the list
    fruitList["fruits"].append(str(request.form["fruit"]))

    # Return the new 'fruits' list in JSON
    return json.dumps(fruitList)

# PUT request - overwrites the 'fruits' list
@app.route("/myshop.com/fruits", methods=['PUT'])
def put_fruits():
    # Empty the list of fruits
    fruitList["fruits"].clear()

    # Add the request data to the empty list
    fruitList["fruits"].extend(list(request.form.getlist("fruits")))

    # Return the new 'fruits' list in JSON
    return json.dumps(fruitList)

# DELETE request - empty the fruits 'fruits' list
@app.route("/myshop.com/fruits", methods=['DELETE'])
def delete_fruits():
    # Empty the list of fruits
    fruitList["fruits"].clear()
    
    # Return the new 'fruits' list in JSON
    return json.dumps(fruitList)
