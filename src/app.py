#!/usr/bin/env python3
"""app.py
Main entry point of the blog web app.
"""
import pathlib

import flask  # import the flask library

import db
import auth
import blog

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app_dir = pathlib.Path(__file__).resolve().parent

app = flask.Flask(__name__)  # instantiate a minimal webserver

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "5 per hour"],
    storage_uri="memory://",
)

@app.route('/register')
@limiter.limit("5 per 1 hour") # limit of request
def register():
    return "5 per 1 hour"

@app.route('/login')
@limiter.limit("5 per 1 hour") # limit of request
def login():
    return "5 per 1 hour"

app.config['DATABASE'] = app_dir / 'db.sqlite'  # path to the db file
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some_random_value'


db.register_db_methods(app)  # register db management methods

app.register_blueprint(auth.bp)  # add auth views to application
app.register_blueprint(blog.bp)  # add blog views to application

app.add_url_rule('/', endpoint='index')  # map the 'index' endpoint with /


if __name__ == '__main__':
    app.run()  # start web server
