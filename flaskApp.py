# Import the Flask library
from flask import Flask

# Import the request library from Flask
from flask import request
as
# Import the library to deal with JSON objects
import json

# Create an application 'app', that is a Flask object
app = Flask(__name__)

# Bind a URI to the index() function
@app.route("/myshop.com/fruits", methods=['GET', 'POST', 'PUT', 'DELETE'])
def homePage():

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

    # GET request - retrieve the full 'fruits' list
    if request.method == "GET":
        # Return the 'fruits' list in JSON
        return json.dumps(fruitList)

    # POST request - add a fruit to the 'fruits' list
    elif request.method == "POST":
        # Add the request data to the end of the list
        fruitList["fruits"].append(str(request.form["fruit"]))
        # Return the new 'fruits' list in JSON
        return json.dumps(fruitList)

    # PUT request - overwrites the 'fruits' list
    elif request.method == "PUT":
        # Empty the list of fruits
        fruitList["fruits"].clear()
        # Add the request data to the empty list
        fruitList["fruits"].extend(list(request.form.getlist("fruits")))
        # Return the new 'fruits' list in JSON
        return json.dumps(fruitList)

    # DELETE request - empty the fruits 'fruits' list
    elif request.method == "DELETE":
        # Empty the list of fruits
        fruitList["fruits"].clear()
        # Return the new 'fruits' list in JSON
        return json.dumps(fruitList)

    # Return a default message for any other potential requests that may be received
    else:
        return "Unknown request received"