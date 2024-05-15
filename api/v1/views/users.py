#!/usr/bin/python3
from models.user import User
from flask import jsonify, abort, make_response, request
from models import storage
from api.v1.views import app_views
from api.v1.views import admin_views
from utils.auth.auth_provider import authenticate
from utils.auth.jwt_handler import generate_jwt


@admin_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """get list of users"""
    all_users = storage.all(User).values()
    list_users = []

    for user in all_users:
        list_users.append(user.to_dict())

    return jsonify(list_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
@admin_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user_by_id(user_id):
    """get user details by user id"""
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    return jsonify(user.to_dict())


@app_views.route('/users', methods=['POST'], strict_slashes=False)
@admin_views.route('/users', methods=['POST'], strict_slashes=False)
def post_user():
    """create a user"""
    data = request.get_json()

    if not data:
        abort(400, description='Not a valid json')

    if 'phone_number' not in data:
        abort(400, description='Phone number is missing')

    if 'password' not in data:
        abort(400, description='Password is missing')

    user = User(**data)
    user.save()

    return make_response(jsonify(user.to_dict()), 201)


@admin_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    """update user info"""
    data = request.get_json()
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    ignore = ['phone_number', 'id', 'created_at', 'updated_at']

    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()

    return make_response(jsonify(user.to_dict()), 200)


@admin_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """delete user"""
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/login', methods=['POST'], strict_slashes=False)
def auth():
    """allow user to log in"""
    phone = request.json.get('phone_number')
    password = request.json.get('password')
    if not phone or not password:
        abort(400, description='Phone number or password missing')

    user_data = authenticate(phone, password)
    if not user_data:
        abort(400, description='Invalid credentials')
    """<--- generates a JWT with valid within 1 hour by now"""
    token = generate_jwt(payload=user_data, lifetime=60)
    return make_response(jsonify({"data": user_data, "token": token}), 200)
