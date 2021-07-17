from flask import redirect, render_template
from config.constants import DefaultValues, ErrorConstants
from errors.errors import custom_errors
from werkzeug.exceptions import NotFound


def ErrorHandler(err):
    """Custom handler"""
    # for default page not found error redirect to main page
    if isinstance(err, NotFound):
        return redirect("/print_page/" + DefaultValues.DEFAULT_FILE_NAME, code=302)

    # it is a custom error
    else:
        error = {
            "code": err.code,
            "type": err.error_type,
            "message": err.message,
        }
        return render_template(
            "error.html",
            error=error,
        )
