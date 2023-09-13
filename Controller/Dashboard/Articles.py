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
Articles_Blueprint = CommonModule.flask.Blueprint(
    'Articles_Blueprint', import_name=__name__)

@Articles_Blueprint.route('/getAllArticles', methods=['POST','GET'])
def getAllArticles():
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
                    # RequestIp = hashlib.md5((request.remote_addr).encode())
                    # RequestIp = RequestIp.hexdigest()
                    # VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
                    # if(int(VerifyIPAdd)>0):
                    Articles= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getAllArticles,
                                    session.query(Model.models.Application.T_Articles.TAID.label('Id'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.T_Articles.TA_Title,'').label('articleTitle'),
                                                        Model.models.Application.T_Articles.TA_Thumbnail.label('articleThumbnail'),
                                                        Model.models.Application.T_Articles.TA_Description.label('articleDesc'),
                                                        Model.models.Application.T_Articles.TA_ArticleHtml.label('articleHtml'),
                                                        ).filter_by(TA_IsActive=1,TA_IsDeleted=0).all())
                    
                    return jsonify(result=Articles)
                            
                    # else:
                    #     return jsonify({'error':'IP is not allowed Please contact Admin'})
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
        
@Articles_Blueprint.route('/getAllArticles/getDetails', methods=['POST','GET'])
def getAllArticlesDtls():
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
                    # RequestIp = hashlib.md5((request.remote_addr).encode())
                    # RequestIp = RequestIp.hexdigest()
                    # VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
                    # if(int(VerifyIPAdd)>0):
                    request_json = request.get_json()
                    if(request_json!='' and request_json!=None):
                        Id = request_json.get('Id')
                        Articles= Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.getAllArticlesDtl,
                                        session.query(Model.models.Application.T_Articles.TAID.label('Id'),
                                                            sqlalchemy.func.coalesce(Model.models.Application.T_Articles.TA_Title,'').label('articleTitle'),
                                                            Model.models.Application.T_Articles.TA_Thumbnail.label('articleThumbnail'),
                                                            Model.models.Application.T_Articles.TA_Description.label('articleDesc'),
                                                            Model.models.Application.T_Articles.TA_ArticleHtml.label('articleHtml'),
                                                            ).filter_by(TA_IsActive=1,TA_IsDeleted=0,TAID =int(Id) ).all())
                        
                        return jsonify(result=Articles)
                            
                    # else:
                    #     return jsonify({'error':'IP is not allowed Please contact Admin'})
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
        
@Articles_Blueprint.route('/getBroadcastdtls', methods=['GET','POST'])
def getBroadcastdtls():
    session=Session()
    try:
        if(request.method == "GET"):

            # queryresult= Common_Function.CommonFun.convertToJson(
            #         Constant.constant.constant.getBroadcastdtls,
            #         session.query(Model.models.Application.M_Broadcast.MBID.label('Id'),
            #                     Model.models.Application.M_Broadcast.MB_Title.label('Title'),
            #                     Model.models.Application.M_Broadcast.MB_Message.label('Message')
            #                     ).filter_by(MB_IsDeleted=0
            #                     ).order_by(Model.models.Application.M_Broadcast.MBID.desc()).all()
            #                 )
            x=session.query(Model.models.Application.M_Broadcast.MBID.label('Id'),
                                Model.models.Application.M_Broadcast.MB_Title.label('Title'),
                                Model.models.Application.M_Broadcast.MB_Message.label('Message')
                                ).filter_by(MB_IsDeleted=0
                                ).order_by(Model.models.Application.M_Broadcast.MBID.desc()).first()
            session.commit()
            test = {'Id':x[0],'img':x[1],'Message':x[2]}
            return jsonify(result=test)
    finally:
        session.close()        
        
        
                