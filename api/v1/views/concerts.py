#!/usr/bin/python3
from api.v1.views import app_views
from api.v1.views import admin_views
from models import storage
from models.concert import Concert
from flask import jsonify, abort, make_response, request


@app_views.route('/concerts', methods=['GET'], strict_slashes=False)
def get_concerts():
    """Show list of all concert events available"""
    all_concerts = storage.all(Concert).values()
    list_concerts = []

    for concert in all_concerts:
        list_concerts.append(concert.to_dict())

    return jsonify(list_concerts)


@app_views.route('/concerts/<concert_id>', methods=['GET'], strict_slashes=False)
def get_concert_by_id(concert_id):
    concert = storage.get(Concert, concert_id)

    if not concert:
        abort(404)

    return jsonify(concert.to_dict())


@admin_views.route('/concerts/<concert_id>', methods=['DELETE'], strict_slashes=False)
def delete_concert(concert_id):
    """Show a specific concert event by its ID"""
    concert = storage.get(Concert, concert_id)

    if not concert:
        abort(404)

    storage.delete(concert)
    storage.save()

    return make_response(jsonify({}), 200)


@admin_views.route('/concerts', methods=['POST'], strict_slashes=False)
def post_concerts():
    """allow admin to create an event"""
    data = request.get_json()

    if not data:
        abort(400, description='Not a json')

    if 'venue' not in data:
        abort(400, description='Venue is missing')

    concert = Concert(**data)
    concert.save()

    return make_response(jsonify(concert.to_dict()), 201)
