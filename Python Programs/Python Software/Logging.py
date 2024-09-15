import logging

#Debug - Detailed Information : Used when Diagnosing Problems

#Info - Confirmations That Things Are Working As Planned

#Warning - Indication That Something Went Wrong Ex) (Low Disk Space) But Code Is Still Functional

#Error - Due To A Problem, A Snipet Of Code Has Stopped Functioning

#Critical - A Serious Error That May Cause Script To Stop Running

#Default Logging Level = Warning+

logging.basicConfig(filename='Test.log',level=logging.DEBUG,
                    format = '%(asctime)s:%(levelname)s:%(message)s')
def Add(x,y):
    return(x + y)
	
def Subtract(x,y):
    return(x - y)
	
def Multiply(x,y):
    return(x * y)
	
def Divide(x,y):
    return(x / y)
	
x = input(": ")
y = input(": ")

logging.info(Add(int(x),int(y)))
logging.info(Subtract(int(x),int(y)))
logging.info(Multiply(int(x),int(y)))
logging.info(Divide(int(x),int(y)))
