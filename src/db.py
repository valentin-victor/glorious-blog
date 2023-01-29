#!/usr/bin/env python3
"""db.py
Create functions to manage the sqlite db
"""
import sqlite3

import flask
import click


def get_db():
    """Return the sqlite3 connection object.
    If no database has been configured in the app, instantiate it and
    attach it to g.
    MUST be called within a flask application context!

    Returns (sqlite3.Connection): sqlite3 connection
    """
    if 'db' not in flask.g:
        flask.g.db = sqlite3.connect(  # instantiate new connection
            database=flask.current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        flask.g.db.row_factory = sqlite3.Row

    return flask.g.db


def close_db(e=None):
    """Remove the db from g. Close db if any.
    MUST be called within a flask application context!

    Returns: None
    """
    db = flask.g.pop('db', None)  # get db or None

    if db is not None:  # if db, close it
        db.close()


def init_db():
    """Create the database scheme as present in schema.sql
    MUST be called within a flask application context!

    Returns: None
    """
    db = get_db()

    with flask.current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def register_db_methods(app: flask.Flask):
    """Register the db management methods to a Flask application to be used
    later.

    Args:
        app (Flask.flask): a Flask application

    Returns: None
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
