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
import Controller.Dashboard.activity
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
Dashboard_Blueprint = CommonModule.flask.Blueprint(
    'Dashboard_Blueprint', import_name=__name__)

@Dashboard_Blueprint.route('/getdashboard', methods=['POST','GET'])
def getdashboard():
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
                    ePatientID= request.headers.get('PatientID')
                    PatientID=Common_Function.CommonFun.decryptString(ePatientID)
                    # request_json = request.get_json()
                    # if(request_json!='' and request_json!=None):
                    #     ParentId = request_json.get('ParentId') 
                        
                    ChildId = Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.Childdtl,
                                    session.query(Model.models.Application.M_PatientFamily.MPFID.label('Id'),
                        Model.models.Application.M_PatientFamily.MPF_Name.label('Name')
                        ).filter(Model.models.Application.M_PatientFamily.MPF_UserId==PatientID
                        ).all())
                    session.commit()
                    session.close()
                        
                    option=[]
                    # DailyWits= Common_Function.CommonFun.getdailyWits()
                    # Actionplan = Common_Function.CommonFun.getActionPlan()
                    # ActivityCateg = Common_Function.CommonFun.getActivityCateg()
                    Articles= Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.T_Articles,
                                        session.query(Model.models.Application.T_Articles.TAID.label('Id'),
                                                            sqlalchemy.func.coalesce(Model.models.Application.T_Articles.TA_Title,'').label('articleTitle'),
                                                            Model.models.Application.T_Articles.TA_Thumbnail.label('articleThumbnail'),
                                                            Model.models.Application.T_Articles.TA_Description.label('articleDesc'),
                                                            Model.models.Application.T_Articles.TA_ArticleHtml.label('articleHtml'),
                                                            ).filter_by(TA_IsActive=1,TA_IsDeleted=0).limit(2))
                    
                    Videoes = Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.getVideoes,
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
                                            ).limit(3))
                    
                    # ActivityCateg= Common_Function.CommonFun.convertToJson(
                    #                 Constant.constant.constant.AllCteg,
                    #                     session.query(Model.models.Application.M_ParamDetails.MPDID.label('Id'),
                    #                                         Model.models.Application.M_ParamDetails.MPD_Value.label('Value'),
                    #                                         sqlalchemy.func.coalesce(Model.models.Application.M_ParamDetails.MPD_Icon,'').label('Icon')
                    #                                         ).filter_by(MPD_IsActive=1,MPD_IsDeleted=0,MPD_MPID=2
                    #                         ).limit(3))
                    # Datebetween = {'ActivityDate':'Dec,01 2021 - Dec 20,2021'}
                    # ActivityPerform= {'ActivityPerformed':'5','MilestoneAchieve':'5'}
                    option.append({'Videoes':Videoes,'Articles':Articles,'ChildDetails':ChildId})
                    return jsonify(result=option),200
                            
                    
                else:
                    #return jsonify({'err':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'}) ,405
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()
        
        
       