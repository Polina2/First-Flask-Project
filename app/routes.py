# -*- coding: utf-8 -*-
from flask import render_template, request
from app import app
from app.models import PhoneNumbers, MovedNumbers


@app.route('/')
@app.route('/index', methods=['POST'])
def index():
    params_post = {}
    for p in request.form:
        params_post[p] = request.form[p]

    region = ''
    mobile_operator = ''

    if 'tel' in params_post:
        request_number = params_post['tel']
        request_code = request_number[:3]
        number_without_code = request_number[3:]
        pn = PhoneNumbers.query.filter(PhoneNumbers.code == request_code)\
            .filter(PhoneNumbers.begin <= number_without_code)\
            .filter(PhoneNumbers.end >= number_without_code).first()
        mn = MovedNumbers.query.get(request_number)
        if pn is not None:
            region = pn.region
            mobile_operator = pn.mobile_operator if mn is None else mn.mobile_operator
    return render_template('index.html', region=region, mobile_operator=mobile_operator)
