"""
This is the Entrypoing of the Web-App

The import below are mandatory
"""
from flask import Flask
from core.app import app
from core import routes

# -> No other code is needed here
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
