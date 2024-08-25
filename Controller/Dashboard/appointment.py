import hashlib
from logging import Logger
import random
from tkinter import N
from tkinter.messagebox import NO
import flask
from flask import Flask, redirect, request, jsonify
import jwt
import pandas as pd
import requests
import sqlalchemy
import Constant.constant
import Model.models
import datetime
from datetime import date
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from sqlalchemy import and_
from Common_Function import Shared_Library as CommonModule
import app
from sqlalchemy import text
from sqlalchemy import func
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Appointments_Blueprint = CommonModule.flask.Blueprint(
    'Appointments_Blueprint', import_name=__name__)

@Appointments_Blueprint.route('/getUpcomingAppointment', methods=['POST','GET'])
def getUpcomingAppointment():
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
                    
                    Mobilenum= request.headers.get('Mobilenumber')
                    mob = Mobilenum[3:]
                    childDtl = session.query(Model.models.Application.M_Patient.MPID,
                            Model.models.Application.M_Patient.MP_Name
                            ).filter_by(MP_Mobile=int(mob)).all()
                    ChildId = [d['MPID'] for d in childDtl]
                    currentdate = datetime.datetime.now().strftime('%Y%m%d')
                    Appointments= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getUpcomingAppointment,
                                session.query(Model.models.Application.M_Appointment.MAID.label('Id'),
                                Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                Model.models.Application.M_Appointment.MP_Procedure,
                                Model.models.Application.M_Service.MS_CategoryName.label('procedure'),
                                Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%W, %d-%b-%Y').label('date'),
                                sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Time,'%I:%i %p').label('time'),
                                Model.models.Application.M_Appointment.M_DoctorDetails_MDDID.label('DoctorId'),
                                sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctor'),
                                Model.models.Application.M_Appointment.MP_Status.label('status')
                                ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0,MP_Status=29
                                ).filter(Model.models.Application.M_Appointment.M_Patient_MPID.in_(ChildId)
                                ).filter(sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%Y%m%d') >= currentdate
                                ).join(Model.models.Application.M_DoctorDetails,
                                Model.models.Application.M_DoctorDetails.MDDID == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                ).outerjoin(Model.models.Application.M_Service, 
                                Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                ).join(Model.models.Application.M_Patient,
                                Model.models.Application.M_Patient.MPID == Model.models.Application.M_Appointment.M_Patient_MPID).all())
                    
                    return jsonify(result=Appointments) 
                            
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


@Appointments_Blueprint.route('/getAllAppointment', methods=['POST','GET'])
def getAllAppointment():
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
                    
                    Mobilenum= request.headers.get('Mobilenumber')
                    mob = Mobilenum[3:]
                    childDtl = session.query(Model.models.Application.M_Patient.MPID,
                            Model.models.Application.M_Patient.MP_Name
                            ).filter_by(MP_Mobile=int(mob)).all()
                    ChildId = [d['MPID'] for d in childDtl]
                    Appointments= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getAllAppointment,
                                    session.query(Model.models.Application.M_Appointment.MAID.label('Id'),
                                    Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                    Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                    Model.models.Application.M_Appointment.MP_Procedure,
                                    Model.models.Application.M_Service.MS_CategoryName.label('procedure'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%W, %d-%b-%Y').label('date'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Time,'%I:%i %p').label('time'),
                                    Model.models.Application.M_Appointment.M_DoctorDetails_MDDID,
                                    sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctor'),
                                    Model.models.Application.M_Appointment.MP_Status.label('status')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0
                                    ).filter(Model.models.Application.M_Appointment.M_Patient_MPID.in_(ChildId)
                                    ).join(Model.models.Application.M_DoctorDetails,
                                    Model.models.Application.M_DoctorDetails.MDDID == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).join(Model.models.Application.M_Service, 
                                    Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                    ).join(Model.models.Application.M_Patient,
                                    Model.models.Application.M_Patient.MPID == Model.models.Application.M_Appointment.M_Patient_MPID).all())
                    
                    return jsonify(result=Appointments) 
                            
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
 
@Appointments_Blueprint.route('/getCancelledAppointment', methods=['POST','GET'])
def getCancelledAppointment():
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
                    
                    Mobilenum= request.headers.get('Mobilenumber')
                    mob = Mobilenum[3:]
                    childDtl = session.query(Model.models.Application.M_Patient.MPID,
                            Model.models.Application.M_Patient.MP_Name
                            ).filter_by(MP_Mobile=int(mob)).all()
                    ChildId = [d['MPID'] for d in childDtl]
                    Appointments= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getCancelledAppointment,
                                    session.query(Model.models.Application.M_Appointment.MAID.label('Id'),
                                    Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                    Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                    Model.models.Application.M_Appointment.MP_Procedure,
                                    Model.models.Application.M_Service.MS_CategoryName.label('procedure'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%W, %d-%b-%Y').label('date'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Time,'%I:%i %p').label('time'),
                                    Model.models.Application.M_Appointment.M_DoctorDetails_MDDID,
                                    sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctor'),
                                    Model.models.Application.M_Appointment.MP_Status.label('status')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=1
                                    ).filter(Model.models.Application.M_Appointment.M_Patient_MPID.in_(ChildId)
                                    ).join(Model.models.Application.M_DoctorDetails,
                                    Model.models.Application.M_DoctorDetails.MDDID == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).join(Model.models.Application.M_Service, 
                                    Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                    ).join(Model.models.Application.M_Patient,
                                    Model.models.Application.M_Patient.MPID == Model.models.Application.M_Appointment.M_Patient_MPID).all())
                    
                    return jsonify(result=Appointments) 
                            
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

@Appointments_Blueprint.route('/getCompletedAppointment', methods=['POST','GET'])
def getCompletedAppointment():
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
                    
                    Mobilenum= request.headers.get('Mobilenumber')
                    mob = Mobilenum[3:]
                    childDtl = session.query(Model.models.Application.M_Patient.MPID,
                            Model.models.Application.M_Patient.MP_Name
                            ).filter_by(MP_Mobile=int(mob)).all()
                    ChildId = [d['MPID'] for d in childDtl]
                    Appointments= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getCompletedAppointment,
                                    session.query(Model.models.Application.M_Appointment.MAID.label('Id'),
                                    Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                    Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                    Model.models.Application.M_Appointment.MP_Procedure,
                                    Model.models.Application.M_Service.MS_CategoryName.label('procedure'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%W, %d-%b-%Y').label('date'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Time,'%I:%i %p').label('time'),
                                    Model.models.Application.M_Appointment.M_DoctorDetails_MDDID,
                                    sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctor'),
                                    Model.models.Application.M_Appointment.MP_Status.label('status')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0
                                    ).filter(Model.models.Application.M_Appointment.M_Patient_MPID.in_(ChildId),
                                    Model.models.Application.M_Appointment.MP_Status.in_([393,527])
                                    ).join(Model.models.Application.M_DoctorDetails,
                                    Model.models.Application.M_DoctorDetails.MDDID == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_Service, 
                                    Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                    ).join(Model.models.Application.M_Patient,
                                    Model.models.Application.M_Patient.MPID == Model.models.Application.M_Appointment.M_Patient_MPID).all())
                    
                    return jsonify(result=Appointments) 
                            
                    # else:
                    #     return jsonify({'error':'IP is not allowed Please contact Admin'})
                else:
                    #return jsonify({'error':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

        
@Appointments_Blueprint.route('/cancelAppointment',methods=['POST'])
def cancelAppointment():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data=Common_Function.CommonFun.verifytoken(token)
                #data = jwt.decode(token,app.config['SECRET_KEY'], algorithms=['HS256', ])
                if(data>0):
                    
                    # request_json = request.get_json(force = True)
                    # Id=request_json.get('id')
                    #Id=request.data
                    Id=request.get_json()
                    if(Id != '' and Id != None):
                        session.query(Model.models.Application.M_Appointment
                                    ).filter(Model.models.Application.M_Appointment.MAID==Id
                                             ).update({Model.models.Application.M_Appointment.MP_IsCancelled:1,
                                                       Model.models.Application.M_Appointment.MP_ModDate:datetime.datetime.now()})
                        session.commit()
                        return jsonify({'success':'Appointment Cancelled Successfully'})
                    else:
                        return jsonify({'err':'something went wrong please try again'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    finally:
        session.close()
        
@Appointments_Blueprint.route('/AddPatientAppointment',methods=['GET','POST'])
def AddPatientAppointment():
    
    session=Session()
    try:

        if(request.method == "POST"):

            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')
                BranchId= request.headers.get('branchId')
                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    # request_json = request.get_json()
                    request_json = request.get_json(force = True)
                    pname = request_json.get('pname')
                    # procedure = request_json.get('procedure')
                    date = request_json.get('date')
                    time = request_json.get('time')
                    duration = request_json.get('duration')
                    doctor = request_json.get('doctor')
                    status = request_json.get('status')
                    appointmentType = request_json.get('appointmentType')
                    branchId = request_json.get('branchId')
                    if(pname!='' and pname!=None and date!='' and date!=None and time!='' and time!=None):
                        currentdate = datetime.datetime.now().strftime('%Y%m%d')
                        currenttime = datetime.datetime.now().strftime('%H%M')
                        # appdate1 = datetime.datetime.strptime(date,'%Y-%m-%d')2023-03-30
                        appdate1 = datetime.datetime.strptime(date,'%d %b %Y')
                        appdateVal = appdate1.strftime('%Y-%m-%d')
                        appdate = appdate1.strftime('%Y%m%d')
                        apptime1 = datetime.datetime.strptime(time,'%I:%M %p')
                        timeval = apptime1.strftime('%X')
                        apptime = apptime1.strftime('%H%M')
                        appdatetime = str(appdate)+str(apptime)
                        doctorout = session.query(Model.models.Application.DoctorOutoffice.DOID
                                                    #).filter_by(DO_FromDate=date,DO_ToDate=date,DO_DoctorId=doctor,DO_IsActive=1,DO_IsDeleted=0
                                                    ).filter_by(DO_DoctorId=doctor,DO_IsActive=1,DO_IsDeleted=0
                                                    ).filter(sqlalchemy.func.date_format(Model.models.Application.DoctorOutoffice.DO_FromDate,'%Y%m%d%H%M')>=appdatetime
                                                    ).all()
                        # print(doctorout)

                        checkdoctor = session.query(Model.models.Application.M_Appointment.MAID
                                                    ).filter_by(MA_Date=date,M_DoctorDetails_MDDID=doctor,MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0
                                                    ).filter(Model.models.Application.M_Appointment.MA_Time==time).all()
                        if(len(checkdoctor)==0):
                            # if(currentdate == appdate or currentdate < appdate):
                            #     if((currentdate == appdate and (apptime >= currenttime and  apptime <='2000')) or (currentdate <= appdate and ('0800' <= apptime and  apptime <='2000'))):
                            if('0800' <= apptime and  apptime <='2000'):        
                                # print('hello')
                                # print(currentdate,currenttime)
                                Insert=Model.models.Application.M_Appointment()
                                Insert.M_Patient_MPID=pname
                                # Insert.MP_Procedure=procedure
                                Insert.MA_Date=appdateVal
                                Insert.MA_Time=timeval
                                Insert.MP_Duration= 520 #duration
                                Insert.M_DoctorDetails_MDDID=doctor
                                Insert.M_Branch_MBID=int(branchId)
                                Insert.MP_Status=29 #status
                                Insert.MA_FromApp='yes'
                                Insert.MP_AddIP= flask.request.remote_addr
                                Insert.MP_AppointmentType = appointmentType
                                Insert.MP_AddDate = datetime.datetime.now()
                                session.add(Insert)
                                session.commit()
                                        #return "inserted Successfully"

                                ORGID= session.query(Model.models.Application.M_Appointment.MAID).order_by(Model.models.Application.M_Appointment.MAID.desc()).first()
                                PatName = session.query(Model.models.Application.M_Patient.MP_Name,
                                                        Model.models.Application.M_Patient.MP_Mobile,
                                                    ).filter_by(MPID=pname,MP_IsActive=1,MP_IsDeleted=0).all()
                                Name= PatName[0].MP_Name
                                Mobile= PatName[0].MP_Mobile
                                date2 = datetime.datetime.strptime(appdateVal, '%Y-%m-%d').date()
                                date3 = date2.strftime('%d-%m-%Y')
                                time2 = datetime.datetime.strptime(timeval, '%H:%M:%S').time()
                                time3 = time2.strftime('%I:%M %p')
                                # catedg = CategoryName[0]
                                dtime = str(date3) +'_'+str(time3)
                                
                                if(Mobile!='' and Mobile!=None):
                                    msg = 'https://api.pinnacle.in/index.php/sms/urlsms?sender=CONKID&numbers=91' + str(Mobile) +'&messagetype=TXT&message=Dear member '+''+', your appointment at Continua Kids for '+str(Name)+' has been created for ' + str(dtime) +'&response=Y&apikey=bb4d93-a1481e-f7c2a2-67d92c-2d3477'
                                    # rese = requests.get('https://api.pinnacle.in/index.php/sms/urlsms?sender=CONKID&numbers=918544388788&messagetype=TXT&message=Dear member Vipul, your appointment at Continua Kids for Test has been created for 20-07-2023_11:00 AM&response=Y&apikey=bb4d93-a1481e-f7c2a2-67d92c-2d3477')
                                    rese = requests.get(msg)
                                    print(rese)
                                else:
                                    pass

                                return jsonify({'msg':'Appointment Added Successfully', 'data': {'AppointmentId':ORGID[0]}})
                            else:
                                return jsonify({'err':'Appointment Not allowed at that time'}),200
                        else:
                            return jsonify({'err':'Appointment Not allowed for that date'}),200
                    else:
                        return jsonify({'err':'Doctor is not available at this time'}),200
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()


@Appointments_Blueprint.route('/updatePayment',methods=['GET','POST'])
def updatePayment():
    
    session=Session()
    try:

        if(request.method == "POST"):

            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')
                # BranchId= request.headers.get('branchId')
                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    
                    # request_json = request.get_json()
                    request_json = request.get_json(force = True)
                    AppointmentId = request_json.get('appointmentId')
                    Payment = request_json.get('payment')
                    # date = request_json.get('date')
                    # time = request_json.get('time')
                    # duration = request_json.get('duration')
                    # doctor = request_json.get('doctor')
                    # status = request_json.get('status')
                    # branchId = request_json.get('branchId')
                    if(AppointmentId!='' and AppointmentId!=None):
                        
                        Insert=session.query(Model.models.Application.M_Appointment).get(AppointmentId)
                        Insert.MA_Payment=Payment
                        Insert.MA_PaymentAddDate=datetime.datetime.now()
                        # Insert.MA_Date=appdateVal
                        # Insert.MA_Time=timeval
                        # Insert.MP_Duration=duration
                        # Insert.M_DoctorDetails_MDDID=doctor
                        # Insert.M_Branch_MBID=int(branchId)
                        # Insert.MP_Status=status
                        # Insert.MP_AddIP= flask.request.remote_addr
                        # # Insert.MP_AddUser = data['id']
                        Insert.MP_ModDate = datetime.datetime.now()
                        session.commit()
                                            #return "inserted Successfully"

                        #             ORGID= session.query(Model.models.Application.M_Appointment.MAID).order_by(Model.models.Application.M_Appointment.MAID.desc()).first()


                        #             return jsonify({'msg':'Appointment Added Successfully', 'data': {'AppointmentId':ORGID[0]}})
                        #         else:
                        #             return jsonify({'err':'Appointment Not allowed at that time'}),200
                        #else:
                        return jsonify({'msg':'Payment status updated successfully!'}),200
                    else:
                        return jsonify({'err':'Appointment Id not available, Please check now'}),403
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()        
 
       
        
@Appointments_Blueprint.route('/getDetailOfAppointment', methods=['POST','GET'])
def getDetailOfAppointment():
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
                    ePatientID= request.headers.get('PatientID')
                    PatientID=Common_Function.CommonFun.decryptString(ePatientID)
                    request_json = request.get_json()
                    AID = request_json.get('AID')
                    
                    Mobilenum= request.headers.get('Mobilenumber')
                    mob = Mobilenum[3:]
                    childDtl = session.query(Model.models.Application.M_Patient.MPID,
                            Model.models.Application.M_Patient.MP_Name
                            ).filter_by(MP_Mobile=int(mob)).all()
                    ChildId = [d['MPID'] for d in childDtl]
                    Appointments= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getDetailOfAppointment,
                                    session.query(Model.models.Application.M_Appointment.MAID.label('Id'),
                                    Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                    Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                    Model.models.Application.M_Appointment.MP_Procedure,
                                    Model.models.Application.M_Service.MS_CategoryName.label('procedure'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_ProfilePic.label('ProfilePic'),
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_MedicalExpertise.label('Expertise'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%W, %d-%b-%Y').label('date'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Time,'%I:%i %p').label('time'),
                                    Model.models.Application.M_Appointment.M_DoctorDetails_MDDID,
                                    sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctor'),
                                    Model.models.Application.M_Appointment.MP_Status.label('status'),
                                    Model.models.Application.M_ProvisionalDiagnosis.MPD_ICDDescription.label('ProvisionalDiagnosis'),
                                    Model.models.Application.M_SessionNotes.MSN_Notes.label('Notes'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_PatientReview.MPR_FollowDate,'%d-%b-%Y').label('ReviewDate')
                                        ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0,MAID=AID
                                    ).filter(Model.models.Application.M_Appointment.MP_Status.in_([393,527])
                                    ).outerjoin(Model.models.Application.M_DoctorDetails,
                                    Model.models.Application.M_DoctorDetails.MDDID == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_DoctorMedicalDetails,
                                    Model.models.Application.M_DoctorMedicalDetails.MDMD_DoctorId == Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).outerjoin(Model.models.Application.M_Service, 
                                    Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                    ).outerjoin(Model.models.Application.M_ProvisionalDiagnosis, 
                                    Model.models.Application.M_ProvisionalDiagnosis.M_AppointmentID==Model.models.Application.M_Appointment.MAID
                                    ).outerjoin(Model.models.Application.M_SessionNotes, 
                                    Model.models.Application.M_SessionNotes.M_AppointmentID==Model.models.Application.M_Appointment.MAID
                                    ).outerjoin(Model.models.Application.M_Patient,
                                    Model.models.Application.M_Patient.MPID == Model.models.Application.M_Appointment.M_Patient_MPID
                                    ).outerjoin(Model.models.Application.M_PatientReview,
                                    Model.models.Application.M_PatientReview.M_AppointmentID == Model.models.Application.M_Appointment.MAID
                                    ).all())
                    
                    return jsonify(result=Appointments) 
                            
                    # else:
                    #     return jsonify({'error':'IP is not allowed Please contact Admin'})
                else:
                    #return jsonify({'error':'Token is expired'})
                    return redirect('/')
            else:
                return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()        
        
@Appointments_Blueprint.route('/AddRescheduleAppointment',methods=['GET','POST'])
def AddRescheduleAppointment():
    
    session=Session()
    try:

        if(request.method == "POST"):

            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')
                BranchId= request.headers.get('branchId')
                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    # request_json = request.get_json()
                    request_json = request.get_json(force = True)
                    
                    date = request_json.get('date')
                    time = request_json.get('time')
                    doctor = request_json.get('doctor')
                    AppID = request_json.get('AppID')
                    if(AppID!='' and AppID!=None and date!='' and date!=None and time!='' and time!=None and doctor!='' and doctor!=None):
                        currentdate = datetime.datetime.now().strftime('%Y%m%d')
                        currenttime = datetime.datetime.now().strftime('%H%M')
                        # appdate1 = datetime.datetime.strptime(date,'%Y-%m-%d')2023-03-30
                        appdate1 = datetime.datetime.strptime(date,'%d %b %Y')
                        appdateVal = appdate1.strftime('%Y-%m-%d')
                        appdate = appdate1.strftime('%Y%m%d')
                        apptime1 = datetime.datetime.strptime(time,'%I:%M %p')
                        timeval = apptime1.strftime('%X')
                        apptime = apptime1.strftime('%H%M')
                        appdatetime = str(appdate)+str(apptime)
                        doctorout = session.query(Model.models.Application.DoctorOutoffice.DOID
                                                    #).filter_by(DO_FromDate=date,DO_ToDate=date,DO_DoctorId=doctor,DO_IsActive=1,DO_IsDeleted=0
                                                    ).filter_by(DO_DoctorId=doctor,DO_IsActive=1,DO_IsDeleted=0
                                                    ).filter(sqlalchemy.func.date_format(Model.models.Application.DoctorOutoffice.DO_FromDate,'%Y%m%d%H%M')>=appdatetime
                                                    ).all()
                        print(doctorout)

                        checkdoctor = session.query(Model.models.Application.M_Appointment.MAID
                                                    ).filter_by(MA_Date=date,M_DoctorDetails_MDDID=doctor,MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0
                                                    ).filter(Model.models.Application.M_Appointment.MA_Time==time).all()
                        if(len(checkdoctor)==0):
                            # if(currentdate == appdate or currentdate < appdate):
                            #     if((currentdate == appdate and (apptime >= currenttime and  apptime <='2000')) or (currentdate <= appdate and ('0800' <= apptime and  apptime <='2000'))):
                            if('0800' <= apptime and  apptime <='2000'):        
                                print('hello')
                                print(currentdate,currenttime)
                                Insert=session.query(Model.models.Application.M_Appointment).get(AppID)
                                Insert.MA_Date=appdateVal
                                Insert.MA_Time=timeval
                                # Insert.MP_ModDate= flask.request.remote_addr
                                Insert.MP_ModDate = datetime.datetime.now()
                                # session.add(Insert)
                                session.commit()
                                        #return "inserted Successfully"

                                ORGID= session.query(Model.models.Application.M_Appointment.MAID,
                                                     Model.models.Application.M_Patient.MPID,
                                                     Model.models.Application.M_Patient.MP_Mobile,
                                                     Model.models.Application.M_Patient.MP_Name,
                                                     
                                                     ).order_by(Model.models.Application.M_Appointment.MAID.desc()
                                                    ).filter(Model.models.Application.M_Appointment.MAID==AppID
                                                    ).join(Model.models.Application.M_Patient,Model.models.Application.M_Patient.MPID==Model.models.Application.M_Appointment.M_Patient_MPID
                                                    ).all()

                                if(ORGID[0].MP_Mobile !=''):
                                    Name= ORGID[0].MP_Name
                                    Mobile= ORGID[0].MP_Mobile
                                    date2 = datetime.datetime.strptime(date,'%d %b %Y')
                                    date3 = date2.strftime('%d-%m-%Y')
                                    time2 = datetime.datetime.strptime(time,'%I:%M %p')
                                    time3 = time2.strftime('%I:%M %p')
                                    dtime = str(date3) +'_'+str(time3)
                                    if(Mobile!='' and Mobile!=None):
                                        msg = 'https://api.pinnacle.in/index.php/sms/urlsms?sender=CONKID&numbers=91' + str(Mobile) +'&messagetype=TXT&message=Your appointment '+str(AppID)+' at Continua Kids for '+str(Name)+' has been updated for ' + str(dtime) +'. Thank you!&response=Y&apikey=bb4d93-a1481e-f7c2a2-67d92c-2d3477'
                                        # rese = requests.get('https://api.pinnacle.in/index.php/sms/urlsms?sender=CONKID&numbers=918544388788&messagetype=TXT&message=Dear member Vipul, your appointment at Continua Kids for Test has been created for 20-07-2023_11:00 AM&response=Y&apikey=bb4d93-a1481e-f7c2a2-67d92c-2d3477')
                                        rese = requests.get(msg)
                                        print(rese)
                                else:
                                    pass
                                return jsonify({'msg':'Appointment Added Successfully', 'data': {'AppointmentId':ORGID[0]}})
                            else:
                                return jsonify({'err':'Appointment Not allowed at that time'}),200
                        else:
                            return jsonify({'err':'Appointment Not allowed for that date'}),200
                    else:
                        return jsonify({'err':'Doctor is not available at this time'}),200
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()        
        
@Appointments_Blueprint.route('/getAvailableTimeSlot',methods=['GET','POST'])
def getAvailableTimeSlot():
    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')
                # BranchId= request.headers.get('branchId')
                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    
                    # request_json = request.get_json()
                    request_json = request.get_json(force = True)
                    doctorId = request_json.get('doctorId')
                    appointDate = request_json.get('appointDate')
                    if(doctorId!='' and doctorId!=None and appointDate!='' and appointDate!=None):
                        # date = datetime.datetime.now()
                        # curDate = date.strftime('%d %b %Y')
                        # if(appointDate == curDate):
                            
                        #     OpenTime='14:00'
                        # else:
                        OpenTime='08:00'
                        CloseTime= '20:00'
                        dateobject = datetime.date.today()
                        Startdate = datetime.datetime.combine(dateobject, datetime.time())
                        EndDate= Startdate + datetime.timedelta(days=1)
                        ListTime = (pd.DataFrame(columns=['NULL'],
                            index=pd.date_range(Startdate, EndDate,freq='30T')).between_time(OpenTime,CloseTime).index.tolist()
                                )
                        # print(ListTime)
                        arr= []
                        for eachtime in ListTime:
                            time= eachtime.strftime('%H%M')
                            timee= eachtime.strftime('%I:%M %p')
                            endTime = eachtime + datetime.timedelta(minutes=29)
                            checkdoctor = session.query(Model.models.Application.M_Appointment.MAID
                                                    ).filter_by(M_DoctorDetails_MDDID=doctorId,MP_IsActive=1,MP_IsDeleted=0,MP_IsCancelled=0
                                                    ).filter(sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%d %b %Y')==appointDate,
                                                    Model.models.Application.M_Appointment.MA_Time.between(eachtime, endTime)
                                                    ).all()
                            if(len(checkdoctor)==0):
                                date = datetime.datetime.now()+ datetime.timedelta(minutes=180)
                                curDate = date.strftime('%d %b %Y')
                                curTime = date.strftime('%H%M')
                                if(appointDate == curDate):
                                    if(curTime<=time):
                                        arr.append(timee)
                                else:
                                    arr.append(timee)
                            
                        print(arr)
                        return jsonify(result=arr),200
                    else:
                        return jsonify({'err':'Appointment Id not available, Please check now'}),403
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()        
                
@Appointments_Blueprint.route('/invoiceDetails',methods=['POST'])
def invoiceDetails():
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    session=Session()
                    request_json = request.get_json(force = True)
                    aid = request_json.get('appointmentId')
                    
                    if(aid != '' and aid != None):
                        queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getDetailedViewInvoice,
                                session.query(sqlalchemy.func.concat(Model.models.Application.M_InvoiceMaster.MPP_Prefix,'/',Model.models.Application.M_InvoiceMaster.MainInvoiceNo).label('InvoiceNo'),
                                            sqlalchemy.func.date_format(Model.models.Application.M_InvoiceMaster.MI_Date,'%d-%b-%Y').label('Date'),
                                            Model.models.Application.M_InvoiceMaster.MI_bankName.label('bankName'),
                                            Model.models.Application.M_InvoiceMaster.MI_Card.label('Card'),
                                            Model.models.Application.M_InvoiceMaster.MI_CardType.label('CardType'),
                                            Model.models.Application.M_InvoiceMaster.MI_Cash.label('Cash'),
                                            Model.models.Application.M_InvoiceMaster.MI_CGST.label('CGST'),
                                            Model.models.Application.M_InvoiceMaster.MI_SGST.label('SGST'),
                                            Model.models.Application.M_InvoiceMaster.MI_Discount.label('Discount'),
                                            Model.models.Application.M_InvoiceMaster.MI_discountPercent.label('discountPercent'),
                                            Model.models.Application.M_InvoiceMaster.MI_DiscountReason.label('DiscountReason'),
                                            Model.models.Application.M_InvoiceMaster.MI_Cheque.label('Cheque'),
                                            Model.models.Application.M_InvoiceMaster.MI_Comments.label('Comments'),
                                            Model.models.Application.M_InvoiceMaster.MI_DueBalance.label('DueBalance'),
                                            Model.models.Application.M_InvoiceMaster.MI_InvoiceTotal.label('InvoiceTotal'),
                                            Model.models.Application.M_InvoiceMaster.MI_invoiceType.label('invoiceType'),
                                            Model.models.Application.M_InvoiceMaster.MI_lastDigits.label('lastDigits'),
                                            Model.models.Application.M_InvoiceMaster.MI_Online.label('Online'),
                                            Model.models.Application.M_InvoiceMaster.MI_Prepaid.label('Prepaid'),
                                            Model.models.Application.M_InvoiceMaster.MI_TotalPayable.label('TotalPayable'),
                                            Model.models.Application.M_InvoiceMaster.MI_Upi.label('Upi'),
                                            Model.models.Application.M_InvoiceMaster.MI_AmountPaid.label('AmountPaid'),
                                            Model.models.Application.M_InvoiceMaster.MI_ServiceId.label('ServiceId'),
                                            Model.models.Application.M_InvoiceMaster.MI_SettleInvoice.label('SettleInvoice'),
                                            Model.models.Application.M_InvoiceMaster.MainInvoiceNo.label('MainInvoiceNo'),
                                            Model.models.Application.M_InvoiceMaster.MI_TotalAmount.label('TotalAmount'),
                                            Model.models.Application.M_InvoiceMaster.MI_PaidByPartner.label('PaidByPartner'),
                                            Model.models.Application.M_InvoiceMaster.MI_PaidByPatient.label('PaidByPatient'),
                                            Model.models.Application.M_InvoiceMaster.MPIA_TotalSessions.label('TotalSessions'),
                                            Model.models.Application.M_InvoiceMaster.MPIA_UsedSession.label('UsedSession'),
                                            Model.models.Application.M_InvoiceMaster.MPIA_PaymentMode.label('PaymentMode'),
                                            Model.models.Application.M_InvoiceMaster.MIP_InvoiceType.label('InvoiceType'),
                                            Model.models.Application.M_InvoiceMaster.MIP_MedicineDetails.label('MedicineDetails'),
                                            Model.models.Application.M_InvoiceMaster.M_PartnerOrgId.label('PartnerOrgId'),
                                            Model.models.Application.M_InvoiceMaster.M_PartnerOrgName.label('PartnerOrgName'),
                                            Model.models.Application.M_InvoiceMaster.MI_ServiceName.label('ServiceName'),
                                            Model.models.Application.M_InvoiceMaster.MI_AppointmentId.label('AppointmentId'),
                                            Model.models.Application.M_InvoiceMaster.M_Branch_MBID.label('M_Branch_MBID'),
                                            Model.models.Application.M_InvoiceMaster.M_Patient_MPID.label('M_Patient_MPID'),
                                            Model.models.Application.M_InvoiceMaster.MPP_PackageName.label('MPP_PackageName'),
                                            Model.models.Application.M_InvoiceMaster.MPP_PackagePrice.label('MPP_PackagePrice'),
                                            Model.models.Application.M_InvoiceMaster.MPP_PackageId.label('MPP_PackageId'),
                                            
                                            Model.models.Application.M_Patient.MP_Name.label('Name'),
                                            Model.models.Application.M_Patient.MP_UHID.label('UHID'),
                                            Model.models.Application.M_Appointment.M_DoctorDetails_MDDID.label('M_DoctorDetails_MDDID'),
                                            sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,Model.models.Application.M_DoctorDetails.MDD_LastName).label('doctorName'),
                                            Model.models.Application.M_Branch.MB_Address.label('Branch'),
                                            sqlalchemy.func.date_format(Model.models.Application.M_Patient.MP_DOB,'%d-%b-%Y').label('DOB')
                                                ).filter_by(MI_IsActive=1,MI_IsDeleted=0,MI_AppointmentId=aid
                                                
                                ).join(Model.models.Application.M_Patient, Model.models.Application.M_Patient.MPID==Model.models.Application.M_InvoiceMaster.M_Patient_MPID
                                ).outerjoin(Model.models.Application.M_Appointment, Model.models.Application.M_Appointment.MAID==Model.models.Application.M_InvoiceMaster.MI_AppointmentId
                                ).outerjoin(Model.models.Application.M_DoctorDetails, and_(Model.models.Application.M_DoctorDetails.MDDID==Model.models.Application.M_Appointment.M_DoctorDetails_MDDID,Model.models.Application.M_DoctorDetails.MDD_Type != 'Therapist')
                                ).outerjoin(Model.models.Application.M_Branch,Model.models.Application.M_Branch.MBID==Model.models.Application.M_InvoiceMaster.M_Branch_MBID
                                ).order_by(Model.models.Application.M_InvoiceMaster.MIID.desc()).all())
                        session.commit()
                        return jsonify(result=queryresult)
                    else:
                        return jsonify({'err':'something went wrong please try again'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()
        
@Appointments_Blueprint.route('/getPrescriptionDtl',methods=['POST','GET'])
def getPrescriptionDtl():
    try:
        if(request.method == "POST"):
            session=Session()
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    # session=Session()
                    request_json = request.get_json(force = True)
                    aid = request_json.get('appointmentId')
                    
                    if(aid != '' and aid != None):
                        queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getPrescriptionDtl,
                                session.query(Model.models.Application.M_Appointment.MAID.label('visitId'),
                                              Model.models.Application.M_Appointment.MP_Procedure.label('Service'),
                                            
                                            Model.models.Application.M_Appointment.MAID.label('visitType'),
                                            sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%d-%b-%Y').label('AppointDate'),
                                            sqlalchemy.func.date_format(Model.models.Application.M_Patient.MP_DOB,'%d-%b-%Y').label('DOB'),
                                            Model.models.Application.M_Patient.MP_Name.label('Name'),
                                            Model.models.Application.M_Patient.MP_UHID.label('UHID'),
                                            Model.models.Application.M_Branch.MB_Address.label('Branch'),
                                            Model.models.Application.M_Service.MS_CategoryName.label('Procedure'),
                                            sqlalchemy.func.concat(Model.models.Application.M_DoctorDetails.MDD_FirstName,' ',Model.models.Application.M_DoctorDetails.MDD_LastName).label('DoctorName'),
                                            ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MAID=aid
                                ).join(Model.models.Application.M_Patient, Model.models.Application.M_Patient.MPID==Model.models.Application.M_Appointment.M_Patient_MPID
                                ).join(Model.models.Application.M_Branch, Model.models.Application.M_Branch.MBID==Model.models.Application.M_Appointment.M_Branch_MBID
                                ).join(Model.models.Application.M_Service, Model.models.Application.M_Service.MSID==Model.models.Application.M_Appointment.MP_Procedure
                                ).join(Model.models.Application.M_DoctorDetails, Model.models.Application.M_DoctorDetails.MDDID==Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                
                                ).order_by(Model.models.Application.M_Appointment.MAID.desc()).all())
                        session.commit()
                
                        Prescrip = Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.Prescrip,
                                session.query(Model.models.Application.M_Prescription.MP_medication,
                                                       Model.models.Application.M_Prescription.MP_type,
                                                       Model.models.Application.M_Prescription.MP_route,
                                                       Model.models.Application.M_Prescription.MP_times,
                                                       Model.models.Application.M_Prescription.MP_duration,
                                                       Model.models.Application.M_Prescription.MP_dosage,
                                                       Model.models.Application.M_Prescription.MP_comments,
                                                       Model.models.Application.M_Prescription.MP_Prescription,
                            ).filter(Model.models.Application.M_Prescription.M_AppointmentID == aid
                            ).filter_by(ShowData=1,MP_IsDeleted=0).all())
                                        
                        session.commit()
                        queryresult[0]['Prescription']=Prescrip
                        return jsonify(result=queryresult)
                    else:
                        return jsonify({'err':'something went wrong please try again'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()        
        


        
# @Appointments_Blueprint.route('/getAppointmentDetails', methods=['POST'])
# def get_appointment_details():
#     try:
#         if(request.method == "POST"):
#             session=Session()
#             if('Authorization' in request.headers):
#                 token= request.headers.get('Authorization')

#                 if not token:
#                     return jsonify({'MSG':'Token is missing'})
#                 data = Common_Function.CommonFun.verifytoken(token)
#                 if(data):
#                     # session=Session()
#                     request_json = request.get_json(force = True)
#                     date = request_json.get('date')
#                     branch = request_json.get('branch')
#                     # reason_for_visit = request_json.get('reason_for_visit')
#                     doctor_id = request_json.get('doctor_id')
#                     if(doctor_id != '' and doctor_id != None):
#                         queryresult= Common_Function.CommonFun.convertToJson(
#                                 Constant.constant.constant.getAppointmentDtl,
#                                 session.query(
#                                     Model.models.Application.M_Appointment.M_Patient_MPID.label('patientId'),
#                                     Model.models.Application.M_Patient.MP_Name.label('patientName'),
#                                     Model.models.Application.M_Appointment.MP_Status.label('status'),
#                                     Model.models.Application.M_Appointment.MAID.label('consultId'),
#                                     Model.models.Application.M_DoctorDetails.MDD_FirstName.label('doctorName'),
#                                     Model.models.Application.M_DoctorDetails.MDDID.label('doctorId'),
#                                     Model.models.Application.M_Appointment.MA_Time.label('visitTimeFrom'),
#                                     Model.models.Application.M_Appointment.MP_Duration.label('visitTimeTo'),
#                                     Model.models.Application.M_Appointment.MA_Date.label('date'),
#                                     Model.models.Application.M_Appointment.MP_AppointmentType.label('mode')
#                                 ).join(
#                                     Model.models.Application.M_Patient, Model.models.Application.M_Appointment.M_Patient_MPID == Model.models.Application.M_Patient.MPID
#                                 ).join(
#                                     Model.models.Application.M_DoctorDetails, Model.models.Application.M_Appointment.M_DoctorDetails_MDDID == Model.models.Application.M_DoctorDetails.MDDID
#                                 ))
#                         if date or branch or doctor_id:
#                             if date:
#                                 queryresult = queryresult.filter(Model.models.Application.M_Appointment.MA_Date == date)
#                             if branch:
#                                 queryresult = queryresult.filter(Model.models.Application.M_Appointment.M_Branch_MBID == branch)
#                             # if reason_for_visit:
#                             #     queryresult = queryresult.filter(Model.models.Application.M_Patient.MP_ReasonForVisit == reason_for_visit)
#                             if doctor_id:
#                                 queryresult = queryresult.filter(Model.models.Application.M_DoctorDetails.MDDID == doctor_id)
#                         else:
#                             raise ValueError("At least one filter must be provided")
                    
#                         session.commit()
#                         return jsonify(result=queryresult)
#                     else:
#                         return jsonify({'err':'something went wrong please try again'})
#                 else:
#                     return jsonify({'err':'Token is expired'})
#             else:
#                 return jsonify({'err':'Please Login'})
#     except Exception as e:
#         return jsonify({'err':str(e)})
#     finally:
#         session.close() 


@Appointments_Blueprint.route('/getAppointmentDetails', methods=['POST'])
def getAppointmentDetails():
    session = Session()
    try:
        if request.method == "POST":
            if 'Authorization' in request.headers:
                token = request.headers.get('Authorization')
                if not token:
                    return jsonify({'MSG': 'Token is missing'}), 401
                data = Common_Function.CommonFun.verifytoken(token)
                if data:
                    request_json = request.get_json(force=True)
                    date = request_json.get('date')
                    branch = request_json.get('branch')
                    doctor_id = request_json.get('doctor_id')

                    query = session.query(
                        Model.models.Application.M_Appointment.M_Patient_MPID.label("patientId"),
                        Model.models.Application.M_Patient.MP_Name.label("patientName"),
                        Model.models.Application.M_Appointment.MP_Status.label("status"),
                        Model.models.Application.M_Appointment.MAID.label("consultId"),
                        Model.models.Application.M_DoctorDetails.MDD_FirstName.label("doctorName"),
                        Model.models.Application.M_DoctorDetails.MDDID.label("doctorId"),
                        Model.models.Application.M_Appointment.MA_Time.label("visitTimeFrom"),
                        Model.models.Application.M_Appointment.MA_Time.label("visitTimeTo"),
                        Model.models.Application.M_Appointment.MA_Date.label("date"),
                        Model.models.Application.M_Appointment.MP_AppointmentType.label("mode")
                    ).join(
                        Model.models.Application.M_Patient, Model.models.Application.M_Appointment.M_Patient_MPID == Model.models.Application.M_Patient.MPID
                    ).join(
                        Model.models.Application.M_DoctorDetails, Model.models.Application.M_Appointment.M_DoctorDetails_MDDID == Model.models.Application.M_DoctorDetails.MDDID
                    )

                    if date:
                        query = query.filter(func.date_format(Model.models.Application.M_Appointment.MA_Date, '%d %b %Y') == date)
                    if branch:
                        query = query.filter(Model.models.Application.M_Appointment.M_Branch_MBID == branch)
                    if doctor_id:
                        query = query.filter(Model.models.Application.M_Appointment.M_DoctorDetails_MDDID == doctor_id)

                    query = query.filter(Model.models.Application.M_Appointment.MP_Status == 527)

                    results = query.all()
                    
                    appointment_details = [
                        {
                            "patientId": result.patientId,
                            "patientName": result.patientName,
                            "status": result.status,
                            "consultId": result.consultId,
                            "doctorName": result.doctorName,
                            "doctorId": result.doctorId,
                            "visitTimeFrom": result.visitTimeFrom.strftime('%I:%M %p'),
                            "visitTimeTo": result.visitTimeTo.strftime('%I:%M %p'),
                            "date": result.date.strftime('%d %b %Y'),
                            "mode": result.mode
                        } for result in results
                    ]

                    return jsonify(result=appointment_details), 200
                else:
                    return jsonify({'err': 'Token is expired'}), 401
            else:
                return jsonify({'err': 'Please Login'}), 401
    except Exception as e:
        return jsonify({'err': str(e)}), 500
    finally:
        session.close()