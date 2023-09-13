import sqlalchemy
import pymysql
import sqlalchemy.ext.declarative as abc

class Connect:
    engine = sqlalchemy.create_engine(
        #'mysql+pymysql://admin:ContinuaAWSDatabase!123@mysqldatabase.cio4zvmrj7je.ap-south-1.rds.amazonaws.com:3306/continua_kids?charset=utf8')
        'mysql+pymysql://admin:Ch08nT!#b2k1@restore-db.cio4zvmrj7je.ap-south-1.rds.amazonaws.com:3306/continua_kids?charset=utf8', pool_size=2000, max_overflow=2000)

    Base = abc.declarative_base()

def createTable():
    Connect.Base.metadata.create_all(Connect.engine)

def connectToDatabase():
    Session = sqlalchemy.orm.sessionmaker(bind=Connect.engine)
    return Session

