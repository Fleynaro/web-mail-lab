import os

# add parent directory to path
import sys
import pathlib
parent_dir = pathlib.Path().resolve()
sys.path.append(str(parent_dir))

from flask import Flask
from dotenv import load_dotenv

from blueprints.message_blueprint import message_blueprint
from blueprints.message_api_blueprint import message_api_blueprint

from database import db_session, init_db

load_dotenv()

url_prefix = os.environ.get('URL_PREFIX', '')

app = Flask(__name__, static_folder='../shared/static', template_folder='../shared/templates', static_url_path=url_prefix + "/static")

app.env = os.environ.get('FLASK_ENV', 'development')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'secret')

# register blueprints and add prefix for k8s/ingress
message_blueprint.url_prefix=url_prefix + message_blueprint.url_prefix
message_api_blueprint.url_prefix=url_prefix + message_api_blueprint.url_prefix
app.register_blueprint(message_blueprint)
app.register_blueprint(message_api_blueprint)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


def run():
    init_db()
    app.run(
        host=os.environ.get('HOST', '0.0.0.0'),
        port=os.environ.get('PORT', 8081),
        debug=int(os.environ.get('DEBUG', '1')),
        use_reloader=True)
