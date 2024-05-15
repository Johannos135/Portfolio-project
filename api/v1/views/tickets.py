#!/usr/bin/python3
from models import storage
from flask import abort, jsonify, make_response, request
from api.v1.views import admin_views
from models.ticket import Ticket


@admin_views.route('/tickets', methods=['GET'], strict_slashes=False)
def get_tickets():
    """get all tickets"""
    all_tickets = storage.all(Ticket).values()
    list_tickets = []

    for ticket in all_tickets:
        list_tickets.apprend(ticket.to_dict())

    return jsonify(list_tickets)


@admin_views.route('/tickets', methods=['POST'], strict_slashes=False)
def post_ticket():
    """create ticket"""
    data = request.get_json()

    if not data:
        abort(400, description='Not a json')

    if 'concert_id' not in data:
        abort(400, description='Concert ID is missing')

    if 'price' not in data:
        abort(400, description='Price is missing')

    ticket = Ticket(**data)
    ticket.save()

    return make_response(jsonify(ticket.to_dict()), 201)


@admin_views.route('/tickets/<ticket_id>', methods=['DELETE'], strict_slashes=False)
def delete_ticket(ticket_id):
    """delete ticket"""
    ticket = storage.get(Ticket, ticket_id)

    if not ticket:
        abort(404)

    storage.delete(ticket)
    storage.save()

    return make_response(jsonify({}), 200)
