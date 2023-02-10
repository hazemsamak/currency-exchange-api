__author__ = 'hsamak'

from functools import wraps

from flask import request
from flask_smorest import abort

api_key = "49c5bc127e5d85080d399a5a0010161e"


def match_api_keys(key):
    """
    Match API keys and discard ip
    @param key: API key from request
    @param ip: remote host IP to match the key.
    @return: boolean
    """
    if key is None:
        return False

    if api_key == key:
        return True
    return False


def require_app_key(f):
    """
    @param f: flask function
    @return: decorator, return the wrapped function or abort json object.
    """

    @wraps(f)
    def decorated(*args, **kwargs):
        # if match_api_keys(request.args.get('api-key')):
        if request.headers.get('x-api-key') and match_api_keys(request.headers.get('x-api-key')):
            return f(*args, **kwargs)
        else:
            abort(401, message="Please send a valid 'api-key'")

    return decorated

