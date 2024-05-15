#!/usr/bin/python3
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
admin_views = Blueprint('admin_views', __name__, url_prefix='/admin')

from api.v1.views.roles import *
from api.v1.views.users import *
from api.v1.views.concerts import *