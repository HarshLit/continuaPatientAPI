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
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Appointment_Blueprint = CommonModule.flask.Blueprint(
    'Appointment_Blueprint', import_name=__name__)

@Appointment_Blueprint.route('/getAppointment', methods=['POST','GET'])
def getAppointment():
    session=Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                serviceId = request_json.get('serviceId') 
                familyId = request_json.get('familyId') 
                getAppointment= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getAppointment,
                        session.query(Model.models.Application.M_PatientFamily.MPF_MemberId.label('memberId'),
                                    Model.models.Application.M_PatientFamily.MPFID.label('Id'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_PatientFamily.MPF_DOB,'%d-%b-%Y').label('DOB'),
                                    Model.models.Application.M_PatientFamily.MPF_Name.label('Name')
                                    ).filter_by(MPF_IsDeleted=0,MPF_IsActive=1,MPFID=familyId).all()
                                )
                session.commit()
                getAppointmentDetails= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getAppointmentDetails,
                        session.query(Model.models.Application.M_PatientServices.MPS_TopicName.label('topicName'),
                                    Model.models.Application.M_PatientServices.MPSID.label('Id')
                                    ).filter_by(MPS_IsDeleted=0,MPS_IsActive=1,MPSID=familyId).all()
                                )
                session.commit()
                eBranchName= request.headers.get('branchName')
                option = []
                # x = {'appointmentDetails': getAppointmentDetails}
                # y = {'getAppointment': getAppointment}
                option.append({'detail':getAppointment,'details':getAppointmentDetails,'branch':eBranchName})
                return jsonify(result=option),200
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()

@Appointment_Blueprint.route('/addAppointment', methods=['POST','GET'])
def addAppointment():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            eBranchID= request.headers.get('branchId')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                name = request_json.get('name') 
                DOB = request_json.get('DOB') 
                familyId =request_json.get('familyId')
                serviceId =request_json.get('serviceId')
                serviceDetails =request_json.get('serviceDetails')
                date =request_json.get('date')
                time =request_json.get('time')
                location =request_json.get('location')
                videoSession =request_json.get('videoSession')
                comments =request_json.get('comments')
                files =request_json.get('files')

                if(familyId !='' and familyId!=None and userId !='' and userId!=None and serviceId !='' and serviceId!=None):
                    Insert = Model.models.Application.M_AddAppointment()
                    Insert.MAA_PatientId = userId
                    Insert.MAA_Name = name
                    Insert.MAA_DOB = DOB
                    Insert.MAA_MemeberId = familyId
                    Insert.MAA_ServiceDetails = serviceDetails
                    Insert.MAA_ServiceConsultId = serviceId
                    Insert.MAA_Date = date
                    Insert.MAA_Time = time
                    Insert.MAA_VideoSession = videoSession
                    Insert.MAA_Comment = comments
                    Insert.MAA_Files = files
                    Insert.MAA_Location = eBranchID
                    
                    Insert.MAA_AddDate = datetime.datetime.now()
                    Insert.MAA_AddIP = request.remote_addr
                    session.add(Insert)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Appointment Added Successfully'})
                    
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


@Appointment_Blueprint.route('/getBranch', methods=['POST','GET'])
def getBranch():
    session=Session()
    try:
        getBranch= Common_Function.CommonFun.convertToJson(
                Constant.constant.constant.getBranch,
                session.query(Model.models.Application.M_Branch.MBID.label('key'),
                            Model.models.Application.M_Branch.MB_Name.label('label')
                            ).filter_by(MB_IsActive=1,MB_IsDeleted=0).order_by(Model.models.Application.M_Branch.MB_Name).all()
                        )
        session.commit()
        return jsonify(result=getBranch),200
    except Exception as identifier:
        print('No parameter is passed.')
     
