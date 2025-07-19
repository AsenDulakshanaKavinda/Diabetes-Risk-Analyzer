import sys 
import logging

def error_message_detail(error: Exception, error_details: sys) -> str:
    """
    Extracts detailed error information including file name, line number and the error message.
    : param error: the exception that accurred.
    : param error_detail: the sys module to access traceback detail.
    : retrun: a formatted error message string.
    """

    # extract traceback details (exception formation)
    _, _, exc_tb = error_details.exc_info()

    # get the file name where the exception occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # create formatted error message string with file name, line number, and the actual error
    line_number = exc_tb.tb_lineno
    error_message = f"Error occurred in python script: [{file_name}] at line number [{line_number}]:  {str(error)}"

    # log the error for better tracking
    logging.error(error_message)

    return error_message

class ProjectException(Exception):
    """
    Custom exception class for handling errors in the Diabetes-Risk-Analyzer
    """

    def __init__(self, error_message: str, error_details: sys):
        """
        Initializes the exception with a detailed error massage.
        : param error_message: a string describing the error.
        : param error_detail: the sys module to access the traceback details.
        """

        # call the base class constructor with the error message.
        super().__init__(error_message)

        # format the detailed error message using the error_message_detail function.
        self.error_message = error_message_detail(error_message, error_details)

    def __str__(self) -> str:
        """
        returns the string representation of the error message.
        """
        return self.error_message












