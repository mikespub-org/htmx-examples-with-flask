from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("preserving_file_inputs", __name__, url_prefix="/preserving_file_inputs")


@bp.route("/")
def index():
    if htmx:
        return render_block("preserving_file_inputs/index.html.j2", "content")
    else:
        return render_template("preserving_file_inputs/index.html.j2")


@bp.route("/upload", methods=("POST",))
def upload_hyperscript():
    return "Uploaded!"
