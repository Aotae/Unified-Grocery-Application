import flask
from flask import request
import UGD_methods

app = flask.Flask(__name__)

# Display webpage functions no AJAX yet, splash page == login page
# if login successful next splash should be the grocery store library 
# if 
@app.route("/")
@app.route("/login")
def display_login():
    return flask.render_template('login.html')

@app.route("/register")
def display_register():
    return flask.render_template('register.html')

@app.route("/store-list")
def display_store_list():
    return flask.render_template('store-list.html')
@app.route("/search")
def display_search():
    return flask.render_template('search.html')
##########
# AJAX Handlers should return jsons instead of rendering pages
##########
@app.route("/_search")
def search():
    """
    this should search the database for a product by keyword.
    current iteration simply retuns the keywords given
    """
    keyword = request.args.get('keyword',type=str)
    # print(f"keyword={keyword}")

    return flask.jsonify({"keyword":keyword})

@app.route("/_register")
def register():
    pass
@app.route("/_validate")
def validate():
    pass


if __name__ == "__main__":
    app.run(port =5000, host = "0.0.0.0")