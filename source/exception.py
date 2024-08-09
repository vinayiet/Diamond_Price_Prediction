from source.logger import logger
import sys

def error_msg_detail(error, error_detail:sys):
    _,_,exc_tb= error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_msg = f'Error: {error} in {file_name} at line {exc_tb.tb_lineno}'

    return error_msg

class CustomException(Exception):
    def __init__(self, error, error_detail:sys):
        self.error = error
        self.error_detail = error_detail
        logger.error(error_msg_detail(self.error, self.error_detail))
        super().__init__(self.error)