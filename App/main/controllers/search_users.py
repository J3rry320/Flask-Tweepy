from ...app import app
from flask import url_for, request
from ..services.search_users import search_users


@app.route('/search_users/<name>', methods=['GET'])
def search_(name):
    return search_users(name)
