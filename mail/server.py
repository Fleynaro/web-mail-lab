import os

from flask import Flask
from dotenv import load_dotenv

from blueprints.message_blueprint import message_blueprint

from database import db_session, init_db

load_dotenv()

app = Flask(__name__, static_folder='../shared/static', template_folder='../shared/templates')

app.env = os.environ.get('FLASK_ENV', 'development')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')

app.register_blueprint(message_blueprint)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def run():
    init_db()
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=os.environ.get('PORT', 8080),
        debug=int(os.environ.get('DEBUG', '1')))