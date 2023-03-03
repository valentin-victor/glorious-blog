# main branch for improving the security and functionality of the website


---

# My glorious blog

One small project of a web blog.

## Installation

### Clone the repository

Clone this repository in your personal directory with the command:

```bash
git clone https://github.com/cseijido-esaip/glorious-blog.git
```

### Create a new virtual environment

On Linux or MacOS

```bash
python3 -m venv .venv --upgrade-deps
source .venv/bin/activate
```

On Windows

```shell
python -m venv .venv --upgrade-deps
.venv\Scripts\activate.bat
```

*For more information about virtual environments see the [official documentation](https://docs.python.org/3/library/venv.html).*

### Install needed packages

Install needed packages with:

```bash
pip install -r requirements.txt
```

List of direct dependencies:

- flask

### Initialize project

Run this command once to initialize the project:

```bash
flask --app src/app.py init-db
```

## Running the program

Execute one of the following command to start the program:

```bash
python src/main.py
```

```bash
python --app src/app.py --debug run
```

## WARNING

This project contains intentional web vulnerabilities. Do not use it as a real web application in your production environment. Use it for educational purposes only.
