from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("dialogs_bootstrap", __name__, url_prefix="/dialogs_bootstrap")


@bp.route("/")
def index():
    if htmx:
        return render_block("dialogs_bootstrap/index.html.j2", "content")
    else:
        return render_template("dialogs_bootstrap/index.html.j2")


@bp.route("/modal")
def modal():
    return render_template("dialogs_bootstrap/modal.html.j2")
