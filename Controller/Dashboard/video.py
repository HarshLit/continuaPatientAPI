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
Video_Blueprint = CommonModule.flask.Blueprint(
    'Video_Blueprint', import_name=__name__)

@Video_Blueprint.route('/getAllVideos', methods=['POST','GET'])
def getActivityPlans():
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
                        # apply = []
                        
                    Videoes = Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getAllVideoes,
                                    session.query(Model.models.Application.T_Videoes.TVID.label('Id'),
                                                        Model.models.Application.T_Videoes.TV_Thumbnail.label('thumbnail'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.T_Videoes.TV_Title,'').label('title'),
                                                        Model.models.Application.T_Videoes.TV_Description.label('description'),
                                                        Model.models.Application.T_Videoes.TV_ArticleHtml.label('article'),
                                                        Model.models.Application.T_Videoes.TV_AreaAge.label('areaAge'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.T_Videoes.TV_YouNeed,'').label('youNeed'),
                                                        Model.models.Application.T_Videoes.TV_FilePath.label('filePath'),
                                                        Model.models.Application.T_Videoes.TV_FileType.label('fileType'),
                                                        Model.models.Application.T_Videoes.TV_NoofDays.label('NoofDays')
                                        ).filter_by(TV_IsActive=1,TV_IsDeleted=0
                                        ).order_by(Model.models.Application.T_Videoes.TVID.desc()).all())
                    
                    return jsonify(result=Videoes)
                        
                    # else:
                    #     return jsonify({'error':'IP is not allowed Please contact Admin'})
                else:
                    #return jsonify({'error':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
            
        # # else:
        # #     if('Authorization' in request.headers):
        # #         token= request.headers.get('Authorization')

        # #         if not token:
        # #             return jsonify({'MSG':'Token is missing'})
        # #         data=Common_Function.CommonFun.verifytoken(token)
        # #         #data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256', ])
        # #         if(data>0):
        # #             RequestIp = hashlib.md5((request.remote_addr).encode())
        # #             RequestIp = RequestIp.hexdigest()
        # #             VerifyIPAdd = Common_Function.CommonFun.verifyIP(RequestIp)
        # #             if(int(VerifyIPAdd)>0):
        # #                 apply = []
        # #                 request_json =request.get_json()
        # #                 if(request_json!='' and request_json!=None):
        # #                     Date =request_json.get('date')
                        
        # #                     if(Date!='' and Date!=None):
        # #                         apply.append((sqlalchemy.func.date_format(Model.models.Application.M_ActivityPlanDetails.MAPD_AddDate,'%Y-%m-%d'))==Date)
        # #                 else:
        # #                     apply.append((sqlalchemy.func.date_format(Model.models.Application.M_ActivityPlanDetails.MAPD_AddDate,'%Y-%m-%d'))==date.today())
        # #                 parentDtls= Common_Function.CommonFun.convertToJson(
        # #                     Constant.constant.constant.getActivityPlans,
        # #                         session.query(Model.models.Application.M_ActivityPlanDetails.MAPDID.label('actPlanId'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_Thumbnail.label('thumbnail'),
        # #                                             sqlalchemy.func.coalesce(Model.models.Application.M_ActivityPlanDetails.MAPD_Title,'').label('title'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_Description.label('description'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_ArticleHtml.label('article'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_AreaAge.label('areaAge'),
        # #                                             sqlalchemy.func.coalesce(Model.models.Application.M_ActivityPlanDetails.MAPD_YouNeed,'').label('youNeed'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_FilePath.label('filePath'),
        # #                                             Model.models.Application.M_ActivityPlanDetails.MAPD_FileType.label('fileType')
        # #                             ).filter_by(MAPD_IsActive=1,MAPD_IsDeleted=0
        # #                             ).filter(*apply
        # #                                     ).all())
                        
        # #                 return jsonify(result=parentDtls)
                        
        #             else:
        #                 return jsonify({'error':'IP is not allowed Please contact Admin'})
            #     else:
            #         #return jsonify({'error':'Token is expired'})
            #         return redirect('/')
            # else:
            #     return redirect('/')
            
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@Video_Blueprint.route('/getAllVideos/complete', methods=['POST','GET'])
def ViewedVideo():
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
                        request_json = request.get_json() #'Vipul'
                        if(request_json!='' and request_json!=None):
                            parentId =request_json.get('Id')  
                            childId = request_json.get('childId')
                            activityId =request_json.get('activityId')
                            emojiId =request_json.get('emojiId')
                            if(parentId!='' and parentId!=None and childId!='' and childId!=None and activityId!='' and activityId!=None):
                                Insert=Model.models.Application.T_PerformedActivity()
                                Insert.TPA_MPDID=parentId
                                Insert.TPA_TCDID=childId
                                Insert.TPA_MAPDID=activityId
                                Insert.TPA_IsDidIt=1
                                Insert.TPA_MPDID=emojiId
                                Insert.TPA_AddDate=datetime.datetime.now()
                                Insert.TPA_AddIP=request.remote_addr
                                session.add(Insert)
                                session.commit()
                                return jsonify({'success':'Activity Feedback done successfully'})
                            else:
                                return jsonify({'error':'All Details are not given'})
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

@Video_Blueprint.route('/getActivityPlans/uploadVideo', methods=['POST','GET'])
def uploadActivityVideo():
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

@Video_Blueprint.route('/getAllVideos/getDetails', methods=['POST','GET'])
def getAllVideosDtls():
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
                        Videoes = Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getAllVideosDtl,
                                    session.query(Model.models.Application.T_Videoes.TVID.label('Id'),
                                                        Model.models.Application.T_Videoes.TV_Thumbnail.label('thumbnail'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.T_Videoes.TV_Title,'').label('title'),
                                                        Model.models.Application.T_Videoes.TV_Description.label('description'),
                                                        Model.models.Application.T_Videoes.TV_ArticleHtml.label('article'),
                                                        Model.models.Application.T_Videoes.TV_AreaAge.label('areaAge'),
                                                        sqlalchemy.func.coalesce(Model.models.Application.T_Videoes.TV_YouNeed,'').label('youNeed'),
                                                        Model.models.Application.T_Videoes.TV_FilePath.label('filePath'),
                                                        Model.models.Application.T_Videoes.TV_FileType.label('fileType'),
                                                        Model.models.Application.T_Videoes.TV_NoofDays.label('NoofDays')
                                        ).filter_by(TV_IsActive=1,TV_IsDeleted=0,TVID=int(Id)
                                        ).order_by(Model.models.Application.T_Videoes.TVID.desc()).all())
                    
                    return jsonify(result=Videoes)
                            
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


