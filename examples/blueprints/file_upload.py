from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("file_upload", __name__, url_prefix="/file_upload")


@bp.route("/")
def index():
    if htmx:
        return render_block("file_upload/index.html.j2", "content")
    else:
        return render_template("file_upload/index.html.j2")


@bp.route("/upload", methods=("POST",))
def upload_hyperscript():
    # upload logic would go here, see e.g. https://flask.palletsprojects.com/en/2.3.x/patterns/fileuploads/

    return (
        "",
        204,
    )  # return empty response so htmx does not overwrite the progress bar value
