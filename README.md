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
5. create a directory called templates and create home.html in the dir.
6. run app.py using command python3 app.py
7. check the output on browser
8. Add a swagger.yml file to define open api:- it is called api configuration file
9. Use connexion to refer to the swagger.yml file inside app.py
10. In the swagger.yml file, you configured Connexion with the operationId value "people.read_all". So, when the API gets an HTTP request for GET /api/people, your Flask app calls a read_all() function within a people module. 
11. To make this work, create a people.py file with a read_all()s
12. Now we look at http://localhost:8000/api/people, we can see the list of people
13. go to http://localhost:8000/api/ui to see the swagger interface
14. create a schema for a person in swagger.yml
15. Add post method in swagger.yml