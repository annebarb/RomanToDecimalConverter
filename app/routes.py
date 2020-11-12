from flask import render_template, request
from app import app

from functions.roman_to_decimal import *


@app.route('/')
def index():
    return render_template('index.html', title='RomToDec Converter')


@app.route('/', methods=['POST'])
def index_post():
    if request.method == 'POST':
        user_input = request.form['Input']
        try:
            value = decimal_to_roman(int(user_input))
        except:
            value = roman_to_decimal(user_input)
        print(value)
    return render_template('index.html', title='RomToDec Converter')


@app.errorhandler(ValueError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter')


@app.errorhandler(TypeError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter')
