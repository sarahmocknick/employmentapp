# this is the "web_app/routes/home_routes.py" file...

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return "Welcome to the Unemployment App!"

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return "About Me"

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")
    return "Hello World"