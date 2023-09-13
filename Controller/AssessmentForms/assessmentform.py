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
Assessment_Blueprint = CommonModule.flask.Blueprint(
    'Assessment_Blueprint', import_name=__name__)

@Assessment_Blueprint.route('/getHamiltonAnxietRatingScaleForm', methods=['POST','GET'])
def getHamiltonAnxietRatingScaleForm():
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
                    AllCateg= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.T_AssessmentForms,
                                session.query(Model.models.Application.T_AssessmentForms.TAFID.label('FormId'),
                                                    Model.models.Application.T_AssessmentForms.TAF_Title.label('FormTitle')
                                                    ).filter_by(TAF_IsActive=1,TAF_IsDeleted=0,TAF_FormName='HamiltonAnxietRatingScale'
                                    ).all())
                        
                    return jsonify(result=AllCateg)
                        
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


@Assessment_Blueprint.route('/getFormOptions', methods=['POST','GET'])
def getFormOptions():
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
                    AllCateg= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.T_Assessmentanswers,
                                session.query(Model.models.Application.T_Assessmentanswers.TAID.label('TAID'),
                                                    Model.models.Application.T_Assessmentanswers.TA_Answers.label('TA_Answers')
                                                    ).filter_by(TA_IsActive=1,TA_IsDeleted=0
                                    ).all())
                        
                    return jsonify(result=AllCateg)
                        
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


@Assessment_Blueprint.route('/saveAssessmentForm', methods=['POST','GET'])
def saveAssessmentForm():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data=Common_Function.CommonFun.verifytoken(token)
                if(data>0):
                    ePatientID= request.headers.get('PatientID')
                    PatientID=Common_Function.CommonFun.decryptString(ePatientID)
                    request_json = request.get_json()
                    if(request_json!='' and request_json!=None):
                        userId = int(PatientID)
                        answer1 = request_json.get('question1') 
                        answer2 = request_json.get('question2') 
                        answer3 = request_json.get('question3') 
                        answer4 = request_json.get('question4')
                        question1 = "Over the last two weeks, how often have you has little interest or pleasure in doing things?"
                        question2 = "Over the last two weeks, how often have you has little interest or pleasure in doing things?"
                        question3 = "Over the last two weeks, how often have you has little interest or pleasure in doing things?"
                        question4 = "Over the last two weeks, how often have you has little interest or pleasure in doing things?"
                        FormName = "Hamilton Anxiety Rating Scale"
                        
                        Common_Function.CommonFun.SaveAssessmentForms(question1,answer1,userId,FormName)
                        Common_Function.CommonFun.SaveAssessmentForms(question2,answer2,userId,FormName)
                        Common_Function.CommonFun.SaveAssessmentForms(question3,answer3,userId,FormName)
                        Common_Function.CommonFun.SaveAssessmentForms(question4,answer4,userId,FormName)
                        
                        return jsonify({'success':'Hamilton Anxiety Rating Scale Saved Successfully'})
                        
                    else:
                        return jsonify({'error':'JSON not available'})
                else:
                    return redirect('/')
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()          

@Assessment_Blueprint.route('/submitPHQAssessmentForm', methods=['GET','POST'])
def submitPHQAssessmentForm():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data=Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    AnyPleasure = request_json.get('question1')
                    AnyDepression = request_json.get('question2')
                    AnyTrouble = request_json.get('question3')
                    Anytiredness = request_json.get('question4')
                    AnyOvereat = request_json.get('question5')
                    Anybadfeel = request_json.get('question6')
                    TroubledbyAnything = request_json.get('question7')
                    MovingAroundAlot = request_json.get('question8')
                    AnyHurtYourself = request_json.get('question9')

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    
                    Insert=Model.models.Application.M_PHQAssessment()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.MPA_AnyPleasure=AnyPleasure
                    Insert.MPA_AnyDepression=AnyDepression
                    Insert.MPA_AnyTrouble=AnyTrouble
                    Insert.MPA_Anytiredness=Anytiredness
                    Insert.MPA_AnyOvereat=AnyOvereat
                    Insert.MPA_Anybadfeel=Anybadfeel
                    Insert.MPA_TroubledbyAnything=TroubledbyAnything
                    Insert.MPA_MovingAroundAlot=MovingAroundAlot
                    Insert.MPA_AnyHurtYourself=AnyHurtYourself
                    
                    Insert.MPA_AddDate = datetime.datetime.now()
                    Insert.MPA_AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'PHQ Assessment Added Successfully'})
                    # else:
                    #     Insert=session.query(Model.models.Application.M_PHQAssessment).get(Id)
                    #     Insert.M_Patient_MPID=PID
                    #     Insert.M_AppointmentID=Aid
                    #     Insert.MPA_AnyPleasure=AnyPleasure
                    #     Insert.MPA_AnyDepression=AnyDepression
                    #     Insert.MPA_AnyTrouble=AnyTrouble
                    #     Insert.MPA_Anytiredness=Anytiredness
                    #     Insert.MPA_AnyOvereat=AnyOvereat
                    #     Insert.MPA_Anybadfeel=Anybadfeel
                    #     Insert.MPA_TroubledbyAnything=TroubledbyAnything
                    #     Insert.MPA_MovingAroundAlot=MovingAroundAlot
                    #     Insert.MPA_AnyHurtYourself=AnyHurtYourself
                        
                    #     Insert.MPA_AddDate = datetime.datetime.now()
                    #     Insert.MPA_AddIP= flask.request.remote_addr

                    #     session.commit()
                    #     return jsonify({'msg':'PHQ Assessment Updated Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()        
   
@Assessment_Blueprint.route('/viewPHQAssessmentForm', methods=['GET','POST'])
def viewPHQAssessmentForm():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewPHQAssessmentForm,
                                session.query(Model.models.Application.M_PHQAssessment.MPAID.label('ID'),
                                            Model.models.Application.M_PHQAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PHQAssessment.MPA_AnyPleasure.label('AnyPleasure'),
                                            Model.models.Application.M_PHQAssessment.MPA_AnyDepression.label('AnyDepression'),
                                            Model.models.Application.M_PHQAssessment.MPA_AnyTrouble.label('AnyTrouble'),
                                            Model.models.Application.M_PHQAssessment.MPA_Anytiredness.label('Anytiredness'),
                                            Model.models.Application.M_PHQAssessment.MPA_AnyOvereat.label('AnyOvereat'),
                                            Model.models.Application.M_PHQAssessment.MPA_Anybadfeel.label('Anybadfeel'),
                                            Model.models.Application.M_PHQAssessment.MPA_TroubledbyAnything.label('TroubledbyAnything'),
                                            Model.models.Application.M_PHQAssessment.MPA_MovingAroundAlot.label('MovingAroundAlot'),
                                            Model.models.Application.M_PHQAssessment.MPA_AnyHurtYourself.label('AnyHurtYourself'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,MPA_IsActive=1,MPA_IsDeleted=0
                                ).order_by(Model.models.Application.M_PHQAssessment.MPAID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()

                
@Assessment_Blueprint.route('/submitHARSAssessmentForm', methods=['GET','POST'])
def submitHARSAssessmentForm():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    anyAnxiousMood = request_json.get('question1')
                    AnyTensionFeeling = request_json.get('question2')
                    AnyFearsfeeling = request_json.get('question3')
                    AnyInsomnia = request_json.get('question4')
                    AnyIntellectual = request_json.get('question5')
                    AnyDipressedMood = request_json.get('question6')
                    AnySomaticpains = request_json.get('question7')
                    AnySomaticWeekness = request_json.get('question8')
                    AnyCardiovascular = request_json.get('question9')
                    AnyRespiratory = request_json.get('question10')
                    AnyGastrontedtinal = request_json.get('question11')
                    AnyGenitourinarySymptoms = request_json.get('question12')
                    AnyAutonomicSymptoms = request_json.get('question13')
                    AnyBehaviouratInterview = request_json.get('question14')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_HARSAssessment()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.MHA_anyAnxiousMood=anyAnxiousMood
                    Insert.MHA_AnyTensionFeeling=AnyTensionFeeling
                    Insert.MHA_AnyFearsfeeling=AnyFearsfeeling
                    Insert.MHA_AnyInsomnia=AnyInsomnia
                    Insert.MHA_AnyIntellectual=AnyIntellectual
                    Insert.MHA_AnyDipressedMood=AnyDipressedMood
                    Insert.MHA_AnySomaticpains=AnySomaticpains
                    Insert.MHA_AnySomaticWeekness=AnySomaticWeekness
                    Insert.MHA_AnyCardiovascular=AnyCardiovascular
                    Insert.MHA_AnyRespiratory=AnyRespiratory
                    Insert.MHA_AnyGastrontedtinal=AnyGastrontedtinal
                    Insert.MHA_AnyGenitourinarySymptoms=AnyGenitourinarySymptoms
                    Insert.MHA_AnyAutonomicSymptoms=AnyAutonomicSymptoms
                    Insert.MHA_AnyBehaviouratInterview=AnyBehaviouratInterview
                    Insert.MHA_AddDate = datetime.datetime.now()
                    Insert.MHA_AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'HARS Assessment Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()        
                    
@Assessment_Blueprint.route('/viewHARSAssessmentForm', methods=['GET','POST'])
def viewHARSAssessmentForm():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewHARSAssessmentForm,
                                session.query(Model.models.Application.M_HARSAssessment.MHAID.label('ID'),
                                            Model.models.Application.M_HARSAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_HARSAssessment.MHA_anyAnxiousMood.label('anyAnxiousMood'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyTensionFeeling.label('AnyTensionFeeling'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyFearsfeeling.label('AnyFearsfeeling'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyInsomnia.label('AnyInsomnia'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyIntellectual.label('AnyIntellectual'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyDipressedMood.label('AnyDipressedMood'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnySomaticpains.label('AnySomaticpains'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnySomaticWeekness.label('AnySomaticWeekness'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyCardiovascular.label('AnyCardiovascular'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyRespiratory.label('AnyRespiratory'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyGastrontedtinal.label('AnyGastrontedtinal'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyGenitourinarySymptoms.label('AnyGenitourinarySymptoms'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyAutonomicSymptoms.label('AnyAutonomicSymptoms'),
                                            Model.models.Application.M_HARSAssessment.MHA_AnyBehaviouratInterview.label('AnyBehaviouratInterview'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,MHA_IsActive=1,MHA_IsDeleted=0
                                ).order_by(Model.models.Application.M_HARSAssessment.MHAID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()                    
                    
                    
@Assessment_Blueprint.route('/submitHRDSAssessmentForm', methods=['GET','POST'])
def submitHRDSAssessmentForm():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    HRDSDepressedMood = request_json.get('HRDSDepressedMood')
                    HRDSFeelingGuilt = request_json.get('HRDSFeelingGuilt')
                    HRDSSuide = request_json.get('HRDSSuide')
                    HRDSInsomnia = request_json.get('HRDSInsomnia')
                    HRDSMidNight = request_json.get('HRDSMidNight')
                    HRDSEarlyMorning = request_json.get('HRDSEarlyMorning')
                    HRDSWork = request_json.get('HRDSWork')
                    HRDSRetardation = request_json.get('HRDSRetardation')
                    HRDSAgitation = request_json.get('HRDSAgitation')
                    HRDSPsychic = request_json.get('HRDSPsychic')
                    HRDSAnxietySomatic = request_json.get('HRDSAnxietySomatic')
                    HRDSSomatic = request_json.get('HRDSSomatic')
                    HDRSGeneralSomatic = request_json.get('HDRSGeneralSomatic')
                    HDRSLossOfLibido = request_json.get('HDRSLossOfLibido')
                    HDRSHypochondriasis = request_json.get('HDRSHypochondriasis')
                    HDRSLossofWeight = request_json.get('HDRSLossofWeight')
                    HDRSInsight = request_json.get('HDRSInsight')

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_HRDSAssessment()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.MHA_HRDSDepressedMood=HRDSDepressedMood
                    Insert.MHA_HRDSFeelingGuilt=HRDSFeelingGuilt
                    Insert.MHA_HRDSSuide=HRDSSuide
                    Insert.MHA_HRDSInsomnia=HRDSInsomnia
                    Insert.MHA_HRDSMidNight=HRDSMidNight
                    Insert.MHA_HRDSEarlyMorning=HRDSEarlyMorning
                    Insert.MHA_HRDSWork=HRDSWork
                    Insert.MHA_HRDSRetardation=HRDSRetardation
                    Insert.MHA_HRDSAgitation=HRDSAgitation
                    Insert.MHA_HRDSPsychic=HRDSPsychic
                    Insert.MHA_HRDSAnxietySomatic=HRDSAnxietySomatic
                    Insert.MHA_HRDSSomatic=HRDSSomatic
                    Insert.MHA_HDRSGeneralSomatic=HDRSGeneralSomatic
                    Insert.MHA_HDRSLossOfLibido=HDRSLossOfLibido
                    Insert.MHA_HDRSHypochondriasis=HDRSHypochondriasis
                    Insert.MHA_HDRSLossofWeight=HDRSLossofWeight
                    Insert.MHA_HDRSInsight=HDRSInsight
                    Insert.MHA_AddUser= data['id']
                    Insert.MHA_AddDate = datetime.datetime.now()
                    Insert.MHA_AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'HRDS Assessment Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'msg':'token is invalid'})
    finally:
        session.close()

@Assessment_Blueprint.route('/viewHRDSAssessmentForm', methods=['GET','POST'])
def viewHRDSAssessmentForm():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewHRDSAssessmentForm,
                                session.query(Model.models.Application.M_HRDSAssessment.MHAID.label('ID'),
                                            Model.models.Application.M_HRDSAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSDepressedMood.label('HRDSDepressedMood'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSFeelingGuilt.label('HRDSFeelingGuilt'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSSuide.label('HRDSSuide'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSInsomnia.label('HRDSInsomnia'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSMidNight.label('HRDSMidNight'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSEarlyMorning.label('HRDSEarlyMorning'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSWork.label('HRDSWork'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSRetardation.label('HRDSRetardation'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSAgitation.label('HRDSAgitation'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSPsychic.label('HRDSPsychic'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSAnxietySomatic.label('HRDSAnxietySomatic'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HRDSSomatic.label('HRDSSomatic'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HDRSGeneralSomatic.label('HDRSGeneralSomatic'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HDRSLossOfLibido.label('HDRSLossOfLibido'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HDRSHypochondriasis.label('HDRSHypochondriasis'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HDRSLossofWeight.label('HDRSLossofWeight'),
                                            Model.models.Application.M_HRDSAssessment.MHA_HDRSInsight.label('HDRSInsight'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,MHA_IsActive=1,MHA_IsDeleted=0
                                ).order_by(Model.models.Application.M_HRDSAssessment.MHAID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()                    
    
                    
@Assessment_Blueprint.route('/submitCKASAssessmentForm', methods=['GET','POST'])
def submitCKASAssessmentForm():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    CKASConsistentEyeContact = request_json.get('question1')
                    CKASPointsTowardsObject = request_json.get('question2')
                    CKASFollowSimpleCommand = request_json.get('question3')
                    CKASRespondWhencalled = request_json.get('question4')
                    CKASTryToCopy = request_json.get('question5')
                    CKASCallOutMama = request_json.get('question6')
                    CKASInterestInplaying = request_json.get('question7')
                    CKASLimitedUseofLanguage = request_json.get('question8')
                    CKASFrequentEyeBlinkt = request_json.get('question9')
                    CKASClimbWithoutScare = request_json.get('question10')
                    CKASSpeakNonContextly = request_json.get('question11')
                    CKASIndicateTowardsObject = request_json.get('question12')
                    CKASAnyRegression = request_json.get('question13')
                    score = request_json.get('score')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKASAssessment()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.MCA_CKASConsistentEyeContact=CKASConsistentEyeContact
                    Insert.MCA_CKASPointsTowardsObject=CKASPointsTowardsObject
                    Insert.MCA_CKASFollowSimpleCommand=CKASFollowSimpleCommand
                    Insert.MCA_CKASRespondWhencalled=CKASRespondWhencalled
                    Insert.MCA_CKASTryToCopy=CKASTryToCopy
                    Insert.MCA_CKASCallOutMama=CKASCallOutMama
                    Insert.MCA_CKASInterestInplaying=CKASInterestInplaying
                    Insert.MCA_CKASLimitedUseofLanguage=CKASLimitedUseofLanguage
                    Insert.MCA_CKASFrequentEyeBlinkt=CKASFrequentEyeBlinkt
                    Insert.MCA_CKASClimbWithoutScare=CKASClimbWithoutScare
                    Insert.MCA_CKASSpeakNonContextly=CKASSpeakNonContextly
                    Insert.MCA_CKASIndicateTowardsObject=CKASIndicateTowardsObject
                    Insert.MCA_CKASAnyRegression=CKASAnyRegression
                    Insert.MCA_CKASscore=score
                    
                    Insert.MCA_AddDate = datetime.datetime.now()
                    Insert.MCA_AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CKAS Assessment Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()
 #################  Till here  #####################

@Assessment_Blueprint.route('/viewCKASAssessmentForm', methods=['GET','POST'])
def viewCKASAssessmentForm():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= session.query(Model.models.Application.M_CKASAssessment.MCAID.label('ID'),
                                            Model.models.Application.M_CKASAssessment.MCA_CKASscore.label('Score')
                                            
                                                ).filter_by(M_Patient_MPID=pid,MCA_IsActive=1,MCA_IsDeleted=0
                                ).order_by(Model.models.Application.M_CKASAssessment.MCAID.desc()).all()

                    if(len(queryresult)>0):
                        return jsonify(result={'Score':queryresult[0].Score})
                    else:
                        return jsonify(result={'Score':''})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()                    
                    
# @Assessment_Blueprint.route('/submitCKASAssessmentForm', methods=['GET','POST'])
# def submitCKASAssessmentForm():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    CKASConsistentEyeContact = request_json.get('question1')
                    CKASPointsTowardsObject = request_json.get('question2')
                    CKASFollowSimpleCommand = request_json.get('question3')
                    CKASRespondWhencalled = request_json.get('question4')
                    CKASTryToCopy = request_json.get('question5')
                    CKASCallOutMama = request_json.get('question6')
                    CKASInterestInplaying = request_json.get('question7')
                    CKASLimitedUseofLanguage = request_json.get('question8')
                    CKASFrequentEyeBlinkt = request_json.get('question9')
                    CKASClimbWithoutScare = request_json.get('question10')
                    CKASSpeakNonContextly = request_json.get('question11')
                    CKASIndicateTowardsObject = request_json.get('question12')
                    CKASAnyRegression = request_json.get('question13')
                    score = request_json.get('score')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('PID')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKASAssessment()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.MCA_CKASConsistentEyeContact=CKASConsistentEyeContact
                    Insert.MCA_CKASPointsTowardsObject=CKASPointsTowardsObject
                    Insert.MCA_CKASFollowSimpleCommand=CKASFollowSimpleCommand
                    Insert.MCA_CKASRespondWhencalled=CKASRespondWhencalled
                    Insert.MCA_CKASTryToCopy=CKASTryToCopy
                    Insert.MCA_CKASCallOutMama=CKASCallOutMama
                    Insert.MCA_CKASInterestInplaying=CKASInterestInplaying
                    Insert.MCA_CKASLimitedUseofLanguage=CKASLimitedUseofLanguage
                    Insert.MCA_CKASFrequentEyeBlinkt=CKASFrequentEyeBlinkt
                    Insert.MCA_CKASClimbWithoutScare=CKASClimbWithoutScare
                    Insert.MCA_CKASSpeakNonContextly=CKASSpeakNonContextly
                    Insert.MCA_CKASIndicateTowardsObject=CKASIndicateTowardsObject
                    Insert.MCA_CKASAnyRegression=CKASAnyRegression
                    Insert.MCA_CKASscore=score
                    Insert.MCA_AddUser= data['id']
                    Insert.MCA_AddDate = datetime.datetime.now()
                    Insert.MCA_AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CKAS Assessment Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()


@Assessment_Blueprint.route('/submitCKADHDScreening', methods=['GET','POST'])
def submitCKADHDScreening():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    question1 = request_json.get('question1')
                    question2 = request_json.get('question2')
                    question3 = request_json.get('question3')
                    question4 = request_json.get('question4')
                    question5 = request_json.get('question5')
                    question6 = request_json.get('question6')
                    question7 = request_json.get('question7')
                    question8 = request_json.get('question8')
                    question9 = request_json.get('question9')
                    question10 = request_json.get('question10')
                    question11 = request_json.get('question11')
                    question12 = request_json.get('question12')
                    question13 = request_json.get('question13')
                    question14 = request_json.get('question14')
                    question15 = request_json.get('question15')
                    question16 = request_json.get('question16')
                    question17 = request_json.get('question17')
                    question18 = request_json.get('question18')
                    question19 = request_json.get('question19')
                    question20 = request_json.get('question20')
                    question21 = request_json.get('question21')
                    
                    often23Count = request_json.get('often2Count')
                    often23Count2 = request_json.get('often2Count2')
                    often23Count3 = request_json.get('often2Count3')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKADHDScreening()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.mistakesinschoolwork=question1
                    Insert.playactivities=question2
                    Insert.spokentodirectly=question3
                    Insert.failstofinishschool=question4
                    Insert.difficulttoorganize=question5
                    Insert.reluctantlyengages=question6
                    Insert.losethings=question7
                    Insert.distractedbyextraneous=question8
                    Insert.dailyactivities=question9
                    Insert.maintainalertness=question10
                    Insert.squirmsinseat=question11
                    Insert.seatinclassroom=question12
                    Insert.climbsexcessively=question13
                    Insert.leisureactivities=question14
                    Insert.drivenbyamotor=question15
                    Insert.Talksexcessively=question16
                    Insert.answersbefore=question17
                    Insert.difficulttosit=question18
                    Insert.symptomspresent=question19
                    Insert.symptomsleading=question20
                    Insert.symptomsaffecting=question21
                    
                    Insert.Score1to9=often23Count
                    Insert.Score10to18=often23Count2
                    Insert.Score19to21=often23Count3
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK-ADHD Screening Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()

@Assessment_Blueprint.route('/viewCKADHDScreening', methods=['GET','POST'])
def viewCKADHDScreening():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewCKADHDScreening,
                                session.query(Model.models.Application.M_CKADHDScreening.MCKID.label('ID'),
                                            Model.models.Application.M_CKADHDScreening.Score1to9.label('A19'),
                                            Model.models.Application.M_CKADHDScreening.Score10to18.label('B1018'),
                                            Model.models.Application.M_CKADHDScreening.Score19to21.label('C1921'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKADHDScreening.MCKID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()                    
                    
@Assessment_Blueprint.route('/submitCKFU', methods=['GET','POST'])
def submitCKFU():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    question1 = request_json.get('question1')
                    question2 = request_json.get('question2')
                    question3 = request_json.get('question3')
                    question4 = request_json.get('question4')
                    question5 = request_json.get('question5')
                    question6 = request_json.get('question6')
                    question7 = request_json.get('question7')
                    question8 = request_json.get('question8')
                    question9 = request_json.get('question9')
                    question10 = request_json.get('question10')
                    question11 = request_json.get('question11')
                    question12 = request_json.get('question12')
                    question13 = request_json.get('question13')
                    question14 = request_json.get('question14')
                    question15 = request_json.get('question15')
                    question16 = request_json.get('question16')
                    question17 = request_json.get('question17')
                    question18 = request_json.get('question18')
                    question19 = request_json.get('question19')
                    question20 = request_json.get('question20')
                    question21 = request_json.get('question21')
                    question22 = request_json.get('question22')
                    question23 = request_json.get('question23')
                    question24 = request_json.get('question24')
                    question25 = request_json.get('question25')
                    question26 = request_json.get('question26')
                    question27 = request_json.get('question27')
                    question28 = request_json.get('question28')
                    question29 = request_json.get('question29')
                    question30 = request_json.get('question30')
                    question31 = request_json.get('question31')
                    question32 = request_json.get('question32')
                    question33 = request_json.get('question33')
                    question34 = request_json.get('question34')
                    question35 = request_json.get('question35')
                    question36 = request_json.get('question36')
                    question37 = request_json.get('question37')
                    question38 = request_json.get('question38')
                    question39 = request_json.get('question39')
                    question40 = request_json.get('question40')
                    question41 = request_json.get('question41')
                    question42 = request_json.get('question42')
                    question43 = request_json.get('question43')
                    question44 = request_json.get('question44')
                    Score = request_json.get('Score')

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKFUForm()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.Noncontextual=question1
                    Insert.Picapresent=question2
                    Insert.Responsetosound=question3
                    Insert.Indicatepottyneeds=question4
                    Insert.Givesattentionwhere=question5
                    Insert.Indicateurineneeds=question6
                    Insert.Walksbetweenpeople=question7
                    Insert.SleepProblemsinitiation=question8
                    Insert.DoesNotUnderstandtone=question9
                    Insert.Overtlysensitivetoweird=question10
                    Insert.Isnotimaginativebad=question11
                    Insert.Overtlysensitivetotextures=question12
                    Insert.Overtlysensitivetosmell=question13
                    Insert.Toewalkingpresent=question14
                    Insert.Notablecommunicatefeelings=question15
                    Insert.unusualeyecontact=question16
                    Insert.Likesshadowssideward=question17
                    Insert.Notabletoimitateothers=question18
                    Insert.Doesnotplayproperly=question19
                    Insert.Doesnotoffercomfort=question20
                    Insert.Difficultyrelatingtoadults=question21
                    Insert.Difficultyrelatingtopeers=question22
                    Insert.Doesnotrespondappropriately=question23
                    Insert.Wandersaimlessly=question24
                    Insert.Toosillyorlaughs=question25
                    Insert.Difficultyanswering=question26
                    Insert.Talkswithunusualtone=question27
                    Insert.Emotionallydistant=question28
                    Insert.Movingincirclespresent=question29
                    Insert.Seemsmorefidgety=question30
                    Insert.Wouldratherbealone=question31
                    Insert.Likesparallelplay=question32
                    Insert.Avoidsstartingsocial=question33
                    Insert.Staresorgazesoff=question34
                    Insert.Feedingchewingisaconcern=question35
                    Insert.Hyperactivitypresent=question36
                    Insert.Behavesinwaysthat=question37
                    Insert.Showsunusualsensory=question38
                    Insert.Thinksortalksabout=question39
                    Insert.Hasanunusuallynarrow=question40
                    Insert.Doesextremelywell=question41
                    Insert.Hasrepetitiveodd=question42
                    Insert.Dislikesbeing=question43
                    Insert.DoesntrespondtoNo=question44
                    Insert.Score=Score
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK-Follow Up Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()


@Assessment_Blueprint.route('/viewCKFU', methods=['GET','POST'])
def viewCKFU():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewCKFU,
                                session.query(Model.models.Application.M_CKFUForm.FUID.label('ID'),
                                            Model.models.Application.M_CKFUForm.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_CKFUForm.Noncontextual.label('Noncontextual'),
                                            Model.models.Application.M_CKFUForm.Picapresent.label('Picapresent'),
                                            Model.models.Application.M_CKFUForm.Responsetosound.label('Responsetosound'),
                                            Model.models.Application.M_CKFUForm.Indicatepottyneeds.label('Indicatepottyneeds'),
                                            Model.models.Application.M_CKFUForm.Givesattentionwhere.label('Givesattentionwhere'),
                                            Model.models.Application.M_CKFUForm.Indicateurineneeds.label('Indicateurineneeds'),
                                            Model.models.Application.M_CKFUForm.Walksbetweenpeople.label('Walksbetweenpeople'),
                                            Model.models.Application.M_CKFUForm.SleepProblemsinitiation.label('SleepProblemsinitiation'),
                                            Model.models.Application.M_CKFUForm.DoesNotUnderstandtone.label('DoesNotUnderstandtone'),
                                            Model.models.Application.M_CKFUForm.Overtlysensitivetoweird.label('Overtlysensitivetoweird'),
                                            Model.models.Application.M_CKFUForm.Isnotimaginativebad.label('Isnotimaginativebad'),
                                            Model.models.Application.M_CKFUForm.Overtlysensitivetotextures.label('Overtlysensitivetotextures'),
                                            Model.models.Application.M_CKFUForm.Overtlysensitivetosmell.label('Overtlysensitivetosmell'),
                                            Model.models.Application.M_CKFUForm.Toewalkingpresent.label('Toewalkingpresent'),
                                            Model.models.Application.M_CKFUForm.Notablecommunicatefeelings.label('Notablecommunicatefeelings'),
                                            Model.models.Application.M_CKFUForm.unusualeyecontact.label('unusualeyecontact'),
                                            Model.models.Application.M_CKFUForm.Likesshadowssideward.label('Likesshadowssideward'),
                                            Model.models.Application.M_CKFUForm.Notabletoimitateothers.label('Notabletoimitateothers'),
                                            Model.models.Application.M_CKFUForm.Doesnotplayproperly.label('Doesnotplayproperly'),
                                            Model.models.Application.M_CKFUForm.Doesnotoffercomfort.label('Doesnotoffercomfort'),
                                            Model.models.Application.M_CKFUForm.Difficultyrelatingtoadults.label('Difficultyrelatingtoadults'),
                                            Model.models.Application.M_CKFUForm.Difficultyrelatingtopeers.label('Difficultyrelatingtopeers'),
                                            Model.models.Application.M_CKFUForm.Doesnotrespondappropriately.label('Doesnotrespondappropriately'),
                                            Model.models.Application.M_CKFUForm.Wandersaimlessly.label('Wandersaimlessly'),
                                            Model.models.Application.M_CKFUForm.Toosillyorlaughs.label('Toosillyorlaughs'),
                                            Model.models.Application.M_CKFUForm.Difficultyanswering.label('Difficultyanswering'),
                                            Model.models.Application.M_CKFUForm.Talkswithunusualtone.label('Talkswithunusualtone'),
                                            Model.models.Application.M_CKFUForm.Emotionallydistant.label('Emotionallydistant'),
                                            Model.models.Application.M_CKFUForm.Movingincirclespresent.label('Movingincirclespresent'),
                                            Model.models.Application.M_CKFUForm.Seemsmorefidgety.label('Seemsmorefidgety'),
                                            Model.models.Application.M_CKFUForm.Wouldratherbealone.label('Wouldratherbealone'),
                                            Model.models.Application.M_CKFUForm.Likesparallelplay.label('Likesparallelplay'),
                                            Model.models.Application.M_CKFUForm.Avoidsstartingsocial.label('Avoidsstartingsocial'),
                                            Model.models.Application.M_CKFUForm.Staresorgazesoff.label('Staresorgazesoff'),
                                            Model.models.Application.M_CKFUForm.Feedingchewingisaconcern.label('Feedingchewingisaconcern'),
                                            Model.models.Application.M_CKFUForm.Hyperactivitypresent.label('Hyperactivitypresent'),
                                            Model.models.Application.M_CKFUForm.Behavesinwaysthat.label('Behavesinwaysthat'),
                                            Model.models.Application.M_CKFUForm.Showsunusualsensory.label('Showsunusualsensory'),
                                            Model.models.Application.M_CKFUForm.Thinksortalksabout.label('Thinksortalksabout'),
                                            Model.models.Application.M_CKFUForm.Hasanunusuallynarrow.label('Hasanunusuallynarrow'),
                                            Model.models.Application.M_CKFUForm.Doesextremelywell.label('Doesextremelywell'),
                                            Model.models.Application.M_CKFUForm.Hasrepetitiveodd.label('Hasrepetitiveodd'),
                                            Model.models.Application.M_CKFUForm.Dislikesbeing.label('Dislikesbeing'),
                                            Model.models.Application.M_CKFUForm.DoesntrespondtoNo.label('DoesntrespondtoNo'),
                                            Model.models.Application.M_CKFUForm.Difficultyrelatingtoadults.label('Difficultyrelatingtoadults'),
                                            Model.models.Application.M_CKFUForm.Difficultyrelatingtoadults.label('Difficultyrelatingtoadults'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKFUForm.FUID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()

@Assessment_Blueprint.route('/submitCKDevelopmental', methods=['GET','POST'])
def submitCKDevelopmental():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request_json = request.get_json()
                    question1 = request_json.get('question1')
                    question2 = request_json.get('question2')
                    question3 = request_json.get('question3')
                    question4 = request_json.get('question4')
                    question5 = request_json.get('question5')
                    question6 = request_json.get('question6')
                    question7 = request_json.get('question7')
                    question8 = request_json.get('question8')
                    question9 = request_json.get('question9')
                    question10 = request_json.get('question10')
                    question11 = request_json.get('question11')
                    question12 = request_json.get('question12')
                    question13 = request_json.get('question13')
                    question14 = request_json.get('question14')
                    question15 = request_json.get('question15')
                    question16 = request_json.get('question16')
                    question17 = request_json.get('question17')
                    question18 = request_json.get('question18')
                    question19 = request_json.get('question19')
                    question20 = request_json.get('question20')
                    question21 = request_json.get('question21')
                    question22 = request_json.get('question22')
                    question23 = request_json.get('question23')
                    question24 = request_json.get('question24')
                    question25 = request_json.get('question25')
                    question26 = request_json.get('question26')
                    question27 = request_json.get('question27')
                    question28 = request_json.get('question28')
                    question29 = request_json.get('question29')
                    question30 = request_json.get('question30')
                    question31 = request_json.get('question31')
                    question32 = request_json.get('question32')
                    question33 = request_json.get('question33')
                    question34 = request_json.get('question34')
                    question35 = request_json.get('question35')
                    question36 = request_json.get('question36')
                    question37 = request_json.get('question37')
                    question38 = request_json.get('question38')
                    question39 = request_json.get('question39')
                    question40 = request_json.get('question40')
                    question41 = request_json.get('question41')
                    question42 = request_json.get('question42')
                    question43 = request_json.get('question43')
                    question44 = request_json.get('question44')
                    question45 = request_json.get('question45')
                    question46 = request_json.get('question46')
                    question47 = request_json.get('question47')
                    question48 = request_json.get('question48')
                    question49 = request_json.get('question49')
                    question50 = request_json.get('question50')
                    question51 = request_json.get('question51')
                    question52 = request_json.get('question52')
                    question53 = request_json.get('question53')
                    question54 = request_json.get('question54')
                    question55 = request_json.get('question55')
                    question56 = request_json.get('question56')
                    question57 = request_json.get('question57')
                    question58 = request_json.get('question58')
                    question59 = request_json.get('question59')
                    question60 = request_json.get('question60')
                    question61 = request_json.get('question61')
                    question62 = request_json.get('question62')
                    question63 = request_json.get('question63')
                    question64 = request_json.get('question64')
                    question65 = request_json.get('question65')
                    question66 = request_json.get('question66')
                    question67 = request_json.get('question67')
                    question68 = request_json.get('question68')
                    question69 = request_json.get('question69')
                    question70 = request_json.get('question70')
                    question71 = request_json.get('question71')
                    question72 = request_json.get('question72')
                    question73 = request_json.get('question73')
                    question74 = request_json.get('question74')
                    question75 = request_json.get('question75')
                    question76 = request_json.get('question76')
                    question77 = request_json.get('question77')
                    question78 = request_json.get('question78')
                    question79 = request_json.get('question79')
                    question80 = request_json.get('question80')
                    question81 = request_json.get('question81')
                    question82 = request_json.get('question82')
                    question83 = request_json.get('question83')
                    question84 = request_json.get('question84')
                    question85 = request_json.get('question85')
                    question86 = request_json.get('question86')
                    question87 = request_json.get('question87')
                    question88 = request_json.get('question88')
                    question89 = request_json.get('question89')
                    question90 = request_json.get('question90')
                    question91 = request_json.get('question91')
                    question92 = request_json.get('question92')
                    question93 = request_json.get('question93')
                    question94 = request_json.get('question94')
                    question95 = request_json.get('question95')
                    question96 = request_json.get('question96')
                    question97 = request_json.get('question97')
                    question98 = request_json.get('question98')
                    question99 = request_json.get('question98')
                    question100 = request_json.get('question100')
                    question101 = request_json.get('question101')
                    question102 = request_json.get('question102')
                    question103 = request_json.get('question103')
                    question104 = request_json.get('question104')
                    question105 = request_json.get('question105')
                    question106 = request_json.get('question106')
                    question107 = request_json.get('question107')
                    
                    
                    
                    grossmotoryes = request_json.get('grossmotoryes')
                    grossmotorno = request_json.get('grossmotorno')
                    finemotoryes = request_json.get('finemotoryes')
                    finemotorno = request_json.get('finemotorno')
                    selfhelpyes = request_json.get('selfhelpyes')
                    selfhelpno = request_json.get('selfhelpno')
                    problemsolvingyes = request_json.get('problemsolvingyes')
                    problemsolvingno = request_json.get('problemsolvingno')
                    emotionalyes = request_json.get('emotionalyes')
                    emotionalno = request_json.get('emotionalno')
                    receptiveyes = request_json.get('receptiveyes')
                    receptiveno = request_json.get('receptiveno')
                    expressiveyes = request_json.get('expressiveyes')
                    expressiveno = request_json.get('expressiveno')
                    socialyes = request_json.get('socialyes')
                    socialno = request_json.get('socialno')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKDevelopmental()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    Insert.canlifttheheadup=question1
                    Insert.triestostabilizehead=question2
                    Insert.lessroundingofback=question3
                    Insert.canstabiliseheadfully=question4
                    Insert.Rollsfromfronttoback=question5
                    Insert.Cansitwithoutsupport=question6
                    Insert.Bearswholebodyweightonlegs=question7
                    Insert.Standswellwitharmshigh=question8
                    Insert.Cruisesfurnitureusinonehand=question9
                    Insert.Walkswithonehandheld=question10
                    Insert.Standsononefootwithslight=question11
                    Insert.Seatsselfinsmallchair=question12
                    Insert.Throwsballwhilestanding=question13
                    Insert.Walksdownstairsholdingrail=question14
                    Insert.Kicksballwithoutdemonstration=question15
                    Insert.Squatsinplay=question16
                    Insert.Walkupstairswithrail=question17
                    Insert.Jumpsinplace=question18
                    Insert.Standswithbothfeetonbalance=question19
                    Insert.Balancesononefootfor3seconds=question20
                    Insert.Goesupstairsnorails=question21
                    Insert.Pedalstricycle=question22
                    Insert.Balancesononefoot4to8second=question23
                    Insert.Hopononefoottwotothreetimes=question24
                    Insert.Standingbroadjump1to2feet=question25
                    Insert.Gallops=question26
                    Insert.Throwsballoverhand10feet=question27
                    Insert.Catchesbouncedball=question28
                    Insert.Walksdownstairswithrail=question29
                    Insert.Balanceononefoot8seconds=question30
                    Insert.Hopononefoot15times=question31
                    Insert.Canskip=question32
                    Insert.Runbroadjumpapproximately2to3feet=question33
                    Insert.Walksbackwardheeltoe=question34
                    
                    Insert.Handsunfisted=question35
                    Insert.Watchesmovement=question36
                    Insert.Whenrattleifplaced=question37
                    Insert.Dropsoneobjectfrom=question38
                    Insert.Abletoholdobjects=question39
                    Insert.Reachesdanglingobjects=question40
                    Insert.pickupobjectsofsmallsize=question41
                    Insert.Canbangtoysontable=question42
                    Insert.Cantransferobjectfromonehandtoanother=question43
                    Insert.Scribblesafterdemonstration=question44
                    Insert.Canholdacrayon=question45
                    Insert.Attemptsputtingoneblock=question46
                    Insert.Makesfourblocktower=question47
                    Insert.Places10blocksinacontainer=question48
                    Insert.Crudelycopiesverticallines=question49
                    Insert.Makesasinglelinetrain=question50
                    Insert.Imitatescircle=question51
                    Insert.Imitateshorizontalline=question52
                    Insert.Stringslargebeadsawkwardly=question53
                    Insert.Unscrewsjarlid=question54
                    Insert.Turnspaperpages=question55
                    Insert.Copiescircle=question56
                    Insert.Cutswithscissors=question57
                    Insert.Stringssmallbeadswell=question58
                    Insert.Imitatescomplexfigureswithblocks=question59
                    Insert.Canusescissorsinabetterway=question60
                    Insert.Washeshandonhisown=question61
                    Insert.Copiessquare=question62
                    Insert.Tiessingleknot=question63
                    Insert.Writespartoffirstname=question64
                    Insert.Putspapercliponpaper=question65
                    Insert.Canuseclothespins=question66
                    Insert.Cutswithscissors=question67
                    Insert.Buildsstairsfrommodel=question68
                    Insert.Drawsdiamond=question69
                    Insert.Writesfirstandlastname=question70
                    Insert.Turnsheadtowardssound=question71
                    Insert.Opensmouthatthesiteofbreast=question72
                    Insert.Suckingestablished=question73
                    Insert.Gumsmouthspureedfood=question74
                    Insert.Placeshandsonbottle=question75
                    Insert.Drinksfromcupwhen=question76
                    Insert.Canholdownbottle=question77
                    Insert.Canholdabiscuittofeed=question78
                    Insert.Biteschewsfood=question79
                    Insert.Cooperateswithdressing=question80
                    Insert.Fingerfeedspartofmeal=question81
                    Insert.Takesoffshoescapetc=question82
                    Insert.Removessocksshoes=question83
                    Insert.Putsspooninmouth=question84
                    Insert.Attemptstobrushownhair=question85
                    Insert.Opensdoorusingsknob=question86
                    Insert.Takesoffclotheswithoutbuttons=question87
                    Insert.Pullsoffpants=question88
                    Insert.Washeshands=question89
                    Insert.Putsthingsaway=question90
                    Insert.Brushesteethwithassistance=question91
                    Insert.Poursliquidfromonecontainer=question92
                    Insert.Independenteating=question93
                    Insert.Putsonshoeswithoutlaces=question94
                    Insert.Unbuttons=question95
                    Insert.Goestotoiletalone=question96
                    Insert.Washesafterbowelmovement=question97
                    Insert.Washesfaceonhisown=question98
                    Insert.Brushesteethalone=question99
                    Insert.Buttons=question100
                    Insert.Usesforkwell=question101
                    Insert.Spreadswithknife=question102
                    Insert.Independentdressing=question103
                    Insert.BathesIndependently=question104
                    Insert.Combshair=question105
                    Insert.Looksbothwaysatstreet=question106
                    
                    # Insert.Reachesforface=question107
                    # Insert.Followsdanglingobjectsfrom=question108
                    # Insert.Looksatobjectsinmidline=question109
                    # Insert.Touchesreflectioninmirror=question110
                    # Insert.Removesclothonface=question111
                    # Insert.Bangsandshakestoys=question112
                    # Insert.Imitatessimpleacts=question113
                    # Insert.Patsimageofselfinmirror=question114
                    # Insert.Reachespersistentlyforobjects=question115
                    # Insert.Couldlocaliseahiddentoy=question116
                    # Insert.Looksatpicturesinbook=question117
                    # Insert.Rattlesspoonincup=question118
                    # Insert.Dumpspelletoutofbottle=question119
                    # Insert.Turnspagesinbook=question120
                    # Insert.Findstoyobservedtobehidden=question121
                    # Insert.Matchesobjectstopictures=question122
                    # Insert.Sortsobjects=question123
                    # Insert.Showsuseoffamiliarobjects=question124
                    # Insert.Matchesshapes=question125
                    # Insert.Matchescolors=question126
                    # Insert.Pointstosmalldetails=question127
                    # Insert.Drawatwotothree=question128
                    # Insert.Understandslongshort=question129
                    # Insert.Knowsowngender=question130
                    # Insert.Knowsownage=question131
                    # Insert.Matcheslettersnumerals=question132
                    # Insert.Drawsafourtosixpartperson=question133
                    # Insert.Cangiveamounts=question134
                    # Insert.Understandssimplenalogies=question135
                    # Insert.Pointstofivetosixcolors=question136
                    # Insert.Pointstolettersnumerals=question137
                    # Insert.Readseveralcommon=question138
                    # Insert.Looksbothwaysatstreet=question139
                    # Insert.Looksbothwaysatstreet=question140
                    # Insert.Looksbothwaysatstreet=question141
                    # Insert.Looksbothwaysatstreet=question142
                    # Insert.Looksbothwaysatstreet=question143
                    
                    
                    
                    
                    Insert.grossmotoryes=grossmotoryes
                    Insert.grossmotorno =grossmotorno 
                    Insert.finemotoryes=finemotoryes
                    Insert.finemotorno=finemotorno
                    Insert.selfhelpyes=selfhelpyes
                    Insert.selfhelpno=selfhelpno
                    Insert.problemsolvingyes=problemsolvingyes
                    Insert.problemsolvingno=problemsolvingno
                    Insert.emotionalyes=emotionalyes
                    Insert.emotionalno=emotionalno
                    Insert.receptiveyes=receptiveyes
                    Insert.receptiveno=receptiveno
                    Insert.expressiveyes=expressiveyes
                    Insert.expressiveno=expressiveno
                    Insert.socialyes=socialyes
                    Insert.socialno=socialno
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK-Developmental Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()

@Assessment_Blueprint.route('/viewCKDevelopScreening', methods=['GET','POST'])
def viewCKDevelopScreening():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    request1= request.get_json()
                    pid = request1.get('pid')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewCKDevelopScreening,
                                session.query(Model.models.Application.M_CKDevelopmental.CKDID.label('ID'),
                                            Model.models.Application.M_CKDevelopmental.grossmotoryes.label('grossmotoryes'),
                                            Model.models.Application.M_CKDevelopmental.grossmotorno.label('grossmotorno'),
                                            Model.models.Application.M_CKDevelopmental.finemotoryes.label('finemotoryes'),
                                            Model.models.Application.M_CKDevelopmental.finemotorno.label('finemotorno'),
                                            Model.models.Application.M_CKDevelopmental.selfhelpyes.label('selfhelpyes'),
                                            Model.models.Application.M_CKDevelopmental.selfhelpno.label('selfhelpno'),
                                            Model.models.Application.M_CKDevelopmental.problemsolvingyes.label('problemsolvingyes'),
                                            Model.models.Application.M_CKDevelopmental.problemsolvingno.label('problemsolvingno'),
                                            Model.models.Application.M_CKDevelopmental.emotionalyes.label('emotionalyes'),
                                            Model.models.Application.M_CKDevelopmental.emotionalno.label('emotionalno'),
                                            Model.models.Application.M_CKDevelopmental.receptiveyes.label('receptiveyes'),
                                            Model.models.Application.M_CKDevelopmental.receptiveno.label('receptiveno'),
                                            Model.models.Application.M_CKDevelopmental.expressiveyes.label('expressiveyes'),
                                            Model.models.Application.M_CKDevelopmental.expressiveno.label('expressiveno'),
                                            Model.models.Application.M_CKDevelopmental.socialyes.label('socialyes'),
                                            Model.models.Application.M_CKDevelopmental.socialno.label('socialno'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKDevelopmental.CKDID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()                    















