import flask
import jwt
import Connection.const
import Controller.Login.login
import Controller.Registration.Signup
import Controller.Family.familydetils
import Controller.Parent.Parent
import Controller.Dashboard.video
import Controller.Dashboard.activity
import Controller.Dashboard.Articles
import Controller.Dashboard.Community
import Controller.Dashboard.dashboard
import Controller.Dashboard.appointment
import Controller.DevelopmentScreening.development
import Controller.Services.service
import Controller.Services.appointment
import Controller.Contact.clinic
import Controller.AssessmentForms.assessmentform
import Controller.Reports.report
import Controller.Reports.Assess

import hashlib
from tkinter import N
import flask
import sqlalchemy
import Connection.const
from sqlalchemy.orm import session
from werkzeug.utils import redirect
import sys
import flask_mail
import smtplib
import cryptography.fernet
import Model.models
import Constant.constant
import datetime
from datetime import datetime as dt
from datetime import timedelta
import logging
import requests
import os
import traceback
from flask import Flask, render_template
from flask import Flask, request
from audioop import minmax
from contextlib import nullcontext

import json
from ntpath import join
from operator import methodcaller
from pyexpat import model
from re import M, X
from sre_parse import State
from tokenize import Name
from turtle import title
from unittest import result
from certifi import where
#from time import clock_settime
import flask
from jinja2 import Undefined
from pandas import json_normalize
import sqlalchemy
import Connection.const
from sqlalchemy.orm import session
from werkzeug.utils import redirect
import sys
from sqlalchemy import String, and_, null, or_, select, true
# from sqlalchemy import func
from sqlalchemy.sql import func
from sqlalchemy.orm import column_property
from sqlalchemy import Date, cast
import Model.models
import flask_mail
import smtplib
import cryptography.fernet
import datetime
import datetime
from datetime import date, timedelta
import Constant.constant 
import logging
import requests
import os
from flask import send_from_directory
import traceback
from flask import Flask, abort, jsonify, render_template, request, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask import Flask, current_app, request
from flask_cors import CORS
from flask_mail import Mail, Message

import Common_Function.CommonFun
from flask_login import LoginManager, UserMixin, \
    login_required, login_user, logout_user

# from flask-session import Session
Session = Connection.const.connectToDatabase()
app = flask.Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
# config
app.config.update(
    # DEBUG=True,
    SECRET_KEY='Dis@Project#29112022'
)
# app.config['JSON_SORT_KEYS'] = False
app.json.sort_keys = False
# # flask-login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/"

mail = flask_mail.Mail(app)

@app.errorhandler(Exception)
def server_error(err):
    app.logger.exception(err)
    return "Something Went wrong", 500


    do_stuff()
if __name__=='__main__':
    app.run(host='localhost',port=5025)  

app.register_blueprint(Controller.Reports.report.Report_Blueprint)
app.register_blueprint(Controller.Reports.Assess.Assess_Blueprint)
app.register_blueprint(Controller.Login.login.Login_Blueprint)
app.register_blueprint(Controller.Registration.Signup.Register_Blueprint)
app.register_blueprint(Controller.Family.familydetils.FamilyDtls_Blueprint)
app.register_blueprint(Controller.Parent.Parent.Parent_Blueprint)
app.register_blueprint(Controller.Dashboard.video.Video_Blueprint)
app.register_blueprint(Controller.Dashboard.activity.Activity_Blueprint)
app.register_blueprint(Controller.Dashboard.Articles.Articles_Blueprint)
app.register_blueprint(Controller.Dashboard.Community.Post_Blueprint)
app.register_blueprint(Controller.DevelopmentScreening.development.Development_Blueprint)
app.register_blueprint(Controller.Services.service.PatientServices_Blueprint)
app.register_blueprint(Controller.Services.appointment.Appointment_Blueprint)
app.register_blueprint(Controller.Contact.clinic.Contact_Blueprint)
app.register_blueprint(Controller.Dashboard.dashboard.Dashboard_Blueprint)
app.register_blueprint(Controller.Dashboard.appointment.Appointments_Blueprint)
app.register_blueprint(Controller.AssessmentForms.assessmentform.Assessment_Blueprint)
        
@app.route("/favicon.ico")
def favicon():
    return "", 200

# @app.route("/")
# def home():
#     session = Session()
#     session.close()
#     #session.clear()
#     return jsonify('Welcome to Project')

@app.route("/")
def home():
    RequestIp = hashlib.md5((request.remote_addr).encode())
    RequestIp = RequestIp.hexdigest()
    #print(RequestIp)
    saveIp=request.remote_addr
    Common_Function.CommonFun.addRequestorIP(saveIp)
    VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
    if(int(VerifyIPAdd)==0):
        return jsonify('Welcome to Project')
    else:
        return jsonify({'error':'IP is not allowed Please contact Admin'})

def encode_auth_token(username,UserId):

    try:
        payload = {
            'exp': datetime.datetime.now() + datetime.timedelta(minutes=150),
            'id': UserId,
            'sub': username
        }
        token = jwt.encode(
            payload,
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        # token = token.decode("utf-8")
        return token
    except Exception as e:
        print(e)