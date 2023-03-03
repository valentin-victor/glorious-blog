#!/usr/bin/env python3
"""Declare a Flask blueprint to register authentication views.
"""
import functools

import flask

from db import get_db


bp = flask.Blueprint(  # declare new blueprint
    name='auth',
    import_name=__name__,
    template_folder='templates',
    url_prefix='/auth',
)


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register view. Answer a GET request with the registration form.
    Insert new user in db when a POST request occurs and return user to login
    page if everything went right, otherwise to the register view.

    Returns (str): register view or redirect to login page
    """
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        if error is None:
            try:
                db.execute(
                    'INSERT INTO user (username, password) VALUES (?, ?)',
                    (username, password)
                )
                db.commit()
            except db.IntegrityError: 
                error = f'User {username} is already registered.'
            else:
                return flask.redirect(flask.url_for('auth.login'))

        flask.flash(error, 'error')

    return flask.render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Login view. Answer a GET request with the login form.
    Attach user id if POST request occurs and return user to index
    page if everything went right, otherwise to the login view.

    Returns (str): login view or redirect to index page
    """
    if flask.request.method == 'POST':
        username = flask.request.form['username']
        password = flask.request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif user['password'] != password:
            error = 'Incorrect password.'

        if error is None:
            response = flask.redirect(flask.url_for('index'))
            response.set_cookie('user_id', str(user['id'], max_age=86400, expires=86400)) # age maximum, 1 jour. |-| "expires" est comme max age mais pour les navigateur sans la compatibilité de max_age
            return response

        flask.flash(error, 'error')

    return flask.render_template('auth/login.html')


@bp.route('/logout')
def logout():
    """Clear current user cookie.

    Returns: redirect to index page
    """
    response = flask.redirect(flask.url_for('index'))
    response.delete_cookie('user_id')
    return response


@bp.before_app_request
def load_logged_in_user():
    """If user is currently connected, attach user object to context.
    """
    user_id = flask.request.cookies.get('user_id')

    if user_id is None:
        flask.g.user = None
    else:
        flask.g.user = get_db().execute(
            f'SELECT * FROM user WHERE id = {user_id}'
        ).fetchone()


def login_required(view):
    """Register a view that need authentication. Redirect client to login if
    they are not authenticated.
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if flask.g.user is None:
            return flask.redirect(flask.url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
