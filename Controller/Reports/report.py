import hashlib
from logging import Logger
import random
import sqlalchemy
import flask
from flask import Flask, redirect, request, jsonify
import jwt
from requests import session
import Model.models
import datetime
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
import Constant.constant
import app
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Report_Blueprint = CommonModule.flask.Blueprint(
    'Report_Blueprint', import_name=__name__)

@Report_Blueprint.route('/getPatientDetailFromAppointment', methods=['GET','POST'])
async def getPatientDetailFromAppointment():
    session=Session()
    try:
        if(request.method == "POST"):
            
            
            request1= request.get_json()
            AID = request1.get('AID')
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getPatientDetailFromAppointment,
                        session.query(Model.models.Application.M_Appointment.MAID.label('AppointId'),
                            Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                            Model.models.Application.M_Appointment.MP_Procedure.label('procedure'),
                            sqlalchemy.func.date_format(Model.models.Application.M_Appointment.MA_Date,'%d-%b-%Y').label('date'),
                            Model.models.Application.M_Appointment.MA_Time.label('time'),
                            Model.models.Application.M_Appointment.MP_Duration.label('duration'),
                            Model.models.Application.M_Appointment.M_DoctorDetails_MDDID.label('doctor'),
                            Model.models.Application.M_Patient.MP_Name.label('Patient'),
                            Model.models.Application.M_Patient.MP_Mobile.label('Mobile'),
                            Model.models.Application.M_Patient.MP_Address.label('Address'),
                            Model.models.Application.M_Patient.MP_DOB.label('DOB'),
                            Model.models.Application.M_Patient.MP_UHID.label('UHID'),
                            Model.models.Application.M_Patient.MP_Email.label('Email'),
                            Model.models.Application.M_DoctorDetails.MDD_FirstName.label('Doctor Name'),
                            Model.models.Application.M_Branch.MB_Name.label('Branch'),
                            Model.models.Application.T_Details.TD_Name.label('Gender'),
                            
                                ).filter_by(MAID=AID,MP_IsActive=1,MP_IsDeleted=0
                            ).join(Model.models.Application.M_Patient,Model.models.Application.M_Patient.MPID==Model.models.Application.M_Appointment.M_Patient_MPID
                            ).join(Model.models.Application.M_DoctorDetails,Model.models.Application.M_DoctorDetails.MDDID==Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                            ).join(Model.models.Application.M_Branch,Model.models.Application.M_Branch.MBID==Model.models.Application.M_Appointment.M_Branch_MBID
                            ).outerjoin(Model.models.Application.T_Details,Model.models.Application.T_Details.TDID==Model.models.Application.M_Patient.MP_Gender
                            ).all()
                )
            session.commit()

            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewVinelandSocialMaturityScaleReport', methods=['GET','POST'])
async def viewVinelandSocialMaturityScaleReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewVinelandSocialMaturityScaleReport,
                        session.query(Model.models.Application.M_VinelandSocialMaturityScale.MVAMID.label('ID'),
                                    Model.models.Application.M_VinelandSocialMaturityScale.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_VinelandSocialMaturityScale.MVAM_SocialAge.label('Social Age'),
                                    Model.models.Application.M_VinelandSocialMaturityScale.MVAM_IQ.label('Social Quotient'),
                                    Model.models.Application.M_VinelandSocialMaturityScale.MVAM_Observations.label('Observations'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MVAM_IsActive=1,MVAM_IsDeleted=0
                        ).order_by(Model.models.Application.M_VinelandSocialMaturityScale.MVAMID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewChildhoodAutismRatingScaleReport', methods=['GET','POST'])
async def viewChildhoodAutismRatingScaleReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewChildhoodAutismRatingScaleReport,
                        session.query(Model.models.Application.M_ChildhoodAutismRatingScale.MCARID.label('ID'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_RelatingtoPeople.label('Relating to People'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Imitation.label('Imitation'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_EmotionalResponse.label('Emotional Response'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_BodyUse.label('Body Use'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ObjectUse.label('Object Use'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_AdaptationChange.label('Daptation Change'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_VisualResponse.label('Visual Response'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ListeningResponse.label('Listening Response'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_TasteSmellUse.label('Taste Smell Use'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Fearornervousness.label('Fear or Nervousness'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Verbal.label('Verbal'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Nonverbal.label('Non Verbal'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ActivityLevel.label('Activity Level'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Consistencyresponse.label('Consistency Response'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_GeneralImpression.label('General Impression'),
                                    Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Concludinremark.label('Concluding Remark')
                                    
                                        ).filter_by(M_AppointmentID=AID,MCAR_IsActive=1,MCAR_IsDeleted=0
                        ).order_by(Model.models.Application.M_ChildhoodAutismRatingScale.MCARID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewIndianScaleAssessmentAutismReport', methods=['GET','POST'])
async def viewIndianScaleAssessmentAutismReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewIndianScaleAssessmentAutismReport,
                        session.query(Model.models.Application.M_IndianScaleAssessmentAutism.MIID.label('ID'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.SOCIALRECIPROCITY.label('SOCIAL RECIPROCITY'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.EMOTIONALRESPONSIVENESS.label('EMOTIONAL RESPONSIVENESS'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.SPEECHCOMMUNICATION.label('SPEECH COMMUNICATION'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.BEHAVIOURPATTERNS.label('BEHAVIOUR PATTERNS'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.SENSORYASPECTS.label('SENSORY ASPECTS'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.COGNITIVECOMPONENT.label('COGNITIVE COMPONENT'),
                                    Model.models.Application.M_IndianScaleAssessmentAutism.FinalComment.label('Final Comment')
                                    
                                        ).filter_by(M_AppointmentID=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_IndianScaleAssessmentAutism.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
               
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewSequinFormBoardTestReport', methods=['GET','POST'])
async def viewSequinFormBoardTestReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewSequinFormBoardTestReport,
                        session.query(Model.models.Application.M_SequinFormBoardTest.MSFBID.label('ID'),
                                    Model.models.Application.M_SequinFormBoardTest.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_MentalAge.label('Mental Age'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_IQ.label('IQ'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_ShortestTime.label('Shortest Time'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_TotalTime.label('Total Time'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_CorrespondsMentalAge.label('Corresponds Mental Age'),
                                    Model.models.Application.M_SequinFormBoardTest.MSFB_suggestingIntellectualfunctioning.label('Suggesting Intellectual Functioning'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MSFB_IsActive=1,MSFB_IsDeleted=0
                        ).order_by(Model.models.Application.M_SequinFormBoardTest.MSFBID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewRavenStandardProgressiveMatricesReport', methods=['GET','POST'])
async def viewRavenStandardProgressiveMatricesReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewRavenStandardProgressiveMatricesReport,
                        session.query(Model.models.Application.M_RavenStandardProgressiveMatrices.MRSPID.label('ID'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_RawScore.label('Raw Score'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Percentile.label('Percentile'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Grade.label('Grade'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Interpretation.label('Interpretation'),
                                    Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_CorrespondsTo.label('Corresponds To'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MRSP_IsActive=1,MRSP_IsDeleted=0
                        ).order_by(Model.models.Application.M_RavenStandardProgressiveMatrices.MRSPID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewGeselsDrawingTestofintelligenceReport', methods=['GET','POST'])
async def viewGeselsDrawingTestofintelligenceReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewGeselsDrawingTestofintelligenceReport,
                        session.query(Model.models.Application.M_GeselsDrawingTestofintelligence.MGDIID.label('ID'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAge.label('Mental Age'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_IQ.label('IQ'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAgeMonths.label('Mental Age Months'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAgeYears.label('Mental Age Years'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_IQof.label('IQ of'),
                                    Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_Depicting.label('Depicting'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MGDI_IsActive=1,MGDI_IsDeleted=0
                        ).order_by(Model.models.Application.M_GeselsDrawingTestofintelligence.MGDIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewDevelopmentalProfileReport', methods=['GET','POST'])
async def viewDevelopmentalProfileReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewDevelopmentalProfileReport,
                        session.query(Model.models.Application.M_DevelopmentalProfile.MDPID.label('ID'),
                                    Model.models.Application.M_DevelopmentalProfile.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalStandardScore.label('Physical Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalDescCategory.label('Physical Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalAgeEquivalent.label('Physical Age Equivalent'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorStandardScore.label('Adaptive Behavior Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorDescCategory.label('Adaptive Behavior Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorAgeEquivalent.label('Adaptive Behavior Age Equivalent'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoStandardScore.label('Social Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoDescCategory.label('Social Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoAgeEquivalent.label('Social Equivalent'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveStandardScore.label('Cognitive Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveDescCategory.label('Cognitive Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveAgeEquivalent.label('Cognitive Age Equivalent'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CommStandardScore.label('Comm Standard Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CommDescCategory.label('Comm Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_CommAgeEquivalent.label('Comm Age Equivalent'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreStandardScore.label('General Dev Score'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreDescCategory.label('General Dev Category'),
                                    Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreAgeEquivalent.label('General Age Equivalent')
                                    
                                        ).filter_by(M_AppointmentID=AID,MDP_IsActive=1,MDP_IsDeleted=0
                        ).order_by(Model.models.Application.M_DevelopmentalProfile.MDPID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
        else:
            return jsonify({'err':request.method})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewPerceptualAndVisualMotorAbilityReport', methods=['GET','POST'])
async def viewPerceptualAndVisualMotorAbilityReport():
    session=Session()
    try:
        if(request.method == "POST"):
                
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewPerceptualAndVisualMotorAbilityReport,
                        session.query(Model.models.Application.M_PerceptualNvisual.MIID.label('ID'),
                                    Model.models.Application.M_PerceptualNvisual.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_PerceptualNvisual.VisualDiscr.label('VisualDiscr'),
                                    Model.models.Application.M_PerceptualNvisual.VisualDiscrComments.label('VisualDiscrComments'),
                                    Model.models.Application.M_PerceptualNvisual.VisualMemoryTest.label('VisualMemoryTest'),
                                    Model.models.Application.M_PerceptualNvisual.VisualMemoryTestComments.label('VisualMemoryTestComments'),
                                    Model.models.Application.M_PerceptualNvisual.AuditoryMemory.label('AuditoryMemory'),
                                    Model.models.Application.M_PerceptualNvisual.AuditoryMemoryComments.label('AuditoryMemoryComments'),
                                    Model.models.Application.M_PerceptualNvisual.Attention.label('Attention'),
                                    Model.models.Application.M_PerceptualNvisual.AttentionComments.label('AttentionComments'),
                                    Model.models.Application.M_PerceptualNvisual.DoubleNumCancel.label('DoubleNumCancel'),
                                    Model.models.Application.M_PerceptualNvisual.DoubleNumCancelComments.label('DoubleNumCancelComments'),
                                    Model.models.Application.M_PerceptualNvisual.Language.label('Language'),
                                    Model.models.Application.M_PerceptualNvisual.LanguageComments.label('LanguageComments'),
                                    Model.models.Application.M_PerceptualNvisual.Reading.label('Reading'),
                                    Model.models.Application.M_PerceptualNvisual.ReadingComments.label('ReadingComments'),
                                    Model.models.Application.M_PerceptualNvisual.Comprehension.label('Comprehension'),
                                    Model.models.Application.M_PerceptualNvisual.ComprehensionComments.label('ComprehensionComments'),
                                    Model.models.Application.M_PerceptualNvisual.Spelling.label('Spelling'),
                                    Model.models.Application.M_PerceptualNvisual.SpellingComments.label('SpellingComments'),
                                    Model.models.Application.M_PerceptualNvisual.WritingAndCopy.label('WritingAndCopy'),
                                    Model.models.Application.M_PerceptualNvisual.WritingAndCopyComments.label('WritingAndCopyComments'),
                                    Model.models.Application.M_PerceptualNvisual.WritingSkills.label('WritingSkills'),
                                    Model.models.Application.M_PerceptualNvisual.WritingSkillsComments.label('WritingSkillsComments'),
                                    Model.models.Application.M_PerceptualNvisual.ExpressiveWriting.label('ExpressiveWriting'),
                                    Model.models.Application.M_PerceptualNvisual.ExpressiveWritingComments.label('ExpressiveWritingComments'),
                                    Model.models.Application.M_PerceptualNvisual.Copying.label('Copying'),
                                    Model.models.Application.M_PerceptualNvisual.CopyingComments.label('CopyingComments'),
                                    Model.models.Application.M_PerceptualNvisual.Arithmetic.label('Arithmetic'),
                                    Model.models.Application.M_PerceptualNvisual.ArithmeticComments.label('ArithmeticComments'),
                                    
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_PerceptualNvisual.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewWechslerTestReport', methods=['GET','POST'])
async def viewWechslerTestReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
                
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewWechslerTestReport,
                        session.query(Model.models.Application.M_WechslerTest.MIID.label('ID'),
                                    Model.models.Application.M_WechslerTest.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_WechslerTest.SubsetScore.label('SubsetScore'),
                                    Model.models.Application.M_WechslerTest.ReadCompStandardScore.label('ReadCompStandardScore'),
                                    Model.models.Application.M_WechslerTest.ReadCompConfidenceInterval.label('ReadCompConfidenceInterval'),
                                    Model.models.Application.M_WechslerTest.ReadCompPercentileRank.label('ReadCompPercentileRank'),
                                    Model.models.Application.M_WechslerTest.ReadCompGradeEquivalent.label('ReadCompGradeEquivalent'),
                                    Model.models.Application.M_WechslerTest.WordReadStandardScore.label('WordReadStandardScore'),
                                    Model.models.Application.M_WechslerTest.WordReadConfidence.label('WordReadConfidence'),
                                    Model.models.Application.M_WechslerTest.WordReadPercentileRank.label('WordReadPercentileRank'),
                                    Model.models.Application.M_WechslerTest.WordReadGradeEquivalent.label('WordReadGradeEquivalent'),
                                    Model.models.Application.M_WechslerTest.EssayCompStandardScore.label('EssayCompStandardScore'),
                                    Model.models.Application.M_WechslerTest.EssayCompConfidence.label('EssayCompConfidence'),
                                    Model.models.Application.M_WechslerTest.EssayCompPercentileRank.label('EssayCompPercentileRank'),
                                    Model.models.Application.M_WechslerTest.EssayCompGradeEquivalent.label('EssayCompGradeEquivalent'),
                                    Model.models.Application.M_WechslerTest.NumOperStandardScore.label('NumOperStandardScore'),
                                    Model.models.Application.M_WechslerTest.NumOperConfidence.label('NumOperConfidence'),
                                    Model.models.Application.M_WechslerTest.NumOperPercentileRank.label('NumOperPercentileRank'),
                                    Model.models.Application.M_WechslerTest.NumOperGradeEquivalent.label('NumOperGradeEquivalent'),
                                    Model.models.Application.M_WechslerTest.SpelStandardScore.label('SpelStandardScore'),
                                    Model.models.Application.M_WechslerTest.SpelConfidence.label('SpelConfidence'),
                                    Model.models.Application.M_WechslerTest.SpelPercentileRank.label('SpelPercentileRank'),
                                    Model.models.Application.M_WechslerTest.SpelGradeEquivalent.label('SpelGradeEquivalent'),
                                    Model.models.Application.M_WechslerTest.Comment.label('Comment'),
                                    Model.models.Application.M_WechslerTest.MathematicsComment.label('MathematicsComment'),
                                    Model.models.Application.M_WechslerTest.WrittenExpComment.label('WrittenExpComment'),
                                    
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_WechslerTest.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewChildBehaviorChecklistReport', methods=['GET','POST'])
async def viewChildBehaviorChecklistReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewChildBehaviorChecklistReport,
                        session.query(Model.models.Application.M_ChildBehaviorChecklist.MCBCID.label('ID'),
                                    Model.models.Application.M_ChildBehaviorChecklist.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AnxiousScores.label('AnxiousScores'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AnxiousTscore.label('AnxiousTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AnxiousRange.label('AnxiousRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.WithdrawnScores.label('WithdrawnScores'),
                                    Model.models.Application.M_ChildBehaviorChecklist.WithdrawnTscore.label('WithdrawnTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.WithdrawnRange.label('WithdrawnRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintScores.label('SomaticComplaintScores'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintTscore.label('SomaticComplaintTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintRange.label('SomaticComplaintRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SocialProblemScores.label('SocialProblemScores'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SocialProblemTscore.label('SocialProblemTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.SocialProblemRange.label('SocialProblemRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemScore.label('ThoughtProblemScore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemTscore.label('ThoughtProblemTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemRange.label('ThoughtProblemRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemScore.label('AttentionProblemScore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemTscore.label('AttentionProblemTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemRange.label('AttentionProblemRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorScore.label('RuleBreakingBehaviorScore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorTscore.label('RuleBreakingBehaviorTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorRange.label('RuleBreakingBehaviorRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorScores.label('AggressiveBehaviorScores'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorTscore.label('AggressiveBehaviorTscore'),
                                    Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorRange.label('AggressiveBehaviorRange'),
                                    Model.models.Application.M_ChildBehaviorChecklist.Comment.label('Comment')

                                    ).filter_by(M_AppointmentID=AID,MCBC_IsActive=1,MCBC_IsDeleted=0
                        ).order_by(Model.models.Application.M_ChildBehaviorChecklist.MCBCID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewChildAnxietyRelatedDisordersReport', methods=['GET','POST'])
async def viewChildAnxietyRelatedDisordersReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewChildAnxietyRelatedDisordersReport,
                        session.query(Model.models.Application.M_ChildAnxietyRelatedDisorders.MIID.label('ID'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.PanicDisScore.label('PanicDisorderScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.GenAnxietyDisScore.label('GeneralizedAnxietyDisorderScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.SepAnxietyDisScore.label('SeparationAnxietyDisorderScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.SocialAnxietyDisScore.label('SocialAnxietyDisorderScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.SchoolAvoidScore.label('SchoolAvoidanceScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.AnxietyDisScore.label('AnxietyDisorderScore'),
                                    Model.models.Application.M_ChildAnxietyRelatedDisorders.Comment.label('Comment'),
                                    
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_ChildAnxietyRelatedDisorders.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewHumanTreePersonTestReport', methods=['GET','POST'])
async def viewHumanTreePersonTestReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewHumanTreePersonTestReport,
                        session.query(Model.models.Application.M_HumanTreePersonTest.MIID.label('ID'),
                                    Model.models.Application.M_HumanTreePersonTest.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_HumanTreePersonTest.findings.label('findings'),
                                    Model.models.Application.M_HumanTreePersonTest.indicators.label('indicators'),
                                    Model.models.Application.M_HumanTreePersonTest.comment.label('comment')
                                    
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_HumanTreePersonTest.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewHumanFormDrawingtestReport', methods=['GET','POST'])
async def viewHumanFormDrawingtestReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewHumanFormDrawingtestReport,
                        session.query(Model.models.Application.M_HumanFormDrawingtest.MIID.label('ID'),
                                    Model.models.Application.M_HumanFormDrawingtest.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_HumanFormDrawingtest.findings.label('findings'),
                                    Model.models.Application.M_HumanFormDrawingtest.indicators.label('indicators'),
                                    Model.models.Application.M_HumanFormDrawingtest.comment.label('comment')
                                    
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_HumanFormDrawingtest.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewDSMVCriteriaReport', methods=['GET','POST'])
async def viewDSMVCriteriaReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewDSMVCriteriaReport,
                        session.query(Model.models.Application.M_DSMVCriteria.MIID.label('ID'),
                                    Model.models.Application.M_DSMVCriteria.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_DSMVCriteria.ACriteria.label('ACriteria'),
                                    Model.models.Application.M_DSMVCriteria.ACriteriaComment.label('ACriteriaComment'),
                                    Model.models.Application.M_DSMVCriteria.BCriteria.label('BCriteria'),
                                    Model.models.Application.M_DSMVCriteria.BCriteriaComment.label('BCriteriaComment'),
                                    Model.models.Application.M_DSMVCriteria.CCriteria.label('CCriteria'),
                                    Model.models.Application.M_DSMVCriteria.CCriteriaComment.label('CCriteriaComment'),
                                    Model.models.Application.M_DSMVCriteria.DCriteria.label('DCriteria'),
                                    Model.models.Application.M_DSMVCriteria.DCriteriaComment.label('DCriteriaComment'),
                                    Model.models.Application.M_DSMVCriteria.Question5.label('Question5'),
                                    Model.models.Application.M_DSMVCriteria.Question5Comment.label('Question5Comment'),
                                    Model.models.Application.M_DSMVCriteria.Question6.label('Question6'),
                                    Model.models.Application.M_DSMVCriteria.Question6Comment.label('Question6Comment'),
                                    Model.models.Application.M_DSMVCriteria.Question7.label('Question7'),
                                    Model.models.Application.M_DSMVCriteria.Question7Comment.label('Question7Comment'),
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_DSMVCriteria.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewEpidemiologicalStudiesDepressionScaleReport', methods=['GET','POST'])
async def viewEpidemiologicalStudiesDepressionScaleReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewEpidemiologicalStudiesDepressionScaleReport,
                        session.query(Model.models.Application.M_EpidemiologicalStudiesDepression.MIID.label('ID'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.MI_AppointmentId.label('Appointment Id'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.NotAtAllScore.label('NotAtAllScore'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.ALittleScore.label('ALittleScore'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.SomeScore.label('SomeScore'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.ALotScore.label('ALotScore'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.TotalRawScore.label('TotalRawScore'),
                                    Model.models.Application.M_EpidemiologicalStudiesDepression.Comment.label('Comment')
                                        ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                        ).order_by(Model.models.Application.M_EpidemiologicalStudiesDepression.MIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewMalinIntelligenceScaleforIndianChildrenReport', methods=['GET','POST'])
async def viewMalinIntelligenceScaleforIndianChildrenReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewMalinIntelligenceScaleforIndianChildrenReport,
                        session.query(Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISIID.label('ID'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_InformationTestScores.label('InformationTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_PictureTestScores.label('PictureTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_GeneralTestScores.label('GeneralTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_BlockDesignTestScores.label('BlockDesignTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_ArithmeticTestScores.label('ArithmeticTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_ObjectScores.label('ObjectScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_VocabularyTestScores.label('VocabularyTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_MazeTestScores.label('MazeTestScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_AnalogiesScores.label('AnalogiesScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_CodingScores.label('CodingScores'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_VQ.label('VQ'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_PQ.label('PQ'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_FullScaleIQ.label('FullScaleIQ'),
                                    Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_Comment.label('Comment'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MISI_IsActive=1,MISI_IsDeleted=0
                        ).order_by(Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISIID.desc()).all())


            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/viewNICHQVanderbiltADHDParentReport', methods=['GET','POST'])
async def viewNICHQVanderbiltADHDParentReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request1= request.get_json()
            AID = request1.get('AID')
            
            queryresult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.viewNICHQVanderbiltADHDParentReport,
                        session.query(Model.models.Application.M_NICHQVanderbiltADHDParent.MVAID.label('ID'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.M_AppointmentID.label('Appointment Id'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_InattentionScore.label('Inattention Score'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_HyperactivityScore.label('Hyperactivity Score'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_CombinedScore.label('Combined Score'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_OppositionalScore.label('Oppositional Score'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_ConductScore.label('Conduct Score'),
                                    Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_AnxietyScore.label('Anxiety Score'),
                                    
                                        ).filter_by(M_AppointmentID=AID,MVA_IsActive=1,MVA_IsDeleted=0
                        ).order_by(Model.models.Application.M_NICHQVanderbiltADHDParent.MVAID.desc()).all())
            session.commit()
            return jsonify(result=queryresult)
                
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/ReceptiveLanguageAssessmentReport', methods=['GET','POST'])
async def ReceptiveLanguageAssessmentReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ReceptiveLanguageAssessmentReport,
                                session.query(Model.models.Application.M_ReceptiveLanguageAssessment.MRLAID.label('ID'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendssounds.label('Comprehends sounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsloud.label('Comprehends loud'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendscategorizesounds.label('Comprehends categorizesounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsanimalsounds.label('Comprehends animalsounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsfruitsname.label('Comprehends fruitsname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendscolorsname.label('Comprehends colorsname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsanimalname.label('Comprehends animalname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsvegetablename.label('Comprehends vegetablename'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsshapesname.label('Comprehends shapesname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsbodyparts.label('Comprehends bodyparts'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsvehiclenames.label('Comprehends vehiclenames'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understandingrhymes.label('Understandingrhymes'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Respondscorrectly.label('Respondscorrectly'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Identifiessounds.label('Identifiessounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Actsoutcommands.label('Actsoutcommands'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsstepscommands.label('Comprehends stepscommands'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understandinggreeting.label('Understandinggreeting'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understanding.label('Understanding'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRLA_IsActive=1,MRLA_IsDeleted=0
                                ).order_by(Model.models.Application.M_ReceptiveLanguageAssessment.MRLAID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/ExpressiveLanguageAssessmentReport', methods=['GET','POST'])
async def ExpressiveLanguageAssessmentReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ExpressiveLanguageAssessmentReport,
                                session.query(Model.models.Application.M_ExpressiveLanguageAssessment.MELAID.label('ID'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesenvironmentalsounds.label('Imitates environmental sounds'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesloudandsoftsounds.label('Imitates loud and softsounds'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitateslexicalcategories.label('Imitates lexical categories'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescolorsname.label('Imitates colors name'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesbodyparts.label('Imitates body parts'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatessingingandphrases.label('Imitates singing and phrases'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_ImitatesalphabetsAtoZ.label('Imitates alphabets AtoZ'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Usesnounwitharticles.label('articles'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Watchesfaceandbody.label('Watches'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescounting.label('Imitates counting'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Clapstobeatoffamiliarsongs.label('Claps'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Respondstosinglesigns.label('Respondstosinglesigns'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatessocialgreetings.label('Imitates socialgreetings'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Occassionallytrytoimitate.label('Occassionallytrytoimitate'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescommonsyllables.label('Imitates commonsyllables'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MELA_IsActive=1,MELA_IsDeleted=0
                                ).order_by(Model.models.Application.M_ExpressiveLanguageAssessment.MELAID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/ConnersParentRatingScaleReport', methods=['GET','POST'])
async def ConnersParentRatingScaleReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ConnersParentRatingScaleReport,
                                session.query(Model.models.Application.M_ConnersParentRatingScale.MCPRID.label('ID'),
                                            Model.models.Application.M_ConnersParentRatingScale.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Scores.label('Scores'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Tscores.label('Tscores'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Range.label('Range'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MCPR_IsActive=1,MCPR_IsDeleted=0
                                ).order_by(Model.models.Application.M_ConnersParentRatingScale.MCPRID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SpecialEdassessmenttwoyearsReport', methods=['GET','POST'])
async def SpecialEdassessmenttwoyearsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmenttwoyearsReport,
                                session.query(Model.models.Application.M_SpecialEdassessmenttwoyears.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Respondstoname.label('Respondstoname'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Makeseyecontact.label('Makeseyecontact'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Respondstolightandsoundtoys.label('Respondstolightandsoundtoys'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmoveeyesupanddown.label('canmoveeyesupanddown'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmoveeyesleftandright.label('canmoveeyesleftandright'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_repeatswords.label('repeatswords'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsidentificationofnumber.label('knowsidentificationofnumber'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canrollpoundandsqueezeclay.label('canrollpoundandsqueezeclay'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyMom.label('vocabularyMom'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyDad.label('vocabularyDad'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Vocabularydog.label('Vocabularydog'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycat.label('vocabularycat'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularytree.label('vocabularytree'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularytable.label('vocabularytable'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularychair.label('vocabularychair'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycow.label('vocabularycow'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycrayons.label('vocabularycrayons'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybus.label('vocabularybus'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycar.label('vocabularycar'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybook.label('vocabularybook'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyapple.label('vocabularyapple'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybanana.label('vocabularybanana'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybottle.label('vocabularybottle'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Candostacking.label('Candostacking'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmaketower.label('canmaketower'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_respondstobubbles.label('respondstobubbles'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Identifieshappyandsad.label('Identifieshappyandsad'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Knowsshapes.label('Knowsshapes'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowscolors.label('knowscolors'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsanimals.label('knowsanimals'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsvehicles.label('knowsvehicles'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsbodyparts.label('knowsbodyparts'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsidentificationofalphabets.label('knowsidentificationofalphabets'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsmoreorless.label('knowsmoreorless'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsbigandsmall.label('knowsbigandsmall'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsnearandfar.label('knowsnearandfar'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifhisorher.label('canidentifhisorher'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifybag.label('canidentifybag'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifyshoes.label('canidentifyshoes'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifybottle.label('canidentifybottle'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialEdassessmenttwoyears.MSATWID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SpecialEdassessmentthreeyearsReport', methods=['GET','POST'])
async def SpecialEdassessmentthreeyearsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentthreeyearsReport,
                                session.query(Model.models.Application.M_SpecialEdassessmentThreeyears.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_respondstoname.label('respondstoname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_makeseyecontact.label('makeseyecontact'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canmoveeyesupanddown.label('canmoveeyesupanddown'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canmoveeyesleftandright.label('canmoveeyesleftandright'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerfullname.label('cananswerfullname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularybodyparts.label('vocabularybodyparts'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfollowstepsinstruction.label('canfollowstepsinstruction'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerold.label('cananswerold'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerwhatsyourmothersname.label('cananswerwhatsyourmothersname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerwhichisyoufavoritecolour.label('cananswerwhichisyoufavoritecolour'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularyshapescircle.label('vocabularyshapescircle'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_Vocabularyfruits.label('Vocabularyfruits'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfollowstepinstruction.label('canfollowstepinstruction'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerseeinsky.label('cangiveanswerseeinsky'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerswiminwater.label('cangiveanswerswiminwater'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerseeontree.label('cangiveanswerseeontree'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_knowsidentificationofalphabets.label('knowsidentificationofalphabets'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_knowsidentificationofnumbers.label('knowsidentificationofnumbers'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_Canholdapencilcrayon.label('Canholdapencilcrayon'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canscribble.label('canscribble'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cancoloringivenshape.label('cancoloringivenshape'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cantearandpaste.label('cantearandpaste'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionshappy.label('canidentifyemotionshappy'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionssad.label('canidentifyemotionssad'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionsangry.label('canidentifyemotionsangry'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionsupset.label('canidentifyemotionsupset'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialEdassessmentThreeyears.MSATWID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SpecialEdassessmentthreefouryearsReport', methods=['GET','POST'])
async def SpecialEdassessmentthreefouryearsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentthreefouryearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_doesrespondtonamecall.label('doesrespondtonamecall'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_doesmakeseyecontact.label('doesmakeseyecontact'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_initiatesinteractiontoward.label('initiatesinteractiontoward'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_understandinstructionslikestand.label('understandinstructionslikestand'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_getthatputthere.label('getthatputthere'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_givemegetthis.label('givemegetthis'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_runwalkjump.label('runwalkjump'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_lookdownup.label('lookdownup'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cananswerwhatis.label('cananswerwhatis'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cananswerfavoritecolour.label('cananswerfavoritecolour'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularyshapes.label('vocabularyshapes'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularyfruits.label('vocabularyfruits'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularybodyparts.label('vocabularybodyparts'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_Canunderstandpositions.label('Canunderstandpositions'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canunderstandstories.label('canunderstandstories'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canWhatquestions.label('canWhatquestions'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canidentifybasicobjects.label('canidentifybasicobjects'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canholdacrayonpencil.label('canholdacrayonpencil'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canmaketower.label('canmaketower'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canimitate.label('canimitate'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canplaydoughballs.label('canplaydoughballs'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canheshethrow.label('canheshethrow'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canrecognisealphabet.label('canrecognisealphabet'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_Canrecognisenumerals.label('Canrecognisenumerals'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cancolourgivenshape.label('cancolourgivenshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATWID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SpecialEdassessmentfouryearsReport', methods=['GET','POST'])
async def SpecialEdassessmentfouryearsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentfouryearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentfourYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_respondnamecall.label('respondnamecall'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_makeseyecontact.label('makeseyecontact'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_interactiontowardothers.label('interactiontowardothers'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cananswerwhatname.label('cananswerwhatname'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_answerfavoritecolour.label('answerfavoritecolour'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularyshapes.label('vocabularyshapes'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularybody.label('vocabularybody'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_Vocabularyfruits.label('Vocabularyfruits'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canunderstandpositions.label('canunderstandpositions'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canunderstandstories.label('canunderstandstories'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_replyWhatquestions.label('replyWhatquestions'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_identifybasicobjects.label('identifybasicobjects'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_holdcrayonpencil.label('holdcrayonpencil'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canimitate.label('canimitate'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_doughmakeballs.label('doughmakeballs'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canthrow.label('canthrow'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_recognisealphabets.label('recognisealphabets'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_recognisenumerals.label('recognisenumerals'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cancolourshape.label('cancolourshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentfourYrs.MSATWID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

################### Report extended ###################################


@Report_Blueprint.route('/SpecialEdassessmentsevenyearsReport', methods=['GET','POST'])
async def SpecialEdassessmentsevenyearsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentsevenyearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentSevenYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_putneedsminimalassistance.label('putneedsminimalassistance'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_eathandsonly.label('eathandsonly'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_fixasandwich.label('fixasandwich'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_givefirstlastname.label('givefirstlastname'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_cangiveaddress.label('cangiveaddress'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_awareofemotions.label('awareofemotions'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_canzipper.label('canzipper'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_independentlyassistanct.label('independentlyassistanct'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_asksmeaningfulquestions.label('asksmeaningfulquestions'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_tellsstorieswords.label('tellsstorieswords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_Doestellage.label('Doestellage'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_canobeysimplecommands.label('canobeysimplecommands'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_readsimplewords.label('readsimplewords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_writesimplewords.label('writesimplewords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_namethingsaround.label('namethingsaround'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_alternatesfeetupdownstairs.label('alternatesfeetupdownstairs'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_pedaltricycle.label('pedaltricycle'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_catchandthrowball.label('catchandthrowball'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_towersmallblocks.label('towersmallblocks'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_doughmakeballs.label('doughmakeballs'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_tieshoes.label('tieshoes'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_holdpencilproperly.label('holdpencilproperly'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_drawsanyshape.label('drawsanyshape'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_usescissorscutshape.label('usescissorscutshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentSevenYrs.MSATWID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/getFollowUpDate', methods=['GET','POST'])
async def getFollowUpDate():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= session.query(Model.models.Application.M_PatientReview.MPDID.label('ID'),
                                            Model.models.Application.M_PatientReview.M_AppointmentID,
                                            Model.models.Application.M_PatientReview.MPR_FollowDate,
                                            sqlalchemy.func.date_format(Model.models.Application.M_PatientReview.MPR_FollowDate,'%d-%b-%Y').label('Date')
                                            ).filter_by(M_AppointmentID=AID,MPR_IsActive=1,MPR_IsDeleted=0
                                            ).order_by(Model.models.Application.M_PatientReview.MPDID.desc()).all()
                    if(len(queryresult)>0):
                        return jsonify(result={'Follow Date':queryresult[0].Date})
                    else:
                        return jsonify(result={'Follow Date':''})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/ProvisionalDiagnosisReport', methods=['POST','GET'])
async def ProvisionalDiagnosisReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request_json = request.get_json()
            AID = request_json.get('AID')
            queryResult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.ProvisionalDiagnosisReport,
                        session.query(Model.models.Application.M_ProvisionalDiagnosis.MPD_ProvisionalDiagnosis.label('ProvisionalDiagnosis'),
                                    Model.models.Application.M_ProvisionalDiagnosis.M_AppointmentID.label('AppointmentId'),
                                    Model.models.Application.M_ProvisionalDiagnosis.MPD_ICDCode.label('ICDCode'),
                                    Model.models.Application.M_ProvisionalDiagnosis.MPD_ICDDescription.label('ICDDescription'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_ProvisionalDiagnosis.MPD_AddDate,'%d-%b-%Y').label('Date'),
                                    ).filter_by(MPD_IsActive=1,MPD_IsDeleted=0,M_AppointmentID=AID,MPD_ShowDtl=1
                                    ).all()
                                )
            session.commit()

            return jsonify(result=queryResult)
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SessionNotesReport', methods=['POST','GET'])
async def SessionNotesReport():
    session=Session()
    try:
        if(request.method == "POST"):
            
            request_json = request.get_json()
            AID = request_json.get('AID')
            StartedDtl = session.query(Model.models.Application.T_Details.TD_Name.label('StartedDl'),
                                          Model.models.Application.T_Details.TDID.label('IDs')).subquery()
            todayfeelDtl = session.query(Model.models.Application.T_Details.TD_Name.label('todayfeelDl'),
                                          Model.models.Application.T_Details.TDID.label('IDs')).subquery()
            queryResult= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.SessionNotesReport,
                        session.query(Model.models.Application.M_SessionNotes.MSN_started.label('Staed'),
                        Model.models.Application.M_SessionNotes.M_AppointmentID.label('AppointmentId'),
                        StartedDtl.c.StartedDl.label('Started'),
                        todayfeelDtl.c.todayfeelDl.label('todayfeel'),
                        
                                    Model.models.Application.M_SessionNotes.MSN_todayfeeling.label('todaeel'),
                                    Model.models.Application.M_SessionNotes.MSN_dotoday.label('dotod'),
                                    Model.models.Application.T_Details.TD_Name.label('dotoday'),
                                    Model.models.Application.M_SessionNotes.MSN_Notes.label('Notes'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_SessionNotes.MSN_AddDate,'%d-%b-%Y').label('Date'),
                                    ).filter_by(MSN_IsActive=1,MSN_IsDeleted=0,M_AppointmentID=AID
                                    ).join(Model.models.Application.T_Details, Model.models.Application.T_Details.TDID==Model.models.Application.M_SessionNotes.MSN_dotoday       
                                    ).outerjoin(StartedDtl, StartedDtl.c.IDs==Model.models.Application.M_SessionNotes.MSN_todayfeeling
                                    ).outerjoin(todayfeelDtl, todayfeelDtl.c.IDs==Model.models.Application.M_SessionNotes.MSN_started
                                    ).all()
                                )
            session.commit()

            return jsonify(result=queryResult)
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/VisitReasonReport', methods=['GET','POST'])
async def VisitReasonReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.VisitReasonReport,
                                session.query(Model.models.Application.M_ReasonForVisit.MRVID.label('ID'),
                                            Model.models.Application.M_ReasonForVisit.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ReasonForVisit.MRV_PresentConcerns.label('Present Concerns'),
                                            Model.models.Application.M_ReasonForVisit.MRV_InformedBy.label('Informed By'),
                                            Model.models.Application.M_ReasonForVisit.MRV_AgeWhenNoticed.label('Noticed Age'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRV_IsActive=1,MRV_IsDeleted=0
                                ).order_by(Model.models.Application.M_ReasonForVisit.MRVID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PastHistoryReport', methods=['GET','POST'])
async def PastHistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PastHistoryReport,
                                session.query(Model.models.Application.M_PastHistory.MPHID.label('ID'),
                                            Model.models.Application.M_PastHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PastHistory.MPH_PastMedications.label('Past Medications')
                                            
                                                ).filter_by(M_AppointmentID=AID,MPH_IsActive=1,MPH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PastHistory.MPHID.desc()).all())

                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PrenatalHistoryReport', methods=['GET','POST'])
async def PrenatalHistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PrenatalHistoryReport,
                                session.query(Model.models.Application.M_PrenatalHistory.MPHID.label('ID'),
                                            Model.models.Application.M_PrenatalHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PrenatalHistory.MPH_MotheraAgeAtConception.label('Mother Conception'),
                                            Model.models.Application.M_PrenatalHistory.MPH_MotherHealthAtPregnancy.label('Mother Pregnancy'),
                                            Model.models.Application.M_PrenatalHistory.MPH_HistoryofAbortions.label('History Abortions'),
                                            Model.models.Application.M_PrenatalHistory.MPH_GestationalDiabetes.label('Gestational Diabetes'),
                                            Model.models.Application.M_PrenatalHistory.MPH_NeurologicalDisorder.label('Neurological Disorder'),
                                            Model.models.Application.M_PrenatalHistory.MPH_PhysicalEmotionalTrauma.label('Physical Emotional'),
                                            Model.models.Application.M_PrenatalHistory.MPH_RhInompatibility.label('Inompatibility'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Jaundice.label('Jaundice'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Seizures.label('Seizures'),
                                            Model.models.Application.M_PrenatalHistory.MPH_TraumaInjury.label('TraumaInjury'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Bleedinginlatepregnancy.label('Bleeding pregnancy'),
                                            Model.models.Application.M_PrenatalHistory.MPH_AdequateNutrition.label('Adequate Nutrition'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Infections.label('Infections'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Smoking.label('Smoking'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPH_IsActive=1,MPH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PrenatalHistory.MPHID.desc()).all())

                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PatientBirthHistoryReport', methods=['GET','POST'])
async def PatientBirthHistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PatientBirthHistoryReport,
                                session.query(Model.models.Application.M_PatientBirthHistory.MPBHID.label('ID'),
                                            Model.models.Application.M_PatientBirthHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_MotherHealth.label('Mother Health'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_DeliveryType.label('Delivery Type'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_typeofdelivery.label('Type of Delivery'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_DeliveryLocationh.label('Delivery Location'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_MultiplePregnancies.label('Multiple Pregnancies'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ComplicationDuringPregnancy.label('Complication Pregnancy'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ChildBirth.label('Child Birth'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ChildBirthWeek.label('Child Birth Week'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_BirthWeight.label('Birth Weight'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_BirthCry.label('Birth Cry'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_NeonatalConditionint.label('Neonatal Condition'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_SpecialCareAny.label('Special CareAny'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_AnyMedicalEvents.label('Any Medical Events'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_Congenital.label('Congenital'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPBH_IsActive=1,MPBH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PatientBirthHistory.MPBHID.desc()).all())

                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/DevelopmentalHistoryReport', methods=['GET','POST'])
async def DevelopmentalHistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DevelopmentalHistoryReport,
                                session.query(Model.models.Application.M_DevelopmentalHistory.MDHID.label('ID'),
                                            Model.models.Application.M_DevelopmentalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_HoldUpHeadAge.label('HoldUp HeadAge'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_Rolloverage.label('Rollover age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_SitAge.label('Sit Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_StandAloneAge.label('Stand Alone Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_WalkAge.label('Walk Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_TalkAge.label('Talk Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_ToiletTrainAge.label('Toilet Train Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_FeedAge.label('Feed Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_DresshimAge.label('Dresshim Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MDH_IsActive=1,MDH_IsDeleted=0
                                ).order_by(Model.models.Application.M_DevelopmentalHistory.MDHID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/SpeechDevelopmentHistoryReport', methods=['GET','POST'])
async def SpeechDevelopmentHistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpeechDevelopmentHistoryReport,
                                session.query(Model.models.Application.M_SpeechDevelopmentalHistory.MSDHID.label('ID'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Vocalization.label('Vocalization'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Babbling.label('Babbling'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_FirstWord.label('First Word'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Phrases.label('Phrases'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_SimpleSentences.label('Simple Sentences'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSDH_IsActive=1,MSDH_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpeechDevelopmentalHistory.MSDHID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/socialhistoryReport', methods=['GET','POST'])
async def socialhistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.socialhistoryReport,
                                session.query(Model.models.Application.M_SocialHistory.MSHID.label('ID'),
                                            Model.models.Application.M_SocialHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_SocialHistory.MSH_Aggressive.label('Social History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSH_IsActive=1,MSH_IsDeleted=0
                                ).order_by(Model.models.Application.M_SocialHistory.MSHID.desc()).all())

                    session.commit()


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/medicalhistoryReport', methods=['GET','POST'])
async def medicalhistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.medicalhistoryReport,
                                session.query(Model.models.Application.M_MedicalHistory.MSHID.label('ID'),
                                            Model.models.Application.M_MedicalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_MedicalHistory.MMH_observations.label('Medical History'),

                                                ).filter_by(M_AppointmentID=AID,MMH_IsActive=1,MMH_IsDeleted=0
                                ).order_by(Model.models.Application.M_MedicalHistory.MSHID.desc()).all())

                    session.commit()


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/familyhistoryReport', methods=['GET','POST'])
async def familyhistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.familyhistoryReport,
                                session.query(Model.models.Application.M_FamilyHistory.MFHID.label('ID'),
                                            Model.models.Application.M_FamilyHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_FamilyHistory.MFH_Familytype.label('Family type'),
                                            Model.models.Application.M_FamilyHistory.MFH_Consanguinity.label('Consanguinity'),
                                            Model.models.Application.M_FamilyHistory.MFH_Observations.label('Family History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFH_IsActive=1,MFH_IsDeleted=0
                                ).order_by(Model.models.Application.M_FamilyHistory.MFHID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/educationhistoryReport', methods=['GET','POST'])
async def educationhistoryReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.educationhistoryReport,
                                session.query(Model.models.Application.M_EducationHistory.MEHID.label('ID'),
                                            Model.models.Application.M_EducationHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_EducationHistory.MEH_CommunicationMode.label('Education History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MEH_IsActive=1,MEH_IsDeleted=0
                                ).order_by(Model.models.Application.M_EducationHistory.MEHID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/GeneralExamReport', methods=['GET','POST'])
async def GeneralExamReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.GeneralExamReport,
                                session.query(Model.models.Application.M_GeneralExamForm.MGEFID.label('ID'),
                                            Model.models.Application.M_GeneralExamForm.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Height.label('Height'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Weight.label('Weight'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_HeadCircumference.label('Head Circumference'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Observations.label('Observations'),

                                                ).filter_by(M_AppointmentID=AID,MGEF_IsActive=1,MGEF_IsDeleted=0
                                ).order_by(Model.models.Application.M_GeneralExamForm.MGEFID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()



@Report_Blueprint.route('/VitalsExamReport', methods=['GET','POST'])
async def VitalsExamReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.VitalsExamReport,
                                session.query(Model.models.Application.M_VitalsExamForm.MVEFID.label('ID'),
                                            Model.models.Application.M_VitalsExamForm.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_BloodPressure.label('Blood Pressure'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_PulseRate.label('Pulse Rate'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_RespiratoryRate.label('Respiratory Rate'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_Temperator.label('Temperator'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MVEF_IsActive=1,MVEF_IsDeleted=0
                                ).order_by(Model.models.Application.M_VitalsExamForm.MVEFID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/SystemicExamReport', methods=['GET','POST'])
async def SystemicExamReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SystemicExamReport,
                                session.query(Model.models.Application.M_SystemicExam.MSEID.label('ID'),
                                            Model.models.Application.M_SystemicExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SystemicExam.MSE_Observations.label('Observations'),
                                                ).filter_by(M_AppointmentID=AID,MSE_IsActive=1,MSE_IsDeleted=0
                                ).order_by(Model.models.Application.M_SystemicExam.MSEID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/STOroperipheralExam', methods=['GET','POST'])
async def STOroperipheralExam():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STOroperipheralExam,
                                session.query(Model.models.Application.M_STOroperipheralExam.MSPEID.label('ID'),
                                            Model.models.Application.M_STOroperipheralExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_LipsAppearance.label('Lips Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_LipsMovements.label('Lips Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TongueAppearance.label('Tongue Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TongueMovements.label('Tongue Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TeethAppearance.label('Teeth Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TeethMovements.label('Teeth Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_HardPalateAppearance.label('Hard Palate Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_SoftPalateAppearance.label('Soft Palate Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_SoftPalateMovements.label('Soft Palate Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_UvulaAppearance.label('Uvula Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_UvulaMovements.label('Uvula Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_MandibleAppearance.label('Mandible Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_MandibleMovements.label('Mandible Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Drooling.label('Drooling'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Blowing.label('Blowing'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Biting.label('Biting'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Sucking.label('Sucking'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Swallowing.label('Swallowing'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSPE_IsActive=1,MSPE_IsDeleted=0
                                ).order_by(Model.models.Application.M_STOroperipheralExam.MSPEID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/STArticulationSpeechIntelligibilityReport', methods=['GET','POST'])
async def STArticulationSpeechIntelligibilityReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STArticulationSpeechIntelligibilityReport,
                                session.query(Model.models.Application.M_STArticulationSpeechIntelligibility.MSSIID.label('ID'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Noonecan.label('Noonecan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_memberscan.label('memberscan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Strangerscan.label('Strangerscan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSSI_IsActive=1,MSSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_STArticulationSpeechIntelligibility.MSSIID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/STArticulationVoiceReport', methods=['GET','POST'])
async def STArticulationVoiceReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STArticulationVoiceReport,
                                session.query(Model.models.Application.M_STArticulationVoice.MSAVID.label('ID'),
                                            Model.models.Application.M_STArticulationVoice.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Pitch.label('Pitch'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Loudness.label('Loudness'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Quality.label('Quality'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSAV_IsActive=1,MSAV_IsDeleted=0
                                ).order_by(Model.models.Application.M_STArticulationVoice.MSAVID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/CognitivePrerequitesReport', methods=['GET','POST'])
async def CognitivePrerequitesReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.CognitivePrerequitesReport,
                                session.query(Model.models.Application.M_CognitivePrerequites.MCPID.label('ID'),
                                            Model.models.Application.M_CognitivePrerequites.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Imitation.label('Imitation'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Objectpermanence.label('Objectpermanence'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Timeconcept.label('Timeconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Colourconcept.label('Colourconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Moneyconcept.label('Moneyconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Sequencing.label('Sequencing'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Matching.label('Matching'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Meanendrelationship.label('Meanendrelationship'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Observations.label('Observations'),

                                                ).filter_by(M_AppointmentID=AID,MCP_IsActive=1,MCP_IsDeleted=0
                                ).order_by(Model.models.Application.M_CognitivePrerequites.MCPID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/STVerbalCommunication', methods=['GET','POST'])
async def STVerbalCommunication():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STVerbalCommunication,
                                session.query(Model.models.Application.M_STVerbalCommunication.MVCID.label('ID'),
                                            Model.models.Application.M_STVerbalCommunication.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Expression.label('Expression'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Comprehension.label('Comprehension'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MVC_IsActive=1,MVC_IsDeleted=0
                                ).order_by(Model.models.Application.M_STVerbalCommunication.MVCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/STNonVerbalCommunicationReport', methods=['GET','POST'])
async def STNonVerbalCommunicationReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STNonVerbalCommunicationReport,
                                session.query(Model.models.Application.M_STNonVerbalCommunication.MNVCID.label('ID'),
                                            Model.models.Application.M_STNonVerbalCommunication.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Expression.label('Expression'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Comprehension.label('Comprehension'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNVC_IsActive=1,MNVC_IsDeleted=0
                                ).order_by(Model.models.Application.M_STNonVerbalCommunication.MNVCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/OTHandFunctionsReport', methods=['GET','POST'])
async def OTHandFunctionsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTHandFunctionsReport,
                                session.query(Model.models.Application.M_OTHandFunctions.MHFID.label('ID'),
                                            Model.models.Application.M_OTHandFunctions.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTHandFunctions.MHF_HandDominance.label('Hand Dominance'),
                                            Model.models.Application.M_OTHandFunctions.MHF_HandPreference.label('Hand Preference'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachForward.label('Reach Forward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachBackward.label('Reach Backward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachLateral.label('Reach Lateral'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachDownward.label('Reach Downward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspUlnarPalmar.label('Grasp UlnarPalmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspPalmar.label('Grasp Palmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspRadialPalmar.label('Grasp RadialPalmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspRadialDigital.label('Grasp RadialDigital'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspInferiorPincer.label('Grasp InferiorPincer'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachUpward.label('Reach Upward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspNeatPincer.label('Grasp NeatPincer'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspPalmarsupinate.label('Grasp Palmarsupinate'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspDigitalpronate.label('Grasp Digitalpronate'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspStatictripod.label('Grasp Statictripod'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspDynamictripod.label('Grasp Dynamictripod'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionPadtoPad.label('Prehension PadtoPad'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionTiptoTip.label('Prehension TiptoTip'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionPadtoSide.label('Prehension PadtoSide'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MHF_IsActive=1,MHF_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTHandFunctions.MHFID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/OTNonEquilibriumCoordinationReport', methods=['GET','POST'])
async def OTNonEquilibriumCoordinationReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewOTNonEquilibriumCoordinationReport,
                                session.query(Model.models.Application.M_NonEquilibrium.MNEID.label('ID'),
                                            Model.models.Application.M_NonEquilibrium.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertonose.label('Fingertonose'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertotherapistfinger.label('Fingertotherapistfinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertofinger.label('Fingertofinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Alternatnosefinger.label('Alternatnosefinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingeropposition.label('Fingeropposition'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Massgrasp.label('Massgrasp'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Pronationsupination.label('Pronationsupination'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Reboundtest.label('Reboundtest'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Tappinghand.label('Tappinghand'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Tappingfeet.label('Tappingfeet'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Pointingandpastpointing.label('Pointingandpastpointing'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Alternateheeltokneeheeltoe.label('Alternateheeltokneeheeltoe'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Toetoexaminersfinger.label('Toetoexaminersfinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Heeltoshin.label('Heeltoshin'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Drawingacircle.label('Drawingacircle'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fixationorpositionholding.label('Fixationorpositionholding'),

                                                ).filter_by(M_AppointmentID=AID,MNE_IsActive=1,MNE_IsDeleted=0
                                ).order_by(Model.models.Application.M_NonEquilibrium.MNEID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/OTEquilibriumCoordinationReport', methods=['GET','POST'])
async def OTEquilibriumCoordinationReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTEquilibriumCoordinationReport,
                                session.query(Model.models.Application.M_Equilibrium.MNEID.label('ID'),
                                            Model.models.Application.M_Equilibrium.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingwithnormalbaseofsupport.label('Standingwithnormalbaseofsupport'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingwithnarrowbaseofsupport.label('Standingwithnarrowbaseofsupport'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingintandemposition.label('Standingintandemposition'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingononefeet.label('Standingononefeet'),
                                            Model.models.Application.M_Equilibrium.MNE_Perturbation.label('Perturbation'),
                                            Model.models.Application.M_Equilibrium.MNE_Standinginfunctionalreach.label('Standinginfunctionalreach'),
                                            Model.models.Application.M_Equilibrium.MNE_Standinglateralflexionofthetrunktoeachside.label('Standinglateralflexionofthetrunktoeachside'),
                                            Model.models.Application.M_Equilibrium.MNE_Tandemwalking.label('Tandemwalking'),
                                            Model.models.Application.M_Equilibrium.MNE_WalkingInastraightline.label('WalkingInastraightline'),
                                            Model.models.Application.M_Equilibrium.MNE_Walksidewaysbackwards.label('Walksidewaysbackwards'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkinhorizontalvertical.label('Walkinhorizontalvertical'),
                                            Model.models.Application.M_Equilibrium.MNE_Marchinplace.label('Marchinplace'),
                                            Model.models.Application.M_Equilibrium.MNE_Startstopabruptly.label('Startstopabruptly'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkandpivotincommand.label('Walkandpivotincommand'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkincircle.label('Walkincircle'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkonheelsandtoes.label('Walkonheelsandtoes'),
                                            Model.models.Application.M_Equilibrium.MNE_Turnsoncommand.label('Turnsoncommand'),
                                            Model.models.Application.M_Equilibrium.MNE_Stepoveraroundobstacles.label('Stepoveraroundobstacles'),
                                            Model.models.Application.M_Equilibrium.MNE_Stairclimbingwithhandrails.label('Stairclimbingwithhandrails'),
                                            Model.models.Application.M_Equilibrium.MNE_Jumpingjacks.label('Jumpingjacks'),
                                            Model.models.Application.M_Equilibrium.MNE_Sittingontherapybal.label('Sittingontherapybal'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNE_IsActive=1,MNE_IsDeleted=0
                                ).order_by(Model.models.Application.M_Equilibrium.MNEID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/OTCognitionAndPerceptionReport', methods=['GET','POST'])
async def OTCognitionAndPerceptionReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTCognitionAndPerceptionReport,
                                session.query(Model.models.Application.M_OTCognition.MOCID.label('ID'),
                                            Model.models.Application.M_OTCognition.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTCognition.MOC_Praxis.label('Praxis'),
                                            Model.models.Application.M_OTCognition.MOC_Rightleftdiscrimination.label('Rightleftdiscrimination'),
                                            Model.models.Application.M_OTCognition.MOC_Fingerindentification.label('Fingerindentification'),
                                            Model.models.Application.M_OTCognition.MOC_Orientationtoperson.label('Orientationtoperson'),
                                            Model.models.Application.M_OTCognition.MOC_Orientationtoplace.label('Orientationtoplace'),
                                            Model.models.Application.M_OTCognition.MOC_Conceputalseriescompletion.label('Conceputalseriescompletion'),
                                            Model.models.Application.M_OTCognition.MOC_Selectiveattention.label('Selectiveattention'),
                                            Model.models.Application.M_OTCognition.MOC_Focusedattention.label('Focusedattention'),
                                            Model.models.Application.M_OTCognition.MOC_Spatialperception.label('Spatialperception'),
                                            Model.models.Application.M_OTCognition.MOC_Visualmemory.label('Visualmemory'),
                                            Model.models.Application.M_OTCognition.MOC_Verbalmemory.label('Verbalmemory'),
                                            Model.models.Application.M_OTCognition.MOC_Identificationofobjects.label('Identificationofobjects'),
                                            Model.models.Application.M_OTCognition.MOC_Proverbinterpretation.label('Proverbinterpretation'),
                                            Model.models.Application.M_OTCognition.MOC_Randomlettertest.label('Randomlettertest'),
                                            Model.models.Application.M_OTCognition.MOC_Overlappingfigures.label('Overlappingfigures'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MOC_IsActive=1,MOC_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTCognition.MOCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/OTSensoryExamReport', methods=['GET','POST'])
async def OTSensoryExamReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTSensoryExamReport,
                                session.query(Model.models.Application.M_OTSensoryExam.MSEID.label('ID'),
                                            Model.models.Application.M_OTSensoryExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Visualtracking.label('Visual tracking'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Choreiformmovements.label('Choreiform movements'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Tremor.label('Tremor'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Exaggeratedassociated.label('Exaggerated associated'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Graphesthesis.label('Graphesthesis'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Stereognosis.label('Stereognosis'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Weightbearinghands.label('Weight bearing hands'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Proneextensionpattern.label('Prone extension pattern'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSE_IsActive=1,MSE_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTSensoryExam.MSEID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/OTSensoryProfileReport', methods=['GET','POST'])
async def OTSensoryProfileReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTSensoryProfileReport,
                                session.query(Model.models.Application.M_OTSensoryProfile.MSPID.label('ID'),
                                            Model.models.Application.M_OTSensoryProfile.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTSensoryProfile.MSP_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSP_IsActive=1,MSP_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTSensoryProfile.MSPID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/AddtionalinfoReport', methods=['GET','POST'])
async def AddtionalinfoReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.AddtionalinfoReport,
                                session.query(Model.models.Application.M_Addtionalinfo.MAIID.label('ID'),
                                            Model.models.Application.M_Addtionalinfo.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_Addtionalinfo.MAI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MAI_IsActive=1,MAI_IsDeleted=0
                                ).order_by(Model.models.Application.M_Addtionalinfo.MAIID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTFunctionalAbilitiesReport', methods=['GET','POST'])
async def PTFunctionalAbilitiesReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTFunctionalAbilitiesReport,
                                session.query(Model.models.Application.M_PTFunctionalAbilities.MFAID.label('ID'),
                                            Model.models.Application.M_PTFunctionalAbilities.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_GrossMotor.label('Gross Motor'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_FineMotor.label('Fine Motor'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_CommunicationSpeech.label('Communication Speech'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_Feeding.label('Feeding'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_Playskills.label('Playskills'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_ADL.label('ADL'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFA_IsActive=1,MFA_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTFunctionalAbilities.MFAID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTFunctionalLimitationsReport', methods=['GET','POST'])
async def PTFunctionalLimitationsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTFunctionalLimitationsReport,
                                session.query(Model.models.Application.M_PTFunctionalLimitations.MFLID.label('ID'),
                                            Model.models.Application.M_PTFunctionalLimitations.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_GrossMotor.label('Gross Motor'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_FineMotor.label('Fine Motor'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_CommunicationSpeech.label('Communication Speech'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_Feeding.label('Feeding'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_Playskills.label('Playskills'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_ADL.label('ADL'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFL_IsActive=1,MFL_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTFunctionalLimitations.MFLID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTPosturalSystemAlignmentReport', methods=['GET','POST'])
async def PTPosturalSystemAlignmentReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemAlignmentReport,
                                session.query(Model.models.Application.M_PosturalSystemAlignments.MPSAID.label('ID'),
                                            Model.models.Application.M_PosturalSystemAlignments.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HeadNeck.label('Head Neck'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShoulderScapular.label('Shoulder Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShoulderandScapular.label('Shoulder and Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShouldernScapular.label('Shouldern Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_RibcageandChest.label('Ribcage and Chest'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Trunk.label('Trunk'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Trunks.label('Trunks'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_PelvicComplexRight.label('Pelvic Complex Right'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_PelvicComplexLeft.label('Pelvic Complex Left'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointAbduction.label('Hipjoint Abduction'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointAdduction.label('Hipjoint Adduction'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointRotation.label('Hipjoint Rotation'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Symmetrical.label('Symmetrical'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Assymetrical.label('Assymetrical'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSA_IsActive=1,MPSA_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemAlignments.MPSAID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTPosturalSystemBOSReport', methods=['GET','POST'])
async def PTPosturalSystemBOSReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemBOSReport,
                                session.query(Model.models.Application.M_PosturalSystemBOS.MPSBID.label('ID'),
                                            Model.models.Application.M_PosturalSystemBOS.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemBOS.MPSB_BaseofSupport.label('Base of Support'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSB_IsActive=1,MPSB_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemBOS.MPSBID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PTPosturalSystemCOMReport', methods=['GET','POST'])
async def PTPosturalSystemCOMReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemCOMReport,
                                session.query(Model.models.Application.M_PosturalSystemCOM.MPSCID.label('ID'),
                                            Model.models.Application.M_PosturalSystemCOM.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_CenterofMass.label('Center of Mass'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_Withinsupport.label('Within support'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_Strategiesposture.label('Strategies posture'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSC_IsActive=1,MPSC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemCOM.MPSCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTAnticipatoryControlReport', methods=['GET','POST'])
async def PTAnticipatoryControlReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTAnticipatoryControlReport,
                                session.query(Model.models.Application.M_PTAnticipatoryControl.MACID.label('ID'),
                                            Model.models.Application.M_PTAnticipatoryControl.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTAnticipatoryControl.MAC_Canchildanti.label('Canchildanti'),
                                            Model.models.Application.M_PTAnticipatoryControl.MAC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MAC_IsActive=1,MAC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTAnticipatoryControl.MACID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTPosturalCounterbalanceReport', methods=['GET','POST'])
async def PTPosturalCounterbalanceReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalCounterbalanceReport,
                                session.query(Model.models.Application.M_PTPosturalCounterbalance.MPCID.label('ID'),
                                            Model.models.Application.M_PTPosturalCounterbalance.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTPosturalCounterbalance.MPC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPC_IsActive=1,MPC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTPosturalCounterbalance.MPCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTPosturalSystemImpairmentsReport', methods=['GET','POST'])
async def PTPosturalSystemImpairmentsReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewPTPosturalSystemImpairments,
                                session.query(Model.models.Application.M_PosturalSystemImpairments.MPSIID.label('ID'),
                                            Model.models.Application.M_PosturalSystemImpairments.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_MuscleArchitecture.label('Muscle Architecture'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Anycallosities.label('Anycallosities'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Anyotherspecificposture.label('Anyother specific posture'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSI_IsActive=1,MPSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemImpairments.MPSIID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTMovementSystemReport', methods=['GET','POST'])
async def PTMovementSystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementSystemReport,
                                session.query(Model.models.Application.M_PTMovementSystem.MPMSID.label('ID'),
                                            Model.models.Application.M_PTMovementSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Cantheyovercome.label('Canthey overcome'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Howdoesthe.label('How do'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Strategiesused.label('Strategies used'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPMS_IsActive=1,MPMS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementSystem.MPMSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PTMovementStrategiesReport', methods=['GET','POST'])
async def PTMovementStrategiesReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementStrategiesReport,
                                session.query(Model.models.Application.M_PTMovementStrategies.MMSID.label('ID'),
                                            Model.models.Application.M_PTMovementStrategies.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_Childgenerallyperformsactivitie.label('Childgenerallyperformsactivitie'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformLateralweightshifts.label('CanperformLateralweightshifts'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformLateralweightshiftsleft.label('CanperformLateralweightshiftsleft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformDiagonalweightRight.label('CanperformDiagonalweightRight'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformDiagonalweightLeft.label('CanperformDiagonalweightLeft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformneckthoracicspineRight.label('CanperformneckthoracicspineRight'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformneckthoracicspineLeft.label('CanperformneckthoracicspineLeft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowarethedissociationsPelvicfemoral.label('HowarethedissociationsPelvicfemoral'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowaredissociationsInterlimb.label('HowaredissociationsInterlimb'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowthedissociationsScapulohumeral.label('HowthedissociationsScapulohumeral'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowthedissociationsUpperLowerbody.label('HowthedissociationsUpperLowerbody'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MMS_IsActive=1,MMS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementStrategies.MMSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTRangeSpeedofMovementReport', methods=['GET','POST'])
async def PTRangeSpeedofMovementReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTRangeSpeedofMovementReport,
                                session.query(Model.models.Application.M_PTRangeSpeed.MPMSID.label('ID'),
                                            Model.models.Application.M_PTRangeSpeed.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_Rangespeedmovement.label('Range Speed Movement'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_atTrunk.label('at Trunk'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_HowisitatExtremities.label('Extremities'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRS_IsActive=1,MRS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTRangeSpeed.MPMSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PTStabilityMobilityReport', methods=['GET','POST'])
async def PTStabilityMobilityReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTStabilityMobilityReport,
                                session.query(Model.models.Application.M_PTStabilityMobility.MSMID.label('ID'),
                                            Model.models.Application.M_PTStabilityMobility.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTStabilityMobility.MSM_StrategiesforStabilityMobility.label('Mobility Strategies'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSM_IsActive=1,MSM_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTStabilityMobility.MSMID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTMovementSystemImpairmentReport', methods=['GET','POST'])
async def PTMovementSystemImpairmentReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementSystemImpairmentReport,
                                session.query(Model.models.Application.M_PTMovementSystemImpairment.MSIID.label('ID'),
                                            Model.models.Application.M_PTMovementSystemImpairment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Excessivemovementfortasks.label('Excessive movement'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Lackofmovementstaticpostures.label('movement StaticPostures'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_IntegrationofPostureMovement.label('Integration of PostureMovement'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Howdoeschildmaintainbalanceintransitions.label('Balance Transitions'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Accuracyofmovements.label('Accuracy of Movements'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSI_IsActive=1,MSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementSystemImpairment.MSIID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTRegulatorySystemReport', methods=['GET','POST'])
async def PTRegulatorySystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTRegulatorySystemReport,
                                session.query(Model.models.Application.M_PTRegulatorySystem.MRSID.label('ID'),
                                            Model.models.Application.M_PTRegulatorySystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Affect.label('Affect'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Arousal.label('Arousal'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Attention.label('Attention'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Action.label('Action'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRS_IsActive=1,MRS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTRegulatorySystem.MRSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()



@Report_Blueprint.route('/PTNeurometerSystemReport', methods=['GET','POST'])
async def PTNeurometerSystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTNeurometerSystemReport,
                                session.query(Model.models.Application.M_PTNeurometerSystem.MPSBID.label('ID'),
                                            Model.models.Application.M_PTNeurometerSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Initiation.label('Initiation'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Sustenance.label('Sustenance'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Termination.label('Termination'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Controlandgradation.label('Control and Gradation'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionConcentric.label('Contraction Concentric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionIsometric.label('Contraction Isometric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionEccentric.label('Contraction Eccentric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_CoactivationReciprocalinhibition.label('Reciprocal Inhibition'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_MasssynergyIsolatedwork.label('Isolated work'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Dynamicstiffness.label('Dynamic stiffness'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Extraneousmovement.label('Extraneous Movement'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNS_IsActive=1,MNS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTNeurometerSystem.MPSBID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTMusculoskeletalSystemReport', methods=['GET','POST'])
async def PTMusculoskeletalSystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMusculoskeletalSystemReport,
                                session.query(Model.models.Application.M_PTMusculoskeletalSystem.MKSID.label('ID'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Muscleendurance.label('Muscle Endurance'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Skeletalcomments.label('Skeletal Comments'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR1.label('Tardieu ScaleTR1'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR2.label('Tardieu ScaleTR2'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR3.label('Tardieu ScaleTR3'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuscaleHamsR1.label('Tardieu ScaleHamsR1'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuscaleHamsR2.label('Tardieu ScaleHamsR2'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MKS_IsActive=1,MKS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMusculoskeletalSystem.MKSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTSensorySystemReport', methods=['GET','POST'])
async def PTSensorySystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTSensorySystemReport,
                                session.query(Model.models.Application.M_PTSensorySystem.MSSID.label('ID'),
                                            Model.models.Application.M_PTSensorySystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTSensorySystem.MSS_sensorymodulationissues.label('Modulation Issues'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Visualsystem.label('Visual system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Auditorysystem.label('Auditory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_AuditorysystemResponse.label('Auditory system Response'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Vestibularsystem.label('Vestibular system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Somatosensorysystem.label('Somatosensory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Oromotorsystem.label('Oromotor system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Olfactorysystem.label('Olfactory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSS_IsActive=1,MSS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTSensorySystem.MSSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Report_Blueprint.route('/PTCognitiveSystemReport', methods=['GET','POST'])
async def PTCognitiveSystemReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTCognitiveSystemReport,
                                session.query(Model.models.Application.M_PTCognitiveSystem.MCSID.label('ID'),
                                            Model.models.Application.M_PTCognitiveSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Intelligence.label('Intelligence'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Memory.label('Memory'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Adaptability.label('Adaptability'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_MotorPlanning.label('Motor Planning'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MCS_IsActive=1,MCS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTCognitiveSystem.MCSID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/DSMVASDCriteriaReport', methods=['GET','POST'])
async def DSMVASDCriteriaReport():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = 1
                if(data):
                    request1= request.get_json()
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DSMVASDCriteriaReport,
                                session.query(Model.models.Application.M_DSMVASDCriteria.persistentDeficit.label('persistentDeficit'),
                                            Model.models.Application.M_DSMVASDCriteria.persistentDeficitComment.label('persistentDeficitComment'),
                                            Model.models.Application.M_DSMVASDCriteria.restrictedRepetitive.label('restrictedRepetitive'),
                                            Model.models.Application.M_DSMVASDCriteria.restrictedRepetitiveComment.label('restrictedRepetitiveComment'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsMust.label('symptomsMust'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsMustComment.label('symptomsMustComment'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsCause.label('symptomsCause'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsCauseComment.label('symptomsCauseComment'),
                                            Model.models.Application.M_DSMVASDCriteria.theseDisturbances.label('theseDisturbances'),
                                            Model.models.Application.M_DSMVASDCriteria.theseDisturbancesComment.label('theseDisturbancesComment'),
                                            Model.models.Application.M_DSMVASDCriteria.question7.label('question7'),
                                            Model.models.Application.M_DSMVASDCriteria.question7Comment.label('question7Comment'),
                                            Model.models.Application.M_DSMVASDCriteria.MDCID.label('Id')
                                                ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_DSMVASDCriteria.MDCID.desc()).all())


                    session.commit()
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()
@Report_Blueprint.route('/HistoryReport', methods=['GET','POST'])
def HistoryReport():
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
                    AID = request1.get('AID')
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.VisitReasonReport,
                                session.query(Model.models.Application.M_ReasonForVisit.MRVID.label('ID'),
                                            Model.models.Application.M_ReasonForVisit.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ReasonForVisit.MRV_PresentConcerns.label('Present Concerns'),
                                            Model.models.Application.M_ReasonForVisit.MRV_InformedBy.label('Informed By'),
                                            Model.models.Application.M_ReasonForVisit.MRV_AgeWhenNoticed.label('Noticed Age'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRV_IsActive=1,MRV_IsDeleted=0
                                ).order_by(Model.models.Application.M_ReasonForVisit.MRVID.desc()).all())
                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PastHistoryReport,
                                session.query(Model.models.Application.M_PastHistory.MPHID.label('ID'),
                                            Model.models.Application.M_PastHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PastHistory.MPH_PastMedications.label('Past Medications')
                                            
                                                ).filter_by(M_AppointmentID=AID,MPH_IsActive=1,MPH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PastHistory.MPHID.desc()).all())
                    session.commit()
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PrenatalHistoryReport,
                                session.query(Model.models.Application.M_PrenatalHistory.MPHID.label('ID'),
                                            Model.models.Application.M_PrenatalHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PrenatalHistory.MPH_MotheraAgeAtConception.label('Mother Conception'),
                                            Model.models.Application.M_PrenatalHistory.MPH_MotherHealthAtPregnancy.label('Mother Pregnancy'),
                                            Model.models.Application.M_PrenatalHistory.MPH_HistoryofAbortions.label('History Abortions'),
                                            Model.models.Application.M_PrenatalHistory.MPH_GestationalDiabetes.label('Gestational Diabetes'),
                                            Model.models.Application.M_PrenatalHistory.MPH_NeurologicalDisorder.label('Neurological Disorder'),
                                            Model.models.Application.M_PrenatalHistory.MPH_PhysicalEmotionalTrauma.label('Physical Emotional'),
                                            Model.models.Application.M_PrenatalHistory.MPH_RhInompatibility.label('Inompatibility'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Jaundice.label('Jaundice'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Seizures.label('Seizures'),
                                            Model.models.Application.M_PrenatalHistory.MPH_TraumaInjury.label('TraumaInjury'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Bleedinginlatepregnancy.label('Bleeding pregnancy'),
                                            Model.models.Application.M_PrenatalHistory.MPH_AdequateNutrition.label('Adequate Nutrition'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Infections.label('Infections'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Smoking.label('Smoking'),
                                            Model.models.Application.M_PrenatalHistory.MPH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPH_IsActive=1,MPH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PrenatalHistory.MPHID.desc()).all())
                    session.commit()
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PatientBirthHistoryReport,
                                session.query(Model.models.Application.M_PatientBirthHistory.MPBHID.label('ID'),
                                            Model.models.Application.M_PatientBirthHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_MotherHealth.label('Mother Health'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_DeliveryType.label('Delivery Type'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_typeofdelivery.label('Type of Delivery'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_DeliveryLocationh.label('Delivery Location'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_MultiplePregnancies.label('Multiple Pregnancies'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ComplicationDuringPregnancy.label('Complication Pregnancy'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ChildBirth.label('Child Birth'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_ChildBirthWeek.label('Child Birth Week'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_BirthWeight.label('Birth Weight'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_BirthCry.label('Birth Cry'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_NeonatalConditionint.label('Neonatal Condition'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_SpecialCareAny.label('Special CareAny'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_AnyMedicalEvents.label('Any Medical Events'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_Congenital.label('Congenital'),
                                            Model.models.Application.M_PatientBirthHistory.MPBH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPBH_IsActive=1,MPBH_IsDeleted=0
                                ).order_by(Model.models.Application.M_PatientBirthHistory.MPBHID.desc()).all())
                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DevelopmentalHistoryReport,
                                session.query(Model.models.Application.M_DevelopmentalHistory.MDHID.label('ID'),
                                            Model.models.Application.M_DevelopmentalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_HoldUpHeadAge.label('HoldUp HeadAge'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_Rolloverage.label('Rollover age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_SitAge.label('Sit Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_StandAloneAge.label('Stand Alone Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_WalkAge.label('Walk Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_TalkAge.label('Talk Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_ToiletTrainAge.label('Toilet Train Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_FeedAge.label('Feed Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_DresshimAge.label('Dresshim Age'),
                                            Model.models.Application.M_DevelopmentalHistory.MDH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MDH_IsActive=1,MDH_IsDeleted=0
                                ).order_by(Model.models.Application.M_DevelopmentalHistory.MDHID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpeechDevelopmentHistoryReport,
                                session.query(Model.models.Application.M_SpeechDevelopmentalHistory.MSDHID.label('ID'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Vocalization.label('Vocalization'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Babbling.label('Babbling'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_FirstWord.label('First Word'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Phrases.label('Phrases'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_SimpleSentences.label('Simple Sentences'),
                                            Model.models.Application.M_SpeechDevelopmentalHistory.MSDH_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSDH_IsActive=1,MSDH_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpeechDevelopmentalHistory.MSDHID.desc()).all())
                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.socialhistoryReport,
                                session.query(Model.models.Application.M_SocialHistory.MSHID.label('ID'),
                                            Model.models.Application.M_SocialHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_SocialHistory.MSH_Aggressive.label('Social History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSH_IsActive=1,MSH_IsDeleted=0
                                ).order_by(Model.models.Application.M_SocialHistory.MSHID.desc()).all())
                    session.commit()
                    queryresult7= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.medicalhistoryReport,
                                session.query(Model.models.Application.M_MedicalHistory.MSHID.label('ID'),
                                            Model.models.Application.M_MedicalHistory.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_MedicalHistory.MMH_observations.label('Medical History'),

                                                ).filter_by(M_AppointmentID=AID,MMH_IsActive=1,MMH_IsDeleted=0
                                ).order_by(Model.models.Application.M_MedicalHistory.MSHID.desc()).all())
                    session.commit()
                    queryresult8= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.familyhistoryReport,
                                session.query(Model.models.Application.M_FamilyHistory.MFHID.label('ID'),
                                            Model.models.Application.M_FamilyHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_FamilyHistory.MFH_Familytype.label('Family type'),
                                            Model.models.Application.M_FamilyHistory.MFH_Consanguinity.label('Consanguinity'),
                                            Model.models.Application.M_FamilyHistory.MFH_Observations.label('Family History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFH_IsActive=1,MFH_IsDeleted=0
                                ).order_by(Model.models.Application.M_FamilyHistory.MFHID.desc()).all())
                    session.commit()
                    queryresult9= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.educationhistoryReport,
                                session.query(Model.models.Application.M_EducationHistory.MEHID.label('ID'),
                                            Model.models.Application.M_EducationHistory.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_EducationHistory.MEH_CommunicationMode.label('Education History'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MEH_IsActive=1,MEH_IsDeleted=0
                                ).order_by(Model.models.Application.M_EducationHistory.MEHID.desc()).all())
                    session.commit()
                    return jsonify(result={'VisitReasonReport':queryresult,'PastHistoryReport':queryresult1,
                                           'PrenatalHistoryReport':queryresult2,'PatientBirthHistoryReport':queryresult3,
                                           'DevelopmentalHistoryReport':queryresult4,'SpeechDevelopmentHistoryReport':queryresult5,
                                           'socialhistoryReport':queryresult6,'medicalhistoryReport':queryresult7,
                                           'familyhistoryReport':queryresult8,'educationhistoryReport':queryresult9})
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()
 
@Report_Blueprint.route('/SpeechTherapy', methods=['GET','POST'])
def SpeechTherapy():
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
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ParentConcernReport,
                                session.query(Model.models.Application.M_ParentConcern.MPID.label('ID'),
                                            Model.models.Application.M_ParentConcern.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ParentConcern.MP_Comment.label('Comment'),
                                            ).filter_by(M_AppointmentID=AID,MP_IsActive=1,MP_IsDeleted=0
                                ).order_by(Model.models.Application.M_ParentConcern.MPID.desc()).all())
                    session.commit()
                    
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.languageExposureReport,
                                session.query(Model.models.Application.M_LanguageExposure.MPID.label('ID'),
                                            Model.models.Application.M_LanguageExposure.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_LanguageExposure.MP_SpokenAtHome.label('SpokenAtHome'),
                                            Model.models.Application.M_LanguageExposure.MP_FamilyModel.label('FamilyModel'),
                                            Model.models.Application.M_LanguageExposure.MP_CommunicationMode.label('CommunicationMode'),
                                            ).filter_by(M_AppointmentID=AID,MP_IsActive=1,MP_IsDeleted=0
                                ).order_by(Model.models.Application.M_LanguageExposure.MPID.desc()).all())
                    session.commit()
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STOroperipheralExam,
                                session.query(Model.models.Application.M_STOroperipheralExam.MSPEID.label('ID'),
                                            Model.models.Application.M_STOroperipheralExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_LipsAppearance.label('Lips Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_LipsMovements.label('Lips Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TongueAppearance.label('Tongue Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TongueMovements.label('Tongue Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TeethAppearance.label('Teeth Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_TeethMovements.label('Teeth Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_HardPalateAppearance.label('Hard Palate Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_SoftPalateAppearance.label('Soft Palate Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_SoftPalateMovements.label('Soft Palate Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_UvulaAppearance.label('Uvula Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_UvulaMovements.label('Uvula Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_MandibleAppearance.label('Mandible Appearance'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_MandibleMovements.label('Mandible Movements'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Drooling.label('Drooling'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Blowing.label('Blowing'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Biting.label('Biting'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Sucking.label('Sucking'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Swallowing.label('Swallowing'),
                                            Model.models.Application.M_STOroperipheralExam.MSPE_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSPE_IsActive=1,MSPE_IsDeleted=0
                                ).order_by(Model.models.Application.M_STOroperipheralExam.MSPEID.desc()).all())
                    session.commit()
                    
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STArticulationSpeechIntelligibilityReport,
                                session.query(Model.models.Application.M_STArticulationSpeechIntelligibility.MSSIID.label('ID'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Noonecan.label('Noonecan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_memberscan.label('memberscan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Strangerscan.label('Strangerscan'),
                                            Model.models.Application.M_STArticulationSpeechIntelligibility.MSSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSSI_IsActive=1,MSSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_STArticulationSpeechIntelligibility.MSSIID.desc()).all())
                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STArticulationVoiceReport,
                                session.query(Model.models.Application.M_STArticulationVoice.MSAVID.label('ID'),
                                            Model.models.Application.M_STArticulationVoice.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Pitch.label('Pitch'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Loudness.label('Loudness'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Quality.label('Quality'),
                                            Model.models.Application.M_STArticulationVoice.MSAV_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSAV_IsActive=1,MSAV_IsDeleted=0
                                ).order_by(Model.models.Application.M_STArticulationVoice.MSAVID.desc()).all())

                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STVerbalCommunication,
                                session.query(Model.models.Application.M_STVerbalCommunication.MVCID.label('ID'),
                                            Model.models.Application.M_STVerbalCommunication.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Expression.label('Expression'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Comprehension.label('Comprehension'),
                                            Model.models.Application.M_STVerbalCommunication.MVC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MVC_IsActive=1,MVC_IsDeleted=0
                                ).order_by(Model.models.Application.M_STVerbalCommunication.MVCID.desc()).all())
                    session.commit()
                    
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.STNonVerbalCommunicationReport,
                                session.query(Model.models.Application.M_STNonVerbalCommunication.MNVCID.label('ID'),
                                            Model.models.Application.M_STNonVerbalCommunication.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Expression.label('Expression'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Comprehension.label('Comprehension'),
                                            Model.models.Application.M_STNonVerbalCommunication.MNVC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNVC_IsActive=1,MNVC_IsDeleted=0
                                ).order_by(Model.models.Application.M_STNonVerbalCommunication.MNVCID.desc()).all())
                    session.commit()
                    queryresult7= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ReceptiveLanguageAssessmentReport,
                                session.query(Model.models.Application.M_ReceptiveLanguageAssessment.MRLAID.label('ID'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendssounds.label('Comprehends sounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsloud.label('Comprehends loud'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendscategorizesounds.label('Comprehends categorizesounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsanimalsounds.label('Comprehends animalsounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsfruitsname.label('Comprehends fruitsname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendscolorsname.label('Comprehends colorsname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsanimalname.label('Comprehends animalname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsvegetablename.label('Comprehends vegetablename'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsshapesname.label('Comprehends shapesname'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsbodyparts.label('Comprehends bodyparts'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsvehiclenames.label('Comprehends vehiclenames'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understandingrhymes.label('Understandingrhymes'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Respondscorrectly.label('Respondscorrectly'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Identifiessounds.label('Identifiessounds'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Actsoutcommands.label('Actsoutcommands'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Comprehendsstepscommands.label('Comprehends stepscommands'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understandinggreeting.label('Understandinggreeting'),
                                            Model.models.Application.M_ReceptiveLanguageAssessment.MRLA_Understanding.label('Understanding'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRLA_IsActive=1,MRLA_IsDeleted=0
                                ).order_by(Model.models.Application.M_ReceptiveLanguageAssessment.MRLAID.desc()).all())
                    session.commit()
                    
                    queryresult8= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ExpressiveLanguageAssessmentReport,
                                session.query(Model.models.Application.M_ExpressiveLanguageAssessment.MELAID.label('ID'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesenvironmentalsounds.label('Imitates environmental sounds'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesloudandsoftsounds.label('Imitates loud and softsounds'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitateslexicalcategories.label('Imitates lexical categories'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescolorsname.label('Imitates colors name'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatesbodyparts.label('Imitates body parts'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatessingingandphrases.label('Imitates singing and phrases'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_ImitatesalphabetsAtoZ.label('Imitates alphabets AtoZ'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Usesnounwitharticles.label('articles'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Watchesfaceandbody.label('Watches'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescounting.label('Imitates counting'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Clapstobeatoffamiliarsongs.label('Claps'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Respondstosinglesigns.label('Respondstosinglesigns'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatessocialgreetings.label('Imitates socialgreetings'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Occassionallytrytoimitate.label('Occassionallytrytoimitate'),
                                            Model.models.Application.M_ExpressiveLanguageAssessment.MELA_Imitatescommonsyllables.label('Imitates commonsyllables'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MELA_IsActive=1,MELA_IsDeleted=0
                                ).order_by(Model.models.Application.M_ExpressiveLanguageAssessment.MELAID.desc()).all())

                    session.commit()
                    queryresult9= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DiagnosticFormulationsReport,
                                session.query(Model.models.Application.M_DiagnosticFormulations.MPID.label('ID'),
                                            Model.models.Application.M_DiagnosticFormulations.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_DiagnosticFormulations.MP_Comment.label('Comment'),
                                            Model.models.Application.M_DiagnosticFormulations.MP_Type.label('Type'),
                                            ).filter_by(M_AppointmentID=AID,MP_IsActive=1,MP_IsDeleted=0
                                ).order_by(Model.models.Application.M_DiagnosticFormulations.MPID.desc()).all())
                    session.commit()
                    queryresult10= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ProvisionalDiagnosisFormReport,
                                session.query(Model.models.Application.M_ProvisionalDiag.MPID.label('ID'),
                                            Model.models.Application.M_ProvisionalDiag.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ProvisionalDiag.MP_Comment.label('Comment'),
                                            ).filter_by(M_AppointmentID=AID,MP_IsActive=1,MP_IsDeleted=0
                                ).order_by(Model.models.Application.M_ProvisionalDiag.MPID.desc()).all())
                    session.commit()
                    queryresult11= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.stutteringhistoryReport,
                                session.query(Model.models.Application.M_stutteringhistory.MPID,
                                    Model.models.Application.M_stutteringhistory.persistent,
                                    Model.models.Application.M_stutteringhistory.recovered,
                                    Model.models.Application.M_stutteringhistory.startedstuttering,
                                    Model.models.Application.M_stutteringhistory.phraserepititions,
                                    Model.models.Application.M_stutteringhistory.wordrepitions,
                                    Model.models.Application.M_stutteringhistory.Syllablerepitions,
                                    Model.models.Application.M_stutteringhistory.Blockslike,
                                    Model.models.Application.M_stutteringhistory.Interjections,
                                    Model.models.Application.M_stutteringhistory.demonstrated,
                                    Model.models.Application.M_stutteringhistory.phsyicaltension,
                                    Model.models.Application.M_stutteringhistory.frustrationabout,
                                    Model.models.Application.M_stutteringhistory.Complaints,
                                    Model.models.Application.M_stutteringhistory.childeverbeenteased,
                                    Model.models.Application.M_stutteringhistory.childeverdiscussed,
                                    Model.models.Application.M_stutteringhistory.childseemstostutter,
                                    Model.models.Application.M_stutteringhistory.stutterinyoursecondary,
                                    Model.models.Application.M_stutteringhistory.childstartedlearning,
                                    Model.models.Application.M_stutteringhistory.remarkableduringpregnancy,
                                    Model.models.Application.M_stutteringhistory.remarkableconditionatbirth,
                                    Model.models.Application.M_stutteringhistory.currenthealthmedicalconcerns,
                                    Model.models.Application.M_stutteringhistory.takinganymedications,
                                    Model.models.Application.M_stutteringhistory.allergies,
                                    Model.models.Application.M_stutteringhistory.developmentalconcerns,
                                    Model.models.Application.M_stutteringhistory.hearingtested,
                                    Model.models.Application.M_stutteringhistory.behavioursoccur,
                                    Model.models.Application.M_stutteringhistory.Inattentiveness,
                                    Model.models.Application.M_stutteringhistory.Hyperactivity,
                                    Model.models.Application.M_stutteringhistory.Nervousness,
                                    Model.models.Application.M_stutteringhistory.sensitivity,
                                    Model.models.Application.M_stutteringhistory.perfectionism,
                                    Model.models.Application.M_stutteringhistory.excitability,
                                    Model.models.Application.M_stutteringhistory.frustration,
                                    Model.models.Application.M_stutteringhistory.strongfears,
                                    Model.models.Application.M_stutteringhistory.excessiveneatness,
                                    Model.models.Application.M_stutteringhistory.excessiveshyness,
                                    Model.models.Application.M_stutteringhistory.lackofconfidence,
                                    Model.models.Application.M_stutteringhistory.competitiveness,
                                    Model.models.Application.M_stutteringhistory.speakfluentlyathome,
                                    Model.models.Application.M_stutteringhistory.speakfluentlyatschool,
                                    Model.models.Application.M_stutteringhistory.speakfluentlyinnewsituation,
                                    Model.models.Application.M_stutteringhistory.speakwithoutstutteringathome,
                                    Model.models.Application.M_stutteringhistory.speakwithoutstutteringatschool,
                                    Model.models.Application.M_stutteringhistory.speakwithoutstutteringinanycondition,
                                    Model.models.Application.M_stutteringhistory.stutteringaffectacademicperformance,
                                    Model.models.Application.M_stutteringhistory.participationinschool,
                                    Model.models.Application.M_stutteringhistory.interactionwithother,
                                    Model.models.Application.M_stutteringhistory.interactionwithfamily,
                                    Model.models.Application.M_stutteringhistory.willingnesstotalk,
                                    Model.models.Application.M_stutteringhistory.selfesteemorattitude,
                                    Model.models.Application.M_stutteringhistory.teachernoticedyourchild
                                            ).filter_by(MP_IsActive=1,MP_IsDeleted=0,M_AppointmentID=AID
                                            
                                ).order_by(Model.models.Application.M_stutteringhistory.MPID.desc()).all())
                    session.commit()
                    return jsonify(result={'ParentConcernReport':queryresult,'languageExposureReport':queryresult1,
                                           'STOroperipheralExam':queryresult2,'STArticulationSpeechIntelligibilityReport':queryresult3,
                                           'STArticulationVoiceReport':queryresult4,'STVerbalCommunication':queryresult5,
                                           'STNonVerbalCommunicationReport':queryresult6,'ReceptiveLanguageAssessmentReport':queryresult7,
                                           'ExpressiveLanguageAssessmentReport':queryresult8,'DiagnosticFormulationsReport':queryresult9,
                                           'ProvisionalDiagnosisFormReport':queryresult10,'stutteringhistoryReport':queryresult11 })
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/OccupationalTherapy', methods=['GET','POST'])
def OccupationalTherapy():
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
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTHandFunctionsReport,
                                session.query(Model.models.Application.M_OTHandFunctions.MHFID.label('ID'),
                                            Model.models.Application.M_OTHandFunctions.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTHandFunctions.MHF_HandDominance.label('Hand Dominance'),
                                            Model.models.Application.M_OTHandFunctions.MHF_HandPreference.label('Hand Preference'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachForward.label('Reach Forward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachBackward.label('Reach Backward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachLateral.label('Reach Lateral'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachDownward.label('Reach Downward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspUlnarPalmar.label('Grasp UlnarPalmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspPalmar.label('Grasp Palmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspRadialPalmar.label('Grasp RadialPalmar'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspRadialDigital.label('Grasp RadialDigital'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspInferiorPincer.label('Grasp InferiorPincer'),
                                            Model.models.Application.M_OTHandFunctions.MHF_ReachUpward.label('Reach Upward'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspNeatPincer.label('Grasp NeatPincer'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspPalmarsupinate.label('Grasp Palmarsupinate'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspDigitalpronate.label('Grasp Digitalpronate'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspStatictripod.label('Grasp Statictripod'),
                                            Model.models.Application.M_OTHandFunctions.MHF_GraspDynamictripod.label('Grasp Dynamictripod'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionPadtoPad.label('Prehension PadtoPad'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionTiptoTip.label('Prehension TiptoTip'),
                                            Model.models.Application.M_OTHandFunctions.MHF_PrehensionPadtoSide.label('Prehension PadtoSide'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MHF_IsActive=1,MHF_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTHandFunctions.MHFID.desc()).all())
                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewOTNonEquilibriumCoordinationForm,
                                session.query(Model.models.Application.M_NonEquilibrium.MNEID.label('ID'),
                                            Model.models.Application.M_NonEquilibrium.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertonose.label('Fingertonose'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertotherapistfinger.label('Fingertotherapistfinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingertofinger.label('Fingertofinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Alternatnosefinger.label('Alternatnosefinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fingeropposition.label('Fingeropposition'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Massgrasp.label('Massgrasp'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Pronationsupination.label('Pronationsupination'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Reboundtest.label('Reboundtest'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Tappinghand.label('Tappinghand'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Tappingfeet.label('Tappingfeet'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Pointingandpastpointing.label('Pointingandpastpointing'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Alternateheeltokneeheeltoe.label('Alternateheeltokneeheeltoe'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Toetoexaminersfinger.label('Toetoexaminersfinger'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Heeltoshin.label('Heeltoshin'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Drawingacircle.label('Drawingacircle'),
                                            Model.models.Application.M_NonEquilibrium.MNE_Fixationorpositionholding.label('Fixationorpositionholding'),

                                                ).filter_by(M_AppointmentID=AID,MNE_IsActive=1,MNE_IsDeleted=0
                                ).order_by(Model.models.Application.M_NonEquilibrium.MNEID.desc()).all())

                    session.commit()
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTEquilibriumCoordinationReport,
                                session.query(Model.models.Application.M_Equilibrium.MNEID.label('ID'),
                                            Model.models.Application.M_Equilibrium.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingwithnormalbaseofsupport.label('Standingwithnormalbaseofsupport'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingwithnarrowbaseofsupport.label('Standingwithnarrowbaseofsupport'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingintandemposition.label('Standingintandemposition'),
                                            Model.models.Application.M_Equilibrium.MNE_Standingononefeet.label('Standingononefeet'),
                                            Model.models.Application.M_Equilibrium.MNE_Perturbation.label('Perturbation'),
                                            Model.models.Application.M_Equilibrium.MNE_Standinginfunctionalreach.label('Standinginfunctionalreach'),
                                            Model.models.Application.M_Equilibrium.MNE_Standinglateralflexionofthetrunktoeachside.label('Standinglateralflexionofthetrunktoeachside'),
                                            Model.models.Application.M_Equilibrium.MNE_Tandemwalking.label('Tandemwalking'),
                                            Model.models.Application.M_Equilibrium.MNE_WalkingInastraightline.label('WalkingInastraightline'),
                                            Model.models.Application.M_Equilibrium.MNE_Walksidewaysbackwards.label('Walksidewaysbackwards'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkinhorizontalvertical.label('Walkinhorizontalvertical'),
                                            Model.models.Application.M_Equilibrium.MNE_Marchinplace.label('Marchinplace'),
                                            Model.models.Application.M_Equilibrium.MNE_Startstopabruptly.label('Startstopabruptly'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkandpivotincommand.label('Walkandpivotincommand'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkincircle.label('Walkincircle'),
                                            Model.models.Application.M_Equilibrium.MNE_Walkonheelsandtoes.label('Walkonheelsandtoes'),
                                            Model.models.Application.M_Equilibrium.MNE_Turnsoncommand.label('Turnsoncommand'),
                                            Model.models.Application.M_Equilibrium.MNE_Stepoveraroundobstacles.label('Stepoveraroundobstacles'),
                                            Model.models.Application.M_Equilibrium.MNE_Stairclimbingwithhandrails.label('Stairclimbingwithhandrails'),
                                            Model.models.Application.M_Equilibrium.MNE_Jumpingjacks.label('Jumpingjacks'),
                                            Model.models.Application.M_Equilibrium.MNE_Sittingontherapybal.label('Sittingontherapybal'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNE_IsActive=1,MNE_IsDeleted=0
                                ).order_by(Model.models.Application.M_Equilibrium.MNEID.desc()).all())
                    session.commit()
                    
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTCognitionAndPerceptionReport,
                                session.query(Model.models.Application.M_OTCognition.MOCID.label('ID'),
                                            Model.models.Application.M_OTCognition.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTCognition.MOC_Praxis.label('Praxis'),
                                            Model.models.Application.M_OTCognition.MOC_Rightleftdiscrimination.label('Rightleftdiscrimination'),
                                            Model.models.Application.M_OTCognition.MOC_Fingerindentification.label('Fingerindentification'),
                                            Model.models.Application.M_OTCognition.MOC_Orientationtoperson.label('Orientationtoperson'),
                                            Model.models.Application.M_OTCognition.MOC_Orientationtoplace.label('Orientationtoplace'),
                                            Model.models.Application.M_OTCognition.MOC_Conceputalseriescompletion.label('Conceputalseriescompletion'),
                                            Model.models.Application.M_OTCognition.MOC_Selectiveattention.label('Selectiveattention'),
                                            Model.models.Application.M_OTCognition.MOC_Focusedattention.label('Focusedattention'),
                                            Model.models.Application.M_OTCognition.MOC_Spatialperception.label('Spatialperception'),
                                            Model.models.Application.M_OTCognition.MOC_Visualmemory.label('Visualmemory'),
                                            Model.models.Application.M_OTCognition.MOC_Verbalmemory.label('Verbalmemory'),
                                            Model.models.Application.M_OTCognition.MOC_Identificationofobjects.label('Identificationofobjects'),
                                            Model.models.Application.M_OTCognition.MOC_Proverbinterpretation.label('Proverbinterpretation'),
                                            Model.models.Application.M_OTCognition.MOC_Randomlettertest.label('Randomlettertest'),
                                            Model.models.Application.M_OTCognition.MOC_Overlappingfigures.label('Overlappingfigures'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MOC_IsActive=1,MOC_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTCognition.MOCID.desc()).all())

                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTSensoryExamReport,
                                session.query(Model.models.Application.M_OTSensoryExam.MSEID.label('ID'),
                                            Model.models.Application.M_OTSensoryExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Visualtracking.label('Visual tracking'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Choreiformmovements.label('Choreiform movements'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Tremor.label('Tremor'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Exaggeratedassociated.label('Exaggerated associated'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Graphesthesis.label('Graphesthesis'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Stereognosis.label('Stereognosis'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Weightbearinghands.label('Weight bearing hands'),
                                            Model.models.Application.M_OTSensoryExam.MSE_Proneextensionpattern.label('Prone extension pattern'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSE_IsActive=1,MSE_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTSensoryExam.MSEID.desc()).all())
                    session.commit()
                    
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.OTSensoryProfileReport,
                                session.query(Model.models.Application.M_OTSensoryProfile.MSPID.label('ID'),
                                            Model.models.Application.M_OTSensoryProfile.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_OTSensoryProfile.MSP_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSP_IsActive=1,MSP_IsDeleted=0
                                ).order_by(Model.models.Application.M_OTSensoryProfile.MSPID.desc()).all())
                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.AddtionalinfoReport,
                                session.query(Model.models.Application.M_Addtionalinfo.MAIID.label('ID'),
                                            Model.models.Application.M_Addtionalinfo.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_Addtionalinfo.MAI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MAI_IsActive=1,MAI_IsDeleted=0
                                ).order_by(Model.models.Application.M_Addtionalinfo.MAIID.desc()).all())
                    session.commit()
                    return jsonify(result={'OTHandFunctionsReport':queryresult,'viewOTNonEquilibriumCoordinationForm':queryresult1,
                                           'OTEquilibriumCoordinationReport':queryresult2,'OTCognitionAndPerceptionReport':queryresult3,
                                           'OTSensoryExamReport':queryresult4,'OTSensoryProfileReport':queryresult5,
                                           'AddtionalinfoReport':queryresult6})
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/PhysicalTherapy1', methods=['GET','POST'])
def PhysicalTherapy1():
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
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTFunctionalAbilitiesReport,
                                session.query(Model.models.Application.M_PTFunctionalAbilities.MFAID.label('ID'),
                                            Model.models.Application.M_PTFunctionalAbilities.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_GrossMotor.label('Gross Motor'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_FineMotor.label('Fine Motor'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_CommunicationSpeech.label('Communication Speech'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_Feeding.label('Feeding'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_Playskills.label('Playskills'),
                                            Model.models.Application.M_PTFunctionalAbilities.MFA_ADL.label('ADL'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFA_IsActive=1,MFA_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTFunctionalAbilities.MFAID.desc()).all())
                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTFunctionalLimitationsReport,
                                session.query(Model.models.Application.M_PTFunctionalLimitations.MFLID.label('ID'),
                                            Model.models.Application.M_PTFunctionalLimitations.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_GrossMotor.label('Gross Motor'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_FineMotor.label('Fine Motor'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_CommunicationSpeech.label('Communication Speech'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_Feeding.label('Feeding'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_Playskills.label('Playskills'),
                                            Model.models.Application.M_PTFunctionalLimitations.MFL_ADL.label('ADL'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MFL_IsActive=1,MFL_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTFunctionalLimitations.MFLID.desc()).all())
                    session.commit()
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemAlignmentReport,
                                session.query(Model.models.Application.M_PosturalSystemAlignments.MPSAID.label('ID'),
                                            Model.models.Application.M_PosturalSystemAlignments.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HeadNeck.label('Head Neck'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShoulderScapular.label('Shoulder Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShoulderandScapular.label('Shoulder and Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_ShouldernScapular.label('Shouldern Scapular'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_RibcageandChest.label('Ribcage and Chest'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Trunk.label('Trunk'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Trunks.label('Trunks'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_PelvicComplexRight.label('Pelvic Complex Right'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_PelvicComplexLeft.label('Pelvic Complex Left'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointAbduction.label('Hipjoint Abduction'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointAdduction.label('Hipjoint Adduction'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_HipjointRotation.label('Hipjoint Rotation'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Symmetrical.label('Symmetrical'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Assymetrical.label('Assymetrical'),
                                            Model.models.Application.M_PosturalSystemAlignments.MPSA_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSA_IsActive=1,MPSA_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemAlignments.MPSAID.desc()).all())
                    session.commit()
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemBOSReport,
                                session.query(Model.models.Application.M_PosturalSystemBOS.MPSBID.label('ID'),
                                            Model.models.Application.M_PosturalSystemBOS.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemBOS.MPSB_BaseofSupport.label('Base of Support'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSB_IsActive=1,MPSB_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemBOS.MPSBID.desc()).all())
                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalSystemCOMReport,
                                session.query(Model.models.Application.M_PosturalSystemCOM.MPSCID.label('ID'),
                                            Model.models.Application.M_PosturalSystemCOM.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_CenterofMass.label('Center of Mass'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_Withinsupport.label('Within support'),
                                            Model.models.Application.M_PosturalSystemCOM.MPSC_Strategiesposture.label('Strategies posture'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSC_IsActive=1,MPSC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemCOM.MPSCID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTAnticipatoryControlReport,
                                session.query(Model.models.Application.M_PTAnticipatoryControl.MACID.label('ID'),
                                            Model.models.Application.M_PTAnticipatoryControl.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTAnticipatoryControl.MAC_Canchildanti.label('Canchildanti'),
                                            Model.models.Application.M_PTAnticipatoryControl.MAC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MAC_IsActive=1,MAC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTAnticipatoryControl.MACID.desc()).all())
                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTPosturalCounterbalanceReport,
                                session.query(Model.models.Application.M_PTPosturalCounterbalance.MPCID.label('ID'),
                                            Model.models.Application.M_PTPosturalCounterbalance.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTPosturalCounterbalance.MPC_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPC_IsActive=1,MPC_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTPosturalCounterbalance.MPCID.desc()).all())
                    session.commit()
                    queryresult7= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewPTPosturalSystemImpairments,
                                session.query(Model.models.Application.M_PosturalSystemImpairments.MPSIID.label('ID'),
                                            Model.models.Application.M_PosturalSystemImpairments.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_MuscleArchitecture.label('Muscle Architecture'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Anycallosities.label('Anycallosities'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Anyotherspecificposture.label('Anyother specific posture'),
                                            Model.models.Application.M_PosturalSystemImpairments.MPSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPSI_IsActive=1,MPSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_PosturalSystemImpairments.MPSIID.desc()).all())
                    session.commit()
                    queryresult8= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementSystemReport,
                                session.query(Model.models.Application.M_PTMovementSystem.MPMSID.label('ID'),
                                            Model.models.Application.M_PTMovementSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Cantheyovercome.label('Canthey overcome'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Howdoesthe.label('How do'),
                                            Model.models.Application.M_PTMovementSystem.MPMS_Strategiesused.label('Strategies used'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MPMS_IsActive=1,MPMS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementSystem.MPMSID.desc()).all())
                    session.commit()
                    queryresult9= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementStrategiesReport,
                                session.query(Model.models.Application.M_PTMovementStrategies.MMSID.label('ID'),
                                            Model.models.Application.M_PTMovementStrategies.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_Childgenerallyperformsactivitie.label('Childgenerallyperformsactivitie'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformLateralweightshifts.label('CanperformLateralweightshifts'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformLateralweightshiftsleft.label('CanperformLateralweightshiftsleft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformDiagonalweightRight.label('CanperformDiagonalweightRight'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformDiagonalweightLeft.label('CanperformDiagonalweightLeft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformneckthoracicspineRight.label('CanperformneckthoracicspineRight'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_CanperformneckthoracicspineLeft.label('CanperformneckthoracicspineLeft'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowarethedissociationsPelvicfemoral.label('HowarethedissociationsPelvicfemoral'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowaredissociationsInterlimb.label('HowaredissociationsInterlimb'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowthedissociationsScapulohumeral.label('HowthedissociationsScapulohumeral'),
                                            Model.models.Application.M_PTMovementStrategies.MMS_HowthedissociationsUpperLowerbody.label('HowthedissociationsUpperLowerbody'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MMS_IsActive=1,MMS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementStrategies.MMSID.desc()).all())
                    session.commit()
                    
                    return jsonify(result={'PTFunctionalAbilitiesReport':queryresult,'PTFunctionalLimitationsReport':queryresult1,
                                           'PTPosturalSystemAlignmentReport':queryresult2,'PTPosturalSystemBOSReport':queryresult3,
                                           'PTPosturalSystemCOMReport':queryresult4,'PTAnticipatoryControlReport':queryresult5,
                                           'PTPosturalCounterbalanceReport':queryresult6,'viewPTPosturalSystemImpairments':queryresult7,
                                           'PTMovementSystemReport':queryresult8,'PTMovementStrategiesReport':queryresult9})
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close() 
 
@Report_Blueprint.route('/PhysicalTherapy2', methods=['GET','POST'])
def PhysicalTherapy2():
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
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTRangeSpeedofMovementReport,
                                session.query(Model.models.Application.M_PTRangeSpeed.MPMSID.label('ID'),
                                            Model.models.Application.M_PTRangeSpeed.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_Rangespeedmovement.label('Range Speed Movement'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_atTrunk.label('at Trunk'),
                                            Model.models.Application.M_PTRangeSpeed.MRS_HowisitatExtremities.label('Extremities'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRS_IsActive=1,MRS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTRangeSpeed.MPMSID.desc()).all())
                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTStabilityMobilityReport,
                                session.query(Model.models.Application.M_PTStabilityMobility.MSMID.label('ID'),
                                            Model.models.Application.M_PTStabilityMobility.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTStabilityMobility.MSM_StrategiesforStabilityMobility.label('Mobility Strategies'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSM_IsActive=1,MSM_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTStabilityMobility.MSMID.desc()).all())
                    session.commit()
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMovementSystemImpairmentReport,
                                session.query(Model.models.Application.M_PTMovementSystemImpairment.MSIID.label('ID'),
                                            Model.models.Application.M_PTMovementSystemImpairment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Excessivemovementfortasks.label('Excessive movement'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Lackofmovementstaticpostures.label('movement StaticPostures'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_IntegrationofPostureMovement.label('Integration of PostureMovement'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Howdoeschildmaintainbalanceintransitions.label('Balance Transitions'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Accuracyofmovements.label('Accuracy of Movements'),
                                            Model.models.Application.M_PTMovementSystemImpairment.MSI_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSI_IsActive=1,MSI_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMovementSystemImpairment.MSIID.desc()).all())

                    session.commit()
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTRegulatorySystemReport,
                                session.query(Model.models.Application.M_PTRegulatorySystem.MRSID.label('ID'),
                                            Model.models.Application.M_PTRegulatorySystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Affect.label('Affect'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Arousal.label('Arousal'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Attention.label('Attention'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Action.label('Action'),
                                            Model.models.Application.M_PTRegulatorySystem.MRS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MRS_IsActive=1,MRS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTRegulatorySystem.MRSID.desc()).all())
                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTNeurometerSystemReport,
                                session.query(Model.models.Application.M_PTNeurometerSystem.MNSID.label('ID'),
                                            Model.models.Application.M_PTNeurometerSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Initiation.label('Initiation'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Sustenance.label('Sustenance'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Termination.label('Termination'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Controlandgradation.label('Control and Gradation'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionConcentric.label('Contraction Concentric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionIsometric.label('Contraction Isometric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_ContractionEccentric.label('Contraction Eccentric'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_CoactivationReciprocalinhibition.label('Reciprocal Inhibition'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_MasssynergyIsolatedwork.label('Isolated work'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Dynamicstiffness.label('Dynamic stiffness'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Extraneousmovement.label('Extraneous Movement'),
                                            Model.models.Application.M_PTNeurometerSystem.MNS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MNS_IsActive=1,MNS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTNeurometerSystem.MNSID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTMusculoskeletalSystemReport,
                                session.query(Model.models.Application.M_PTMusculoskeletalSystem.MKSID.label('ID'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Muscleendurance.label('Muscle Endurance'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Skeletalcomments.label('Skeletal Comments'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR1.label('Tardieu ScaleTR1'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR2.label('Tardieu ScaleTR2'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuScaleTR3.label('Tardieu ScaleTR3'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuscaleHamsR1.label('Tardieu ScaleHamsR1'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_TardieuscaleHamsR2.label('Tardieu ScaleHamsR2'),
                                            Model.models.Application.M_PTMusculoskeletalSystem.MKS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MKS_IsActive=1,MKS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTMusculoskeletalSystem.MKSID.desc()).all())

                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTSensorySystemReport,
                                session.query(Model.models.Application.M_PTSensorySystem.MSSID.label('ID'),
                                            Model.models.Application.M_PTSensorySystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTSensorySystem.MSS_sensorymodulationissues.label('Modulation Issues'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Visualsystem.label('Visual system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Auditorysystem.label('Auditory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_AuditorysystemResponse.label('Auditory system Response'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Vestibularsystem.label('Vestibular system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Somatosensorysystem.label('Somatosensory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Oromotorsystem.label('Oromotor system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Olfactorysystem.label('Olfactory system'),
                                            Model.models.Application.M_PTSensorySystem.MSS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSS_IsActive=1,MSS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTSensorySystem.MSSID.desc()).all())

                    session.commit()
                    queryresult7= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.PTCognitiveSystemReport,
                                session.query(Model.models.Application.M_PTCognitiveSystem.MCSID.label('ID'),
                                            Model.models.Application.M_PTCognitiveSystem.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Intelligence.label('Intelligence'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Memory.label('Memory'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Adaptability.label('Adaptability'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_MotorPlanning.label('Motor Planning'),
                                            Model.models.Application.M_PTCognitiveSystem.MCS_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MCS_IsActive=1,MCS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PTCognitiveSystem.MCSID.desc()).all())

                    session.commit()
                    return jsonify(result={'PTRangeSpeedofMovementReport':queryresult,'PTStabilityMobilityReport':queryresult1,
                                           'PTMovementSystemImpairmentReport':queryresult2,'PTRegulatorySystemReport':queryresult3,
                                           'PTNeurometerSystemReport':queryresult4,'PTMusculoskeletalSystemReport':queryresult5,
                                           'PTSensorySystemReport':queryresult6,'PTCognitiveSystemReport':queryresult7})
                    
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()  
              
@Report_Blueprint.route('/SpecialEducation', methods=['GET','POST'])
def SpecialEducation():
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
                    AID = request1.get('AID')
                    
                    
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmenttwoyearsReport,
                                session.query(Model.models.Application.M_SpecialEdassessmenttwoyears.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Respondstoname.label('Respondstoname'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Makeseyecontact.label('Makeseyecontact'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Respondstolightandsoundtoys.label('Respondstolightandsoundtoys'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmoveeyesupanddown.label('canmoveeyesupanddown'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmoveeyesleftandright.label('canmoveeyesleftandright'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_repeatswords.label('repeatswords'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsidentificationofnumber.label('knowsidentificationofnumber'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canrollpoundandsqueezeclay.label('canrollpoundandsqueezeclay'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyMom.label('vocabularyMom'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyDad.label('vocabularyDad'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Vocabularydog.label('Vocabularydog'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycat.label('vocabularycat'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularytree.label('vocabularytree'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularytable.label('vocabularytable'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularychair.label('vocabularychair'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycow.label('vocabularycow'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycrayons.label('vocabularycrayons'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybus.label('vocabularybus'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularycar.label('vocabularycar'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybook.label('vocabularybook'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularyapple.label('vocabularyapple'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybanana.label('vocabularybanana'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_vocabularybottle.label('vocabularybottle'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Candostacking.label('Candostacking'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canmaketower.label('canmaketower'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_respondstobubbles.label('respondstobubbles'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Identifieshappyandsad.label('Identifieshappyandsad'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_Knowsshapes.label('Knowsshapes'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowscolors.label('knowscolors'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsanimals.label('knowsanimals'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsvehicles.label('knowsvehicles'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsbodyparts.label('knowsbodyparts'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsidentificationofalphabets.label('knowsidentificationofalphabets'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsmoreorless.label('knowsmoreorless'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsbigandsmall.label('knowsbigandsmall'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_knowsnearandfar.label('knowsnearandfar'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifhisorher.label('canidentifhisorher'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifybag.label('canidentifybag'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifyshoes.label('canidentifyshoes'),
                                            Model.models.Application.M_SpecialEdassessmenttwoyears.MSATW_canidentifybottle.label('canidentifybottle'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialEdassessmenttwoyears.MSATWID.desc()).all())
                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentthreeyearsReport,
                                session.query(Model.models.Application.M_SpecialEdassessmentThreeyears.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_respondstoname.label('respondstoname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_makeseyecontact.label('makeseyecontact'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canmoveeyesupanddown.label('canmoveeyesupanddown'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canmoveeyesleftandright.label('canmoveeyesleftandright'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerfullname.label('cananswerfullname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularybodyparts.label('vocabularybodyparts'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfollowstepsinstruction.label('canfollowstepsinstruction'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerold.label('cananswerold'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerwhatsyourmothersname.label('cananswerwhatsyourmothersname'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cananswerwhichisyoufavoritecolour.label('cananswerwhichisyoufavoritecolour'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularyshapescircle.label('vocabularyshapescircle'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_Vocabularyfruits.label('Vocabularyfruits'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canfollowstepinstruction.label('canfollowstepinstruction'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerseeinsky.label('cangiveanswerseeinsky'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerswiminwater.label('cangiveanswerswiminwater'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cangiveanswerseeontree.label('cangiveanswerseeontree'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_knowsidentificationofalphabets.label('knowsidentificationofalphabets'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_knowsidentificationofnumbers.label('knowsidentificationofnumbers'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_Canholdapencilcrayon.label('Canholdapencilcrayon'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canscribble.label('canscribble'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cancoloringivenshape.label('cancoloringivenshape'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_cantearandpaste.label('cantearandpaste'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionshappy.label('canidentifyemotionshappy'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionssad.label('canidentifyemotionssad'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionsangry.label('canidentifyemotionsangry'),
                                            Model.models.Application.M_SpecialEdassessmentThreeyears.MSATW_canidentifyemotionsupset.label('canidentifyemotionsupset'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialEdassessmentThreeyears.MSATWID.desc()).all())
                    session.commit()
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentthreefouryearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_doesrespondtonamecall.label('doesrespondtonamecall'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_doesmakeseyecontact.label('doesmakeseyecontact'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_initiatesinteractiontoward.label('initiatesinteractiontoward'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_understandinstructionslikestand.label('understandinstructionslikestand'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_getthatputthere.label('getthatputthere'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_givemegetthis.label('givemegetthis'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_runwalkjump.label('runwalkjump'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_lookdownup.label('lookdownup'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cananswerwhatis.label('cananswerwhatis'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cananswerfavoritecolour.label('cananswerfavoritecolour'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularyshapes.label('vocabularyshapes'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularyfruits.label('vocabularyfruits'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_vocabularybodyparts.label('vocabularybodyparts'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_Canunderstandpositions.label('Canunderstandpositions'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canunderstandstories.label('canunderstandstories'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canWhatquestions.label('canWhatquestions'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canidentifybasicobjects.label('canidentifybasicobjects'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canholdacrayonpencil.label('canholdacrayonpencil'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canmaketower.label('canmaketower'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canimitate.label('canimitate'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canplaydoughballs.label('canplaydoughballs'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canheshethrow.label('canheshethrow'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_canrecognisealphabet.label('canrecognisealphabet'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_Canrecognisenumerals.label('Canrecognisenumerals'),
                                            Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATW_cancolourgivenshape.label('cancolourgivenshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentthrefourYrs.MSATWID.desc()).all())

                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentfouryearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentfourYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_respondnamecall.label('respondnamecall'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_makeseyecontact.label('makeseyecontact'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_interactiontowardothers.label('interactiontowardothers'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cansitformins.label('cansitformins'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cananswerwhatname.label('cananswerwhatname'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_answerfavoritecolour.label('answerfavoritecolour'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canfixpiecepuzzle.label('canfixpiecepuzzle'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularyshapes.label('vocabularyshapes'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularycolors.label('vocabularycolors'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularywild.label('vocabularywild'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_vocabularybody.label('vocabularybody'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_Vocabularyfruits.label('Vocabularyfruits'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canunderstandpositions.label('canunderstandpositions'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cansingrhymes.label('cansingrhymes'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canunderstandstories.label('canunderstandstories'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_replyWhatquestions.label('replyWhatquestions'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_identifybasicobjects.label('identifybasicobjects'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_holdcrayonpencil.label('holdcrayonpencil'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canimitate.label('canimitate'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_doughmakeballs.label('doughmakeballs'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_canthrow.label('canthrow'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_recognisealphabets.label('recognisealphabets'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_recognisenumerals.label('recognisenumerals'),
                                            Model.models.Application.M_SpecialAssessmentfourYrs.MSATW_cancolourshape.label('cancolourshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentfourYrs.MSATWID.desc()).all())

                    session.commit()
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SpecialEdassessmentsevenyearsReport,
                                session.query(Model.models.Application.M_SpecialAssessmentSevenYrs.MSATWID.label('ID'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_putneedsminimalassistance.label('putneedsminimalassistance'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_eathandsonly.label('eathandsonly'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_fixasandwich.label('fixasandwich'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_givefirstlastname.label('givefirstlastname'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_cangiveaddress.label('cangiveaddress'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_awareofemotions.label('awareofemotions'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_canzipper.label('canzipper'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_independentlyassistanct.label('independentlyassistanct'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_asksmeaningfulquestions.label('asksmeaningfulquestions'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_tellsstorieswords.label('tellsstorieswords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_Doestellage.label('Doestellage'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_canobeysimplecommands.label('canobeysimplecommands'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_readsimplewords.label('readsimplewords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_writesimplewords.label('writesimplewords'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_namethingsaround.label('namethingsaround'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_alternatesfeetupdownstairs.label('alternatesfeetupdownstairs'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_pedaltricycle.label('pedaltricycle'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_catchandthrowball.label('catchandthrowball'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_towersmallblocks.label('towersmallblocks'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_doughmakeballs.label('doughmakeballs'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_tieshoes.label('tieshoes'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_holdpencilproperly.label('holdpencilproperly'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_drawsanyshape.label('drawsanyshape'),
                                            Model.models.Application.M_SpecialAssessmentSevenYrs.MSATW_usescissorscutshape.label('usescissorscutshape'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSATW_IsActive=1,MSATW_IsDeleted=0
                                ).order_by(Model.models.Application.M_SpecialAssessmentSevenYrs.MSATWID.desc()).all())
                    session.commit()
                    
                    return jsonify(result={'SpecialEdassessmentthreefouryearsReport':queryresult,'SpecialEdassessmentfouryearsReport':queryresult1,
                                           'SpecialEdassessmentsevenyearsReport':queryresult2,'SpecialEdassessmenttwoyearsReport':queryresult3,
                                           'SpecialEdassessmentthreeyearsReport':queryresult4})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/LanguageAssessment1', methods=['GET','POST'])
def LanguageAssessment1():
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
                    AID = request1.get('AID')
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SystemicExamReport,
                                session.query(Model.models.Application.M_SystemicExam.MSEID.label('ID'),
                                            Model.models.Application.M_SystemicExam.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_SystemicExam.MSE_Observations.label('Observations'),
                                                ).filter_by(M_AppointmentID=AID,MSE_IsActive=1,MSE_IsDeleted=0
                                ).order_by(Model.models.Application.M_SystemicExam.MSEID.desc()).all())
                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.CognitivePrerequitesReport,
                                session.query(Model.models.Application.M_CognitivePrerequites.MCPID.label('ID'),
                                            Model.models.Application.M_CognitivePrerequites.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Imitation.label('Imitation'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Objectpermanence.label('Objectpermanence'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Timeconcept.label('Timeconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Colourconcept.label('Colourconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Moneyconcept.label('Moneyconcept'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Sequencing.label('Sequencing'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Matching.label('Matching'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Meanendrelationship.label('Meanendrelationship'),
                                            Model.models.Application.M_CognitivePrerequites.MCP_Observations.label('Observations'),

                                                ).filter_by(M_AppointmentID=AID,MCP_IsActive=1,MCP_IsDeleted=0
                                ).order_by(Model.models.Application.M_CognitivePrerequites.MCPID.desc()).all())
                    session.commit()
                    queryresult2= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewNICHQVanderbiltADHDParentReport,
                            session.query(Model.models.Application.M_NICHQVanderbiltADHDParent.MVAID.label('ID'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_InattentionScore.label('Inattention Score'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_HyperactivityScore.label('Hyperactivity Score'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_CombinedScore.label('Combined Score'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_OppositionalScore.label('Oppositional Score'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_ConductScore.label('Conduct Score'),
                                        Model.models.Application.M_NICHQVanderbiltADHDParent.MVA_AnxietyScore.label('Anxiety Score'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MVA_IsActive=1,MVA_IsDeleted=0
                            ).order_by(Model.models.Application.M_NICHQVanderbiltADHDParent.MVAID.desc()).all())
                    session.commit()
                    
                    queryresult3= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewSequinFormBoardTestReport,
                            session.query(Model.models.Application.M_SequinFormBoardTest.MSFBID.label('ID'),
                                        Model.models.Application.M_SequinFormBoardTest.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_MentalAge.label('Mental Age'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_IQ.label('IQ'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_ShortestTime.label('Shortest Time'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_TotalTime.label('Total Time'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_CorrespondsMentalAge.label('Corresponds Mental Age'),
                                        Model.models.Application.M_SequinFormBoardTest.MSFB_suggestingIntellectualfunctioning.label('Suggesting Intellectual Functioning'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MSFB_IsActive=1,MSFB_IsDeleted=0
                            ).order_by(Model.models.Application.M_SequinFormBoardTest.MSFBID.desc()).all())
                    session.commit()
                    
                    queryresult4= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewChildhoodAutismRatingScaleReport,
                            session.query(Model.models.Application.M_ChildhoodAutismRatingScale.MCARID.label('ID'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_RelatingtoPeople.label('Relating to People'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Imitation.label('Imitation'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_EmotionalResponse.label('Emotional Response'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_BodyUse.label('Body Use'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ObjectUse.label('Object Use'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_AdaptationChange.label('Daptation Change'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_VisualResponse.label('Visual Response'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ListeningResponse.label('Listening Response'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_TasteSmellUse.label('Taste Smell Use'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Fearornervousness.label('Fear or Nervousness'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Verbal.label('Verbal'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Nonverbal.label('Non Verbal'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_ActivityLevel.label('Activity Level'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Consistencyresponse.label('Consistency Response'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_GeneralImpression.label('General Impression'),
                                        Model.models.Application.M_ChildhoodAutismRatingScale.MCAR_Concludinremark.label('Concluding Remark')
                                        
                                            ).filter_by(M_AppointmentID=AID,MCAR_IsActive=1,MCAR_IsDeleted=0
                            ).order_by(Model.models.Application.M_ChildhoodAutismRatingScale.MCARID.desc()).all())
                    session.commit()
                    
                    queryresult5= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewVinelandSocialMaturityScaleReport,
                            session.query(Model.models.Application.M_VinelandSocialMaturityScale.MVAMID.label('ID'),
                                        Model.models.Application.M_VinelandSocialMaturityScale.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_VinelandSocialMaturityScale.MVAM_SocialAge.label('Social Age'),
                                        Model.models.Application.M_VinelandSocialMaturityScale.MVAM_IQ.label('Social Quotient'),
                                        Model.models.Application.M_VinelandSocialMaturityScale.MVAM_Observations.label('Observations'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MVAM_IsActive=1,MVAM_IsDeleted=0
                            ).order_by(Model.models.Application.M_VinelandSocialMaturityScale.MVAMID.desc()).all())

                    session.commit()
                    
                    queryresult6= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewGeselsDrawingTestofintelligenceReport,
                            session.query(Model.models.Application.M_GeselsDrawingTestofintelligence.MGDIID.label('ID'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAge.label('Mental Age'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_IQ.label('IQ'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAgeMonths.label('Mental Age Months'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_MentalAgeYears.label('Mental Age Years'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_IQof.label('IQ of'),
                                        Model.models.Application.M_GeselsDrawingTestofintelligence.MGDI_Depicting.label('Depicting'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MGDI_IsActive=1,MGDI_IsDeleted=0
                            ).order_by(Model.models.Application.M_GeselsDrawingTestofintelligence.MGDIID.desc()).all())
                    return jsonify(result={'SystemicExamReport':queryresult,'CognitivePrerequitesReport':queryresult1,
                                           'viewNICHQVanderbiltADHDParentReport':queryresult2,'viewSequinFormBoardTestReport':queryresult3,
                                           'viewChildhoodAutismRatingScaleReport':queryresult4,'viewVinelandSocialMaturityScaleReport':queryresult5,
                                           'viewGeselsDrawingTestofintelligenceReport':queryresult6})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/LanguageAssessment2', methods=['GET','POST'])
def LanguageAssessment2():
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
                    AID = request1.get('AID')
                    
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewMalinIntelligenceScaleforIndianChildrenReport,
                            session.query(Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISIID.label('ID'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_InformationTestScores.label('InformationTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_PictureTestScores.label('PictureTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_GeneralTestScores.label('GeneralTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_BlockDesignTestScores.label('BlockDesignTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_ArithmeticTestScores.label('ArithmeticTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_ObjectScores.label('ObjectScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_VocabularyTestScores.label('VocabularyTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_MazeTestScores.label('MazeTestScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_AnalogiesScores.label('AnalogiesScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_CodingScores.label('CodingScores'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_VQ.label('VQ'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_PQ.label('PQ'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_FullScaleIQ.label('FullScaleIQ'),
                                        Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISI_Comment.label('Comment'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MISI_IsActive=1,MISI_IsDeleted=0
                            ).order_by(Model.models.Application.M_MalinIntelligenceScaleforIndianChildren.MISIID.desc()).all())
                    session.commit()
                    
                    queryresult1= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewDevelopmentalProfileReport,
                            session.query(Model.models.Application.M_DevelopmentalProfile.MDPID.label('ID'),
                                        Model.models.Application.M_DevelopmentalProfile.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalStandardScore.label('Physical Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalDescCategory.label('Physical Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_PhysicalAgeEquivalent.label('Physical Age Equivalent'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorStandardScore.label('Adaptive Behavior Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorDescCategory.label('Adaptive Behavior Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_AdaptiveBehaviorAgeEquivalent.label('Adaptive Behavior Age Equivalent'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoStandardScore.label('Social Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoDescCategory.label('Social Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_SocialEmoAgeEquivalent.label('Social Equivalent'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveStandardScore.label('Cognitive Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveDescCategory.label('Cognitive Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CognitiveAgeEquivalent.label('Cognitive Age Equivalent'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CommStandardScore.label('Comm Standard Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CommDescCategory.label('Comm Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_CommAgeEquivalent.label('Comm Age Equivalent'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreStandardScore.label('General Dev Score'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreDescCategory.label('General Dev Category'),
                                        Model.models.Application.M_DevelopmentalProfile.MDP_GeneralDevScoreAgeEquivalent.label('General Age Equivalent')
                                        
                                            ).filter_by(M_AppointmentID=AID,MDP_IsActive=1,MDP_IsDeleted=0
                            ).order_by(Model.models.Application.M_DevelopmentalProfile.MDPID.desc()).all())
                    session.commit()
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewChildBehaviorChecklistReport,
                            session.query(Model.models.Application.M_ChildBehaviorChecklist.MCBCID.label('ID'),
                                        Model.models.Application.M_ChildBehaviorChecklist.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AnxiousScores.label('AnxiousScores'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AnxiousTscore.label('AnxiousTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AnxiousRange.label('AnxiousRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.WithdrawnScores.label('WithdrawnScores'),
                                        Model.models.Application.M_ChildBehaviorChecklist.WithdrawnTscore.label('WithdrawnTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.WithdrawnRange.label('WithdrawnRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintScores.label('SomaticComplaintScores'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintTscore.label('SomaticComplaintTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SomaticComplaintRange.label('SomaticComplaintRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SocialProblemScores.label('SocialProblemScores'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SocialProblemTscore.label('SocialProblemTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.SocialProblemRange.label('SocialProblemRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemScore.label('ThoughtProblemScore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemTscore.label('ThoughtProblemTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.ThoughtProblemRange.label('ThoughtProblemRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemScore.label('AttentionProblemScore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemTscore.label('AttentionProblemTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AttentionProblemRange.label('AttentionProblemRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorScore.label('RuleBreakingBehaviorScore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorTscore.label('RuleBreakingBehaviorTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.RuleBreakingBehaviorRange.label('RuleBreakingBehaviorRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorScores.label('AggressiveBehaviorScores'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorTscore.label('AggressiveBehaviorTscore'),
                                        Model.models.Application.M_ChildBehaviorChecklist.AggressiveBehaviorRange.label('AggressiveBehaviorRange'),
                                        Model.models.Application.M_ChildBehaviorChecklist.Comment.label('Comment')

                                        ).filter_by(M_AppointmentID=AID,MCBC_IsActive=1,MCBC_IsDeleted=0
                            ).order_by(Model.models.Application.M_ChildBehaviorChecklist.MCBCID.desc()).all())
                    session.commit()
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.ConnersParentRatingScaleReport,
                                session.query(Model.models.Application.M_ConnersParentRatingScale.MCPRID.label('ID'),
                                            Model.models.Application.M_ConnersParentRatingScale.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Scores.label('Scores'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Tscores.label('Tscores'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Range.label('Range'),
                                            Model.models.Application.M_ConnersParentRatingScale.MCPR_Observations.label('Observations'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MCPR_IsActive=1,MCPR_IsDeleted=0
                                ).order_by(Model.models.Application.M_ConnersParentRatingScale.MCPRID.desc()).all())

                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewRavenStandardProgressiveMatricesReport,
                            session.query(Model.models.Application.M_RavenStandardProgressiveMatrices.MRSPID.label('ID'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_RawScore.label('Raw Score'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Percentile.label('Percentile'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Grade.label('Grade'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_Interpretation.label('Interpretation'),
                                        Model.models.Application.M_RavenStandardProgressiveMatrices.MRSP_CorrespondsTo.label('Corresponds To'),
                                        
                                            ).filter_by(M_AppointmentID=AID,MRSP_IsActive=1,MRSP_IsDeleted=0
                            ).order_by(Model.models.Application.M_RavenStandardProgressiveMatrices.MRSPID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewStutteringAssessmentReport,
                                session.query(Model.models.Application.M_StutteringAssessment.MSAID.label('ID'),
                                            Model.models.Application.M_StutteringAssessment.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_StutteringAssessment.MSA_Behaviouralassessment.label('Behavioural assessment'),
                                            Model.models.Application.M_StutteringAssessment.MSA_Cognitiveassessment.label('Cognitive assessment'),
                                            Model.models.Application.M_StutteringAssessment.MSA_Impacteducationalparticipation.label('Impact educational participation'),
                                            Model.models.Application.M_StutteringAssessment.MSA_thechildlikelytoachieve.label('Likely to Achieve'),
                                            Model.models.Application.M_StutteringAssessment.MSA_prognosisforeffect.label('Prognosis Effect'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MSA_IsActive=1,MSA_IsDeleted=0
                                ).order_by(Model.models.Application.M_StutteringAssessment.MSAID.desc()).all())
                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.viewPragmaticSkillsReport,
                                session.query(Model.models.Application.M_PragmaticSkills.MVEFID.label('Id'),
                            Model.models.Application.M_PragmaticSkills.MPS_InitiationSkills.label('InitiationSkills'),
                            Model.models.Application.M_PragmaticSkills.MPS_RespondingSkills.label('RespondingSkills'),
                            Model.models.Application.M_PragmaticSkills.MPS_MaintenanceSkills.label('MaintenanceSkills'),
                            Model.models.Application.M_PragmaticSkills.MPS_TerminationSkills.label('TerminationSkills'),
                            Model.models.Application.M_PragmaticSkills.MPS_Observations.label('Observations')
                                ).filter_by(M_AppointmentID=AID,MPS_IsActive=1,MPS_IsDeleted=0
                                ).order_by(Model.models.Application.M_PragmaticSkills.MVEFID.desc()).all())
                    session.commit()
                    return jsonify(result={'viewMalinIntelligenceScaleforIndianChildrenReport':queryresult,'viewDevelopmentalProfileReport':queryresult1,
                                           'viewChildBehaviorChecklistReport':queryresult2,'ConnersParentRatingScaleReport':queryresult3,
                                           'viewRavenStandardProgressiveMatricesReport':queryresult4,'viewStutteringAssessmentReport':queryresult5,
                                           'viewPragmaticSkillsReport':queryresult6})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/Examination1', methods=['GET','POST'])
def Examination1():
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
                    AID = request1.get('AID')
                    queryresult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.VitalsExamReport,
                                session.query(Model.models.Application.M_VitalsExamForm.MVEFID.label('ID'),
                                            Model.models.Application.M_VitalsExamForm.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_BloodPressure.label('Blood Pressure'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_PulseRate.label('Pulse Rate'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_RespiratoryRate.label('Respiratory Rate'),
                                            Model.models.Application.M_VitalsExamForm.MVEF_Temperator.label('Temperator'),
                                            
                                                ).filter_by(M_AppointmentID=AID,MVEF_IsActive=1,MVEF_IsDeleted=0
                                ).order_by(Model.models.Application.M_VitalsExamForm.MVEFID.desc()).all())
                    # queryresult= Common_Function.CommonFun.convertToJson(
                    #             Constant.constant.constant.VitalExamReport,
                    #             session.query(Model.models.Application.M_SystemicExam.MSEID.label('ID'),
                    #                         Model.models.Application.M_SystemicExam.M_AppointmentID.label('Appointment Id'),
                    #                         Model.models.Application.M_SystemicExam.MSE_Observations.label('Observations'),
                    #                             ).filter_by(M_AppointmentID=AID,MSE_IsActive=1,MSE_IsDeleted=0
                    #             ).order_by(Model.models.Application.M_SystemicExam.MSEID.desc()).all())
                    session.commit()
                    
                    queryresult1= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.GeneralExamReport,
                                session.query(Model.models.Application.M_GeneralExamForm.MGEFID.label('ID'),
                                            Model.models.Application.M_GeneralExamForm.M_AppointmentID.label('Appointment Id'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Height.label('Height'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Weight.label('Weight'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_HeadCircumference.label('Head Circumference'),
                                            Model.models.Application.M_GeneralExamForm.MGEF_Observations.label('Observations'),

                                                ).filter_by(M_AppointmentID=AID,MGEF_IsActive=1,MGEF_IsDeleted=0
                                ).order_by(Model.models.Application.M_GeneralExamForm.MGEFID.desc()).all())
                    session.commit()
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewIndianScaleAssessmentAutismReport,
                            session.query(Model.models.Application.M_IndianScaleAssessmentAutism.MIID.label('ID'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.M_AppointmentID.label('Appointment Id'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.SOCIALRECIPROCITY.label('SOCIAL RECIPROCITY'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.EMOTIONALRESPONSIVENESS.label('EMOTIONAL RESPONSIVENESS'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.SPEECHCOMMUNICATION.label('SPEECH COMMUNICATION'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.BEHAVIOURPATTERNS.label('BEHAVIOUR PATTERNS'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.SENSORYASPECTS.label('SENSORY ASPECTS'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.COGNITIVECOMPONENT.label('COGNITIVE COMPONENT'),
                                        Model.models.Application.M_IndianScaleAssessmentAutism.FinalComment.label('Final Comment')
                                        
                                            ).filter_by(M_AppointmentID=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_IndianScaleAssessmentAutism.MIID.desc()).all())
                    session.commit()
                    
                    queryresult3= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewPerceptualAndVisualMotorAbilityReport,
                            session.query(Model.models.Application.M_PerceptualNvisual.MIID.label('ID'),
                                        Model.models.Application.M_PerceptualNvisual.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_PerceptualNvisual.VisualDiscr.label('VisualDiscr'),
                                        Model.models.Application.M_PerceptualNvisual.VisualDiscrComments.label('VisualDiscrComments'),
                                        Model.models.Application.M_PerceptualNvisual.VisualMemoryTest.label('VisualMemoryTest'),
                                        Model.models.Application.M_PerceptualNvisual.VisualMemoryTestComments.label('VisualMemoryTestComments'),
                                        Model.models.Application.M_PerceptualNvisual.AuditoryMemory.label('AuditoryMemory'),
                                        Model.models.Application.M_PerceptualNvisual.AuditoryMemoryComments.label('AuditoryMemoryComments'),
                                        Model.models.Application.M_PerceptualNvisual.Attention.label('Attention'),
                                        Model.models.Application.M_PerceptualNvisual.AttentionComments.label('AttentionComments'),
                                        Model.models.Application.M_PerceptualNvisual.DoubleNumCancel.label('DoubleNumCancel'),
                                        Model.models.Application.M_PerceptualNvisual.DoubleNumCancelComments.label('DoubleNumCancelComments'),
                                        Model.models.Application.M_PerceptualNvisual.Language.label('Language'),
                                        Model.models.Application.M_PerceptualNvisual.LanguageComments.label('LanguageComments'),
                                        Model.models.Application.M_PerceptualNvisual.Reading.label('Reading'),
                                        Model.models.Application.M_PerceptualNvisual.ReadingComments.label('ReadingComments'),
                                        Model.models.Application.M_PerceptualNvisual.Comprehension.label('Comprehension'),
                                        Model.models.Application.M_PerceptualNvisual.ComprehensionComments.label('ComprehensionComments'),
                                        Model.models.Application.M_PerceptualNvisual.Spelling.label('Spelling'),
                                        Model.models.Application.M_PerceptualNvisual.SpellingComments.label('SpellingComments'),
                                        Model.models.Application.M_PerceptualNvisual.WritingAndCopy.label('WritingAndCopy'),
                                        Model.models.Application.M_PerceptualNvisual.WritingAndCopyComments.label('WritingAndCopyComments'),
                                        Model.models.Application.M_PerceptualNvisual.WritingSkills.label('WritingSkills'),
                                        Model.models.Application.M_PerceptualNvisual.WritingSkillsComments.label('WritingSkillsComments'),
                                        Model.models.Application.M_PerceptualNvisual.ExpressiveWriting.label('ExpressiveWriting'),
                                        Model.models.Application.M_PerceptualNvisual.ExpressiveWritingComments.label('ExpressiveWritingComments'),
                                        Model.models.Application.M_PerceptualNvisual.Copying.label('Copying'),
                                        Model.models.Application.M_PerceptualNvisual.CopyingComments.label('CopyingComments'),
                                        Model.models.Application.M_PerceptualNvisual.Arithmetic.label('Arithmetic'),
                                        Model.models.Application.M_PerceptualNvisual.ArithmeticComments.label('ArithmeticComments'),
                                        
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_PerceptualNvisual.MIID.desc()).all())
                    session.commit()
                    
                    queryresult4= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewWechslerTestReport,
                            session.query(Model.models.Application.M_WechslerTest.MIID.label('ID'),
                                        Model.models.Application.M_WechslerTest.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_WechslerTest.SubsetScore.label('SubsetScore'),
                                        Model.models.Application.M_WechslerTest.ReadCompStandardScore.label('ReadCompStandardScore'),
                                        Model.models.Application.M_WechslerTest.ReadCompConfidenceInterval.label('ReadCompConfidenceInterval'),
                                        Model.models.Application.M_WechslerTest.ReadCompPercentileRank.label('ReadCompPercentileRank'),
                                        Model.models.Application.M_WechslerTest.ReadCompGradeEquivalent.label('ReadCompGradeEquivalent'),
                                        Model.models.Application.M_WechslerTest.WordReadStandardScore.label('WordReadStandardScore'),
                                        Model.models.Application.M_WechslerTest.WordReadConfidence.label('WordReadConfidence'),
                                        Model.models.Application.M_WechslerTest.WordReadPercentileRank.label('WordReadPercentileRank'),
                                        Model.models.Application.M_WechslerTest.WordReadGradeEquivalent.label('WordReadGradeEquivalent'),
                                        Model.models.Application.M_WechslerTest.EssayCompStandardScore.label('EssayCompStandardScore'),
                                        Model.models.Application.M_WechslerTest.EssayCompConfidence.label('EssayCompConfidence'),
                                        Model.models.Application.M_WechslerTest.EssayCompPercentileRank.label('EssayCompPercentileRank'),
                                        Model.models.Application.M_WechslerTest.EssayCompGradeEquivalent.label('EssayCompGradeEquivalent'),
                                        Model.models.Application.M_WechslerTest.NumOperStandardScore.label('NumOperStandardScore'),
                                        Model.models.Application.M_WechslerTest.NumOperConfidence.label('NumOperConfidence'),
                                        Model.models.Application.M_WechslerTest.NumOperPercentileRank.label('NumOperPercentileRank'),
                                        Model.models.Application.M_WechslerTest.NumOperGradeEquivalent.label('NumOperGradeEquivalent'),
                                        Model.models.Application.M_WechslerTest.SpelStandardScore.label('SpelStandardScore'),
                                        Model.models.Application.M_WechslerTest.SpelConfidence.label('SpelConfidence'),
                                        Model.models.Application.M_WechslerTest.SpelPercentileRank.label('SpelPercentileRank'),
                                        Model.models.Application.M_WechslerTest.SpelGradeEquivalent.label('SpelGradeEquivalent'),
                                        Model.models.Application.M_WechslerTest.Comment.label('Comment'),
                                        Model.models.Application.M_WechslerTest.MathematicsComment.label('MathematicsComment'),
                                        Model.models.Application.M_WechslerTest.WrittenExpComment.label('WrittenExpComment'),
                                        
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_WechslerTest.MIID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewHumanFormDrawingtestReport,
                            session.query(Model.models.Application.M_HumanFormDrawingtest.MIID.label('ID'),
                                        Model.models.Application.M_HumanFormDrawingtest.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_HumanFormDrawingtest.findings.label('findings'),
                                        Model.models.Application.M_HumanFormDrawingtest.indicators.label('indicators'),
                                        Model.models.Application.M_HumanFormDrawingtest.comment.label('comment')
                                        
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_HumanFormDrawingtest.MIID.desc()).all())
                    session.commit()
                    queryresult6= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewHumanTreePersonTestReport,
                            session.query(Model.models.Application.M_HumanTreePersonTest.MIID.label('ID'),
                                        Model.models.Application.M_HumanTreePersonTest.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_HumanTreePersonTest.findings.label('findings'),
                                        Model.models.Application.M_HumanTreePersonTest.indicators.label('indicators'),
                                        Model.models.Application.M_HumanTreePersonTest.comment.label('comment')
                                        
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_HumanTreePersonTest.MIID.desc()).all())
                    session.commit()
                    return jsonify(result={'VisitReasonReport':queryresult,'GeneralExamReport':queryresult1,
                                           'viewIndianScaleAssessmentAutismReport':queryresult2,'viewPerceptualAndVisualMotorAbilityReport':queryresult3,
                                           'viewWechslerTestReport':queryresult4,'viewHumanFormDrawingtestReport':queryresult5,
                                           'viewHumanTreePersonTestReport':queryresult6})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/Examination2', methods=['GET','POST'])
def Examination2():
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
                    AID = request1.get('AID')
                    
                    queryresult= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewChildAnxietyRelatedDisordersReport,
                            session.query(Model.models.Application.M_ChildAnxietyRelatedDisorders.MIID.label('ID'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.PanicDisScore.label('PanicDisorderScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.GenAnxietyDisScore.label('GeneralizedAnxietyDisorderScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.SepAnxietyDisScore.label('SeparationAnxietyDisorderScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.SocialAnxietyDisScore.label('SocialAnxietyDisorderScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.SchoolAvoidScore.label('SchoolAvoidanceScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.AnxietyDisScore.label('AnxietyDisorderScore'),
                                        Model.models.Application.M_ChildAnxietyRelatedDisorders.Comment.label('Comment'),
                                        
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_ChildAnxietyRelatedDisorders.MIID.desc()).all())

                    session.commit()
                    queryresult1= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewDSMVCriteriaReport,
                            session.query(Model.models.Application.M_DSMVCriteria.MIID.label('ID'),
                                        Model.models.Application.M_DSMVCriteria.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_DSMVCriteria.ACriteria.label('ACriteria'),
                                        Model.models.Application.M_DSMVCriteria.ACriteriaComment.label('ACriteriaComment'),
                                        Model.models.Application.M_DSMVCriteria.BCriteria.label('BCriteria'),
                                        Model.models.Application.M_DSMVCriteria.BCriteriaComment.label('BCriteriaComment'),
                                        Model.models.Application.M_DSMVCriteria.CCriteria.label('CCriteria'),
                                        Model.models.Application.M_DSMVCriteria.CCriteriaComment.label('CCriteriaComment'),
                                        Model.models.Application.M_DSMVCriteria.DCriteria.label('DCriteria'),
                                        Model.models.Application.M_DSMVCriteria.DCriteriaComment.label('DCriteriaComment'),
                                        Model.models.Application.M_DSMVCriteria.Question5.label('Question5'),
                                        Model.models.Application.M_DSMVCriteria.Question5Comment.label('Question5Comment'),
                                        Model.models.Application.M_DSMVCriteria.Question6.label('Question6'),
                                        Model.models.Application.M_DSMVCriteria.Question6Comment.label('Question6Comment'),
                                        Model.models.Application.M_DSMVCriteria.Question7.label('Question7'),
                                        Model.models.Application.M_DSMVCriteria.Question7Comment.label('Question7Comment'),
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_DSMVCriteria.MIID.desc()).all())
                    
                    queryresult2= Common_Function.CommonFun.convertToJson(
                            Constant.constant.constant.viewEpidemiologicalStudiesDepressionScaleReport,
                            session.query(Model.models.Application.M_EpidemiologicalStudiesDepression.MIID.label('ID'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.MI_AppointmentId.label('Appointment Id'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.NotAtAllScore.label('NotAtAllScore'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.ALittleScore.label('ALittleScore'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.SomeScore.label('SomeScore'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.ALotScore.label('ALotScore'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.TotalRawScore.label('TotalRawScore'),
                                        Model.models.Application.M_EpidemiologicalStudiesDepression.Comment.label('Comment')
                                            ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                            ).order_by(Model.models.Application.M_EpidemiologicalStudiesDepression.MIID.desc()).all())

                    session.commit()
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DSMVASDCriteriaReport,
                                session.query(Model.models.Application.M_DSMVASDCriteria.persistentDeficit.label('persistentDeficit'),
                                            Model.models.Application.M_DSMVASDCriteria.persistentDeficitComment.label('persistentDeficitComment'),
                                            Model.models.Application.M_DSMVASDCriteria.restrictedRepetitive.label('restrictedRepetitive'),
                                            Model.models.Application.M_DSMVASDCriteria.restrictedRepetitiveComment.label('restrictedRepetitiveComment'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsMust.label('symptomsMust'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsMustComment.label('symptomsMustComment'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsCause.label('symptomsCause'),
                                            Model.models.Application.M_DSMVASDCriteria.symptomsCauseComment.label('symptomsCauseComment'),
                                            Model.models.Application.M_DSMVASDCriteria.theseDisturbances.label('theseDisturbances'),
                                            Model.models.Application.M_DSMVASDCriteria.theseDisturbancesComment.label('theseDisturbancesComment'),
                                            Model.models.Application.M_DSMVASDCriteria.question7.label('question7'),
                                            Model.models.Application.M_DSMVASDCriteria.question7Comment.label('question7Comment'),
                                            Model.models.Application.M_DSMVASDCriteria.MDCID.label('Id')
                                                ).filter_by(MI_AppointmentId=AID,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_DSMVASDCriteria.MDCID.desc()).all())

                    session.commit()
                    queryresult4= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.DSMVADHDCriteriaReport,
                                session.query(Model.models.Application.M_DSMVADHDCriteria.MDID.label('ID'),
                                            Model.models.Application.M_DSMVADHDCriteria.MI_AppointmentId.label('Appointment Id'),
                                            Model.models.Application.M_DSMVADHDCriteria.APersistent.label('APersistent'),
                                            Model.models.Application.M_DSMVADHDCriteria.BSeveral.label('BSeveral'),
                                            Model.models.Application.M_DSMVADHDCriteria.CSeveral.label('CSeveral'),
                                            Model.models.Application.M_DSMVADHDCriteria.Combinedpresentation.label('Combinedpresentation'),
                                            Model.models.Application.M_DSMVADHDCriteria.DThere.label('DThere'),
                                            Model.models.Application.M_DSMVADHDCriteria.Ethesymptoms.label('Ethesymptoms'),
                                            Model.models.Application.M_DSMVADHDCriteria.Predominantly.label('Predominantly'),
                                                ).filter_by(IsActive=1,IsDeleted=0,MI_AppointmentId=AID
                                                
                                ).order_by(Model.models.Application.M_DSMVADHDCriteria.MDID.desc()).all())
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SocialResponsivenessScaleReport,
                                session.query(Model.models.Application.M_SocialResponsivenessScale.MSID.label('ID'),
                                            Model.models.Application.M_SocialResponsivenessScale.MI_AppointmentId.label('Appointment Id'),
                                            Model.models.Application.M_SocialResponsivenessScale.SCIRawScore.label('SCIRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.SCITscore.label('SCITscore'),
                                            Model.models.Application.M_SocialResponsivenessScale.BehaviorsRawScore.label('BehaviorsRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.BehaviorsTscore.label('BehaviorsTscore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialAwarenessRawScore.label('socialAwarenessRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialAwarenessTscore.label('socialAwarenessTscore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialCognitionRawScore.label('socialCognitionRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialCognitionTscore.label('socialCognitionTscore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialCommunicationRawScore.label('socialCommunicationRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialCommunicationTscore.label('socialCommunicationTscore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialMotivationRawScore.label('socialMotivationRawScore'),
                                            Model.models.Application.M_SocialResponsivenessScale.socialMotivationTscore.label('socialMotivationTscore'),
                                                ).filter_by(IsActive=1,IsDeleted=0,MI_AppointmentId=AID
                                                
                                ).order_by(Model.models.Application.M_SocialResponsivenessScale.MSID.desc()).all())
                    session.commit()
                    return jsonify(result={'viewChildAnxietyRelatedDisordersReport':queryresult,'viewDSMVCriteriaReport':queryresult1,
                                           'viewEpidemiologicalStudiesDepressionScaleReport':queryresult2,'DSMVASDCriteriaReport':queryresult3,
                                           'DSMVADHDCriteriaReport':queryresult4,'SocialResponsivenessScaleReport':queryresult5})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Report_Blueprint.route('/MiscReport', methods=['GET','POST'])
def MiscReport():
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
                    AID = request1.get('AID')
                    
                    StartedDtl = session.query(Model.models.Application.T_Details.TD_Name.label('StartedDl'),
                                          Model.models.Application.T_Details.TDID.label('IDs')).subquery()
                    todayfeelDtl = session.query(Model.models.Application.T_Details.TD_Name.label('todayfeelDl'),
                                                Model.models.Application.T_Details.TDID.label('IDs')).subquery()
                    queryResult= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.SessionNotesReport,
                                session.query(Model.models.Application.M_SessionNotes.MSN_started.label('Staed'),
                                Model.models.Application.M_SessionNotes.M_AppointmentID.label('AppointmentId'),
                                StartedDtl.c.StartedDl.label('Started'),
                                todayfeelDtl.c.todayfeelDl.label('todayfeel'),
                                
                                            Model.models.Application.M_SessionNotes.MSN_todayfeeling.label('todaeel'),
                                            Model.models.Application.M_SessionNotes.MSN_dotoday.label('dotod'),
                                            Model.models.Application.T_Details.TD_Name.label('dotoday'),
                                            Model.models.Application.M_SessionNotes.MSN_Notes.label('Notes'),
                                            sqlalchemy.func.date_format(Model.models.Application.M_SessionNotes.MSN_AddDate,'%d-%b-%Y').label('Date'),
                                            ).filter_by(MSN_IsActive=1,MSN_IsDeleted=0,M_AppointmentID=AID
                                            ).join(Model.models.Application.T_Details, Model.models.Application.T_Details.TDID==Model.models.Application.M_SessionNotes.MSN_dotoday       
                                            ).outerjoin(StartedDtl, StartedDtl.c.IDs==Model.models.Application.M_SessionNotes.MSN_todayfeeling
                                            ).outerjoin(todayfeelDtl, todayfeelDtl.c.IDs==Model.models.Application.M_SessionNotes.MSN_started
                                            ).all()
                                        )
                    session.commit()
                    
                    queryResult1= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.ProvisionalDiagnosisReport,
                        session.query(Model.models.Application.M_ProvisionalDiagnosis.MPD_ProvisionalDiagnosis.label('ProvisionalDiagnosis'),
                                    Model.models.Application.M_ProvisionalDiagnosis.M_AppointmentID.label('AppointmentId'),
                                    Model.models.Application.M_ProvisionalDiagnosis.MPD_ICDCode.label('ICDCode'),
                                    Model.models.Application.M_ProvisionalDiagnosis.MPD_ICDDescription.label('ICDDescription'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_ProvisionalDiagnosis.MPD_AddDate,'%d-%b-%Y').label('Date'),
                                    ).filter_by(MPD_IsActive=1,MPD_IsDeleted=0,M_AppointmentID=AID,MPD_ShowDtl=1
                                    ).all()
                                )
                    session.commit()
                    queryresult4= session.query(Model.models.Application.M_PatientReview.MPDID.label('ID'),
                                            Model.models.Application.M_PatientReview.M_AppointmentID,
                                            Model.models.Application.M_PatientReview.MPR_FollowDate,
                                            sqlalchemy.func.date_format(Model.models.Application.M_PatientReview.MPR_FollowDate,'%d-%b-%Y').label('Date')
                                            ).filter_by(M_AppointmentID=AID,MPR_IsActive=1,MPR_IsDeleted=0
                                            ).order_by(Model.models.Application.M_PatientReview.MPDID.desc()).all()
                    if(len(queryresult4)>0):
                        followdate = queryresult4[0].Date
                        # return jsonify(result={'Follow Date':queryresult[0].Date})
                    else:
                        followdate = ''
                        # return jsonify(result={'Follow Date':''})
                    queryresult3= Common_Function.CommonFun.convertToJson(
                                Constant.constant.constant.getPatientDetailFromAppointment,
                                session.query(Model.models.Application.M_Appointment.MAID.label('AppointId'),
                                    Model.models.Application.M_Appointment.M_Patient_MPID.label('Pid'),
                                    Model.models.Application.M_Appointment.MP_Procedure.label('procedure'),
                                    Model.models.Application.M_Appointment.MA_Date.label('date'),
                                    Model.models.Application.M_Appointment.MA_Time.label('time'),
                                    Model.models.Application.M_Appointment.MP_Duration.label('duration'),
                                    Model.models.Application.M_Appointment.M_DoctorDetails_MDDID.label('doctor'),
                                    Model.models.Application.M_Patient.MP_Name.label('Patient'),
                                    Model.models.Application.M_Patient.MP_Mobile.label('Mobile'),
                                    Model.models.Application.M_Patient.MP_Address.label('Address'),
                                    Model.models.Application.M_Patient.MP_DOB.label('DOB'),
                                    Model.models.Application.M_Patient.MP_UHID.label('UHID'),
                                    Model.models.Application.M_Patient.MP_Email.label('Email'),
                                    Model.models.Application.M_DoctorDetails.MDD_FirstName.label('Doctor Name'),
                                    Model.models.Application.M_Branch.MB_Name.label('Branch'),
                                    Model.models.Application.T_Details.TD_Name.label('Gender'),
                                    
                                        ).filter_by(MAID=AID,MP_IsActive=1,MP_IsDeleted=0
                                    ).join(Model.models.Application.M_Patient,Model.models.Application.M_Patient.MPID==Model.models.Application.M_Appointment.M_Patient_MPID
                                    ).join(Model.models.Application.M_DoctorDetails,Model.models.Application.M_DoctorDetails.MDDID==Model.models.Application.M_Appointment.M_DoctorDetails_MDDID
                                    ).join(Model.models.Application.M_Branch,Model.models.Application.M_Branch.MBID==Model.models.Application.M_Appointment.M_Branch_MBID
                                    ).outerjoin(Model.models.Application.T_Details,Model.models.Application.T_Details.TDID==Model.models.Application.M_Patient.MP_Gender
                                    ).all()
                        )
                    session.commit()
                    queryresult5= Common_Function.CommonFun.convertToJson(
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
                                            ).filter_by(MP_IsActive=1,MP_IsDeleted=0,MAID=AID
                                            
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
                        ).filter(Model.models.Application.M_Prescription.M_AppointmentID == AID,
                        Model.models.Application.M_Prescription.MP_Prescription==None
                        ).filter_by(ShowData=1,MP_IsDeleted=0).all())
                                    
                    session.commit()
                    Prescrip1 = session.query(Model.models.Application.M_Prescription.MP_Prescription,
                            ).filter(Model.models.Application.M_Prescription.M_AppointmentID == AID,
                                     Model.models.Application.M_Prescription.MP_Prescription.is_not(None)
                                     
                            ).filter_by(MP_IsDeleted=0).all()
                                       
                    session.commit()
                    if(len(Prescrip1)>0): 
                        test = Prescrip1[0].MP_Prescription
                        queryresult5[0]['Desc']=test
                    queryresult5[0]['Prescription']=Prescrip
                    queryresult2 = queryresult5
                    return jsonify(result={'SessionNotesReport':queryResult,'ProvisionalDiagnosisReport':queryResult1,
                                           'getFollowUpDate':followdate,'getPrescriptionDtl':queryresult2,
                                           'getPatientDetailFromAppointment':queryresult3})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

