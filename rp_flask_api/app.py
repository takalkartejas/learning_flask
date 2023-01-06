from flask import Flask, render_template
import connexion

#create flask application instace named flask
'''app = Flask(__name__) '''
# intead of creating app using flask as shown in red text above...
# we create app using connexion the specification dir ...
# tells the connexion where to look for its api config file

app = connexion.App(__name__, specification_dir="./")
#we add the api configuration file
app.add_api("swagger.yml")

# connect to URL route "/"
@app.route("/")
def home():
    # flask expects the file to be in template directory
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)