# Import the Flask library
from flask import Flask

# Create an application 'app', that is a Flask object
app = Flask(__name__)

# Bind a URI to the index() function
@app.route("/myshop.com/fruits")
def index():
    # Return a hello world string
    return "Hello World!"