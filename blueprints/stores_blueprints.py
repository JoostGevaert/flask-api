from flask import Blueprint, jsonify

stores_blueprint = Blueprint('stores_blueprint', __name__)

@stores_blueprint.route('/api/stores')
def store_list():
    return jsonify({'data': [{'id': 1, 'name': '4th Avenue Cafe'}]})

