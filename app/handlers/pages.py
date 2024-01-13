import flask

from app.repositories import weight as weight_repository


def front_page():
    return flask.render_template("index.html")


def home():
    return flask.render_template(
        "home.html", recent_history=weight_repository.recent_history()
    )
