import flask

def front_page():
	return flask.render_template('index.html')

def home():
	return flask.render_template('home.html')