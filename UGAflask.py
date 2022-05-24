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
@app.route("/register",methods=['POST'])
def store_library():
    pass
@app.route("/couponpage",methods=['GET'])
def display_coupons():
    pass

if __name__ == "__main__":
    app.run(port =5000, host = "0.0.0.0")