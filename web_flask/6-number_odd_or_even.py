#!/usr/bin/python3
''' Script that starts a flask web application on seven routes
'''

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_hbhb(text):
    ''' fuxntion that handles variables '''
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_hbnb(text):
    ''' function that handles variables '''
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def is_number_hbnh(n):
    ''' function that handles numerical variables '''
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_templates_hnbn(n):
    ''' function that displays an html if n is an integer '''
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_hbnb(n):
    ''' renders pages based on whether the input is odd or even '''
    if n % 2 == 0:
        message = f'{n} is even'
    else:
        message = f'{n} is odd'
    return render_template('6-number_odd_or_even.html', message=message)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
