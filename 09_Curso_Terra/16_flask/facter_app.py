#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
from facter_utils import get_argument
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('facter.html', fields=None)


@app.route('/', methods=['POST'])
def index_post():
    name = request.form.get('name')
    value = get_argument(name)
    fields = {'name': name, 'value': value}
    return render_template('facter.html', fields=fields)


app.run(debug=True)
