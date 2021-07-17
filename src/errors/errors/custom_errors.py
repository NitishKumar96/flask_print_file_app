from flask import redirect, render_template
from config.constants import DefaultValues, ErrorConstants
from werkzeug.exceptions import HTTPException, NotFound


class FileNotFound(Exception):
    """error when file is not present on server"""

    code = ErrorConstants.ERROR_FILE_NOT_FOUND_CODE
    error_type = ErrorConstants.ERROR_FILE_NOT_FOUND_TYPE
    message = ErrorConstants.ERROR_FILE_NOT_FOUND_MSG

    def __init__(self, message=ErrorConstants.ERROR_FILE_NOT_FOUND_MSG):
        self.message = message


class InvalidValue(Exception):
    """error when file is not present on server"""

    code = ErrorConstants.ERROR_NOT_ACCEPTABLE_CODE
    error_type = ErrorConstants.ERROR_NOT_ACCEPTABLE_TYPE
    message = ErrorConstants.ERROR_NOT_ACCEPTABLE_MSG

    def __init__(self, message=ErrorConstants.ERROR_NOT_ACCEPTABLE_MSG):
        self.message = message


class FileReadError(Exception):
    """error when file is not present on server"""

    code = ErrorConstants.ERROR_FILE_READ_CODE
    error_type = ErrorConstants.ERROR_FILE_READ_TYPE
    message = ErrorConstants.ERROR_FILE_READ_MSG

    def __init__(self, message=ErrorConstants.ERROR_FILE_READ_MSG):
        self.message = message
