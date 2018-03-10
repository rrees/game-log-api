import os

import flask
import flask_sslify

from . import handlers

ENV = os.environ.get("ENV", "PROD")


app = flask.Flask(__name__)

routes = [
    ('/', 'index', handlers.info.root, ['GET']),
]

for path, endpoint, handler, methods in routes:
	app.add_url_rule(path, endpoint, handler, methods=methods)

@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    app.logger.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500