from flask import render_template, request
from app import app

from functions.roman_to_decimal import *


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        entered_value = request.form['Input']
        try:
            value = decimal_to_roman(int(entered_value))
        except:
            value = roman_to_decimal(entered_value)
        print(value)
        return render_template('index.html', title='Converter', entered_value=entered_value, result=value)
    else:
        return render_template('index.html', title='Converter')


@app.errorhandler(ValueError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter', message='Invalid value entered')


@app.errorhandler(TypeError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter', message='Invalid value entered')
