# learning_flask

## tutorial 1
Follow the quickstart guide at the following link along side this repo

https://flask.palletsprojects.com/en/2.2.x/quickstart/

### Learning steps
    
    1. Hello world:- Create flask_hello_world.py
    2. execute the hello world code using flask --app flask_hello_world run
    3. run in debug mode :- cmd 2
    4. Routing:- Create routing.py and check on browser if the routes are working
    5. Escaping :- client can write a script for eg. HTML in the url which request for eg. name and the script will be executed. We use escaping to escape this
    6. Getting variables from url
    7. create file VariableRules.py
    8. url_for():- create file url_for.py
    9. HTTP Methods:- this topic covers how to use add the http methods like get() and post()
    10. Rendering templates:- covers how to use html or css etc. templates alongside of flask. For eg. pass name trough url the file returns hello name using html.
    11. 

### Commands 
    1. flask --app [filename] run :- run flask command
    2. flask --app [filename] --debug run :- run in debug mode


## Tutorial 2

https://realpython.com/flask-connexion-rest-api/#demo


### Aim

Create a REST API to keep track of the notes for people that visit thoughout the year.
### Learning steps

1. Create a folder named rp_flask_api which will be our root folder
2. create a virtual enviornment inside the folder so that all installations are folder specific
3. add dependencies
4. create app.py