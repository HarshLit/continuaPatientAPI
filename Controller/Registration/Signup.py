import hashlib
from logging import Logger
import random
import re
import flask
from flask import Flask, request, jsonify
import Model.models
import datetime
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule

# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Register_Blueprint = CommonModule.flask.Blueprint(
    'Register_Blueprint', import_name=__name__)

@Register_Blueprint.route('/signUp', methods=['POST','GET'])
def signUp():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            
            RequestIp = hashlib.md5((request.remote_addr).encode())
            RequestIp = RequestIp.hexdigest()
            #print(RequestIp)
            
            request_json = request.get_json() #'Vipul'#
            if(request_json!='' and request_json!=None):
                Mobile = request_json.get('mobile') # 8544388789 #
                Name = request_json.get('name') # 'Vipul Kumar' #
                Email = request_json.get('email')  #'vipulvict@gmail.com' #
                #TermsConds = request_json.get('termsConds') #'Yes' #
                Password = request_json.get('password') #'V!pul@4812' #
                
                if(Mobile !='' and Mobile!=None):
                    # reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
                    # pat = re.compile(reg)
                    # mat = re.search(pat, Password)
                    # if mat:
                    pswrd= hashlib.sha1(Password.encode())
                    ChcekPWd = pswrd.hexdigest()
                    CheckMobile = Common_Function.CommonFun.verifyMobile(Mobile)
                    if(CheckMobile==0):
                        Insert = Model.models.Application.M_PatientsDtl()
                        if(Mobile !='' and Mobile!=None):
                            Insert.MPD_Mobile = Mobile
                        if(Name !='' and Name!=None):
                            Insert.MPD_Name = Name
                        if(Email !='' and Email!=None):
                            Insert.MPD_Email = Email
                        Insert.MPD_Username = Mobile
                        Insert.MPD_Password = Password
                        Insert.MPD_hashedPassword = ChcekPWd       
                        Insert.MPD_AddDate = datetime.datetime.now()
                        Insert.MPD_AddIP = request.remote_addr
                        Insert.MPD_User = 0
                        session.add(Insert)
                        session.commit()
                        session.close()
                        
                        PatientNo = session.query(Model.models.Application.M_PatientsDtl.MPDID).order_by(
                                                Model.models.Application.M_PatientsDtl.MPDID.desc()
                        ).all()
                        output = []
                            
                        output.append({'success':'Registered Successfully','PatientId':PatientNo[0].MPDID
                                        })
                        
                        return jsonify(result=output)
                        # return jsonify({'success':'Registered Successfully','PatientId':PatientNo}),201
                    else:
                        return jsonify({'error':'Mobile No already registered'})
                    # else:
                    #     return jsonify({'error':'Mobile No already registered'}),409
                else:
                    return jsonify({'error':'Not Matched'})
                        
            else:
                return jsonify({'error':'JSON not available'})
            
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@Register_Blueprint.route('/verifyOtp', methods=['POST','GET'])
def verifyOtp():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            RequestIp = hashlib.md5((request.remote_addr).encode())
            RequestIp = RequestIp.hexdigest()
            #print(RequestIp)
            
            request_json = request.get_json() #'Vipul'#
            if(request_json!='' and request_json!=None):
                PatientId =request_json.get('PatientId') # 8544388789 #
                otpVerify = request_json.get('otpVerify') # 'Vipul Kumar' #
                Insert = session.query(Model.models.Application.M_PatientsDtl).get(PatientId)
                Insert.MPD_ModDate = datetime.datetime.now()
                Insert.MPD_User = 1
                session.commit()
                session.close()       
                return jsonify({'error':'User verified successfully'}),201 
            else:
                return jsonify({'error':'JSON not available'}),400
            
        else:
            return jsonify({'error':'Method is not allowed'}),405
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@Register_Blueprint.route('/forgetPassword', methods=['POST','GET'])
def forgetPassword():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            RequestIp = hashlib.md5((request.remote_addr).encode())
            RequestIp = RequestIp.hexdigest()
            #print(RequestIp)
            
            request_json = request.get_json() #'Vipul'#
            if(request_json!='' and request_json!=None):
                mobileNo =request_json.get('mobileNo') # 8544388789 #
                password = request_json.get('password') # 'Vipul Kumar' #
                PatientNo = session.query(Model.models.Application.M_PatientsDtl.MPDID
                                            ).filter_by(MPD_Mobile=mobileNo
                                        ).order_by(Model.models.Application.M_PatientsDtl.MPDID.desc()).all()
                pswrd= hashlib.sha1(password.encode())
                ChcekPWd = pswrd.hexdigest()
                PatientId = PatientNo[0].MPDID
                Insert = session.query(Model.models.Application.M_PatientsDtl).get(PatientId)
                Insert.MPD_Password = password
                Insert.MPD_User = 1
                Insert.MPD_hashedPassword = ChcekPWd
                Insert.MPD_ModDate = datetime.datetime.now()
                Insert.MPD_IsActive = 1
                Insert.MPD_IsDeleted = 0
                session.commit()
                session.close()       
                return jsonify({'success':'Password Created successfully'}),201 
            else:
                return jsonify({'error':'JSON not available'}),400
            
        else:
            return jsonify({'error':'Method is not allowed'}),405
    except Exception as identifier:
        Logger.error(identifier) 
    finally:
        session.close()        
        