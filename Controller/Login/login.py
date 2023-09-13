import hashlib
from logging import Logger
import random
import flask
from flask import Flask, redirect, request, jsonify
import jwt
from requests import session
import Model.models
import datetime
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
#from app import encode_auth_token
import app
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Login_Blueprint = CommonModule.flask.Blueprint(
    'Login_Blueprint', import_name=__name__)

@Login_Blueprint.route('/validCredential', methods=['GET','POST'])
def validCredential():
    session = Session()
    try:
        if(request.method == "POST"):
            RequestIp = hashlib.md5((request.remote_addr).encode())
            RequestIp = RequestIp.hexdigest()
            #print(RequestIp)
            VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
            if(int(VerifyIPAdd)==0):
                session = Session()
                request_json = request.get_json()
                if(request_json!='' and request_json!=None):
                    username = request_json.get('username')
                    pswd = request_json.get('pswd')
                    DbUserName= session.query(Model.models.Application.M_PatientsDtl.MPD_Name,
                                            Model.models.Application.M_PatientsDtl.MPDID,
                                            Model.models.Application.M_PatientsDtl.MPD_hashedPassword
                                            ).filter_by(MPD_Username=username, MPD_IsActive=1,MPD_User=1, MPD_IsDeleted=0
                    ).all()
                    # session.commit()
                    if(len(DbUserName) > 0):
                        getDbUserName = session.query(Model.models.Application.M_PatientsDtl.MPD_Name,
                                            Model.models.Application.M_PatientsDtl.MPDID,
                                            Model.models.Application.M_PatientsDtl.MPD_Mobile,
                                            Model.models.Application.M_PatientsDtl.MPD_hashedPassword).filter_by(
                        MPD_hashedPassword=pswd, MPD_Username=username, MPD_User=1, MPD_IsActive=1, MPD_IsDeleted=0).all()
                        if(len(getDbUserName) > 0):
                        
                            disable= disabletoken(username)
                            token = app.encode_auth_token(username,getDbUserName[0].MPDID)
                            ChildCounts = Common_Function.CommonFun.Childcount(getDbUserName[0].MPD_Mobile)
                            # print(ChildCounts)
                            Id = getDbUserName[0].MPDID
                            Mobile = getDbUserName[0].MPD_Mobile
                            add_Token(token,username,Id)
                            # print(token)
                            output = []
                            eId=Common_Function.CommonFun.encryptString(str(Id))
                            output.append({'PatientID':eId,'Mobile':Mobile,'token':token,'ChildCount':ChildCounts,'Name':getDbUserName[0].MPD_Name
                                            })
                            
                            return jsonify(result=output)
                        else:
                            return jsonify({'error':'Please enter correct password'})
                    else:
                        return jsonify({'error':'Not Registered'})
                else:
                    return jsonify({'error':'JSON not available'})
            else:
                return jsonify({'error':'IP is not allowed Please contact Admin'})
        else:
            return jsonify({'error':'method not allowed'})
    finally:
        session.close()

def add_Token(token,username,Id):
    session = Session()
    try:
        Insert= Model.models.Application.T_TokenLog()
        Insert.TL_Token=token
        Insert.TL_UserName=username
        Insert.TL_UserId=Id
        Insert.TL_AddDate=datetime.datetime.now()
        Insert.TL_AddIp=request.remote_addr
        Insert.TL_IsActive=1
        Insert.TL_IsDeleted=0
        session.add(Insert)
        session.commit()
        session.close()
    except Exception as e:
        print(e)

def disabletoken(username):
    session = Session()
    try:
        session.query(Model.models.Application.T_TokenLog
                      ).filter(Model.models.Application.T_TokenLog.TL_UserName==username
                    ).update({Model.models.Application.T_TokenLog.TL_IsDeleted:0})
        session.commit()
        session.close()
    except Exception as e:
        print(e)        

        
        