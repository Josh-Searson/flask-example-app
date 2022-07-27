# Program to test the API

# Import the HTTP requests library
import requests

# Variable to store the base URL
BASEURL = "http://127.0.0.1:5000/myshop.com/fruits"

# ------------------------------ GET Request ---------------------------------------
# Variable to store the response from the GET request to the given URL/resource
response = requests.get(BASEURL)

# Print the response data and status code
print(str(response.json()) + " " + str(response))

#------------------------------ POST Request ---------------------------------------

# Variable to store the response from the POST request to the given URL/resource
response = requests.post(BASEURL, data = {"fruit": "lemon"})

# Print the response data and status code
print(str(response.json()) + " " + str(response))

#------------------------------ PUT Request ---------------------------------------

# Variable to store the response from the PUT request to the given URL/resource
response = requests.put(BASEURL, data = { "fruits": ["kiwi", "orange", "lime"]})

# Print the response data and status code
print(str(response.json()) + " " + str(response))

# ------------------------------ DELETE Request ---------------------------------------
# Variable to store the response from the DELETE request to the given URL/resource
response = requests.delete(BASEURL)

# Print the response data and status code
print(str(response.json()) + " " + str(response))