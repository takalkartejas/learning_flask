#import the flask class
from flask import Flask
# Next we create an instance of this class. The first argument is the name 
# of the application’s module or package. __name__ is a convenient shortcut
#  for this that is appropriate for most cases. This is needed so that Flask 
#  knows where to look for resources such as templates and static files
app = Flask(__name__)

@app.route("/")
def hello_world(): 
    #return html string
    return "<p>Hello, World!</p>"