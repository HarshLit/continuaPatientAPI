import datetime
from logging import makeLogRecord
import logging
import math
import os
import hmac
#from application import mail
from sqlalchemy.orm import session
from sqlalchemy.sql.expression import false
import Common_Function.CommonFun
import Common_Function.MailFun
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
import threading

from flask import copy_current_request_context
#from flask_mail import Mail
from flask_mail import  Message , Mail
#
#from app import mail

#mail = Mail()

Session = Connection.const.connectToDatabase()

#This is user(basic registration individual and corporate) registration confirmation mail send to the admin
def Registration_Mail_Admin(Name,UserName,Contact,UserType):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
        mail_body=  """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>"""+Name+""" Registered on Digikul!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+LinkUrl+"""' target="_blank"><img src='""" +LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span style="font-size:16px;">A new user, having following details, has registered successfully:</span></h3>
                    </td>
                    </tr>


                    <td width="40%">Name:</td>
                    <td><b>"""+Name+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">Email:</td>
                    <td><b>"""+UserName+"""</b></td>
                    </tr>
                    <tr>
                    <td width="40%">Mobile:</td>
                    <td><b>"""+Contact+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">User Type:</td>
                    <td><b>"""+UserType+"""</b></td>
                    </tr>

                        <tr>
                        <td  colspan="2"><p style="font-size:14px; margin-top:40px;">User can login after completing the registration process.</p>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>


                    </body>
                    </html>"""
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = Name + ' Registered on Digikul!'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

#This is send subscription confirmation mail to admin
def Subscription_Mail_Admin(Name,TXNID,BankTxnID,Amount,ExpDate,UserEmail,Contact,PlanName,FreqName,User_Type):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
        mail_body="""<!doctype html>
                        <html>
                        <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="icon" type="image/png" href="favicon.png" />
                        <title>Digikul User Subscription Successful !</title>
                        </head>
                        <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                        <center>
                        <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                        </center>

                        <table align="center" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px; font-size:14px;">
                        <tbody><tr style="background-color:#dbedd9; padding:0px;">
                        <td colspan="2">
                        <h3 style="font-size:16px; margin:0px;">The user, having following details:</h3>
                        </td>
                        </tr>
                        <tr>
                        <td width="40%">Name:</td>
                        <td><b>"""+Name+"""</b></td>
                        </tr>
                        <tr style="background-color:#E8E8E8;">
                        <td width="40%">Email:</td>
                        <td><b>"""+UserEmail+"""</b></td>
                        </tr>
                        <tr>
                        <td width="40%">Mobile:</td>
                        <td><b>"""+Contact+"""</b></td>
                        </tr>
                        <tr style="background-color:#E8E8E8;">
                        <td width="40%">User Type:</td>
                        <td><b>"""+User_Type+"""</b></td>
                        </tr>
                        <tr>
                        <td colspan="2">&nbsp;</td>
                        </tr>
                        <tr style="background-color:#dbedd9; padding:0px;">
                        <td colspan="2">
                        <h3 style="font-size:16px; margin:0px;">has subscribed successfully as per following details:</h3>
                        </td>
                        </tr>
                        <tr>
                        <td width="40%">Plan Name:</td>
                        <td><b>"""+PlanName+"""</b></td>
                        </tr>
                        <tr style="background-color:#E8E8E8;">
                        <td width="40%">Plan Frequency:</td>
                        <td><b>"""+FreqName+"""</b></td>
                        </tr>
                        <tr>
                        <td width="40%">Paid Amount (INR):</td>
                        <td><b>"""+Amount+"""</b></td>
                        </tr>
                        <tr style="background-color:#E8E8E8;">
                        <td width="40%">Plan Expiry Date:</td>
                        <td><b>"""+ExpDate+"""</b></td>
                        </tr>
                        <tr>
                        <td width="40%">Transaction Id:</td>
                        <td><b>"""+TXNID+"""</b></td>
                        </tr>
                        <tr style="background-color:#E8E8E8;">
                        <td width="40%">Bank Transaction Id:</td>
                        <td><b>"""+BankTxnID+"""</b></td>
                        </tr>
                            <tr>
                            <td  colspan="2">
                                <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                                <p style="color:#999; font-size:12px;">Thank you, click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a> !</p></td>
                            </tr>
                        </tbody>
                        </table>
                        <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                            Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                        <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>

                        </body>
                        </html>
                        """
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Digikul User Subscription Successful !'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

#This is send registration confirmation mail to user
def SendRegistration_Mail(Name,UserName,Password,URL):
    session=Session()
    try:
        # getAdminEmailID=Admin_Mail_Dtls()
        # Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL= False #getMailCredential[0].MMC_ISSSL
        MAIL_ISTLS= True
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
#changing the Password Cycle
        mail_body=  """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Your Registration is Successful!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+URL+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span data-markjs="true" class="markgkk7swyt2 _2mvHg_8QQFEuo2e0RlZLXB">Congratulations</span> """+Name+"""<br>

                    <span style="font-size:16px;">Your Registration is Successful !</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
                    <tr>
                    <td width="40%" style="background-color:#f1f1f1;">User Name:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+UserName+"""</b></td>
                    </tr>
                    

                        <tr>
                        <td  colspan="2"><p style="font-size:14px; margin-top:40px;"><a href='"""+URL+"""' style="background:#00affe; padding:1px 2px; color:white;text-decoration:none; letter-spacing:1.2px; font-size:13px; font-weight:500;">Click here</a> to Generate Password.</p>
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>
                    </body>
                    </html>
                    """


        #The mail addresses and password
        sender_address = Sender_Mail#'shamshersingh03071995@gmail.com'
        sender_pass = Sender_Pwd#'7388333748'
        To_Add=UserName
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your Registration is Successful!'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        text = message.as_string()
        print(text)
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent')
    except Exception as identifier:
        print(identifier)
    finally:
        pass
    
#This is send subscription confirmation mail to user
def SendSubscription_Mail(Name,TXNID,BankTxnID,Amount,ExpDate,UserEmail,PlanName,FreqName):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        
        mail_body="""<!doctype html>
                            <html>
                            <head>
                            <meta charset="utf-8" />
                            <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                            <meta name="viewport" content="width=device-width, initial-scale=1" />
                            <link rel="icon" type="image/png" href="favicon.png" />
                            <title>Your Digikul Subscription is Successful !</title>
                            </head>
                            <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                            <center>
                            <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                            </center>


                            <table align="center" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                            <tbody><tr>
                            <td align="center" colspan="2">
                            <h3><span data-markjs="true" class="markda6kui796 _2mvHg_8QQFEuo2e0RlZLXB">Congratulations</span>&nbsp; """+Name+""" !<br>

                            <span style="font-size:16px;">You have successfully subscribed Digikul membership plan!</span></h3>
                            </td>
                            </tr>
                            <tr>
                            <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                            </tr>
                            <tr>
                            <td width="40%">Plan Name:</td>
                            <td><b>"""+PlanName+"""</b></td>
                            </tr>
                            <tr style="background-color:#E8E8E8;">
                            <td width="35%">Plan Frequency:</td>
                            <td><b>"""+FreqName+"""</b></td>
                            </tr>
                            <tr>
                            <td width="40%">Paid Amount (INR):</td>
                            <td><b>"""+Amount+"""</b></td>
                            </tr>
                            <tr style="background-color:#E8E8E8;">
                            <td width="35%">Plan Expiry Date:</td>
                            <td><b>"""+ExpDate+"""</b></td>
                            </tr>
                            <tr>
                            <td width="40%">Transaction Id:</td>
                            <td><b>"""+TXNID+"""</b></td>
                            </tr>
                            <tr style="background-color:#E8E8E8;">
                            <td width="35%">Bank Transaction Id:</td>
                            <td><b>"""+BankTxnID+"""</b></td>
                            </tr>

                                <tr>
                                <td  colspan="2">
                                    <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                                    <p style="color:#999; font-size:12px;">Thank you, click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a> !</p></td>
                                </tr>
                            </tbody>
                            </table>
                            <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                                Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                            <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>


                            </body>
                            </html>
                            """

        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=UserEmail
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,CC_Add,BCC_Add] #--If you want cc bcc option then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] = message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Subscription is Successful.'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, int(Mail_Port)) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass

#This is send subscription confirmation mail to Corporate Employee
def SendCorEmpRegistration_Mail(Name,UserName,Password,mail_message,URL):
    session=Session()
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        

        mail_body=    """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Your Registration is Successful!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+URL+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3>Congratulations &nbsp;"""+Name+"""<br><span style="font-size:16px;">"""+mail_message+"""</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
                    <tr>
                    <td width="40%" style="background-color:#f1f1f1;">User Name:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+UserName+"""</b></td>
                    </tr>
                     <tr>
                        <td  colspan="2"><p style="font-size:14px; margin-top:40px;"><a href='"""+URL+"""' style="background:#00affe; padding:1px 2px; color:white;text-decoration:none; letter-spacing:1.2px; font-size:13px; font-weight:500;">Click here</a> to Generate Password.</p>
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>
                    </body>
                    </html>
                    """
                    

                   
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=UserName
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your Registration is Successful!'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent')
    except Exception as identifier:
        print(identifier)

#This is send subscription confirmation mail to admin
def CorEmpReg_Mail_Admin(Name,UserName,Contact,CorName,Corp_AdminMailID):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        

        mail_body= """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>"""+Name+""" Registered on Digikul!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span style="font-size:16px;">A new user, having following details, has registered successfully:</span></h3>
                    </td>
                    </tr>

                    <td width="40%">Name:</td>
                    <td><b>"""+Name+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">Email:</td>
                    <td><b>"""+UserName+"""</b></td>
                    </tr>
                    <tr>
                    <td width="40%">Mobile:</td>
                    <td><b>"""+Contact+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">Corporate Name:</td>
                    <td><b>"""+CorName+"""</b></td>
                    </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>


                    </body>
                    </html>"""

        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add+','+Corp_AdminMailID
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = Name + " Registered on Digikul!"
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

#This is excel imported individual/corporate users details mail to admin
def Send_UsersExcelImportDtls_Admin(Total,Success,Failed,UserType):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        mail_body=    """<!doctype html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="shortcut icon" href="favicon.ico" type="image/ico" sizes="16x16" />  
                    <title>User Details Import From Excel Sheet</title>  
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center><a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul" style="margin-top:20px; margin-bottom: 5px;" height="60"></a></center>
                    <table cellpadding="10" cellspacing="0"align="center" width="450" style="background-color:#fdfdff; border-radius:10px; padding: 10px 25px;">
                    <tbody>
                    <tr><td colspan="2" align ="center"><h3 style="font-size:16px;">Excel import details:</h3></td></tr> 
                    
                    <tr><td width="40%">Total Employee:</td><td><b>"""+Total+"""</b></td></tr>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Successfull:</td><td><b>"""+Success+"""</b></td></tr> </p>
                    <tr><td width="40%">Failed:</td><td><b>"""+Failed+"""</b></td></tr> </p>
                    <tr style="background-color: #e8e8e8;"><td width="40%">User Type:</td><td><b>"""+UserType+"""</b></td></tr> </p>                               
                    <tr><td colspan="2" style=" font-size:14px"><p>User can login after completing the registration process.
                    <p>If you believe you received this email in error, please mail to <a href=""style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></p>
                    <p>Thank you,&nbsp;<a href='"""+LinkUrl+"""' target="_blank"style="color:#18aef4;">Click here </a> &nbsp;to visit Digikul. </p>
                    <p style="color:#8e8c8f; text-align:center;">
                    <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br> Mail ID - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#4f4f88;">"""+Tech_SupportMailID+"""</a></small></p></td></tr></tbody></table>
                    
                    <table align="center" style="display:none;">
                    <tr><td><a href="" target="_blank">
                    <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/facebook.jpg" alt="Facebook" title="Facebook"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/twitter.jpg" alt="Twitter" title="Twitter"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/linkedin.jpg" alt="Linkedin" title="Linkedin"></a></td></tr></table>
                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul <br> <br><span style="font-size:10px;">You received this Email because you signed up in Digikul<br><a href="#" style="color:#4f4f88;">Unsubscribe</a></span></small> </p>
                    </body>
                    </html>"""
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'User Details Import From Excel Sheet'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

#This is excel imported employee details mail to admin
def Send_CopEmpExcelImport_Admin(Total,Success,Failed,CorName,Corp_AdminMailID):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        mail_body=    """<!doctype html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="shortcut icon" href="favicon.ico" type="image/ico" sizes="16x16" />  
                    <title>User Details Import From Excel Sheet.</title>  
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center><a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul" style="margin-top:20px; margin-bottom: 5px;" height="60"></a></center>
                    <table cellpadding="10" cellspacing="0"align="center" width="450" style="background-color:#fdfdff; border-radius:10px; padding: 10px 25px;">
                    <tbody>
                    <tr><td colspan="2" align ="center"><h3 style="font-size:16px;">Excel import details&nbsp;("""+CorName+"""):</h3></td></tr> 
                    
                    <tr><td width="40%">Total:</td><td><b>"""+Total+"""</b></td></tr>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Successful:</td><td><b>"""+Success+"""</b></td></tr> </p>
                    <tr><td width="40%">Failed:</td><td><b>"""+Failed+"""</b></td></tr> </p>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Corporate Name:</td><td><b>"""+CorName+"""</b></td></tr> </p>                               
                    <tr><td colspan="2" style=" font-size:14px">
                    <p>If you believe you received this email in error, please mail to <a href=""style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></p>
                    <p>Thank you,&nbsp;<a href='"""+LinkUrl+"""' target="_blank"style="color:#18aef4;">Click here </a> &nbsp;to visit Digikul. </p>
                    <p style="color:#8e8c8f; text-align:center;">
                    <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br> Mail ID - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#4f4f88;">"""+Tech_SupportMailID+"""</a></small></p></td></tr></tbody></table>
                    
                    <table align="center" style="display:none;">
                    <tr><td><a href="" target="_blank">
                    <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/facebook.jpg" alt="Facebook" title="Facebook"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/twitter.jpg" alt="Twitter" title="Twitter"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/linkedin.jpg" alt="Linkedin" title="Linkedin"></a></td></tr></table>
                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul <br> <br><span style="font-size:10px;">You received this Email because you signed up in Digikul<br><a href="#" style="color:#4f4f88;">Unsubscribe</a></span></small> </p>
                    </body>
                    </html>"""
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add+','+Corp_AdminMailID
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'User Details Import From Excel Sheet.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()


def Approval_Mail_Users(Name,UserName,URL):
    session=Session()
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        mail_body=    """<!doctype html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="shortcut icon" href="favicon.ico" type="image/ico" sizes="16x16" />  
                    <title>Your Registration is Approved Successfully.</title>  
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center><a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul" style="margin-top:20px; margin-bottom: 5px;" height="60"></a></center>
                    <table cellpadding="5" cellspacing="0"align="center" width="450" style="background-color:#fdfdff; border-radius:10px; padding: 10px 25px;">
                    <tbody>
                    <tr><td colspan="2"><h4>Dear&nbsp;&nbsp;"""+Name+""",</h4></td></tr> 
                    <tr><td colspan="2" style=" font-size:14px">You're <b>enabled</b> to login to Digikul now!</td></tr>
                    <tr><td colspan="2" style=" font-size:14px"><p>Kindly &nbsp;<a href='"""+URL+"""' target="_blank"style="color:#18aef4;">Click here </a> &nbsp;to login. </p>
                    <p>If you believe you received this email in error, please mail to <a href=""style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></p>
                    <p>Thank you,&nbsp;<a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4;">Click here </a> &nbsp;to visit Digikul. </p>
                    <p style="color:#8e8c8f; text-align:center;">
                    <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br> Mail ID - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#4f4f88;">"""+Tech_SupportMailID+"""</a></small></p></td></tr></tbody></table>
                    
                    <table align="center" style="display:none;">
                    <tr><td><a href="" target="_blank">
                    <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/facebook.jpg" alt="Facebook" title="Facebook"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/twitter.jpg" alt="Twitter" title="Twitter"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/linkedin.jpg" alt="Linkedin" title="Linkedin"></a></td></tr></table>
                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul <br> <br><span style="font-size:10px;">You received this Email because you signed up in Digikul<br><a href="#" style="color:#4f4f88;">Unsubscribe</a></span></small> </p>
                    </body>
                    </html>"""
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=UserName
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your Registration is Approved Successfully.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        session.close() 

def Approval_Mail_Admin():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close() 

def Blocked_Mail_Users():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

def  Blocked_Mail_Admin():
    session=Session()
    try:
        pass
    except Exception as identifier:
        print(identifier)
    finally:
        session.close() 

#This is use to send contact form data to the admin
def ContactFrom_Mail_Admin(Name,Email,Contact,Message):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        mail_body=    """<!doctype html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="shortcut icon" href="favicon.ico" type="image/ico" sizes="16x16" />  
                    <title>Contact Form Notification.</title>  
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center><a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul" style="margin-top:20px; margin-bottom: 5px;" height="60"></a></center>
                    <table cellpadding="10" cellspacing="0"align="center" width="450" style="background-color:#fdfdff; border-radius:10px; padding: 10px 25px;">
                    <tbody>
                    <tr><td colspan="2" align ="center"><h3 style="font-size:16px;">You have a new inquiry from your website.</h3></td></tr> 
                    
                    <tr><td width="40%">Name:</td><td><b>"""+Name+"""</b></td></tr>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Email ID:</td><td><b>"""+Email+"""</b></td></tr> </p>
                    <tr><td width="40%">Mobile No.:</td><td><b>"""+Contact+"""</b></td></tr> </p>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Message:</td><td><b>"""+Message+"""</b></td></tr> </p>                               
                    <tr><td colspan="2" style=" font-size:14px"><p>
                    <p>If you believe you received this email in error, please mail to <a href=""style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></p>
                    <p>Thank you,&nbsp;<a href='"""+LinkUrl+"""' target="_blank"style="color:#18aef4;">Click here </a> &nbsp;to visit Digikul. </p>
                    <p style="color:#8e8c8f; text-align:center;">
                    <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br> Mail ID - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#4f4f88;">"""+Tech_SupportMailID+"""</a></small></p></td></tr></tbody></table>
                    
                    <table align="center" style="display:none;">
                    <tr><td><a href="" target="_blank">
                    <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/facebook.jpg" alt="Facebook" title="Facebook"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/twitter.jpg" alt="Twitter" title="Twitter"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/linkedin.jpg" alt="Linkedin" title="Linkedin"></a></td></tr></table>
                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul <br> <br><span style="font-size:10px;">You received this Email because you signed up in Digikul<br><a href="#" style="color:#4f4f88;">Unsubscribe</a></span></small> </p>
                    </body>
                    </html>"""
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Contact Form Notification.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()


# def UserQuery_ToExpert(Category,QDetails,ExpMail,URL):
def UserQuery_ToExpert(Category,QDetails,ExpMail,URL,UserName,PendingQueryCount,queryTime,ExpertName):
    session=Session()
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body = """
                    <!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Query under """+Category+""" @ Digikul is raised on """+queryTime+""" by """+UserName+"""!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>

                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td colspan="2" style="font-size:14px;">
                    <p style="margin-top:0;margin-bottom:0;"><strong>Dear """+ExpertName+""",</strong><br>

                    <br>
                    """+UserName+""" has raised a query as per following details:<br>
                    <br>
                    </td></tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="30%"><strong>Category:</strong></td>
                    <td>"""+Category+"""</td>
                    </tr>
                    <tr>
                    <td><strong>Query:</strong></td>
                    <td>"""+QDetails+"""</td>
                    </tr>

                        <tr>
                        <td colspan="2">
                            <p style="font-size:14px; margin-top:40px;">Currently, """+PendingQueryCount+""" query(ies) are pending to be answered.  <a href="""+URL+""" style="background:#00affe; padding:1px 2px; color:white;text-decoration:none; letter-spacing:1.2px; font-size:13px; font-weight:500;">Click here</a> to respond now.</p>
                            
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a> !</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>

                    </body>
                    </html>

                """

        sender_address = Sender_Mail#'shamshersingh03071995@gmail.com'
        sender_pass = Sender_Pwd#'7388333748'
        To_Add=ExpMail
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Query under ' + Category + ' is raised on ' + queryTime + ', by ' + UserName + '!'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()

    except Exception as identifier:
        print(identifier)
    finally:
        pass

def QueryDetail_ToAdmin(Name,UserName,UserType,Category):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL
        mail_body= """<!doctype html>
                    <html>
                    <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="shortcut icon" href="favicon.ico" type="image/ico" sizes="16x16" />  
                    <title>User Query: Emailer</title>  
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center><a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul" style="margin-top:20px; margin-bottom: 5px;" height="60"></a></center>
                    <table cellpadding="10" cellspacing="0"align="center" width="450" style="background-color:#fdfdff; border-radius:10px; padding: 10px 25px;">
                    <tbody>
                    <tr><td colspan="2" align ="center"><h3 style="font-size:16px;">A new user having following details has registered successfully:</h3></td></tr> 
                    
                    <tr><td width="40%">User Name:</td><td><b>"""+Name+"""</b></td></tr>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Email ID:</td><td><b>"""+UserName+"""</b></td></tr> </p>
                    <tr><td width="40%">User Type.:</td><td><b>"""+UserType+"""</b></td></tr> </p>
                    <tr style="background-color: #e8e8e8;"><td width="40%">Categary:</td><td><b>"""+Category+"""</b></td></tr> </p>                               
                    <tr><td colspan="2" style=" font-size:14px"><p>Expert Responce to the query.
                    <p>If you believe you received this email in error, please mail to <a href=""style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></p>
                    <p>Thank you,&nbsp;<a href='"""+LinkUrl+"""' target="_blank"style="color:#18aef4;">Click here </a> &nbsp;to visit Digikul. </p>
                    <p style="color:#8e8c8f; text-align:center;">
                    <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br> Mail ID - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#4f4f88;">"""+Tech_SupportMailID+"""</a></small></p></td></tr></tbody></table>
                    
                    <table align="center" style="display:none;">
                    <tr><td><a href="" target="_blank">
                    <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/facebook.jpg" alt="Facebook" title="Facebook"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/twitter.jpg" alt="Twitter" title="Twitter"></a></td>
                    <td><a href="" target="_blank"> <img src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/linkedin.jpg" alt="Linkedin" title="Linkedin"></a></td></tr></table>
                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul <br> <br><span style="font-size:10px;">You received this Email because you signed up in Digikul<br><a href="#" style="color:#4f4f88;">Unsubscribe</a></span></small> </p>
                    </body>
                    </html>"""
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'User Query Successful.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        #print('Mail Sent TO Admin')
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

def Sendtestingmail():
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID= 'ajay@digitalsolutions.co.in' #getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body=    """Enter Mail Body Hear"""

        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Site Opened Successful.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        logging.error(identifier)
    finally:
        pass


def Query_AnswerMail():
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body=    """Enter Mail Body Hear"""

        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'User Registration Successful.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def Query_AnswerMailToAdmin():
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body=    """Enter Mail Body Hear"""

        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'User Registration Successful.'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def Admin_Mail_Dtls():
    session=Session()
    try:
        getAdminEmailID=session.query(Model.models.Admin.M_UserDetails.MUD_Admin_EmailID).filter_by(MUD_Type=0,MUD_IsActive=1,MUD_IsDeleted=0).first()
        return getAdminEmailID
    except Exception as identifier:
        print(identifier)

def Mail_Credential():
    session=Session()
    try:
        getMailCredential=session.query(Model.models.Application.M_MailCredentials.MMC_ID,Model.models.Application.M_MailCredentials.MMC_From_MailID,
                                        Model.models.Application.M_MailCredentials.MMC_Password,Model.models.Application.M_MailCredentials.MMC_MailDisplayName,
                                        Model.models.Application.M_MailCredentials.MMC_MailHost,Model.models.Application.M_MailCredentials.MMC_MailPort,
                                        Model.models.Application.M_MailCredentials.MMC_ISSSL,Model.models.Application.M_MailCredentials.MMC_ReplyTo,
                                        Model.models.Application.M_MailCredentials.MMC_CC_MailID,Model.models.Application.M_MailCredentials.MMC_BCC_MailID).filter_by(MMC_IsActive=1,MMC_IsDeleted=0).order_by(Model.models.Application.M_MailCredentials.MMC_ID).all()
        return getMailCredential
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def App_SupportDtls():
    session=Session()
    try:
        getSupportDtls=session.query(Model.models.Application.M_TechnicalDtls.MTD_SupportMailID,Model.models.Application.M_TechnicalDtls.MTD_SupportContact,Model.models.Application.M_TechnicalDtls.MTD_CopyRightYear,Model.models.Application.M_TechnicalDtls.MTD_SupportPersonMailId,Model.models.Application.M_TechnicalDtls.MTD_URL).filter_by(MTD_IsActive=1,MTD_IsDeleted=0).all()
        return getSupportDtls
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def QueryRespondMail(receiverMailID):
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear

        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body= """<!doctype html>
                        <html>
                        <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="icon" type="image/png" href="favicon.png" />
                        <title>Query Response is Live @ Digikul !</title>
                        </head>
                        <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                        <center>
                        <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                        </center>

                        <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                        <tbody><tr>
                        <td colspan="2" style="font-size:14px;">
                        <p style="margin-top:0;margin-bottom:0; margin-top:20px;"><strong>The Response is Live, now!</strong></p>
                        <p style="font-size:14px; margin-top:20px;">Please <a href='"""+LinkUrl+"""' style="background:#00affe; padding:1px 2px; color:white;text-decoration:none; letter-spacing:1.2px; font-size:13px; font-weight:500;">Click here</a> to view the Response!</p>
                        </td></tr>
                            <tr>
                            <td colspan="2">
                                <p style="margin-top:20px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                                <p style="color:#999; font-size:12px;">Thank you, click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a> !</p></td>
                            </tr>
                        </tbody>
                        </table>
                        <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                            Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                        <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>

                        </body>
                        </html>"""
    
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=receiverMailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Query Response is Live @ Digikul !'
        message.attach(MIMEText(mail_body,'html'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass

def User_QueryMail(receiverMailID, recieverName):
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear

        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL



        mail_body= """<!doctype html>
                        <html>
                        <head>
                        <meta charset="utf-8" />
                        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                        <meta name="viewport" content="width=device-width, initial-scale=1" />
                        <link rel="icon" type="image/png" href="favicon.png" />
                        <title>Your query is received on Digikul!</title>
                        </head>
                        <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                        <center>
                        <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                        </center>

                        <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                        <tbody><tr>
                        <td colspan="2" style="font-size:14px;">
                        <p style="margin-top:0;margin-bottom:0;">Hi """+recieverName+""",<br>

                        <br>

                        Thank you for your query! One of our experts will respond ASAP.<br>

                        <br>

                        Thanks,<br>
                        <strong>Team Digikul</strong> </p>
                        </td></tr>
                            <tr>
                            <td colspan="2">
                                <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                                <p style="color:#999; font-size:12px;">Thank you, click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a> !</p></td>
                            </tr>
                        </tbody>
                        </table>
                        <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                            Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                        <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>

                        </body>
                        </html>"""
    
        #The mail addresses and password
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=receiverMailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your query is received on Digikul!'
        message.attach(MIMEText(mail_body,'html'))
        #Create SMTP session for sending the mail
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass


#This is send registration confirmation mail to Expert
def SendExpertRegistration_Mail(Name,UserName,Password,URL):
    session=Session()
    try:
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL= False #getMailCredential[0].MMC_ISSSL
        MAIL_ISTLS= True
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body=  """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>Your Registration is Successful!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+URL+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span data-markjs="true" class="markgkk7swyt2 _2mvHg_8QQFEuo2e0RlZLXB">Congratulations</span> """+Name+"""<br>

                    <span style="font-size:16px;">Your Registration is Successful !</span></h3>
                    </td>
                    </tr>
                    <tr>
                    <td align="center" colspan="2"><img data-imagetype="External" src="https://backoffice.meripunji.com/cyber_charcha_mailer_images/success.png" width="60" height="60" style="padding:0 5px;"></td>
                    </tr>
                    <tr>
                    <td width="40%" style="background-color:#f1f1f1;">User Name:</td>
                    <td style="background-color:#f1f1f1;"><b>"""+UserName+"""</b></td>
                    </tr>
                    

                        <tr>
                        <td  colspan="2"><p style="font-size:14px; margin-top:40px;"><a href='"""+URL+"""' style="background:#00affe; padding:1px 2px; color:white;text-decoration:none; letter-spacing:1.2px; font-size:13px; font-weight:500;">Click here</a> to Generate Password.</p>
                            <p style="margin-top:50px; color:#999; font-size:12px;">If you believe you received this email in error, please contact <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a>.</p>
                            <p style="color:#999; font-size:12px;">Thank you, Click here to visit <a href='"""+LinkUrl+"""' target="_blank" style="color:#18aef4; font-size:12px;">Digikul</a>!</p></td>
                        </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>
                    </body>
                    </html>
                    """
        #The mail addresses and password
        sender_address = Sender_Mail#'shamshersingh03071995@gmail.com'
        sender_pass = Sender_Pwd#'7388333748'
        To_Add=UserName
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        #receiver_address=UserName
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        #message['From'] = Sender_DisplayName + f''+sender_address +''#sender_address
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = 'Your Registration is Successful!'   #The subject line
        #The body and the attachments for the mail
        #message.attach(MIMEText(mail_content, 'plain'))
        message.attach(MIMEText(mail_body,'html'))
        #Create SMTP session for sending the mail
        #session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session = smtplib.SMTP(Mail_host, Mail_Port) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        pass

#This is Expert registration confirmation mail send to the admin
def ExpertRegistration_Mail_Admin(Name,UserName,Contact,UserType):
    session=Session()
    try:
        getAdminEmailID=Admin_Mail_Dtls()
        Admin_MailID=getAdminEmailID[0]
        getSupportDtls=App_SupportDtls()
        Tech_SupportMailID=getSupportDtls[0].MTD_SupportMailID
        CopyRightYear=getSupportDtls[0].MTD_CopyRightYear
        getMailCredential=Mail_Credential()
        Sender_Mail=getMailCredential[0].MMC_From_MailID
        Sender_Pwd=getMailCredential[0].MMC_Password
        Sender_DisplayName=getMailCredential[0].MMC_MailDisplayName
        Mail_host=getMailCredential[0].MMC_MailHost
        Mail_Port=getMailCredential[0].MMC_MailPort
        Mail_ISSSL=getMailCredential[0].MMC_ISSSL
        Reply_To=getMailCredential[0].MMC_ReplyTo
        CC_MailID=getMailCredential[0].MMC_CC_MailID
        BCC_MailID=getMailCredential[0].MMC_BCC_MailID
        LinkUrl = getSupportDtls[0].MTD_URL

        mail_body=  """<!doctype html>
                    <html>
                    <head>
                    <meta charset="utf-8" />
                    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
                    <meta name="viewport" content="width=device-width, initial-scale=1" />
                    <link rel="icon" type="image/png" href="favicon.png" />
                    <title>"""+Name+""" Registered on Digikul!</title>
                    </head>
                    <body style="background-color: #f0f0f0;margin: 0;padding: 0;font-family:Segoe UI, Open Sans, Helvetica Neue, Helvetica, Arial, sans-serif;">
                    <center>
                    <a href='"""+LinkUrl+"""' target="_blank"><img src='"""+LinkUrl+"""static/Home_Theme/img/logo.png' alt="Digikul" title="Digikul"style="margin-top:20px; margin-bottom:20px;" height="60"></a>
                    </center>


                    <table align="center" width="500" cellspacing="0" cellpadding="10" style="background-color:#FDFDFF;border-radius:10px;padding:10px 25px;">
                    <tbody><tr>
                    <td align="center" colspan="2">
                    <h3><span style="font-size:16px;">A new user, having following details, has registered successfully:</span></h3>
                    </td>
                    </tr>


                    <td width="40%">Name:</td>
                    <td><b>"""+Name+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">Email:</td>
                    <td><b>"""+UserName+"""</b></td>
                    </tr>
                    <tr>
                    <td width="40%">Mobile:</td>
                    <td><b>"""+Contact+"""</b></td>
                    </tr>
                    <tr style="background-color:#E8E8E8;">
                    <td width="40%">User Type:</td>
                    <td><b>"""+UserType+"""</b></td>
                    </tr>
                    </tbody>
                    </table>
                    <p style="color:#8e8c8f; text-align:center; font-size:14px;"> <small>106, Siddharth Chambers Hauz Khas, Kalu Sarai, New Delhi 110016. (Near IIT Gate, Adj. Azad Appt.)<br>
                        Mail us - <a href='mailto:"""+Tech_SupportMailID+"""' style="color:#18aef4;">"""+Tech_SupportMailID+"""</a></small></p>

                    <p style="color:#8e8c8f; margin-top: 5px;text-align:center;"><small>@ Copyright <script>document.write(new Date().getFullYear());</script> Digikul</p>


                    </body>
                    </html>"""
        #The mail addresses and password
        # send_async(Sender_Mail, Sender_Pwd, Admin_MailID, CC_MailID,BCC_MailID,Sender_DisplayName,Reply_To,Name,mail_body,Mail_host,Mail_Port)
        sender_address = Sender_Mail
        sender_pass = Sender_Pwd
        To_Add=Admin_MailID
        CC_Add=CC_MailID
        BCC_Add=BCC_MailID
        
        #receiver_address = [To_Add,Admin_MailID,CC_Add,BCC_Add]#If you want cc bcc option  then use this
        Receiver_MailList=To_Add
        receiver_address=Receiver_MailList.split(',')
        #Setup the MIME
        message = MIMEMultipart()
        message['From'] =formataddr((str(Header(Sender_DisplayName, 'utf-8')), sender_address))
        message['To'] = To_Add
        #message['Cc'] = CC_Add
        #message['Bcc'] = BCC_Add
        message.add_header('reply-to', Reply_To)
        message['Subject'] = Name + ' Registered on Digikul!'
        message.attach(MIMEText(mail_body,'html'))
        session = smtplib.SMTP(Mail_host, Mail_Port)
        session.starttls()
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
    except Exception as identifier:
        print(identifier)
    finally:
        session.close()

