
from flask import Flask
import os

from web_app.routes.home_routes import home_routes
from web_app.routes.simple_routes import simple_routes
from web_app.routes.complex_routes import complex_routes

SECRET_KEY = os.getenv("SECRET_KEY", default="abc123") 

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY
    app.register_blueprint(home_routes)
    app.register_blueprint(simple_routes)
    app.register_blueprint(complex_routes)
    return app


if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)


   
