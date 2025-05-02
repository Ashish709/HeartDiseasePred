import sys
from heartdisease.logging import logger
from heartdisease.exception import exception

if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Cu as e:
           raise (e,sys)



