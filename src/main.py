import os
from flask import Flask, render_template, url_for, request
from config.constants import DefaultValues
from errors.handler import custom_handler
from errors.errors import custom_errors
from services.print_file.controller import PrintController

app = Flask(__name__)

app.register_error_handler(404, custom_handler.ErrorHandler)
app.register_error_handler(custom_errors.FileNotFound, custom_handler.ErrorHandler)
app.register_error_handler(custom_errors.InvalidValue, custom_handler.ErrorHandler)
app.register_error_handler(custom_errors.FileReadError, custom_handler.ErrorHandler)


@app.route("/print_page/<path:file_name>")
def index(file_name="file1.txt"):
    """
    api to print file name given

    Arguments:
    ----------
        file_name : from the url, eg "/print_file/" + "file/name/inside/of/render_file/dir "
        start_line (int): count of line to skip before printing
        end_line (int): stop after this cont of lines
    """
    file_path = os.path.join(app.root_path, DefaultValues.DEFAULT_RENDER_FOLDER, file_name)
    start_line = request.args.get("start_line") or 0
    end_line = request.args.get("end_line") or 0
    show_markup = request.args.get("show_markup") or False
    return PrintController.print_page(
        file_path=file_path,
        file_name=file_name,
        start_line=start_line,
        end_line=end_line,
        show_markup=show_markup,
    )


if __name__ == "__main__":
    app.run(debug=DefaultValues.DEFAULT_RUN_DEBUG, port=DefaultValues.DEFAULT_PORT)
