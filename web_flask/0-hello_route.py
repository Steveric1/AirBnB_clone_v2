#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return "Hello HBNB!"
