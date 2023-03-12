# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

# CHANGELOG


2023-01-03  BRIEU Emma  <ebrieu.ing2024@esaip.org>

### ADDED 

- Download of the werkzeug library with the "pip install werkzeug" command
- Import of generate_password_hash, check_password_hash functions
- Add password hash
    * In app.py
        - line 40 : generating a hash
        - line 44 : stocking the hashed password in db
        - line 76 : checking if the unhashed password and password are equals for log in


2023-03-03  VALENTIN Victor  <vvalentin.ir2024@esaip.org>

### FIXED 

- XSS Injection : no possibility anymore to add some code by filling the the article creation form
- SQL Injection : no possibility anymore to add some code by filling the login / register form


2023-12-03  BRIEU Emma  <ebrieu.ing2024@esaip.org>

### ADDED

- Download of the limiter library with the "pip install Flask-Limiter" command
- Add a rate limit in the "app.py" file to limit the request
- Add a description of the web application on the main page ("base.html" & "main.css" files)


2023-12-03  BOUHAMDI Chaimae  <cbouhamdi.ir2024@esaip.org>

### ADDED

- Add some comments
