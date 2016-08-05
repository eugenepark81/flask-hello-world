# flask hello world #

#import flask class from the flask package
from flask import Flask

# create the application object
app = Flask(__name__)

# use deocrators to link th function to a url
@app.route("/")
@app.route("/hello")

#define the view using a function which returns a string
def hello_world():
	return "Hello, World!"

# start the dev server using the run() method
if __name__ == "__main__":
	app.run()