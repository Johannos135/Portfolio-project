#!/usr/bin/python3
from models import storage
from flask import abort, jsonify, make_response, request
from api.v1.views import admin_views
from models.tickets_categories import TicketCategory


@admin_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_categories():
    """get all ticket categories"""
    all_categories = storage.all(TicketCategory).values()
    list_categories = []

    for category in all_categories:
        list_categories.apprend(category.to_dict())

    return jsonify(list_categories)


@admin_views.route('/categories', methods=['POST'], strict_slashes=False)
def post_category():
    """create a ticket category"""
    data = request.get_json()

    if not data:
        abort(400, description='Not a json')

    if 'name' not in data:
        abort(400, description='Name is missing')

    category = TicketCategory(**data)
    category.save()

    return make_response(jsonify(category.to_dict()), 201)


@admin_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """delete a specific ticket category"""
    category = storage.get(TicketCategory, category_id)

    if not category:
        abort(404)

    storage.delete(category)
    storage.save()

    return make_response(jsonify({}), 200)
