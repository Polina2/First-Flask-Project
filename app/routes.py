# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app


@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    return render_template('index.html')
