import hashlib
from logging import Logger
import random
from tkinter import N
from tkinter.messagebox import NO
import flask
from flask import Flask, redirect, request, jsonify
import jwt
import sqlalchemy
import Constant.constant
import Model.models
import datetime
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
import app
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Parent_Blueprint = CommonModule.flask.Blueprint(
    'Parent_Blueprint', import_name=__name__)

@Parent_Blueprint.route('/getParentData', methods=['POST','GET'])
def getParentData():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data=Common_Function.CommonFun.verifytoken(token)
                #data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256', ])
                if(data>0):
                    RequestIp = hashlib.md5((request.remote_addr).encode())
                    RequestIp = RequestIp.hexdigest()
                    VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
                    if(int(VerifyIPAdd)>0):
                        request_json =  request.get_json() #'Vipul'
                        if(request_json!='' and request_json!=None):
                            parentId = request_json.get('parentId') #8544388788 
                            if(parentId!='' and parentId!=None):
                                parentDtls= Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.getParentData,
                                        session.query(Model.models.Application.M_ParentSignUpDetails.MPDID.label('ParentId'),
                                                        Model.models.Application.M_ParentSignUpDetails.MPD_FirstName.label('ParentFirstName'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.M_ParentSignUpDetails.MPD_LastName,'').label('ParentLastName'),
                                                        Model.models.Application.M_ParentSignUpDetails.MPD_Mobile.label('ParentMobile'),
                                                        Model.models.Application.M_ParentSignUpDetails.MPD_MPDID.label('ParentRelationId'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.M_ParentSignUpDetails.MPD_Email,'').label('ParentEmail'),
                                                        Model.models.Application.M_ParamDetails.MPD_Value.label('ParentRelation')
                                            ).filter_by(MPDID=int(parentId),MPD_IsActive=1,MPD_IsDeleted=0
                                            ).join(Model.models.Application.M_ParamDetails,
                                    Model.models.Application.M_ParamDetails.MPDID==Model.models.Application.M_ParentSignUpDetails.MPD_MPDID
                                    ).all())
                                
                                return jsonify(result=parentDtls)
                            else:
                                #flask.session.clear()
                                return redirect('/')    
                                
                        # return jsonify({'error':'IP is valid'})
                    else:
                        return jsonify({'error':'IP is not allowed Please contact Admin'})
                else:
                    #return jsonify({'error':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@Parent_Blueprint.route('/updateParent', methods=['POST','GET'])
def updateParent():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data=Common_Function.CommonFun.verifytoken(token)
                #data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256', ])
                if(data>0):
                    RequestIp = hashlib.md5((request.remote_addr).encode())
                    RequestIp = RequestIp.hexdigest()
                    #print(RequestIp)
                    VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
                    if(int(VerifyIPAdd)>0):
                        request_json =  request.get_json() #'Vipul'
                        if(request_json!='' and request_json!=None):
                            Mobile =request_json.get('mobile') #8544388788 
                            firstName =request_json.get('firstName') #'Vipul Kumar' #
                            secondName = request_json.get('secondName') #'Vipul Kumar' #
                            Relation =request_json.get('relation')  #3 #
                            Email = request_json.get('email') #'Yes' #
                            parentId =request_json.get('parentId') #'Yes' #
                            if(firstName !='' and firstName!=None and Mobile !='' and Mobile!=None):
                                Insert = session.query(Model.models.Application.M_ParentSignUpDetails).get(int(parentId))
                                if(Mobile !='' and Mobile!=None):
                                    Insert.MPD_Mobile = Mobile
                                
                                    Insert.MPD_FirstName = firstName
                                    Insert.MPD_LastName = secondName
                                if(Relation !='' and Relation!=None):
                                    Insert.MPD_MPDID = Relation
                                Insert.MPD_Email = Email    
                                Insert.MPD_ModDate = datetime.datetime.now()
                                Insert.MPD_ModIP = request.remote_addr
                                session.commit()
                                session.close()
                                
                                return jsonify({'success':'User Updated Successfully'})
                                
                            else:
                                jsonify({'error':'Please enter FirstName / Mobile'})
                                
                        # return jsonify({'error':'IP is valid'})
                    else:
                        return jsonify({'error':'IP is not allowed Please contact Admin'})
                else:
                    #return jsonify({'error':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
        return redirect('/')
    finally:
        session.close()

