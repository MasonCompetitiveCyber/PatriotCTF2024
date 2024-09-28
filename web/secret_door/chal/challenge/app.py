from blueprints.web_routes import web
from blueprints.api_routes import api
from flask import Flask, render_template, jsonify
from database import mysql

app = Flask(__name__)
app.config.from_object('config.Config')

mysql.init_app(app)

app.register_blueprint(web, url_prefix='/')
app.register_blueprint(api, url_prefix='/api')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404 

@app.errorhandler(403)
def not_found(error):
    return render_template('403.html'), 403

@app.errorhandler(Exception)
def handle_error(error):
    print(error)
    message = error.description if hasattr(error, 'description') else [str(x) for x in error.args]
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }
    error_code = error.code if hasattr(error, 'code') else 500
    return jsonify(response), error_code