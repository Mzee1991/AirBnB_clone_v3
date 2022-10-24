#!/usr/bin/python3
from os import getenv
from dotenv import load_dotenv
from flask import Flask, Blueprint, jsonify
from models import storage
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="0.0.0.0")
app.register_blueprint(app_views)
CORS(app_views)

load_dotenv()

@app.teardown_appcontext
def close_session(error):
    """Close current session."""
    storage.close()
    
@app.errorhandler(404)
def page_not_found(err):
    """Handler for 404 errors that returns a JSON formatted error response"""
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(host = getenv('HBNB_API_HOST'),
            port=getenv('HBNB_API_PORT'), threaded=True, debug=True)
    