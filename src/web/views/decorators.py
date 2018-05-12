from sqlalchemy import or_
from functools import wraps
from flask import abort
from flask_login import current_user
from web.models import JsonObject, Organization


def check_object_view_permission(f):
    """Check if the user has permission to access to the requested
    JsonObject."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        object_id = kwargs['object_id']
        if current_user.is_authenticated:
            obj = JsonObject.query. \
                filter(JsonObject.id==object_id). \
                filter(or_(JsonObject.is_public,
                            JsonObject.organization. \
                            has(Organization.id.in_([org.id for org in current_user.organizations]))))
        else:
            obj = JsonObject.query. \
                    filter(JsonObject.id==object_id). \
                    filter(JsonObject.is_public)
        if not obj.first():
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function


def check_object_edit_permission(f):
    """Check if the user has permission to edit/delete the requested
    JsonObject."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated:
            return abort(403)
        object_id = kwargs['object_id']
        if current_user.is_authenticated:
            obj = JsonObject.query. \
                filter(JsonObject.id==object_id). \
                filter(JsonObject.organization. \
                has(Organization.id.in_([org.id for org in current_user.organizations])))
        if not obj.first():
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function