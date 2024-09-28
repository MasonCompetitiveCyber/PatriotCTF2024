from functools import wraps
from flask import abort, session
import hashlib
import os
import jwt
import datetime
import re

def generate_key(x): return os.urandom(x).hex()

FLASK_SECRET_KEY = generate_key(256)
jwt_key = generate_key(256)

def create_JWT(email: str, role="regular"):
    utc_time = datetime.datetime.now(datetime.UTC)
    token_expiration = utc_time + datetime.timedelta(minutes=1000)
    data = {
        'email': email,
        "exp": token_expiration,
        'role': role
    }
    encoded = jwt.encode(data, jwt_key, algorithm='HS256')
    return encoded


def verify_JWT(token):
    try:
        token_decode = jwt.decode(
            token,
            jwt_key,
            algorithms='HS256'
        )
        return token_decode
    except:
        return abort(401, 'Invalid authentication token!')


def is_valid_email(email):
    # Don't support long emails addr
    if len(email) > 50:
        return False
    # Canonical email addresses according to RFC 5322
    email_regex = r'([#-\'*+/-9=?A-Z^-~-]+(\.[#-\'*+/-9=?A-Z^-~-]+)*|"([]#-[^-~ \t]|(\\[\t -~]))+")@([#-\'*+/-9=?A-Z^-~-]+(\.[#-\'*+/-9=?A-Z^-~-]+)*|\[[\t -Z^-~]*])'
    if re.fullmatch(email_regex, email, re.IGNORECASE):
        return True
    return False

def create_hash(password):
    sha256_hash = hashlib.sha256(password.encode())
    return sha256_hash.hexdigest()

def verify_password(hashedPassword, password):
    sha256_hash = create_hash(password)
    if sha256_hash == hashedPassword:
        return True
    else:
        return False

def timestamp():
    return datetime.now()

def is_authenticated(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = session.get('auth')
        print(token)
        if not token:
            return abort(401, 'Unauthorized access detected!!')

        verify_JWT(token)

        return f(*args, **kwargs)

    return decorator


def is_admin(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = session.get('auth')
        if not token:
            return abort(401, 'Unauthorized access detected!!')

        decoded_token = verify_JWT(token)
        if decoded_token["role"] != "admin":
            return abort(401, 'Unauthorized access detected!!')
        
        return f(*args, **kwargs)

    return decorator

def escape_html(s):
    # Define a mapping of special characters to HTML entities
    html_escape_table = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;",
        "`": "&#96;"
    }
    # Use a list comprehension to replace each special character with its HTML entity
    return ''.join(html_escape_table.get(c, c) for c in s)