import datetime
import math
import os
import hmac
import cryptography
from datetime import timedelta
import json
from sqlalchemy.orm import session
import Common_Function.CommonFun
import Connection.const
import Model.models
import hashlib
import flask
#import crypto
import sys
import base64
import Constant.constant
import smtplib
import socket
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

UPLOAD_FOLDER = '/home/Vipul'

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'xlsx'}
Session = Connection.const.connectToDatabase()

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convertToJson(jsonFields, data):
    try:
        convertTxtToJson = [{col: getattr(
            d, col) for col in jsonFields} for d in data]
    except Exception as identifier:
        print('No parametes is passed.')
    return convertTxtToJson

# def verifyIP(IP):
#     session=Session()
#     try:
#         CheckIp = session.query(Model.models.Application.M_AllowedIPs.MAIID
#                     ).filter(Model.models.Application.M_AllowedIPs.MAI_IPs == IP
#                     ).filter_by(MAI_IsActive =1, MAI_IsDeleted =0).all()
#         return len(CheckIp)
#     except Exception as identifier:
#         print(identifier)
#     finally:
#         session.close()
        
def verifytoken(token):
    session=Session()
    try:
        CheckIp = session.query(Model.models.Application.T_TokenLog.TLID
                    ).filter(Model.models.Application.T_TokenLog.TL_Token == token
                    ).filter_by(TL_IsActive =1, TL_IsDeleted =0).all()
        return len(CheckIp)
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()        

def verifyIP(IP):
    session=Session()
    try:
        CheckIp = session.query(Model.models.Application.M_BlockedIPs.MBIID
                    ).filter(Model.models.Application.M_BlockedIPs.MBI_IPs == IP
                    ).filter_by(MBI_IsActive =1, MBI_IsDeleted =0).all()
        if(len(CheckIp)>0):
            return 1
        else:
            return 0
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()
         
def addRequestorIP(token):
    session=Session()
    try:
        Insert = Model.models.Application.M_RequestIPs()
        Insert.MRI_IPs=token
        Insert.MRI_AddDate=datetime.datetime.now()
        Insert.MRI_IsActive=1
        Insert.MRI_IsDeleted=0
        session.add(Insert)
        session.commit()
        session.close()
        
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

  
def verifyMobile(mobile):
    session=Session()
    try:
        CheckMobile = session.query(Model.models.Application.M_PatientsDtl.MPDID
                    ).filter(Model.models.Application.M_PatientsDtl.MPD_Mobile == mobile
                    ).filter_by(MPD_IsActive = 1, MPD_IsDeleted = 0, MPD_User =1).all()
        return len(CheckMobile)
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()
        
def Childcount(Id):
    session=Session()
    try:
        num=Id[3:]
        Childscount= session.query(Model.models.Application.M_Patient.MPID.label('Id'),
                Model.models.Application.M_Patient.MP_Name.label('Name')
                ).filter_by(MP_IsDeleted=0,MP_IsActive=1,MP_Mobile=num).all()
        return len(Childscount)
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()
        
# Added by Vipul Kumar:-29-11-2022
# Desc:- It will return ciphertext string value.
def encryptString(plainText):
    key = b'F4sEtLhzEL36Kg1vaoxY1U-cYl3Sw-LkmWoyJXG3w4s='
    encryption_type = cryptography.fernet.Fernet(key)
    encrypted_message = (encryption_type.encrypt(plainText.encode())).decode()
    return encrypted_message
# End

# Added by Vipul Kumar:-29-11-2022
# Desc:- It will return plain text string value.


def decryptString(ciphertext):
    key = b'F4sEtLhzEL36Kg1vaoxY1U-cYl3Sw-LkmWoyJXG3w4s='
    encryption_type = cryptography.fernet.Fernet(key)
    decrypted_message = (encryption_type.decrypt(
        ciphertext.encode())).decode()
    return decrypted_message        



def SaveAssessmentForms(Question,Answer,ParentId,FormName):
    session = Session()
    Insert =Model.models.Application.T_SaveAssessmentForms()
    Insert.TAF_FormName = FormName
    Insert.TAF_Question = Question
    Insert.TAF_Answer = Answer
    Insert.TAF_ParentId = int(ParentId)
    Insert.TAF_ChildId = 2
    
    Insert.TAF_AddDate = datetime.datetime.now()
    Insert.TAF_AddedBy = int(ParentId)
    session.add(Insert)
    session.commit()
    session.close()
    message = "Added Successfully"
    return message



