"""Global constant file """


class DefaultValues:
    """Deafult values for the api"""

    DEFAULT_RUN_DEBUG = True
    DEFAULT_PORT = 5000
    DEFAULT_FILE_NAME = "file1.txt"
    DEFAULT_RENDER_FOLDER = "render_files"
    DEFAULT_START_LINE = 0
    DEFAULT_END_LINE = 10


class ErrorConstants:
    """Constants related to error"""

    ERROR_FILE_NOT_FOUND_TYPE = "FileNotFound"
    ERROR_FILE_NOT_FOUND_CODE = 404
    ERROR_FILE_NOT_FOUND_MSG = "File not present: {file_name}"

    ERROR_NOT_ACCEPTABLE_TYPE = "ValueNotAcceptable"
    ERROR_NOT_ACCEPTABLE_CODE = 406
    ERROR_NOT_ACCEPTABLE_MSG = "Invalid Value Provided: "

    ERROR_FILE_READ_TYPE = "FileReadError"
    ERROR_FILE_READ_CODE = 500
    ERROR_FILE_READ_MSG = "error while reading the file: "

    SHOW_SEPARATE_ERROR_PAGE = False
