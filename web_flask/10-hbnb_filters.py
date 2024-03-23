#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from models import storage, State, City, Amenity
from flask import Flask, render_template


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
	""" Method to remove the current SQLAlchemy Session """
	storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
	""" Display a HTML page with filters for searching listings """
	states = storage.all(State).values()
	cities = storage.all(City).values()
	amenities = storage.all(Amenity).values()
	return render_template('10-hbnb_filters.html',
			       states=states, cities=cities,
			       amenities=amenities)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
