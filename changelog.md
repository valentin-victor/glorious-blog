# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added

- added "changelog.md" file.

### Security

- update packages


## 2023-01-03  BRIEU Emma  <ebrieu.ing2024@esaip.org>

### ADDED 

- Download of the werkzeug library with the "pip install werkzeug" command
- Import of generate_password_hash, check_password_hash functions
- Add password hash
    * In app.py
        - line 40 : generating a hash
        - line 44 : stocking the hashed password in db
        - line 76 : checking if the unhashed password and password are equals for log in



[latest main release]: https://github.com/valentin-victor/glorious-blog
