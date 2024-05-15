#!/usr/bin/python3
from api.v1.views import admin_views
from flask import jsonify, request, abort, make_response
from models.role import Role
from models import storage
from utils.auth.auth_guard import auth_guard


@admin_views.route('/roles', methods=['GET'], strict_slashes=False)
@auth_guard('admin')
def get_roles():
    """get list of user roles"""
    roles = storage.all(Role).values()
    list_roles = []

    for role in roles:
        list_roles.append(role.to_dict())

    return jsonify(list_roles)


@admin_views.route('/roles', methods=['POST'], strict_slashes=False)
def post_role():
    """create user role"""
    data = request.get_json()

    if not data:
        abort(400, description='Not a json')
        
    if 'name' not in data:
        abort(400, description='Name is missing')

    role = Role(**data)
    role.save()

    return make_response(jsonify(role.to_dict()), 201)


@admin_views.route('/roles/<role_id>', methods=['DELETE'], strict_slashes=False)
def delete_role(role_id):
    """delete user role"""
    role = storage.get(Role, role_id)

    if not role:
        abort(404)

    storage.delete(role)
    storage.save()

    return make_response(jsonify({}), 200)
