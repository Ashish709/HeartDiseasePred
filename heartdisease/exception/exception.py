import os
import sys
from heartdisease.logging import logger
import logging



class CustomException(Exception):
    def __init__(self,error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()
        
        self.lineno=exc_tb.tb_lineno
        self.file_name=exc_tb.tb_frame.f_code.co_filename 
    
    def __str__(self):
        return "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name, self.lineno, str(self.error_message))
        
if __name__=='__main__':
    try:
        logger.logging.info("Enter the try block")
        a=1/0
        print("This will not be printed",a)
    except Exception as e:
           raise CustomException(e,sys)














# class CustomException(Exception):
#     def __init__(self, error_message:Exception, error_detail:sys):
#         super().__init__(error_message)
        
#         self.error_message = CustomException.get_detailed_error_message(error_message=error_message,
#                                                                          error_detail=error_detail)
        
        
#     @staticmethod
#     def get_detailed_error_message(error_message:Exception, error_detail:sys) -> str:
        
#         """
#         error_message: Exception object
#         error_detail: object of sys module
#         """
#         _, _, exec_tb = error_detail.exc_info()
        
#         line_number = exec_tb.tb_lineno
        
#         exception_block_line_number = exec_tb.tb_frame.f_lineno
#         try_block_line_number = exec_tb.tb_lineno
        
#         file_name = exec_tb.tb_frame.f_code.co_filename
        
#         error_message = f"""
#         Error occured in script: 
#         [ {file_name} ] at 
#         try block line number: [{try_block_line_number}] and 
#         exception block line number: [{exception_block_line_number}] 
#         error message: [{error_message}]
#         """
#         #logging.info("Error Occured ",error_message)  
#         return error_message
        
    
#     def __str__(self):
#         return self.error_message
    
    
#     def __repr__(self) -> str:
#         return CustomException.__name__.str()

     

# # if __name__=='__main__':
# #     try:
# #         logger.logging.info("Enter the try block")
# #         a=1/0
# #         print("This will not be printed",a)
# #     except Exception as e:
# #            raise CustomException(e,sys)