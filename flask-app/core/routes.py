"""
Handles all possible HTTP requests to the web-server
"""

import os
import requests

from flask import send_file, request, render_template, redirect, jsonify, url_for, Response

from core.app import app


# Global Utilities for Routes
@app.after_request
def after_request(response):
    """
    Adds HTTP headers for Cross origin
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,X-Requested-With,Content-Length,Accept,Origin')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


@app.after_request
def add_header(response):
    """
    Adds HTTP headers for Cache Max Age
    """
    response.cache_control.max_age = 100
    return response



# Routes Defined Here
@app.route('/')
def home():
    """
    The Home Page
    """
    #index_path = os.path.join(app.static_folder, 'index.html')
    #return send_file(index_path)
    doc = {
        'title':'Home',
        'header':'The Page Title',
        'content':'This is a test!'
    }
    return render_template('index.html', doc=doc)

@app.route('/explore')
def gui():
    """
    Some other GUI
    """

    doc = {
        'title':'Search Interface'
    }

    return render_template('index.html', doc=doc)





# Catch all routes
# No change should be needed below here

@app.route('/<path:fpath>', methods=['GET', 'PUT', 'POST', 'DELETE', 'OPTIONS'])
def route_frontend(fpath):
    """
    The Catch all route
    Everything not declared before (not a Flask route / API endpoint)...
    """
    doc = {
        'title':'Home',
        'header':'The Page Title',
        'content':'This is a test!'
    }
    if '..' in fpath:
        doc['title'] = 'Access Denied'
        doc['header'] = 'Error: Access Denied'
        doc['sub-head'] = 'The Page requested cannot be accessed.'

        app.logger.error("Page '%s' is illegal request", fpath)
        return render_template('error.html', doc=doc), 403

    # ...could be a static file needed by the front end that
    # doesn't use the `static` path (like in `<script src="bundle.js">`)
    file_path = os.path.join(app.static_folder, fpath)
    app.logger.info("Search for '%s' PATH '%s' into STATIC FOLDER %s ",
                    request.method, fpath, app.static_folder)

    if os.path.isfile(file_path):
        return send_file(file_path)

    # ...or no
    doc['title'] = 'Page not Found'
    doc['header'] = 'Error: Page not Found'
    doc['sub-head'] = "The Page requested cannot be found on the server."

    app.logger.error("Page '%s' not found", fpath)
    return render_template('error.html', doc=doc), 404


# Error Pages


@app.errorhandler(500)
def coding_error(error):
    """
    Error 500 page
    """
    doc = {
        'title': 'Server Error',
        'header': 'Server Error',
        'sub-head': 'The Application has Encountered an Error',
        'content': 'This is a test!'
    }
    app.logger.error("Raising error 500 '%s'", error)
    return render_template('error.html', doc=doc), 500


@app.errorhandler(404)
def page_not_found(error):
    """
    Error 404 page
    """
    doc = {
        'title': 'Page not Found',
        'header': 'Error: Page not Found',
        'sub-head': "The Page requested cannot be found on the server.",
        'content': 'This is a test!'
    }


    app.logger.error("Raising error 404 '%s'", error)
    return render_template('error.html', doc=doc), 404
