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
from sqlalchemy import and_, or_
from Common_Function import Shared_Library as CommonModule
import app
import Constant.constant
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
PatientServices_Blueprint = CommonModule.flask.Blueprint(
    'PatientServices_Blueprint', import_name=__name__)

@PatientServices_Blueprint.route('/getServices', methods=['POST','GET'])
def getServices():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
                getServices= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getServices,
                        session.query(Model.models.Application.M_PatientServices.MPSID.label('Id'),
                                    Model.models.Application.M_PatientServices.MPS_TopicName.label('Heading'),
                                    Model.models.Application.M_PatientServices.MPS_Description.label('Description')
                                    ).filter_by(MPS_IsDeleted=0,MPS_IsActive=1).all()
                                )
                session.commit()
                return jsonify(result=getServices),200
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()  

@PatientServices_Blueprint.route('/addServiceEnquire', methods=['POST','GET'])
def addServiceEnquire():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                serviceId = request_json.get('serviceId') 
                enquireMsg = request_json.get('enquireMsg') 
                branchId = 1#request_json.get('branchId')

                if(enquireMsg !='' and enquireMsg!=None and userId !='' and userId!=None and serviceId !='' and serviceId!=None):
                    Insert = Model.models.Application.M_PatientEnquire()
                    Insert.MPE_PatientId = userId
                    Insert.MPE_ServiceId = serviceId
                    Insert.MPE_EnqMessage = enquireMsg
                    Insert.MPE_BranchId = branchId
                    
                    Insert.MPE_AddDate = datetime.datetime.now()
                    Insert.MPE_AddIP = request.remote_addr
                    session.add(Insert)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Enquire Added Successfully'})
                    
                else:
                    jsonify({'error':'Please Enter Name and DOB'})
                        
                
            else:
                return jsonify({'error':'JSON not available'})
            #     else:
            #         return redirect('/')
            # else:
            #     return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@PatientServices_Blueprint.route('/getServiceDoctors', methods=['POST','GET'])
def getServiceDoctors():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                serviceId =request_json.get('serviceId') 
                branchId = 1#request_json.get('branchId')

                # if(serviceId !='' and serviceId!=None):
                getServiceDoctors= Common_Function.CommonFun.convertToJson(
                    Constant.constant.constant.getServiceDoctors,
                    session.query(sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ', Model.models.Application.M_DoctorDetails.MDD_LastName).label('Name'),
                                Model.models.Application.M_DoctorDetails.MDDID.label('DoctorId'),
                                Model.models.Application.M_DoctorDetails.MDD_OnlineFeeINR.label('Fees'),
                                Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                Model.models.Application.M_DoctorMedicalDetails.MDMD_Category.label('Category')
                                ).filter_by(MDD_IsDeleted=0,MDD_IsActive=1
                                ).filter(Model.models.Application.M_DoctorDetails.MDD_Type!='Therapist'
                                ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId==Model.models.Application.M_DoctorDetails.MDDID
                                ).all()
                            )
                session.commit()
                return jsonify(result=getServiceDoctors),200
                
            else:
                return jsonify({'error':'JSON not available'})
            
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()     

@PatientServices_Blueprint.route('/serviceDoctorDetails', methods=['POST','GET'])
def serviceDoctorDetails():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId =int(PatientID)
                DoctorId =request_json.get('DoctorId') 
                branchId = 1#request_json.get('branchId')

                if(DoctorId !='' and DoctorId!=None):
                    serviceDoctorDetails= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.serviceDoctorDetails,
                        session.query(Model.models.Application.M_DoctorDetails.MDDID.label('DoctorId'),
                                    sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ', Model.models.Application.M_DoctorDetails.MDD_LastName).label('Name'),
                                   
                                    Model.models.Application.M_DoctorDetails.MDD_OnlineFeeINR.label('Fees'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_Category.label('Category'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_MedicalDegree.label('MedicalDegree'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_Registration.label('Registration'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_PracticingSince.label('PracticingSince'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_MedicalExpertise.label('MedicalExpertise'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_AwardRecognitions.label('AwardRecognitions'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_Languages.label('Languages')
                                    ).filter_by(MDD_IsDeleted=0,MDD_IsActive=1,MDDID=int(DoctorId)
                                    ).join(Model.models.Application.M_DoctorMedicalDetails,
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId==Model.models.Application.M_DoctorDetails.MDDID
                                    ).all()
                                )
                    session.commit()
                    return jsonify(result=serviceDoctorDetails),200
                    
                else:
                    jsonify({'error':'Please Enter DoctorId'})
                        
                
            else:
                return jsonify({'error':'JSON not available'})
            #     else:
            #         return redirect('/')
            # else:
            #     return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@PatientServices_Blueprint.route('/serviceConsultForm', methods=['POST','GET'])
def serviceConsultForm():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            # if('Authorization' in request.headers):
            #     token= request.headers.get('Authorization')

            #     if not token:
            #         return jsonify({'MSG':'Token is missing'})
            #     data=Common_Function.CommonFun.verifytoken(token)
            #     #data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256', ])
            #     if(data>0):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            request_json = request.get_json()
            if(request_json!='' and request_json!=None):
                userId = int(PatientID)
                doctorName = request_json.get('doctorName') 
                files = request_json.get('files[]') 
                patientName = request_json.get('patientName') 
                consultQuery = request_json.get('consultQuery')
                sinceWhen = request_json.get('sinceWhen')
                currentMedication = request_json.get('currentMedication')

                if(doctorName !='' and doctorName!=None and patientName !='' and patientName!=None):
                    Insert=Model.models.Application.M_ServiceConsultForm()
                    Insert.MSC_DoctorName = doctorName
                    Insert.MSC_PatientName = patientName
                    Insert.MSC_ConsultQuery = consultQuery
                    Insert.MSC_SinceWhen = sinceWhen
                    Insert.MSC_CurrentMeditation = currentMedication
                    
                    Insert.MSC_ModDate = datetime.datetime.now()
                    Insert.MSC_ModUser = int(PatientID)
                    session.add(Insert)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Consult Form Saved Successfully'})
                    
                else:
                    jsonify({'error':'Please Check Doctor and Patient Name'})
                        
                
            else:
                return jsonify({'error':'JSON not available'})
            #     else:
            #         return redirect('/')
            # else:
            #     return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()   

@PatientServices_Blueprint.route('/getConditions', methods=['POST','GET'])
def getConditions():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
                getConditions= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getConditions,
                        session.query(Model.models.Application.M_PatientConditions.MPSID.label('Id'),
                                    Model.models.Application.M_PatientConditions.MPS_TopicName.label('Heading'),
                                    Model.models.Application.M_PatientConditions.MPS_Description.label('Description')
                                    ).filter_by(MPS_IsDeleted=0,MPS_IsActive=1).all()
                                )
                session.commit()
                return jsonify(result=getConditions),200
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()






