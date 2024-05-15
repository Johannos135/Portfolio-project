#!/usr/bin/python3
from os import environ
from models import storage
from api.v1.views import app_views
from api.v1.views import admin_views
from flask import Flask, jsonify, make_response
from flask_cors import CORS


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
app.register_blueprint(admin_views)
CORS(app)


@app.teardown_appcontext
def close_db(error):
    """close db connection"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)


@app.errorhandler(400)
def bad_request(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': error.description}), 400)


if __name__ == '__main__':
    host = environ.get('PORTFOLIO_API_HOST')
    port = environ.get('PORTFOLIO_API_PORT')

    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'

    app.run(host=host, port=port, threaded=True)
