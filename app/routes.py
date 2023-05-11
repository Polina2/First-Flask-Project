# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    params_post = {}
    for p in request.form:
        params_post[p] = request.form[p]

    region = ''
    mobile_operator = ''
    return render_template('index.html', region=region, mobile_operator=mobile_operator)
