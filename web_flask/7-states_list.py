#!/usr/bin/python3
"""
Script that starts a Flask web application
"""


from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """
    Method to remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def display_states_list():
    """
    Display a HTML page with a list of all State objects
    """
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
