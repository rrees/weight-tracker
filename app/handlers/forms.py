import logging

import flask

LOG = logging.getLogger(__name__)

def weight_log():
	LOG.debug(flask.request.form)
	return flask.redirect(flask.url_for('home'))