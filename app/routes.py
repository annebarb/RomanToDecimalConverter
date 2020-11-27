from flask import render_template, request
from app import app

from functions.roman_to_decimal import *


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            value = decimal_to_roman(int(request.form['Input']))
        except:
            value = roman_to_decimal(request.form['Input'])
        print(value)
        return render_template('index.html', title='Converter', result=value)
    else:
        return render_template('index.html', title='Converter')


@app.errorhandler(ValueError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter', message='Invalid value entered')


@app.errorhandler(TypeError)
def handle_value_error(err):
    return render_template('index.html', title='RomToDec Converter', message='Invalid value entered')
