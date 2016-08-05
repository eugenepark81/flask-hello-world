# flask hello world #

#import flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# error handling
app.config["DEBUG"] = True

# use deocrators to link th function to a url
@app.route("/")
@app.route("/hello")


#define the view using a function which returns a string
def hello_world():
	return "Hello, World?!?!?!?!"

# dynamic route
@app.route("/test/<search_query>")
def search(search_query):
	return search_query

# dynamic route that accepts slashes
@app.route("/path/<path:value>")
def path_type(value):
	print value
	return "correct"

# dynamic route with status codes
@app.route("/name/<name>")
def index(name):
	if name.lower() == "michael":
		return "Hello, {}".format(name)
	else:
		return "Not Found", 404


# start the dev server using the run() method
if __name__ == "__main__":
	app.run()