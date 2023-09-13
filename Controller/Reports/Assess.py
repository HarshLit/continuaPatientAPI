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
Assess_Blueprint = CommonModule.flask.Blueprint(
    'Assess_Blueprint', import_name=__name__)

@Assess_Blueprint.route('/submitGrossMotorForm', methods=['GET','POST'])
def submitGrossMotorForm():

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
                    question4B = request_json.get('question4B')
                    question4C = request_json.get('question4C')
                    
                    grossmotor3yes = request_json.get('grossMotor0To3Yes')
                    grossmotor3no = request_json.get('grossMotor0To3No')
                    grossmotor6yes = request_json.get('grossMotor3To6Yes')
                    grossmotor6no = request_json.get('grossMotor3To6No')
                    grossmotor9yes = request_json.get('grossMotor6To9Yes')
                    grossmotor9no = request_json.get('grossMotor6To9No')
                    grossmotor12yes = request_json.get('grossMotor9To12Yes')
                    grossmotor12no = request_json.get('grossMotor9To12No')
                    grossmotor18yes = request_json.get('grossMotor12To18Yes')
                    grossmotor18no = request_json.get('grossMotor12To18No')
                    grossmotor24yes = request_json.get('grossMotor18To24Yes')
                    grossmotor24no = request_json.get('grossMotor18To24No')
                    grossmotor30yes = request_json.get('grossMotor24To30Yes')
                    grossmotor30no = request_json.get('grossMotor24To30No')
                    grossmotor36yes = request_json.get('grossMotor30To36Yes')
                    grossmotor36no = request_json.get('grossMotor30To36No')
                    grossmotor42yes = request_json.get('grossMotor36To42Yes')
                    grossmotor42no = request_json.get('grossMotor36To42No')
                    grossmotor48yes = request_json.get('grossMotor42To48Yes')
                    grossmotor48no = request_json.get('grossMotor42To48No')
                    grossmotor54yes = request_json.get('grossMotor48To54Yes')
                    grossmotor54no = request_json.get('grossMotor48To54No')
                    grossmotor60yes = request_json.get('grossMotor54To60Yes')
                    grossmotor60no = request_json.get('grossMotor54To60No')


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKGrossmotor()
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
                    Insert.Rollsfrombacktofront=question4B
                    Insert.Sittingsupportstarts=question4C
                    
                    Insert.grossmotor3yes=grossmotor3yes
                    Insert.grossmotor3no =grossmotor3no 
                    Insert.grossmotor6yes=grossmotor6yes
                    Insert.grossmotor6no=grossmotor6no
                    Insert.grossmotor9yes=grossmotor9yes
                    Insert.grossmotor9no=grossmotor9no
                    Insert.grossmotor12yes=grossmotor12yes
                    Insert.grossmotor12no=grossmotor12no
                    Insert.grossmotor18yes=grossmotor18yes
                    Insert.grossmotor18no=grossmotor18no
                    Insert.grossmotor24yes=grossmotor24yes
                    Insert.grossmotor24no=grossmotor24no
                    Insert.grossmotor30yes=grossmotor30yes
                    Insert.grossmotor30no=grossmotor30no
                    Insert.grossmotor36yes=grossmotor36yes
                    Insert.grossmotor36no=grossmotor36no
                    Insert.grossmotor42yes=grossmotor42yes
                    Insert.grossmotor42no=grossmotor42no
                    Insert.grossmotor48yes=grossmotor48yes
                    Insert.grossmotor48no=grossmotor48no
                    Insert.grossmotor54yes=grossmotor54yes
                    Insert.grossmotor54no=grossmotor54no
                    Insert.grossmotor60yes=grossmotor60yes
                    Insert.grossmotor60no=grossmotor60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Gross Motor Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewGrossMotorForm', methods=['GET','POST'])
def viewGrossMotorForm():
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
                                Constant.constant.constant.viewGrossMotorForm,
                                session.query(Model.models.Application.M_CKGrossmotor.CKGID.label('ID'),
                                            Model.models.Application.M_CKGrossmotor.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor3no.label('grossmotor03no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor6no.label('grossmotor36no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor9no.label('grossmotor69no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor12no.label('grossmotor12no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor18no.label('grossmotor1218no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor24no.label('grossmotor1824no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor30no.label('grossmotor2430no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor36no.label('grossmotor3036no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor42no.label('grossmotor3642no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor48no.label('grossmotor4248no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor54no.label('grossmotor4854no'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKGrossmotor.grossmotor60no.label('grossmotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKGrossmotor.CKGID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()
              
@Assess_Blueprint.route('/submitCKSelfHelp', methods=['GET','POST'])
def submitCKSelfHelp():

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
                    question108 = request_json.get('question108')
                    
                    selfhelp3yes = request_json.get('selfHelp0To3Yes')
                    selfhelp3no = request_json.get('selfHelp0To3No')
                    selfhelp6yes = request_json.get('selfHelp3To6Yes')
                    selfhelp6no = request_json.get('selfHelp3To6No')
                    selfhelp9yes = request_json.get('selfHelp6To9Yes')
                    selfhelp9no = request_json.get('selfHelpTo9No')
                    selfhelp12yes = request_json.get('selfHelp9To12Yes')
                    selfhelp12no = request_json.get('selfHelp9To12No')
                    selfhelp18yes = request_json.get('selfHelp12To18Yes')
                    selfhelp18no = request_json.get('selfHelp12To18No')
                    selfhelp24yes = request_json.get('selfHelp18To24Yes')
                    selfhelp24no = request_json.get('selfHelp18To24No')
                    selfhelp30yes = request_json.get('selfHelp24To30Yes')
                    selfhelp30no = request_json.get('selfHelp24To30No')
                    selfhelp36yes = request_json.get('selfHelp30To36Yes')
                    selfhelp36no = request_json.get('selfHelp30To36No')
                    selfhelp42yes = request_json.get('selfHelp36To42Yes')
                    selfhelp42no = request_json.get('selfHelp36To42No')
                    selfhelp48yes = request_json.get('selfHelp42To48Yes')
                    selfhelp48no = request_json.get('selfHelp42To48No')
                    selfhelp54yes = request_json.get('selfHelp48To54Yes')
                    selfhelp54no = request_json.get('selfHelp48To54No')
                    selfhelp60yes = request_json.get('selfHelp54To60Yes')
                    selfhelp60no = request_json.get('selfHelp54To60No')

                    
                    


                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKSelfhelp()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.Turnsheadtowardssound=question73
                    Insert.Opensmouthatthesiteofbreast=question74
                    Insert.Suckingestablished=question75
                    Insert.Gumsmouthspureedfood=question76
                    Insert.Placeshandsonbottle=question77
                    Insert.Drinksfromcupwhen=question78
                    Insert.Canholdownbottle=question79
                    Insert.Canholdabiscuittofeed=question80
                    Insert.Biteschewsfood=question81
                    Insert.Cooperateswithdressing=question82
                    Insert.Fingerfeedspartofmeal=question83
                    Insert.Takesoffshoescapetc=question84
                    Insert.Removessocksshoes=question85
                    Insert.Putsspooninmouth=question86
                    Insert.Attemptstobrushownhair=question87
                    Insert.Opensdoorusingsknob=question88
                    Insert.Takesoffclotheswithoutbuttons=question89
                    Insert.Pullsoffpants=question90
                    Insert.Washeshands=question91
                    Insert.Putsthingsaway=question92
                    Insert.Brushesteethwithassistance=question93
                    Insert.Poursliquidfromonecontainer=question94
                    Insert.Independenteating=question95
                    Insert.Putsonshoeswithoutlaces=question96
                    Insert.Unbuttons=question97
                    Insert.Goestotoiletalone=question98
                    Insert.Washesafterbowelmovement=question99
                    Insert.Washesfaceonhisown=question100
                    Insert.Brushesteethalone=question101
                    Insert.Buttons=question102
                    Insert.Usesforkwell=question103
                    Insert.Spreadswithknife=question104
                    Insert.Independentdressing=question105
                    Insert.BathesIndependently=question106
                    Insert.Combshair=question107
                    Insert.Looksbothwaysatstreet=question108
                    
                    Insert.selfhelp3yes=selfhelp3yes
                    Insert.selfhelp3no =selfhelp3no 
                    Insert.selfhelp6yes=selfhelp6yes
                    Insert.selfhelp6no=selfhelp6no
                    Insert.selfhelp9yes=selfhelp9yes
                    Insert.selfhelp9no=selfhelp9no
                    Insert.selfhelp12yes=selfhelp12yes
                    Insert.selfhelp12no=selfhelp12no
                    Insert.selfhelp18yes=selfhelp18yes
                    Insert.selfhelp18no=selfhelp18no
                    Insert.selfhelp24yes=selfhelp24yes
                    Insert.selfhelp24no=selfhelp24no
                    Insert.selfhelp30yes=selfhelp30yes
                    Insert.selfhelp30no=selfhelp30no
                    Insert.selfhelp36yes=selfhelp36yes
                    Insert.selfhelp36no=selfhelp36no
                    Insert.selfhelp42yes=selfhelp42yes
                    Insert.selfhelp42no=selfhelp42no
                    Insert.selfhelp48yes=selfhelp48yes
                    Insert.selfhelp48no=selfhelp48no
                    Insert.selfhelp54yes=selfhelp54yes
                    Insert.selfhelp54no=selfhelp54no
                    Insert.selfhelp60yes=selfhelp60yes
                    Insert.selfhelp60no=selfhelp60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Self Help Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewSelfHelpForm', methods=['GET','POST'])
def viewSelfHelpForm():
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
                                Constant.constant.constant.viewSelfHelpForm,
                                session.query(Model.models.Application.M_CKSelfhelp.CKSID.label('ID'),
                                            Model.models.Application.M_CKSelfhelp.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp3no.label('selfhelp03no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp6no.label('selfhelp36no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp9no.label('selfhelp69no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp12no.label('selfhelp12no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp18no.label('selfhelp1218no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp24no.label('selfhelp1824no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp30no.label('selfhelp2430no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp36no.label('selfhelp3036no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp42no.label('selfhelp3642no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp48no.label('selfhelp4248no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp54no.label('selfhelp4854no'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKSelfhelp.selfhelp60no.label('selfhelp5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKSelfhelp.CKSID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()


@Assess_Blueprint.route('/submitCKFinemotor', methods=['GET','POST'])
def submitCKFinemotor():

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
                    
                    finemotor3yes = request_json.get('fineMotor0To3Yes')
                    finemotor3no = request_json.get('fineMotor0To3No')
                    finemotor6yes = request_json.get('fineMotor3To6Yes')
                    finemotor6no = request_json.get('fineMotorTo6No')
                    finemotor9yes = request_json.get('fineMotor6To9Yes')
                    finemotor9no = request_json.get('fineMotor6To9No')
                    finemotor12yes = request_json.get('fineMotor9To12Yes')
                    finemotor12no = request_json.get('fineMotor9To12No')
                    finemotor18yes = request_json.get('fineMotor12To18Yes')
                    finemotor18no = request_json.get('fineMotor12To18No')
                    finemotor24yes = request_json.get('fineMotor18To24Yes')
                    finemotor24no = request_json.get('fineMotor18To24No')
                    finemotor30yes = request_json.get('fineMotor24To30Yes')
                    finemotor30no = request_json.get('fineMotor24To30No')
                    finemotor36yes = request_json.get('fineMotor30To36Yes')
                    finemotor36no = request_json.get('fineMotor30To36No')
                    finemotor42yes = request_json.get('fineMotor36To42Yes')
                    finemotor42no = request_json.get('fineMotor36To42No')
                    finemotor48yes = request_json.get('fineMotor42To48Yes')
                    finemotor48no = request_json.get('fineMotor42To48No')
                    finemotor54yes = request_json.get('fineMotor48To54Yes')
                    finemotor54no = request_json.get('fineMotor48To54No')
                    finemotor60yes = request_json.get('fineMotor54To60Yes')
                    finemotor60no = request_json.get('fineMotor54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKFinemotor()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.Handsunfisted=question37
                    Insert.Watchesmovement=question38
                    Insert.Whenrattleifplaced=question39
                    Insert.Dropsoneobjectfrom=question40
                    Insert.Abletoholdobjects=question41
                    Insert.Reachesdanglingobjects=question42
                    Insert.pickupobjectsofsmallsize=question43
                    Insert.Canbangtoysontable=question44
                    Insert.Cantransferobjectfromonehandtoanother=question45
                    Insert.Scribblesafterdemonstration=question46
                    Insert.Canholdacrayon=question47
                    Insert.Attemptsputtingoneblock=question48
                    Insert.Makesfourblocktower=question49
                    Insert.Places10blocksinacontainer=question50
                    Insert.Crudelycopiesverticallines=question51
                    Insert.Makesasinglelinetrain=question52
                    Insert.Imitatescircle=question53
                    Insert.Imitateshorizontalline=question54
                    Insert.Stringslargebeadsawkwardly=question55
                    Insert.Unscrewsjarlid=question56
                    Insert.Turnspaperpages=question57
                    Insert.Copiescircle=question58
                    Insert.Cutswithscissors=question59
                    Insert.Stringssmallbeadswell=question60
                    Insert.Imitatescomplexfigureswithblocks=question61
                    Insert.Canusescissorsinabetterway=question62
                    Insert.Washeshandonhisown=question63
                    Insert.Copiessquare=question64
                    Insert.Tiessingleknot=question65
                    Insert.Writespartoffirstname=question66
                    Insert.Putspapercliponpaper=question67
                    Insert.Canuseclothespins=question68
                    Insert.Cutswithscissors=question69
                    Insert.Buildsstairsfrommodel=question70
                    Insert.Drawsdiamond=question71
                    Insert.Writesfirstandlastname=question72
                    
                    Insert.finemotor3yes=finemotor3yes
                    Insert.finemotor3no =finemotor3no 
                    Insert.finemotor6yes=finemotor6yes
                    Insert.finemotor6no=finemotor6no
                    Insert.finemotor9yes=finemotor9yes
                    Insert.finemotor9no=finemotor9no
                    Insert.finemotor12yes=finemotor12yes
                    Insert.finemotor12no=finemotor12no
                    Insert.finemotor18yes=finemotor18yes
                    Insert.finemotor18no=finemotor18no
                    Insert.finemotor24yes=finemotor24yes
                    Insert.finemotor24no=finemotor24no
                    Insert.finemotor30yes=finemotor30yes
                    Insert.finemotor30no=finemotor30no
                    Insert.finemotor36yes=finemotor36yes
                    Insert.finemotor36no=finemotor36no
                    Insert.finemotor42yes=finemotor42yes
                    Insert.finemotor42no=finemotor42no
                    Insert.finemotor48yes=finemotor48yes
                    Insert.finemotor48no=finemotor48no
                    Insert.finemotor54yes=finemotor54yes
                    Insert.finemotor54no=finemotor54no
                    Insert.finemotor60yes=finemotor60yes
                    Insert.finemotor60no=finemotor60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Fine Motor Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewFineMotorForm', methods=['GET','POST'])
def viewFineMotorForm():
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
                                Constant.constant.constant.viewFineMotorForm,
                                session.query(Model.models.Application.M_CKFinemotor.CKGID.label('ID'),
                                            Model.models.Application.M_CKFinemotor.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKFinemotor.finemotor3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor3no.label('finemotor03no'),
                                            Model.models.Application.M_CKFinemotor.finemotor6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor6no.label('finemotor36no'),
                                            Model.models.Application.M_CKFinemotor.finemotor9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor9no.label('finemotor69no'),
                                            Model.models.Application.M_CKFinemotor.finemotor12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor12no.label('finemotor12no'),
                                            Model.models.Application.M_CKFinemotor.finemotor18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKFinemotor.finemotor24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKFinemotor.finemotor30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKFinemotor.finemotor36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKFinemotor.finemotor42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKFinemotor.finemotor48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKFinemotor.finemotor54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKFinemotor.finemotor60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKFinemotor.finemotor60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKFinemotor.CKGID.desc()).all())


                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/submitCKProblemSolving', methods=['GET','POST'])
def submitCKProblemSolving():

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
                    
                    question37 = request_json.get('question109')
                    question38 = request_json.get('question110')
                    question39 = request_json.get('question111')
                    question40 = request_json.get('question112')
                    question41 = request_json.get('question113')
                    question42 = request_json.get('question114')
                    question43 = request_json.get('question115')
                    question44 = request_json.get('question116')
                    question45 = request_json.get('question117')
                    question46 = request_json.get('question118')
                    question47 = request_json.get('question119')
                    question48 = request_json.get('question120')
                    question49 = request_json.get('question121')
                    question50 = request_json.get('question122')
                    question51 = request_json.get('question123')
                    question52 = request_json.get('question124')
                    question53 = request_json.get('question125')
                    question54 = request_json.get('question126')
                    question55 = request_json.get('question127')
                    question56 = request_json.get('question128')
                    question57 = request_json.get('question129')
                    question58 = request_json.get('question130')
                    question59 = request_json.get('question131')
                    question60 = request_json.get('question132')
                    question61 = request_json.get('question133')
                    question62 = request_json.get('question134')
                    question63 = request_json.get('question135')
                    question64 = request_json.get('question136')
                    question65 = request_json.get('question137')
                    question66 = request_json.get('question138')
                    question67 = request_json.get('question139')
                    question68 = request_json.get('question140')
                    question69 = request_json.get('question141')
                    question70 = request_json.get('question142')
                    question71 = request_json.get('question143')
                    question72 = request_json.get('question144')
                    
                    problem3yes = request_json.get('problemSolving0To3Yes')
                    problem3no = request_json.get('problemSolving0To3No')
                    problem6yes = request_json.get('problemSolving3To6Yes')
                    problem6no = request_json.get('problemSolvingTo6No')
                    problem9yes = request_json.get('problemSolving6To9Yes')
                    problem9no = request_json.get('problemSolving6To9No')
                    problem12yes = request_json.get('problemSolving9To12Yes')
                    problem12no = request_json.get('problemSolving9To12No')
                    problem18yes = request_json.get('problemSolving12To18Yes')
                    problem18no = request_json.get('problemSolving12To18No')
                    problem24yes = request_json.get('problemSolving18To24Yes')
                    problem24no = request_json.get('problemSolving18To24No')
                    problem30yes = request_json.get('problemSolving24To30Yes')
                    problem30no = request_json.get('problemSolving24To30No')
                    problem36yes = request_json.get('problemSolving30To36Yes')
                    problem36no = request_json.get('problemSolving30To36No')
                    problem42yes = request_json.get('problemSolving36To42Yes')
                    problem42no = request_json.get('problemSolving36To42No')
                    problem48yes = request_json.get('problemSolving42To48Yes')
                    problem48no = request_json.get('problemSolving42To48No')
                    problem54yes = request_json.get('problemSolving48To54Yes')
                    problem54no = request_json.get('problemSolving48To54No')
                    problem60yes = request_json.get('problemSolving54To60Yes')
                    problem60no = request_json.get('problemSolving54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKProblemSolving()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.Reachesforface=question37
                    Insert.Followsdanglingobjectsfrom=question38
                    Insert.Looksatobjectsinmidline=question39
                    Insert.Touchesreflectioninmirror=question40
                    Insert.Removesclothonface=question41
                    Insert.Bangsandshakestoys=question42
                    Insert.Imitatessimpleacts=question43
                    Insert.Patsimageofselfinmirror=question44
                    Insert.Reachespersistentlyforobjects=question45
                    Insert.Couldlocaliseahiddentoy=question46
                    Insert.Looksatpicturesinbook=question47
                    Insert.Rattlesspoonincup=question48
                    Insert.Dumpspelletoutofbottle=question49
                    Insert.Turnspagesinbook=question50
                    Insert.Findstoyobservedtobehidden=question51
                    Insert.Matchesobjectstopictures=question52
                    Insert.Sortsobjects=question53
                    Insert.Showsuseoffamiliarobjects=question54
                    Insert.Matchesshapes=question55
                    Insert.Matchescolors=question56
                    Insert.Pointstosmalldetails=question57
                    Insert.Drawatwotothree=question58
                    Insert.Understandslongshort=question59
                    Insert.Knowsowngender=question60
                    Insert.Knowsownage=question61
                    Insert.Matcheslettersnumerals=question62
                    Insert.Drawsafourtosixpartperson=question63
                    Insert.Cangiveamounts=question64
                    Insert.Understandssimplenalogies=question65
                    Insert.Pointstofivetosixcolors=question66
                    Insert.Pointstolettersnumerals=question67
                    Insert.Readseveralcommon=question68
                    Insert.RoteCountsToforty=question69
                    Insert.Pointstoeighttotenbodypart=question70
                    Insert.AmountGreaterThanTen=question71
                    Insert.ReadtwofiveWords=question72
                    
                    Insert.problem3yes=problem3yes
                    Insert.problem3no =problem3no 
                    Insert.problem6yes=problem6yes
                    Insert.problem6no=problem6no
                    Insert.problem9yes=problem9yes
                    Insert.problem9no=problem9no
                    Insert.problem12yes=problem12yes
                    Insert.problem12no=problem12no
                    Insert.problem18yes=problem18yes
                    Insert.problem18no=problem18no
                    Insert.problem24yes=problem24yes
                    Insert.problem24no=problem24no
                    Insert.problem30yes=problem30yes
                    Insert.problem30no=problem30no
                    Insert.problem36yes=problem36yes
                    Insert.problem36no=problem36no
                    Insert.problem42yes=problem42yes
                    Insert.problem42no=problem42no
                    Insert.problem48yes=problem48yes
                    Insert.problem48no=problem48no
                    Insert.problem54yes=problem54yes
                    Insert.problem54no=problem54no
                    Insert.problem60yes=problem60yes
                    Insert.problem60no=problem60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Problem Solving Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewProblemSolvingForm', methods=['GET','POST'])
def viewProblemSolvingForm():
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
                                Constant.constant.constant.viewProblemSolvingForm,
                                session.query(Model.models.Application.M_CKProblemSolving.CKPID.label('ID'),
                                            Model.models.Application.M_CKProblemSolving.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKProblemSolving.problem3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem3no.label('finemotor03no'),
                                            Model.models.Application.M_CKProblemSolving.problem6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem6no.label('finemotor36no'),
                                            Model.models.Application.M_CKProblemSolving.problem9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem9no.label('finemotor69no'),
                                            Model.models.Application.M_CKProblemSolving.problem12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem12no.label('finemotor12no'),
                                            Model.models.Application.M_CKProblemSolving.problem18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKProblemSolving.problem24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKProblemSolving.problem30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKProblemSolving.problem36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKProblemSolving.problem42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKProblemSolving.problem48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKProblemSolving.problem54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKProblemSolving.problem60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKProblemSolving.problem60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKProblemSolving.CKPID.desc()).all())
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/submitEmotionalForm', methods=['GET','POST'])
def submitEmotionalForm():

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
                    
                    question37 = request_json.get('question145')
                    question38 = request_json.get('question146')
                    question39 = request_json.get('question147')
                    question40 = request_json.get('question148')
                    question41 = request_json.get('question149')
                    question42 = request_json.get('question150')
                    question43 = request_json.get('question151')
                    question44 = request_json.get('question152')
                    question45 = request_json.get('question153')
                    question46 = request_json.get('question154')
                    question47 = request_json.get('question155')
                    question48 = request_json.get('question156')
                    question49 = request_json.get('question157')
                    question50 = request_json.get('question158')
                    question51 = request_json.get('question159')
                    question52 = request_json.get('question160')
                    question53 = request_json.get('question161')
                    question54 = request_json.get('question162')
                    question55 = request_json.get('question163')
                    question56 = request_json.get('question164')
                    question57 = request_json.get('question165')
                    question58 = request_json.get('question166')
                    question59 = request_json.get('question167')
                    question60 = request_json.get('question168')
                    question61 = request_json.get('question169')
                    question62 = request_json.get('question170')
                    question63 = request_json.get('question171')
                    question64 = request_json.get('question172')
                    question65 = request_json.get('question173')
                    question66 = request_json.get('question174')
                    question67 = request_json.get('question175')
                    question68 = request_json.get('question176')
                    question69 = request_json.get('question177')
                    question70 = request_json.get('question178')
                    question71 = request_json.get('question179')
                    question72 = request_json.get('question180')
                    
                    problem3yes = request_json.get('emotional0To3Yes')
                    problem3no = request_json.get('emotional0To3No')
                    problem6yes = request_json.get('emotional3To6Yes')
                    problem6no = request_json.get('emotionalTo6No')
                    problem9yes = request_json.get('emotional6To9Yes')
                    problem9no = request_json.get('emotional6To9No')
                    problem12yes = request_json.get('emotional9To12Yes')
                    problem12no = request_json.get('emotionalg9To12No')
                    problem18yes = request_json.get('emotional12To18Yes')
                    problem18no = request_json.get('emotional12To18No')
                    problem24yes = request_json.get('emotional18To24Yes')
                    problem24no = request_json.get('emotional18To24No')
                    problem30yes = request_json.get('emotional24To30Yes')
                    problem30no = request_json.get('emotional24To30No')
                    problem36yes = request_json.get('emotional30To36Yes')
                    problem36no = request_json.get('emotional30To36No')
                    problem42yes = request_json.get('emotional36To42Yes')
                    problem42no = request_json.get('emotional36To42No')
                    problem48yes = request_json.get('emotional42To48Yes')
                    problem48no = request_json.get('emotional42To48No')
                    problem54yes = request_json.get('emotional48To54Yes')
                    problem54no = request_json.get('emotional48To54No')
                    problem60yes = request_json.get('emotional54To60Yes')
                    problem60no = request_json.get('emotional54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKEmotional()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.RespondToVoice=question37
                    Insert.ExpressionOfDisgust=question38
                    Insert.VisuallyFollowsPerson=question39
                    Insert.RecognizesCaregiver=question40
                    Insert.ExcitesOnSeeingToys=question41
                    Insert.LooktoSeenWhereGone=question42
                    Insert.SoundsToGetAttention=question43
                    Insert.LooksInDirection=question44
                    Insert.EngagesInGaze=question45
                    Insert.GivesObjectsToAdults=question46
                    Insert.ShowsObjectsToParent=question47
                    Insert.PointsTogetDesire=question48
                    Insert.ShowsEmpathy=question49
                    Insert.HugsAdults=question50
                    Insert.RecognizesDemo=question51
                    Insert.EngagesInPretend=question52
                    Insert.BeginsToShowShame=question53
                    Insert.WatchesOtherChildren=question54
                    Insert.BeginsToShow=question55
                    Insert.ParellelPlay=question56
                    Insert.IncreasedUnderstanding=question57
                    Insert.FearImaginary=question58
                    Insert.SenseOfPersonalIdentity=question59
                    Insert.StartsToSharePrompt=question60
                    Insert.InterestedInTricking=question61
                    Insert.HasPrefferedFriend=question62
                    Insert.LabelsHappiness=question63
                    Insert.GroupPlay=question64
                    Insert.ApologizesMistake=question65
                    Insert.IdentityFeeling=question66
                    Insert.BestFriendofSameSex=question67
                    Insert.PlayBoardGames=question68
                    Insert.DistinguisesFantacy=question69
                    Insert.WantsTobeFriends=question70
                    Insert.EnjoysSchool=question71
                    Insert.EngagesInHouseHoldRole=question72
                    
                    Insert.emotional3yes=problem3yes
                    Insert.emotional3no =problem3no 
                    Insert.emotional6yes=problem6yes
                    Insert.emotional6no=problem6no
                    Insert.emotional9yes=problem9yes
                    Insert.emotional9no=problem9no
                    Insert.emotional12yes=problem12yes
                    Insert.emotional12no=problem12no
                    Insert.emotional18yes=problem18yes
                    Insert.emotional18no=problem18no
                    Insert.emotional24yes=problem24yes
                    Insert.emotional24no=problem24no
                    Insert.emotional30yes=problem30yes
                    Insert.emotional30no=problem30no
                    Insert.emotional36yes=problem36yes
                    Insert.emotional36no=problem36no
                    Insert.emotional42yes=problem42yes
                    Insert.emotional42no=problem42no
                    Insert.emotional48yes=problem48yes
                    Insert.emotional48no=problem48no
                    Insert.emotional54yes=problem54yes
                    Insert.emotional54no=problem54no
                    Insert.emotional60yes=problem60yes
                    Insert.emotional60no=problem60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Emotional Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewEmotionalForm', methods=['GET','POST'])
def viewEmotionalForm():
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
                                Constant.constant.constant.viewEmotionalForm,
                                session.query(Model.models.Application.M_CKEmotional.CKEID.label('ID'),
                                            Model.models.Application.M_CKEmotional.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKEmotional.emotional3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKEmotional.emotional3no.label('finemotor03no'),
                                            Model.models.Application.M_CKEmotional.emotional6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKEmotional.emotional6no.label('finemotor36no'),
                                            Model.models.Application.M_CKEmotional.emotional9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKEmotional.emotional9no.label('finemotor69no'),
                                            Model.models.Application.M_CKEmotional.emotional12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKEmotional.emotional12no.label('finemotor12no'),
                                            Model.models.Application.M_CKEmotional.emotional18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKEmotional.emotional18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKEmotional.emotional24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKEmotional.emotional24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKEmotional.emotional30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKEmotional.emotional30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKEmotional.emotional36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKEmotional.emotional36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKEmotional.emotional42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKEmotional.emotional42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKEmotional.emotional48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKEmotional.emotional48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKEmotional.emotional54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKEmotional.emotional54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKEmotional.emotional60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKEmotional.emotional60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKEmotional.CKEID.desc()).all())
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/submitReceptiveLanguageForm', methods=['GET','POST'])
def submitReceptiveLanguageForm():

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
                    
                    question37 = request_json.get('question181')
                    question38 = request_json.get('question182')
                    question39 = request_json.get('question183')
                    question40 = request_json.get('question184')
                    question41 = request_json.get('question185')
                    question42 = request_json.get('question186')
                    question43 = request_json.get('question187')
                    question44 = request_json.get('question188')
                    question45 = request_json.get('question189')
                    question46 = request_json.get('question190')
                    question47 = request_json.get('question191')
                    question48 = request_json.get('question192')
                    question49 = request_json.get('question193')
                    question50 = request_json.get('question194')
                    question51 = request_json.get('question195')
                    question52 = request_json.get('question196')
                    question53 = request_json.get('question197')
                    question54 = request_json.get('question198')
                    question55 = request_json.get('question199')
                    question56 = request_json.get('question200')
                    question57 = request_json.get('question201')
                    question58 = request_json.get('question202')
                    question59 = request_json.get('question203')
                    question60 = request_json.get('question204')
                    question61 = request_json.get('question205')
                    question62 = request_json.get('question206')
                    question63 = request_json.get('question207')
                    question64 = request_json.get('question208')
                    question65 = request_json.get('question209')
                    question66 = request_json.get('question210')
                    question67 = request_json.get('question211')
                    question68 = request_json.get('question212')
                    question69 = request_json.get('question213')
                    question70 = request_json.get('question214')
                    question71 = request_json.get('question215')
                    question72 = request_json.get('question216')
                    
                    problem3yes = request_json.get('receptiveLanguage0To3Yes')
                    problem3no = request_json.get('receptiveLanguage0To3No')
                    problem6yes = request_json.get('receptiveLanguage3To6Yes')
                    problem6no = request_json.get('receptiveLanguage3To6No')
                    problem9yes = request_json.get('receptiveLanguage6To9Yes')
                    problem9no = request_json.get('receptiveLanguage6To9No')
                    problem12yes = request_json.get('receptiveLanguage9To12Yes')
                    problem12no = request_json.get('receptiveLanguage9To12No')
                    problem18yes = request_json.get('receptiveLanguage12To18Yes')
                    problem18no = request_json.get('receptiveLanguage12To18No')
                    problem24yes = request_json.get('receptiveLanguage18To24Yes')
                    problem24no = request_json.get('receptiveLanguage18To24No')
                    problem30yes = request_json.get('receptiveLanguage24To30Yes')
                    problem30no = request_json.get('receptiveLanguage24To30No')
                    problem36yes = request_json.get('receptiveLanguage30To36Yes')
                    problem36no = request_json.get('receptiveLanguage30To36No')
                    problem42yes = request_json.get('receptiveLanguage36To42Yes')
                    problem42no = request_json.get('receptiveLanguage36To42No')
                    problem48yes = request_json.get('receptiveLanguage42To48Yes')
                    problem48no = request_json.get('receptiveLanguage42To48No')
                    problem54yes = request_json.get('receptiveLanguage48To54Yes')
                    problem54no = request_json.get('receptiveLanguage48To54No')
                    problem60yes = request_json.get('receptiveLanguage54To60Yes')
                    problem60no = request_json.get('receptiveLanguage54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKReceptive()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.question181=question37
                    Insert.question182=question38
                    Insert.question183=question39
                    Insert.question184=question40
                    Insert.question185=question41
                    Insert.question186=question42
                    Insert.question187=question43
                    Insert.question188=question44
                    Insert.question189=question45
                    Insert.question190=question46
                    Insert.question191=question47
                    Insert.question192=question48
                    Insert.question193=question49
                    Insert.question194=question50
                    Insert.question195=question51
                    Insert.question196=question52
                    Insert.question197=question53
                    Insert.question198=question54
                    Insert.question199=question55
                    Insert.question200=question56
                    Insert.question201=question57
                    Insert.question202=question58
                    Insert.question203=question59
                    Insert.question204=question60
                    Insert.question205=question61
                    Insert.question206=question62
                    Insert.question207=question63
                    Insert.question208=question64
                    Insert.question209=question65
                    Insert.question210=question66
                    Insert.question211=question67
                    Insert.question212=question68
                    Insert.question213=question69
                    Insert.question214=question70
                    Insert.question215=question71
                    Insert.question216=question72
                    
                    Insert.receptive3yes=problem3yes
                    Insert.receptive3no =problem3no 
                    Insert.receptive6yes=problem6yes
                    Insert.receptive6no=problem6no
                    Insert.receptive9yes=problem9yes
                    Insert.receptive9no=problem9no
                    Insert.receptive12yes=problem12yes
                    Insert.receptive12no=problem12no
                    Insert.receptive18yes=problem18yes
                    Insert.receptive18no=problem18no
                    Insert.receptive24yes=problem24yes
                    Insert.receptive24no=problem24no
                    Insert.receptive30yes=problem30yes
                    Insert.receptive30no=problem30no
                    Insert.receptive36yes=problem36yes
                    Insert.receptive36no=problem36no
                    Insert.receptive42yes=problem42yes
                    Insert.receptive42no=problem42no
                    Insert.receptive48yes=problem48yes
                    Insert.receptive48no=problem48no
                    Insert.receptive54yes=problem54yes
                    Insert.receptive54no=problem54no
                    Insert.receptive60yes=problem60yes
                    Insert.receptive60no=problem60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Receptive Language Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewReceptiveForm', methods=['GET','POST'])
def viewReceptiveForm():
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
                                Constant.constant.constant.viewReceptiveForm,
                                session.query(Model.models.Application.M_CKReceptive.CKRID.label('ID'),
                                            Model.models.Application.M_CKReceptive.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKReceptive.receptive3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKReceptive.receptive3no.label('finemotor03no'),
                                            Model.models.Application.M_CKReceptive.receptive6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKReceptive.receptive6no.label('finemotor36no'),
                                            Model.models.Application.M_CKReceptive.receptive9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKReceptive.receptive9no.label('finemotor69no'),
                                            Model.models.Application.M_CKReceptive.receptive12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKReceptive.receptive12no.label('finemotor12no'),
                                            Model.models.Application.M_CKReceptive.receptive18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKReceptive.receptive18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKReceptive.receptive24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKReceptive.receptive24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKReceptive.receptive30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKReceptive.receptive30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKReceptive.receptive36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKReceptive.receptive36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKReceptive.receptive42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKReceptive.receptive42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKReceptive.receptive48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKReceptive.receptive48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKReceptive.receptive54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKReceptive.receptive54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKReceptive.receptive60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKReceptive.receptive60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKReceptive.CKRID.desc()).all())
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/submitExpressiveLanguageForm', methods=['GET','POST'])
def submitExpressiveLanguageForm():

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
                    
                    question37 = request_json.get('question217')
                    question38 = request_json.get('question218')
                    question39 = request_json.get('question219')
                    question40 = request_json.get('question220')
                    question41 = request_json.get('question221')
                    question42 = request_json.get('question222')
                    question43 = request_json.get('question223')
                    question44 = request_json.get('question224')
                    question45 = request_json.get('question225')
                    question46 = request_json.get('question226')
                    question47 = request_json.get('question227')
                    question48 = request_json.get('question228')
                    question49 = request_json.get('question229')
                    question50 = request_json.get('question230')
                    question51 = request_json.get('question231')
                    question52 = request_json.get('question232')
                    question53 = request_json.get('question233')
                    question54 = request_json.get('question234')
                    question55 = request_json.get('question235')
                    question56 = request_json.get('question236')
                    question57 = request_json.get('question237')
                    question58 = request_json.get('question238')
                    question59 = request_json.get('question239')
                    question60 = request_json.get('question240')
                    question61 = request_json.get('question241')
                    question62 = request_json.get('question242')
                    question63 = request_json.get('question243')
                    question64 = request_json.get('question244')
                    question65 = request_json.get('question245')
                    question66 = request_json.get('question246')
                    question67 = request_json.get('question247')
                    question68 = request_json.get('question248')
                    question69 = request_json.get('question249')
                    question70 = request_json.get('question250')
                    question71 = request_json.get('question251')
                    question72 = request_json.get('question252')
                    
                    problem3yes = request_json.get('expressiveLanguage0To3Yes')
                    problem3no = request_json.get('expressiveLanguage0To3No')
                    problem6yes = request_json.get('expressiveLanguage3To6Yes')
                    problem6no = request_json.get('expressiveLanguage3To6No')
                    problem9yes = request_json.get('expressiveLanguage6To9Yes')
                    problem9no = request_json.get('expressiveLanguage6To9No')
                    problem12yes = request_json.get('expressiveLanguage9To12Yes')
                    problem12no = request_json.get('expressiveLanguage9To12No')
                    problem18yes = request_json.get('expressiveLanguage12To18Yes')
                    problem18no = request_json.get('expressiveLanguage12To18No')
                    problem24yes = request_json.get('expressiveLanguage18To24Yes')
                    problem24no = request_json.get('expressiveLanguage18To24No')
                    problem30yes = request_json.get('expressiveLanguage24To30Yes')
                    problem30no = request_json.get('expressiveLanguage24To30No')
                    problem36yes = request_json.get('expressiveLanguage30To36Yes')
                    problem36no = request_json.get('expressiveLanguage30To36No')
                    problem42yes = request_json.get('expressiveLanguage36To42Yes')
                    problem42no = request_json.get('expressiveLanguage36To42No')
                    problem48yes = request_json.get('expressiveLanguage42To48Yes')
                    problem48no = request_json.get('expressiveLanguage42To48No')
                    problem54yes = request_json.get('expressiveLanguage48To54Yes')
                    problem54no = request_json.get('expressiveLanguage48To54No')
                    problem60yes = request_json.get('expressiveLanguage54To60Yes')
                    problem60no = request_json.get('expressiveLanguage54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKExpressive()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.question217=question37
                    Insert.question218=question38
                    Insert.question219=question39
                    Insert.question220=question40
                    Insert.question221=question41
                    Insert.question222=question42
                    Insert.question223=question43
                    Insert.question224=question44
                    Insert.question225=question45
                    Insert.question226=question46
                    Insert.question227=question47
                    Insert.question228=question48
                    Insert.question229=question49
                    Insert.question230=question50
                    Insert.question231=question51
                    Insert.question232=question52
                    Insert.question233=question53
                    Insert.question234=question54
                    Insert.question235=question55
                    Insert.question236=question56
                    Insert.question237=question57
                    Insert.question238=question58
                    Insert.question239=question59
                    Insert.question240=question60
                    Insert.question241=question61
                    Insert.question242=question62
                    Insert.question243=question63
                    Insert.question244=question64
                    Insert.question245=question65
                    Insert.question246=question66
                    Insert.question247=question67
                    Insert.question248=question68
                    Insert.question249=question69
                    Insert.question250=question70
                    Insert.question251=question71
                    Insert.question252=question72
                    
                    Insert.expressive3yes=problem3yes
                    Insert.expressive3no =problem3no 
                    Insert.expressive6yes=problem6yes
                    Insert.expressive6no=problem6no
                    Insert.expressive9yes=problem9yes
                    Insert.expressive9no=problem9no
                    Insert.expressive12yes=problem12yes
                    Insert.expressive12no=problem12no
                    Insert.expressive18yes=problem18yes
                    Insert.expressive18no=problem18no
                    Insert.expressive24yes=problem24yes
                    Insert.expressive24no=problem24no
                    Insert.expressive30yes=problem30yes
                    Insert.expressive30no=problem30no
                    Insert.expressive36yes=problem36yes
                    Insert.expressive36no=problem36no
                    Insert.expressive42yes=problem42yes
                    Insert.expressive42no=problem42no
                    Insert.expressive48yes=problem48yes
                    Insert.expressive48no=problem48no
                    Insert.expressive54yes=problem54yes
                    Insert.expressive54no=problem54no
                    Insert.expressive60yes=problem60yes
                    Insert.expressive60no=problem60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Expressive Language Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewExpressiveLanguageForm', methods=['GET','POST'])
def viewExpressiveLanguageForm():
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
                                Constant.constant.constant.viewExpressiveLanguageForm,
                                session.query(Model.models.Application.M_CKExpressive.CKRID.label('ID'),
                                            Model.models.Application.M_CKExpressive.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKExpressive.expressive3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKExpressive.expressive3no.label('finemotor03no'),
                                            Model.models.Application.M_CKExpressive.expressive6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKExpressive.expressive6no.label('finemotor36no'),
                                            Model.models.Application.M_CKExpressive.expressive9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKExpressive.expressive9no.label('finemotor69no'),
                                            Model.models.Application.M_CKExpressive.expressive12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKExpressive.expressive12no.label('finemotor12no'),
                                            Model.models.Application.M_CKExpressive.expressive18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKExpressive.expressive18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKExpressive.expressive24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKExpressive.expressive24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKExpressive.expressive30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKExpressive.expressive30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKExpressive.expressive36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKExpressive.expressive36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKExpressive.expressive42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKExpressive.expressive42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKExpressive.expressive48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKExpressive.expressive48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKExpressive.expressive54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKExpressive.expressive54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKExpressive.expressive60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKExpressive.expressive60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKExpressive.CKRID.desc()).all())
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/submitSocialSkillsForm', methods=['GET','POST'])
def submitSocialSkillsForm():

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
                    
                    question37 = request_json.get('question253')
                    question38 = request_json.get('question254')
                    question39 = request_json.get('question255')
                    question40 = request_json.get('question256')
                    question41 = request_json.get('question257')
                    question42 = request_json.get('question258')
                    question43 = request_json.get('question259')
                    question44 = request_json.get('question260')
                    question45 = request_json.get('question261')
                    question46 = request_json.get('question262')
                    question47 = request_json.get('question263')
                    question48 = request_json.get('question264')
                    question49 = request_json.get('question265')
                    question50 = request_json.get('question266')
                    question51 = request_json.get('question267')
                    question52 = request_json.get('question268')
                    question53 = request_json.get('question269')
                    question54 = request_json.get('question270')
                    question55 = request_json.get('question271')
                    question56 = request_json.get('question272')
                    question57 = request_json.get('question273')
                    question58 = request_json.get('question274')
                    question59 = request_json.get('question275')
                    question60 = request_json.get('question276')
                    question61 = request_json.get('question277')
                    question62 = request_json.get('question278')
                    question63 = request_json.get('question279')
                    question64 = request_json.get('question280')
                    question65 = request_json.get('question281')
                    question66 = request_json.get('question282')
                    question67 = request_json.get('question283')
                    question68 = request_json.get('question284')
                    question69 = request_json.get('question285')
                    question70 = request_json.get('question286')
                    question71 = request_json.get('question287')
                    question72 = request_json.get('question288')
                    
                    problem3yes = request_json.get('socialSkills0To3Yes')
                    problem3no = request_json.get('socialSkills0To3No')
                    problem6yes = request_json.get('socialSkills3To6Yes')
                    problem6no = request_json.get('socialSkills3To6No')
                    problem9yes = request_json.get('socialSkills6To9Yes')
                    problem9no = request_json.get('socialSkills6To9No')
                    problem12yes = request_json.get('socialSkills9To12Yes')
                    problem12no = request_json.get('socialSkills9To12No')
                    problem18yes = request_json.get('socialSkills12To18Yes')
                    problem18no = request_json.get('socialSkills12To18No')
                    problem24yes = request_json.get('socialSkills18To24Yes')
                    problem24no = request_json.get('socialSkills18To24No')
                    problem30yes = request_json.get('socialSkills24To30Yes')
                    problem30no = request_json.get('socialSkills24To30No')
                    problem36yes = request_json.get('socialSkills30To36Yes')
                    problem36no = request_json.get('socialSkills30To36No')
                    problem42yes = request_json.get('socialSkills36To42Yes')
                    problem42no = request_json.get('socialSkills36To42No')
                    problem48yes = request_json.get('socialSkills42To48Yes')
                    problem48no = request_json.get('socialSkills42To48No')
                    problem54yes = request_json.get('socialSkills48To54Yes')
                    problem54no = request_json.get('socialSkills48To54No')
                    problem60yes = request_json.get('socialSkills54To60Yes')
                    problem60no = request_json.get('socialSkills54To60No')
                    

                    Aid = request_json.get('Aid')
                    PID = request_json.get('pid')
                    Id = request_json.get('Id')

                    Insert=Model.models.Application.M_CKSocialSkills()
                    Insert.M_Patient_MPID=PID
                    Insert.M_AppointmentID=Aid
                    
                    Insert.question253=question37
                    Insert.question254=question38
                    Insert.question255=question39
                    Insert.question256=question40
                    Insert.question257=question41
                    Insert.question258=question42
                    Insert.question259=question43
                    Insert.question260=question44
                    Insert.question261=question45
                    Insert.question262=question46
                    Insert.question263=question47
                    Insert.question264=question48
                    Insert.question265=question49
                    Insert.question266=question50
                    Insert.question267=question51
                    Insert.question268=question52
                    Insert.question269=question53
                    Insert.question270=question54
                    Insert.question271=question55
                    Insert.question272=question56
                    Insert.question273=question57
                    Insert.question274=question58
                    Insert.question275=question59
                    Insert.question276=question60
                    Insert.question277=question61
                    Insert.question278=question62
                    Insert.question279=question63
                    Insert.question280=question64
                    Insert.question281=question65
                    Insert.question282=question66
                    Insert.question283=question67
                    Insert.question284=question68
                    Insert.question285=question69
                    Insert.question286=question70
                    Insert.question287=question71
                    Insert.question288=question72
                    
                    Insert.socialskill3yes=problem3yes
                    Insert.socialskill3no =problem3no 
                    Insert.socialskill6yes=problem6yes
                    Insert.socialskill6no=problem6no
                    Insert.socialskill9yes=problem9yes
                    Insert.socialskill9no=problem9no
                    Insert.socialskill12yes=problem12yes
                    Insert.socialskill12no=problem12no
                    Insert.socialskill18yes=problem18yes
                    Insert.socialskill18no=problem18no
                    Insert.socialskill24yes=problem24yes
                    Insert.socialskill24no=problem24no
                    Insert.socialskill30yes=problem30yes
                    Insert.socialskill30no=problem30no
                    Insert.socialskill36yes=problem36yes
                    Insert.socialskill36no=problem36no
                    Insert.socialskill42yes=problem42yes
                    Insert.socialskill42no=problem42no
                    Insert.socialskill48yes=problem48yes
                    Insert.socialskill48no=problem48no
                    Insert.socialskill54yes=problem54yes
                    Insert.socialskill54no=problem54no
                    Insert.socialskill60yes=problem60yes
                    Insert.socialskill60no=problem60no
                    
                    Insert.AddDate = datetime.datetime.now()
                    Insert.AddIP= flask.request.remote_addr
                    session.add(Insert)
                    session.commit()
                    return jsonify({'msg':'CK Social Skills Added Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})

    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@Assess_Blueprint.route('/viewSocialSkillsForm', methods=['GET','POST'])
def viewSocialSkillsForm():
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
                                Constant.constant.constant.viewSocialSkillsForm,
                                session.query(Model.models.Application.M_CKSocialSkills.CKSID.label('ID'),
                                            Model.models.Application.M_CKSocialSkills.M_AppointmentID.label('Appointment ID'),
                                            Model.models.Application.M_CKSocialSkills.socialskill3yes.label('0-3 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill3no.label('finemotor03no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill6yes.label('3-6 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill6no.label('finemotor36no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill9yes.label('6-9 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill9no.label('finemotor69no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill12yes.label('9-12 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill12no.label('finemotor12no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill18yes.label('12-18 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill18no.label('finemotor1218no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill24yes.label('18-24 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill24no.label('finemotor1824no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill30yes.label('24-30 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill30no.label('finemotor2430no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill36yes.label('30-36 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill36no.label('finemotor3036no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill42yes.label('36-42 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill42no.label('finemotor3642no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill48yes.label('42-48 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill48no.label('finemotor4248no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill54yes.label('48-54 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill54no.label('finemotor4854no'),
                                            Model.models.Application.M_CKSocialSkills.socialskill60yes.label('54-60 Months'),
                                            Model.models.Application.M_CKSocialSkills.socialskill60no.label('finemotor5460no'),
                                            
                                                ).filter_by(M_Patient_MPID=pid,IsActive=1,IsDeleted=0
                                ).order_by(Model.models.Application.M_CKSocialSkills.CKSID.desc()).all())
                    return jsonify(result=queryresult)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()              
 