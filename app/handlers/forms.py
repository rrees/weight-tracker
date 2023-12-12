import logging

import flask

from forms.weight import WeightForm


def weight_log():
    flask.current_app.logger.debug(flask.request.form)

    weight_form = WeightForm(flask.request.form)

    if weight_form.validate():
        return flask.redirect(flask.url_for("home"))

    return flask.abort(400)
