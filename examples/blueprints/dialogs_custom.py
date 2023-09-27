from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("dialogs_custom", __name__, url_prefix="/dialogs_custom")


@bp.route("/")
def index():
    if htmx:
        return render_block("dialogs_custom/index.html.j2", "content")
    else:
        return render_template("dialogs_custom/index.html.j2")


@bp.route("/modal")
def modal():
    return render_template("dialogs_custom/modal.html.j2")
