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
from datetime import date
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
import app
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Post_Blueprint = CommonModule.flask.Blueprint(
    'Post_Blueprint', import_name=__name__)

@Post_Blueprint.route('/createPost', methods=['POST','GET'])
def createPost():
    session = Session()
    try:
        if(flask.request.method == 'GET'):
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
                        request_json =request.get_json() #'Vipul'
                        if(request_json!='' and request_json!=None):
                            parentId =request_json.get('parentId') #8544388788 
                            childId = request_json.get('childId')
                            activityId =request_json.get('activityId')
                            Video =request_json.get('Video')
                            VideoDesc =request_json.get('VideoDesc')
                            
                            if(parentId!='' and parentId!=None and childId!='' and childId!=None and activityId!='' and activityId!=None and Video!='' and Video!=None):
                                Activity = session.query(Model.models.Application.T_PerformedActivity
                                            ).filter_by(TPAID=activityId).all()
                                if(len(Activity)>0):
                                    session.query(Model.models.Application.T_PerformedActivity
                                                ).filter_by(TPA_MPDID=int(parentId),
                                                TPA_TCDID=int(childId),TPA_MAPDID=int(activityId)
                                                ).update({Model.models.Application.T_PerformedActivity.TPA_VideoPath:Video,
                                                        Model.models.Application.T_PerformedActivity.TPA_VideoDesc:VideoDesc})
                                    session.commit()
                                    # Insert=session.query(Model.models.Application.T_PerformedActivity).get(int(activityId))
                                    # Insert.TPA_VideoPath=Video
                                    # Insert.TPA_VideoDesc=VideoDesc
                                    # Insert.TPA_ModDate=datetime.datetime.now()
                                    # Insert.TPA_ModIP=request.remote_addr
                                    # session.commit()
                                    return jsonify({'success':'Video Uploaded successfully'})
                                else:
                                    return jsonify({'error':'Activity is not done yet'})
                            else:
                                return jsonify({'error':'All Details are not given'})
                        else:
                            return jsonify({'error':'JSON not available'})
                        
                        return jsonify(result=getdailyWits)
                            
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
        
        
        
        
        
                