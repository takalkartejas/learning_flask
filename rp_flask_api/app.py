from flask import Flask, render_template

#create flask application instace named flask
app = Flask(__name__)

# connect to URL route "/"
@app.route("/")
def home():
    # flask expects the file to be in template directory
    return render_template("home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)