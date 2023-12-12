import os
import logging
import sys

import flask

from . import handlers
from . import redis_utils

APPLICATION_NAME = "weight_tracker"
DEFAULT_DEBUG_LEVEL = os.environ.get("DEFAULT_DEBUG_LEVEL", "INFO")

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=DEFAULT_DEBUG_LEVEL,
    stream=sys.stderr,
)

redis_url = os.environ.get("REDIS_URL", None)

redis = redis_utils.setup_redis(redis_url) if redis_url else None

app = flask.Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))

logger = app.logger

routes = [
    ("/", "index", handlers.pages.front_page, ["GET"]),
    ("/home", "home", handlers.pages.home, ["GET"]),
    ("/forms/weight-log", "log_weight", handlers.forms.weight_log, ["POST"]),
]

for path, endpoint, handler, methods in routes:
    app.add_url_rule(path, endpoint, handler, methods=methods)


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception("An error occurred during a request.")
    return "An internal error occurred.", 500
