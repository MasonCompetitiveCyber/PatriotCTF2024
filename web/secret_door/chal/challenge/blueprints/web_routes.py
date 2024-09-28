from util import is_authenticated, is_admin
from flask import Blueprint, render_template, session, redirect, url_for, current_app

web = Blueprint('web', __name__)

@web.route('/')
def login():
    session['auth'] = None
    return render_template('login.html')

@web.route('/register')
def web_register():
    session['auth'] = None
    return render_template('register.html')

@web.route('/logout')
def logout():
    session['auth'] = None
    return redirect(url_for('web.login'))

@web.route('/home')
@is_authenticated
def home():
    return render_template('home.html')

@web.route('/update-email')
@is_authenticated
def web_update_email():
    return render_template('update-email.html')

@web.route('/update-logs')
@is_authenticated
def web_view_personal_logs():
    return render_template('personal-logs.html')

@web.route('/admin')
@is_admin
def admin_home():
    flag = current_app.config['FLAG']
    return render_template('admin.html', flag=flag)
