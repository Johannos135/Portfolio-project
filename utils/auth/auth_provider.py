#!/usr/bin/python3
from models.user import User
from flask import abort, jsonify
from models import storage
from hashlib import md5


def authenticate(phone, password):
    """authentication middleware"""
    user = storage.get_by_phone(User, phone)

    if not user:
        abort(404)

    role = user.role.to_dict() if user.role else None
    tab = [role['name'] if role else None]
    if user.phone_number == phone and user.password == md5(password.encode()).hexdigest()[:20]:
        return {
            'name': user.name,
            'phone_number': user.phone_number,
            'roles': tab
        }
    else:
        return False
