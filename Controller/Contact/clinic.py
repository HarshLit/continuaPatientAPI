import hashlib
from logging import Logger
import random
import flask
from flask import Flask, redirect, request, jsonify
import jwt
import sqlalchemy
import Model.models
import datetime
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
import app
import Constant.constant

Session = Connection.const.connectToDatabase()
Contact_Blueprint = CommonModule.flask.Blueprint(
    'Contact_Blueprint', import_name=__name__)

@Contact_Blueprint.route('/contactClinic', methods=['POST','GET'])
def contactClinic():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            eBranchID= request.headers.get('branchId')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                message = request_json.get('message') 
                
                if(userId !='' and userId!=None and message !='' and message!=None):
                    Insert = Model.models.Application.M_ContactClinic()
                    Insert.MCC_UserId = userId
                    Insert.MCC_Message = message
                
                    Insert.MCC_AddDate = datetime.datetime.now()
                    Insert.MCC_AddIP = request.remote_addr
                    session.add(Insert)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Your messsage send to Continua kids.We will get in touch with you shortly!'})
                    
                else:
                    jsonify({'error':'Please Enter Name and DOB'})
                        
                
            else:
                return jsonify({'error':'JSON not available'})
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()    