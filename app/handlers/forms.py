import logging

import flask

from forms.weight import WeightForm
from app.repositories import weight


def weight_log():
    logger = flask.current_app.logger
    logger.debug(flask.request.form)

    weight_form = WeightForm(flask.request.form)

    if weight_form.validate():
        reported_value = weight_form.weight.data
        logger.debug(reported_value)
        weight.today(reported_value * 1000)
        return flask.redirect(flask.url_for("home"))

    logger.info(weight_form.errors)
    return flask.abort(400)
