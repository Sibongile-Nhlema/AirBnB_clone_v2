#!/usr/bin/python3
"""
Starts a Flask web application.
"""


from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
	""" Remove the current SQLAlchemy Session """
	storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
	""" Display a list of states """
	states = storage.all("State").values()
	sorted_states = sorted(states, key=lambda state: state.name)
	return render_template('7-states_list.html', states=sorted_states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
	""" Display a list of cities grouped by states """
	states = storage.all("State").values()
	sorted_states = sorted(states, key=lambda state: state.name)
	return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
