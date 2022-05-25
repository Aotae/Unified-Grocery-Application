import flask
from flask import request
import UGD_methods

app = flask.Flask(__name__)

# Display webpage functions no AJAX yet, splash page == login page
# if login successful next splash should be the grocery store library 
@app.route("/")
@app.route("/login")
def login():
    return flask.render_template('login.html')

@app.route("/register")
def register():
    return flask.render_template('register.html')

@app.route("/store-list")
def display_coupons():
    return flask.render_template('store-list.html')
@app.route("/search")
def display_search():
    return flask.render_template('search.html')

if __name__ == "__main__":
    app.run(port =5000, host = "0.0.0.0")