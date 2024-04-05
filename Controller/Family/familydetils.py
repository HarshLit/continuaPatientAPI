import base64
import hashlib
import json
from logging import Logger
import os
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
FamilyDtls_Blueprint = CommonModule.flask.Blueprint(
    'FamilyDtls_Blueprint', import_name=__name__)

@FamilyDtls_Blueprint.route('/addFamily', methods=['POST','GET'])
def addFamily():
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
                userId =int(PatientID)
                image = request_json.get('image') 
                memberID = request_json.get('memberID') 
                fullName = request_json.get('fullName')
                gender = request_json.get('gender')
                DOB = request_json.get('DOB')
                address = request_json.get('address')
                country = request_json.get('country')
                state = request_json.get('state')
                city = request_json.get('city')
                zip = request_json.get('zip')
                profession = request_json.get('profession')
                preferredLanguages = request_json.get('preferredLanguages')
                bloodGroup = request_json.get('bloodGroup')
                knownAllergies = request_json.get('knownAllergies')
                preCondition = request_json.get('preCondition')

                if(fullName !='' and fullName!=None and DOB !='' and DOB!=None):
                    Insert = Model.models.Application.M_PatientFamily()
                    Insert.MPF_UserId = userId
                    Insert.MPF_ProfilePath = image
                    Insert.MPF_MemberId = memberID
                    Insert.MPF_Name = fullName
                    Insert.MPF_Gender = gender
                    Insert.MPF_DOB = DOB
                    Insert.MPF_Address = address
                    Insert.MPF_Country = country
                    Insert.MPF_State = state
                    Insert.MPF_City = city
                    Insert.MPF_Zip = zip
                    # Insert.MPF_Profession = profession
                    # Insert.MPF_PrefferedLanguage = preferredLanguages
                    Insert.MPF_BloodGroup = bloodGroup
                    Insert.MPF_Allergies = knownAllergies
                    Insert.MPF_PreMedication = preCondition
                    
                    Insert.MPF_AddDate = datetime.datetime.now()
                    Insert.MPF_AddIP = request.remote_addr
                    session.add(Insert)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Family Added Successfully'})
                    
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


@FamilyDtls_Blueprint.route('/addChild', methods=['POST','GET'])
def addChild():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            Mobilenum= request.headers.get('Mobilenumber')
            mob = Mobilenum[3:]

            # request_json = request.get_json()
            Data= request.form.get('data')
            if(Data!='' and Data!=None):
                getjson= json.loads(Data)
                file = request.files['files[]']
                
                # PID =
                if(getjson!='' and getjson!=None):
                    userId =int(PatientID)
                    # image = request_json.get('image') 
                    # memberID = request_json.get('memberID') 
                    abhaNo = getjson['abhaNo'] 
                    fullName = getjson['childName']
                    gender = getjson['gender']
                    DOB = getjson['dob']
                    address = getjson['address']
                    country = getjson['country']
                    state = getjson['state']
                    city =getjson['city']
                    zip = getjson['zip']
                    identityType = getjson['identityType']
                    identityNumber = getjson['identityNumber']
                    relation = getjson['relation']
                    bloodGroup = getjson['bloodGroup']
                    knownAllergies = getjson['knownAllergies']
                    preCondition = getjson['preCondition']
                    FilePath = 'static/Patient_Profile/'
                    if(file.filename!='' and file.filename!= None):
                        date = str(datetime.datetime.now().strftime('%d%m%Y%H%M%S'))
                        name, ext = os.path.splitext(file.filename)
                        files = (fullName.replace(" ", ""))+ '_'+ (name.replace(" ", "")) +'_'  + date  + ext
                        fileName=files
                        if(os.path.exists(FilePath)):
                            file.save(os.path.join(FilePath, fileName))
                            print(file.filename)
                        else:
                            os.makedirs(FilePath)
                            file.save(os.path.join(FilePath, fileName))
                    totalPatientinbranch= session.query(Model.models.Application.M_Patient.MP_UHID
                                    ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Patient.MPID.desc()).first()
                    # clinicname=getClinic[0].MB_Code
                    sn=len(totalPatientinbranch) + 1
                    lastPatientIDs = totalPatientinbranch[0]
                    lastPatientID=  lastPatientIDs[-5:]
                    newPatientID= str(int(lastPatientID)+1).zfill(5)
                    UHID='CK'+'App' + str(newPatientID)
                    userId =int(PatientID)
                    if(fullName !='' and fullName!=None and DOB !='' and DOB!=None):
                        Insert=Model.models.Application.M_Patient()
                        Insert.MP_ProfilePath=FilePath+fileName
                        if(UHID!='' and UHID!=None):
                            Insert.MP_UHID=UHID
                        if(fullName!='' and fullName!=None):
                            Insert.MP_Name=fullName
                        if(mob!='' and mob!=None):
                            Insert.MP_Mobile=mob
                        if(address!='' and address!=None):
                            Insert.MP_Address=address
                        if(gender!='' and gender!=None):
                            Insert.MP_Gender=gender
                        if(DOB!='' and DOB!=None):
                            Insert.MP_DOB=DOB
                        if(abhaNo!='' and abhaNo!=None):
                            Insert.MP_Code=abhaNo
                        if(zip!='' and zip!=None):
                            Insert.MP_Zip=zip
                        if(relation!='' and relation!=None):
                            Insert.MP_Relationchild=relation
                        if(city!='' and city!=None):
                            Insert.MP_City=city
                        if(state!='' and state!=None):
                            Insert.MP_State=state
                        if(country!='' and country!=None):
                            Insert.MP_Country=country
                        if(bloodGroup!='' and bloodGroup!=None):
                            Insert.MP_BloodGroup=bloodGroup
                        if(knownAllergies!='' and knownAllergies!=None):
                            Insert.MP_Allergies=knownAllergies
                        if(identityType!='' and identityType!=None):
                            Insert.M_IdentityType=identityType
                        if(identityNumber!='' and identityNumber!=None):
                            Insert.M_IdentityNumber=identityNumber
                        if(preCondition!='' and preCondition!=None):
                            Insert.MP_PreExMed=preCondition
                        Insert.MP_AddIP= flask.request.remote_addr
                        Insert.MP_ModDate=datetime.datetime.now()
                        session.add(Insert)
                        session.commit()
                        
                        return jsonify({'success':'Child Added Successfully'})
                        
                    else:
                        return jsonify({'error':'Please Enter Name and DOB'})
                   
            else:
                request_json = request.get_json()
                abhaNo = request_json.get('abhaNo') 
                childName = request_json.get('childName') 
                gender = request_json.get('gender') 
                dob = request_json.get('dob')
                address = request_json.get('address')
                country = request_json.get('country') 
                state = request_json.get('state') 
                city = request_json.get('city') 
                zip = request_json.get('zip')
                identityType = request_json.get('identityType')
                identityNumber = request_json.get('identityNumber') 
                relation = request_json.get('relation') 
                bloodGroup = request_json.get('bloodGroup') 
                knownAllergies = request_json.get('knownAllergies')
                preCondition = request_json.get('preCondition')
                totalPatientinbranch= session.query(Model.models.Application.M_Patient.MP_UHID
                                    ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Patient.MPID.desc()).first()
                    # clinicname=getClinic[0].MB_Code
                sn=len(totalPatientinbranch) + 1
                lastPatientIDs = totalPatientinbranch[0]
                lastPatientID=  lastPatientIDs[-5:]
                newPatientID= str(int(lastPatientID)+1).zfill(5)
                UHID='CK'+'App' + str(newPatientID)
                userId =int(PatientID)
                if(childName !='' and childName!=None and dob !='' and dob!=None):
                    Insert=Model.models.Application.M_Patient()
                        
                    if(UHID!='' and UHID!=None):
                        Insert.MP_UHID=UHID
                    if(childName!='' and childName!=None):
                        Insert.MP_Name=childName
                    if(mob!='' and mob!=None):
                        Insert.MP_Mobile=mob
                    if(address!='' and address!=None):
                        Insert.MP_Address=address
                    if(gender!='' and gender!=None):
                        Insert.MP_Gender=gender
                    if(dob!='' and dob!=None):
                        Insert.MP_DOB=dob
                    if(abhaNo!='' and abhaNo!=None):
                        Insert.MP_Code=abhaNo
                    if(zip!='' and zip!=None):
                        Insert.MP_Zip=zip
                    if(relation!='' and relation!=None):
                        Insert.MP_Relationchild=relation
                    if(city!='' and city!=None):
                        Insert.MP_City=city
                    if(state!='' and state!=None):
                        Insert.MP_State=state
                    if(country!='' and country!=None):
                        Insert.MP_Country=country
                    if(bloodGroup!='' and bloodGroup!=None):
                        Insert.MP_BloodGroup=bloodGroup
                    if(knownAllergies!='' and knownAllergies!=None):
                        Insert.MP_Allergies=knownAllergies
                    if(identityType!='' and identityType!=None):
                        Insert.M_IdentityType=identityType
                    if(identityNumber!='' and identityNumber!=None):
                        Insert.M_IdentityNumber=identityNumber
                    if(preCondition!='' and preCondition!=None):
                        Insert.MP_PreExMed=preCondition
                    Insert.MP_AddIP= flask.request.remote_addr
                    Insert.MP_ModDate=datetime.datetime.now()
                    session.add(Insert)
                    session.commit()
                   
                    return jsonify({'success':'Child Added Successfully'})
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/genderDropdown', methods=['POST','GET'])
def genderDropdown():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
            genderDropdown= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.genderDropdown,
                        session.query(Model.models.Application.T_Details.TDID.label('key'),
                                    Model.models.Application.T_Details.TD_Name.label('label')
                                    ).filter_by(TD_IsDeleted=0,TD_IsActive=1,M_Details_MDID=4).all()
                                )
            session.commit()
            return jsonify(result=genderDropdown)
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/bloodgroupDropdown', methods=['POST','GET'])
def bloodgroupDropdown():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
            bloodgroupDropdown= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.bloodgroupDropdown,
                        session.query(Model.models.Application.T_Details.TDID.label('key'),
                                    Model.models.Application.T_Details.TD_Name.label('label')
                                    ).filter_by(TD_IsDeleted=0,TD_IsActive=1,M_Details_MDID=7).all()
                                )
            session.commit()
            return jsonify(result=bloodgroupDropdown)
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/editChildDtl', methods=['POST','GET'])
def editChildDtl():
    session=Session()
    try:
        if(flask.request.method == 'POST'):
            Id= request.data
            Id = Id.decode()
            if(Id!=''): 
                editFamilyDtl= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.editChildDtl,
                        session.query(Model.models.Application.M_Patient.MPID.label('Id'),
                                    Model.models.Application.M_Patient.MPID.label('MemberId'),
                                    Model.models.Application.M_Patient.MP_Name.label('Name'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Patient.MP_DOB,'%Y-%m-%d').label('DOB'),
                                    Model.models.Application.M_Patient.MP_Gender.label('Gender'),
                                    Model.models.Application.M_Patient.MP_Mobile.label('Mobile'),
                                    Model.models.Application.M_Patient.MP_BloodGroup.label('BloodGroup'),
                                    Model.models.Application.M_Patient.MP_Allergies.label('Allergies'),
                                    Model.models.Application.M_Patient.MP_PreExMed.label('PreMeditation'),
                                    Model.models.Application.M_Patient.MP_ProfilePath.label('ProfilePath'),
                                    Model.models.Application.M_Patient.MP_Relationchild.label('Relation'),
                                    Model.models.Application.M_Patient.MP_Address.label('Address'),
                                    Model.models.Application.M_Patient.MP_Country.label('Country'),
                                    Model.models.Application.M_Patient.MP_State.label('State'),
                                    Model.models.Application.M_Patient.M_IdentityType.label('IdentityType'),
                                    Model.models.Application.M_Patient.MP_Zip.label('Zip'),
                                    Model.models.Application.M_Patient.MP_Code.label('Abha'),
                                    Model.models.Application.M_Patient.M_IdentityNumber.label('IdentityNumber'),
                                    Model.models.Application.M_Patient.MP_City.label('City'),
                                    ).filter_by(MP_IsDeleted=0,MP_IsActive=1,MPID=int(Id)).all()
                                )
                session.commit()
                return jsonify(result=editFamilyDtl),200
            else:
                return jsonify({'error':'Data not available'}),405
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/getFamilyDtl', methods=['POST','GET'])
def getFamilyDtl():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            Mobilenum= request.headers.get('Mobilenumber')
            mob = Mobilenum[3:]

            if(PatientID!='' and PatientID!=None):
                UserId =int(PatientID)
                getFamilyDtl= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.getFamilyDtl,
                        session.query(Model.models.Application.M_Patient.MPID.label('Id'),
                                    Model.models.Application.M_Patient.MPID.label('MemberId'),
                                    Model.models.Application.M_Patient.MP_Name.label('Name'),
                                    sqlalchemy.func.date_format(Model.models.Application.M_Patient.MP_DOB,'%d-%b-%Y').label('DOB'),
                                    Model.models.Application.M_Patient.MP_DOB.label('DOB1'),
                                    ).filter_by(MP_IsDeleted=0,MP_IsActive=1,MP_Mobile=mob).all()
                                )
                session.commit()
                return jsonify(result=getFamilyDtl),200
            else:
                return jsonify({'error':'JSON not available'}),405
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/updateFamily', methods=['POST','GET'])
def updateFamily():
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
                familyID = request_json.get('familyID') 
                image = request_json.get('image') 
                memberID = request_json.get('memberID') 
                fullName = request_json.get('fullName')
                gender = request_json.get('gender')
                DOB = request_json.get('DOB')
                address = request_json.get('address')
                country = request_json.get('country')
                state = request_json.get('state')
                city = request_json.get('city')
                zip = request_json.get('zip')
                profession = request_json.get('profession')
                preferredLanguages = request_json.get('preferredLanguages')
                bloodGroup = request_json.get('bloodGroup')
                knownAllergies = request_json.get('knownAllergies')
                preCondition = request_json.get('preCondition')

                if(fullName !='' and fullName!=None and DOB !='' and DOB!=None):
                    Insert = session.query(Model.models.Application.M_PatientFamily).get(int(familyID))
                    Insert.MPF_UserId = userId
                    Insert.MPF_ProfilePath = image
                    Insert.MPF_MemberId = memberID
                    Insert.MPF_Name = fullName
                    Insert.MPF_Gender = gender
                    Insert.MPF_DOB = DOB
                    Insert.MPF_Address = address
                    Insert.MPF_Country = country
                    Insert.MPF_State = state
                    Insert.MPF_City = city
                    Insert.MPF_Zip = zip
                    Insert.MPF_Profession = profession
                    Insert.MPF_PrefferedLanguage = preferredLanguages
                    Insert.MPF_BloodGroup = bloodGroup
                    Insert.MPF_Allergies = knownAllergies
                    Insert.MPF_PreMedication = preCondition
                    
                    Insert.MPF_ModDate = datetime.datetime.now()
                    Insert.MPF_ModUser = int(PatientID)
                    session.commit()
                    session.close()
                    
                    return jsonify({'success':'Family Updated Successfully'})
                    
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

@FamilyDtls_Blueprint.route('/addPatientFile',methods=['GET','POST'])
def addPatientFile():

    session=Session()
    try:

        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    content_type = request.headers.get('Content-Type')
                    files= request.files.getlist(str('files[]'))
                    docname= request.form.get('docname')
                    PID= request.form.get('pid')
                    
                    FilePath2 = 'static/PatientFile_Document'
                    FilePath = 'C:/inetpub/wwwroot/Continua/ContinuaPY/static/PatientFile_Document/'
                    for file in files:
                        if(file.filename!='' and file.filename!= None):
                            date = str(datetime.datetime.now().strftime('%d%m%Y%H%M%S'))
                            name, ext = os.path.splitext(file.filename)
                            files = 'PF'+ '_'+ (name.replace(" ", "")) +'_' + date  + ext
                            fileName=files
                            if(os.path.exists(FilePath)):
                                file.save(os.path.join(FilePath, fileName))
                                print(file.filename)
                            else:
                                os.makedirs(FilePath)
                                file.save(os.path.join(FilePath, fileName))
                            if(os.path.exists(FilePath2)):
                                file.save(os.path.join(FilePath2, fileName))
                                print(file.filename)
                            else:
                                os.makedirs(FilePath2)
                                file.save(os.path.join(FilePath2, fileName))
                        # User = data['id']
                        Insert=Model.models.Application.M_PatientFiles()
                        Insert.MPF_PatientID=PID
                        Insert.MPF_Name=fileName
                        Insert.MPF_FilePath=FilePath2
                        Insert.MPF_DocName=docname
                        Insert.MPF_FileType='NotAvailable'
                        Insert.MPF_AddIP= flask.request.remote_addr
                        # Insert.MPF_ModUser= int(User)
                        Insert.MPF_ModDate = datetime.datetime.now()
                        session.add(Insert)
                        session.commit()
                        return jsonify({'msg':'File Uploaded Successfully'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except:
        return jsonify({'err':'token is invalid'})
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/getUploadedFile', methods=['POST','GET'])
def getUploadedFile():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    # FormItems=[]
                    # content_type = request.headers.get('Content-Type')
                    PId= request.data
                    # # if(Id=="0" and Id==0):
                    # #if(PId!="b'0'"):
                    getTextField= Common_Function.CommonFun.convertToJson(
                                    Constant.constant.constant.getUploadedFile,
                                    session.query(Model.models.Application.M_PatientFiles,
                                            Model.models.Application.M_PatientFiles.MPFID.label('ID'),
                                            Model.models.Application.M_Patient.MP_Name.label('Patient Name'),
                                            Model.models.Application.M_PatientFiles.MPF_DocName.label('DocName'),
                                            sqlalchemy.func.concat(Model.models.Application.M_PatientFiles.MPF_FilePath, '/', Model.models.Application.M_PatientFiles.MPF_Name).label('Path'),
                                            Model.models.Application.M_PatientFiles.MPF_Name.label('File Name'),
                                            Model.models.Application.M_PatientFiles.MPF_AddDate.label('Add Date')
                                            ).filter_by(MPF_IsActive=1 ,MPF_IsDeleted=0,MPF_PatientID=PId).join(Model.models.Application.M_Patient,
                                                Model.models.Application.M_Patient.MPID==Model.models.Application.M_PatientFiles.MPF_PatientID
                                                ).all()
                            )
                    return jsonify(result=getTextField)
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    except Exception as e:
        return jsonify({'err':str(e)})
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/DeleteUploadedFile',methods=['POST'])
def DeleteUploadedFile():
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    session=Session()
                    Id=request.get_json()
                    #Id=request.data
                    if(Id != '' and Id != None):
                        session.query(Model.models.Application.M_PatientFiles
                                    ).filter(Model.models.Application.M_PatientFiles.MPFID==Id
                                             ).update({Model.models.Application.M_PatientFiles.MPF_IsDeleted:1,
                                                       Model.models.Application.M_PatientFiles.MPF_ModDate:datetime.datetime.now()})
                        session.commit()
                        return jsonify({'msg':'File Deleted Successfully'})
                    else:
                        return jsonify({'msg':'something went wrong please try again'})
                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()


@FamilyDtls_Blueprint.route('/DownloadUploadFile', methods=['POST','GET'])
def DownloadUploadFile():
    session=Session()
    try:
        if(request.method == "POST"):
            if('Authorization' in request.headers):
                token= request.headers.get('Authorization')

                if not token:
                    return jsonify({'MSG':'Token is missing'})
                data = Common_Function.CommonFun.verifytoken(token)
                if(data):
                    PId= request.data
                    getTextField= session.query(Model.models.Application.M_PatientFiles,
                                            sqlalchemy.func.concat(Model.models.Application.M_PatientFiles.MPF_FilePath, '/', Model.models.Application.M_PatientFiles.MPF_Name).label('Path'),
                                            (Model.models.Application.M_PatientFiles.MPF_Name).label('Fname')
                                            ).filter_by(MPF_IsActive=1 ,MPF_IsDeleted=0,MPFID=PId).all()
                    value = getTextField[0].Path
                    Name = getTextField[0].Fname
                    name, ext = os.path.splitext(Name)
                    

                    with open(value, "rb") as encofile:
                        encoded_string = base64.b64encode(encofile.read())
                    # name, ext = os.path.splitext(value)
                    fname=name
                    fext=ext[1:]
                    fbstring=str(encoded_string)
                    #print(encoded_string)
                    return jsonify({'fname':fname,'fext': fext,'fbstring':fbstring[2:-1]})

                else:
                    return jsonify({'err':'Token is expired'})
            else:
                return jsonify({'err':'Please Login'})
    finally:
        session.close()


@FamilyDtls_Blueprint.route('/updateChild', methods=['POST','GET'])
def updateChild():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            ePatientID= request.headers.get('PatientID')
            PatientID=Common_Function.CommonFun.decryptString(ePatientID)
            Mobilenum= request.headers.get('Mobilenumber')
            mob = Mobilenum[3:]

            # request_json = request.get_json()
            Data= request.form.get('data')
            if(Data!='' and Data!=None):
                getjson= json.loads(Data)
                file = request.files['files[]']
                
                # PID =
                if(getjson!='' and getjson!=None):
                    userId =int(PatientID)
                    # image = request_json.get('image') 
                    # memberID = request_json.get('memberID') 
                    abhaNo = getjson['abhaNo'] 
                    fullName = getjson['childName']
                    gender = getjson['gender']
                    DOB = getjson['dob']
                    address = getjson['address']
                    country = getjson['country']
                    state = getjson['state']
                    city =getjson['city']
                    zip = getjson['zip']
                    identityType = getjson['identityType']
                    identityNumber = getjson['identityNumber']
                    relation = getjson['relation']
                    bloodGroup = getjson['bloodGroup']
                    knownAllergies = getjson['knownAllergies']
                    preCondition = getjson['preCondition']
                    Id = getjson['Id']
                    FilePath = 'static/Patient_Profile/'
                    if(file.filename!='' and file.filename!= None):
                        date = str(datetime.datetime.now().strftime('%d%m%Y%H%M%S'))
                        name, ext = os.path.splitext(file.filename)
                        files = (fullName.replace(" ", ""))+ '_'+ (name.replace(" ", "")) +'_'  + date  + ext
                        fileName=files
                        if(os.path.exists(FilePath)):
                            file.save(os.path.join(FilePath, fileName))
                            print(file.filename)
                        else:
                            os.makedirs(FilePath)
                            file.save(os.path.join(FilePath, fileName))
                    totalPatientinbranch= session.query(Model.models.Application.M_Patient.MP_UHID
                                    ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Patient.MPID.desc()).first()
                    # clinicname=getClinic[0].MB_Code
                    sn=len(totalPatientinbranch) + 1
                    lastPatientIDs = totalPatientinbranch[0]
                    lastPatientID=  lastPatientIDs[-5:]
                    newPatientID= str(int(lastPatientID)+1).zfill(5)
                    UHID='CK'+'App' + str(newPatientID)
                    userId =int(PatientID)
                    fullName=fullName.title()
                    if(fullName !='' and fullName!=None and DOB !='' and DOB!=None):
                        Insert=session.query(Model.models.Application.M_Patient).get(Id)
                        Insert.MP_ProfilePath=FilePath+fileName
                        if(UHID!='' and UHID!=None):
                            Insert.MP_UHID=UHID
                        if(fullName!='' and fullName!=None):
                            Insert.MP_Name=fullName
                        if(mob!='' and mob!=None):
                            Insert.MP_Mobile=mob
                        if(address!='' and address!=None):
                            Insert.MP_Address=address
                        if(gender!='' and gender!=None):
                            Insert.MP_Gender=gender
                        if(DOB!='' and DOB!=None):
                            Insert.MP_DOB=DOB
                        if(abhaNo!='' and abhaNo!=None):
                            Insert.MP_Code=abhaNo
                        if(zip!='' and zip!=None):
                            Insert.MP_Zip=zip
                        if(relation!='' and relation!=None):
                            Insert.MP_Relationchild=relation
                        if(city!='' and city!=None):
                            Insert.MP_City=city
                        if(state!='' and state!=None):
                            Insert.MP_State=state
                        if(country!='' and country!=None):
                            Insert.MP_Country=country
                        if(bloodGroup!='' and bloodGroup!=None):
                            Insert.MP_BloodGroup=bloodGroup
                        if(knownAllergies!='' and knownAllergies!=None):
                            Insert.MP_Allergies=knownAllergies
                        if(identityType!='' and identityType!=None):
                            Insert.M_IdentityType=identityType
                        if(identityNumber!='' and identityNumber!=None):
                            Insert.M_IdentityNumber=identityNumber
                        if(preCondition!='' and preCondition!=None):
                            Insert.MP_PreExMed=preCondition
                        Insert.MP_AddIP= flask.request.remote_addr
                        Insert.MP_ModDate=datetime.datetime.now()
                        session.commit()
                        
                        return jsonify({'success':'Child Updated Successfully'})
                        
                    else:
                        return jsonify({'error':'Please Enter Name and DOB'})
                   
            else:
                request_json = request.get_json()
                abhaNo = request_json.get('abhaNo') 
                childName = request_json.get('childName') 
                gender = request_json.get('gender') 
                dob = request_json.get('dob')
                address = request_json.get('address')
                country = request_json.get('country') 
                state = request_json.get('state') 
                city = request_json.get('city') 
                zip = request_json.get('zip')
                identityType = request_json.get('identityType')
                identityNumber = request_json.get('identityNumber') 
                relation = request_json.get('relation') 
                bloodGroup = request_json.get('bloodGroup') 
                knownAllergies = request_json.get('knownAllergies')
                preCondition = request_json.get('preCondition')
                Id = request_json.get('Id')
                totalPatientinbranch= session.query(Model.models.Application.M_Patient.MP_UHID
                                    ).filter_by(MP_IsActive=1,MP_IsDeleted=0).order_by(Model.models.Application.M_Patient.MPID.desc()).first()
                    # clinicname=getClinic[0].MB_Code
                sn=len(totalPatientinbranch) + 1
                lastPatientIDs = totalPatientinbranch[0]
                lastPatientID=  lastPatientIDs[-5:]
                newPatientID= str(int(lastPatientID)+1).zfill(5)
                UHID='CK'+'App' + str(newPatientID)
                userId =int(PatientID)
                childName=childName.title()
                if(childName !='' and childName!=None and dob !='' and dob!=None):
                    Insert=session.query(Model.models.Application.M_Patient).get(Id)
                        
                    if(UHID!='' and UHID!=None):
                        Insert.MP_UHID=UHID
                    if(childName!='' and childName!=None):
                        Insert.MP_Name=childName
                    if(mob!='' and mob!=None):
                        Insert.MP_Mobile=mob
                    if(address!='' and address!=None):
                        Insert.MP_Address=address
                    if(gender!='' and gender!=None):
                        Insert.MP_Gender=gender
                    if(dob!='' and dob!=None):
                        Insert.MP_DOB=dob
                    if(abhaNo!='' and abhaNo!=None):
                        Insert.MP_Code=abhaNo
                    if(zip!='' and zip!=None):
                        Insert.MP_Zip=zip
                    if(relation!='' and relation!=None):
                        Insert.MP_Relationchild=relation
                    if(city!='' and city!=None):
                        Insert.MP_City=city
                    if(state!='' and state!=None):
                        Insert.MP_State=state
                    if(country!='' and country!=None):
                        Insert.MP_Country=country
                    if(bloodGroup!='' and bloodGroup!=None):
                        Insert.MP_BloodGroup=bloodGroup
                    if(knownAllergies!='' and knownAllergies!=None):
                        Insert.MP_Allergies=knownAllergies
                    if(identityType!='' and identityType!=None):
                        Insert.M_IdentityType=identityType
                    if(identityNumber!='' and identityNumber!=None):
                        Insert.M_IdentityNumber=identityNumber
                    if(preCondition!='' and preCondition!=None):
                        Insert.MP_PreExMed=preCondition
                    Insert.MP_AddIP= flask.request.remote_addr
                    Insert.MP_ModDate=datetime.datetime.now()
                    session.commit()
                   
                    return jsonify({'success':'Child Updated Successfully'})
        else:
            return jsonify({'error':'Method is not allowed'})
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()

@FamilyDtls_Blueprint.route('/updateFcmToken', methods=['POST','GET'])
def updateFcmToken():
    session = Session()
    try:
        if(flask.request.method == 'POST'):
            RequestIp = hashlib.md5((request.remote_addr).encode())
            RequestIp = RequestIp.hexdigest()
            #print(RequestIp)
            
            request_json = request.get_json() #'Vipul'#
            if(request_json!='' and request_json!=None):
                PID =request_json.get('PID') # 8544388789 #
                PatientId=Common_Function.CommonFun.decryptString(PID)
                tokenFcm = request_json.get('tokenFcm') # 'Vipul Kumar' #
                Insert = session.query(Model.models.Application.M_PatientsDtl).get(PatientId)
                Insert.MPD_TokenFCM = tokenFcm
                session.commit()
                session.close()       
                return jsonify({'error':'Token updated successfully'}),201 
            else:
                return jsonify({'error':'JSON not available'}),400
            
        else:
            return jsonify({'error':'Method is not allowed'}),405
    except Exception as identifier:
        Logger.error(identifier)
    finally:
        session.close()