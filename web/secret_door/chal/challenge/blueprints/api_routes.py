from flask import Blueprint, request, abort, session, redirect, url_for, jsonify
from util import is_valid_email, verify_password, create_JWT, create_hash, is_authenticated, verify_JWT, escape_html, timestamp
from database import query_db, call_procedure
from datetime import datetime

api = Blueprint('api', __name__)


@api.route('/login', methods=["POST"])
def api_login():
    if not request.is_json:
        return abort(400, 'Invalid POST format!')
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    if not email or not password:
        return abort(401, 'All fields are required')
    query = "SELECT * FROM users WHERE email = %s"
    user = query_db(query, (email,), one=True)
    if user:
        password_check = verify_password(user['password'], password)
        if password_check:
            token = create_JWT(user['email'], user['role'])
            session['auth'] = token
            return redirect(url_for('web.home'))
        else:
            return abort(401, 'Invalid Credential')
    else:
        return abort(401, 'Invalid Credential')


@api.route('/register', methods=["POST"])
def api_register():
    if not request.is_json:
        return abort(400, 'Invalid POST format!')
    data = request.get_json()
    email = data.get('email', '')
    password = data.get('password', '')
    if not email or not password:
        return abort(401, 'All fields are required')
    if not is_valid_email(email):
        return abort(401, 'Invalid Email')
    hashed_password = create_hash(password)
    try:
        call_procedure("insert_user", (email, hashed_password))
        return redirect(url_for('web.login'))
    except Exception as e:
        return abort(500, 'Registration failed - some error occurred')


@api.route('/update-email', methods=["POST"])
@is_authenticated
def update_email():
    if not request.is_json:
        return abort(400, 'Invalid POST format!')
    data = request.get_json()
    new_email = data.get('email', '')
    if not is_valid_email(new_email):
        return abort(401, 'Invalid Email')
    # Get old email address
    token = session.get('auth')
    decoded_token = verify_JWT(token)
    old_email = decoded_token["email"]
    # Logging Data
    time = datetime.now()
    update_date = time.strftime("%Y-%m-%d %H:%M:%S")
    log_text = f"Email updated to {new_email} at {update_date}"
    log_text = log_text.format(new_email=new_email, timestamp=timestamp, update_date=update_date)
    # Update users
    call_procedure("update_user_email", (old_email, new_email))
    # Insert Logs
    log_text = escape_html(log_text)
    call_procedure("insert_log", (new_email, log_text))
    # Log out of the page
    session['auth'] = None
    return redirect(url_for('web.logout'))


@api.route('/view-logs', methods=["GET"])
@is_authenticated
def view_logs():
    # Get email from JWT token
    token = session.get('auth')
    decoded_token = verify_JWT(token)
    email = decoded_token["email"]

    user_query = "SELECT id FROM users WHERE email = %s"
    user = query_db(user_query, (email,), one=True)
    log_query = "SELECT log_text, log_date FROM logs WHERE user_id = %s ORDER BY log_date DESC"
    logs = query_db(log_query, (user['id'],), one=False)
    return jsonify(logs)
