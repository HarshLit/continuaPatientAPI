import hashlib
from logging import Logger
import random
import re
import flask
from flask import Flask, request, jsonify
import Model.models
import datetime
import Common_Function
import Common_Function.CommonFun
import Connection.const
from sqlalchemy import or_
from Common_Function import Shared_Library as CommonModule
import Constant.constant
# import Common_Function.Logs
# logger=Common_Function.Logs.getloggingDetails()

Session = Connection.const.connectToDatabase()
Development_Blueprint = CommonModule.flask.Blueprint(
    'Development_Blueprint', import_name=__name__)


        
@Development_Blueprint.route('/DevelopmentDropdown', methods=['POST','GET'])
def DevelopmentDropdown():
    session=Session()
    try:
        if(flask.request.method == 'GET'):
            DevelopmentDropdown= Common_Function.CommonFun.convertToJson(
                        Constant.constant.constant.DevelopmentDropdown,
                        session.query(Model.models.Application.M_Service.MSID.label('key'),
                                    Model.models.Application.M_Service.MS_CategoryName.label('label')
                                    ).filter_by(MS_IsDeleted=0).all()
                                )
            session.commit()
            return jsonify(result=DevelopmentDropdown)
        else:
            return jsonify({'error':'Method is not allowed'}),405
    
    finally:
        session.close()        