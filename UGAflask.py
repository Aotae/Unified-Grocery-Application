import flask
from flask import request
import UGD_methods
import API_server
import json
import sys

app = flask.Flask(__name__)

# Display webpage functions no AJAX yet, splash page == login page
# if login successful next splash should be the grocery store library 
# if 

@app.route("/")
@app.route("/login")
def display_login():
    # renders the login page
    return flask.render_template('login.html')
@app.route("/register")
def display_register():
    # renders the register page
    return flask.render_template('register.html')
@app.route("/search")
def display_search():
    # renders the search page
    return flask.render_template('search.html')

##########
# AJAX Handlers should return jsons instead of rendering pages
##########
@app.route("/_search")
def search():
    """
    this should search the database for a product by keyword.
    current iteration simply retuns the keywords given

    search html page -> request -> flask server answers
    request should be formatted s.t store = [] (list of stores), keyword = search keyword.
    """
    keyword = request.args.get('keyword',type=str)
    store = json.loads(request.args.get('store'))
    couponpage = API_server.search_coupon_page(store,keyword)
    #print(couponpage)
    #couponpage.append()
    return flask.jsonify({"coupons":couponpage})

@app.route("/_storelist")
def display_store_list():
    # returns the entire list of stores in the collection
    # This simply grabs the stores from our store collection and updates the html with them.
    UGD_methods.connect()
    list = UGD_methods.get_store_library()
    store_list = []
    for store in list:
        store_name = store["name"]
        store_list.append(store_name)
    print(store_list)
    return flask.jsonify({"list":store_list})

@app.route("/_register")

##STRETCH GOAL FUNCTIONS
##DEPRECATED SINCE WE COULDN'T GET ACCESS TO MOST GROCERY STORES API
def register():
    """
    this should insert the users credentials into the db
    after hashing the password
    """
    pass
@app.route("/_validate")
def validate():
    """
    this should compare the users credentials to the db after hashing the input
    should return valid true or false to /register
    """
    pass
@app.route("/_compare")
def compare():
    """
    This should take in a coupon id from the search or coupon page template
    and check its price/discount then look for coupons that match the keyword from the given coupon
    and compare prices return all found coupons and mark the lowest price/ highest discount.
    """
    pass
if __name__ == "__main__":
    app.run(port =5000, host = "0.0.0.0",debug=True)