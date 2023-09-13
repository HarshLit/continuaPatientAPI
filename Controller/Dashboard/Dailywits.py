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
Dailywits_Blueprint = CommonModule.flask.Blueprint(
    'Dailywits_Blueprint', import_name=__name__)

@Dailywits_Blueprint.route('/getdailyWits', methods=['POST','GET'])
def getdailyWits():
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
                        getdailyWits= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.getdailyWits,
                                session.query(Model.models.Application.T_ActivityBlogs.TABID.label('Id'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_MPDID.label('categoryId'),
                                                    sqlalchemy.func.coalesce(Model.models.Application.T_ActivityBlogs.TAB_Title,'').label('activityTitle'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_Thumbnail.label('activityThumbnail'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_Description.label('activityDesc'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_Html.label('activityHtml'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_FilePath.label('activityFilePath'),
                                                    Model.models.Application.T_ActivityBlogs.TAB_FileType.label('activityFileType'),
                                                    ).filter_by(TAB_IsActive=1,TAB_IsDeleted=0,TAB_MPDID=9
                        ).all())
                        
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
        
        
        
        
        
                