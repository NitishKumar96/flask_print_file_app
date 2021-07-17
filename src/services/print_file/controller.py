""" Print Page Controller file """
from os import path
from flask import render_template
from charset_normalizer import from_path
from errors.errors import custom_errors
from config.constants import DefaultValues, ErrorConstants


class PrintController:
    """Controller class to handle all request to print page api"""

    @classmethod
    def print_page(
        cls,
        file_path: str,
        file_name: str,
        start_line: int,
        end_line: int,
        show_markup: bool = False,
    ):
        """methor to read given file and return the view file"""

        old_data = {"file_name": file_name, "start_line": start_line, "end_line": end_line}
        file_lines = []
        error = None

        if path.exists(file_path) is False:
            if ErrorConstants.SHOW_SEPARATE_ERROR_PAGE is True:
                raise custom_errors.FileNotFound(
                    message=ErrorConstants.ERROR_FILE_NOT_FOUND_MSG.format(file_name=file_name)
                )
            error = {
                "code": 404,
                "type": "NotFound",
                "message": "File not present: " + file_name,
            }

        try:
            end_line = int(end_line)
            start_line = int(start_line)
        except:
            if ErrorConstants.SHOW_SEPARATE_ERROR_PAGE is True:
                raise custom_errors.InvalidValue(
                    message=ErrorConstants.ERROR_NOT_ACCEPTABLE_MSG
                    + " Start line and end line should be int value"
                )
            error = {
                "code": 406,
                "type": "NotAcceptable",
                "message": "Start line and end line should be int value",
            }

        show_markup = True if show_markup in ["true", "True", True] else False

        if start_line > end_line:
            if ErrorConstants.SHOW_SEPARATE_ERROR_PAGE is True:
                raise custom_errors.InvalidValue(
                    message=ErrorConstants.ERROR_NOT_ACCEPTABLE_MSG
                    + " Start line should be smaller than end line"
                )
            error = {
                "code": 406,
                "type": "NotAcceptable",
                "message": "Start line should be smaller than end line",
            }

        if error is None:
            try:
                encoding = from_path(file_path).best().encoding
                current_line_number = 0
                txt_file = open(file_path, "r", encoding=encoding)
                for line in txt_file:
                    if current_line_number >= start_line:
                        file_lines.append(line)

                    if end_line > 0 and current_line_number >= end_line:
                        break
                    current_line_number += 1

            except Exception as e:
                if ErrorConstants.SHOW_SEPARATE_ERROR_PAGE is True:
                    raise custom_errors.FileReadError(
                        message=ErrorConstants.ERROR_FILE_READ_MSG
                        + " Error while reading File - "
                        + str(e)
                    )
                error = {
                    "code": 500,
                    "type": "ServerError",
                    "message": "Error while reading file: " + str(e.with_traceback),
                }

        return render_template(
            "index.html",
            old_data=old_data,
            error=error,
            file_lines=file_lines,
            show_markup=show_markup,
        )
