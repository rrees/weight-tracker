import flask
from uuid import uuid4

from . import forms
from . import middleware

URL_PREFIX = "/auth"
AUTH_SESSION_KEY = "authenticated"

auth_blueprint = flask.Blueprint(
    "auth_password", __name__, template_folder="templates", url_prefix=URL_PREFIX
)


def check_credentials(username, password):
    return True


@auth_blueprint.route("/login")
def login():
    return flask.render_template("login.html")


@auth_blueprint.route("/login/form", methods=["POST"])
def login_form():
    login_form = forms.Login(flask.request.form)

    if login_form.validate():
        username = login_form.username.data
        password = login_form.password.data
        flask.current_app.logger.info(username)
        flask.current_app.logger.info(password)
        if check_credentials(username, password):
            flask.session[AUTH_SESSION_KEY] = "temp"
        return flask.redirect(flask.url_for("home"))

    return flask.redirect(flask.url_for("auth_password.login"))


@auth_blueprint.route("/logout")
def logout():
    flask.session.pop(AUTH_SESSION_KEY, None)
    return flask.redirect(flask.url_for("index"))


auth_blueprint.before_app_request(
    middleware.check_session(URL_PREFIX, AUTH_SESSION_KEY)
)
