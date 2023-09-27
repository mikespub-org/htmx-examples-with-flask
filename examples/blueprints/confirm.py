from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("confirm", __name__, url_prefix="/confirm")


@bp.route("/")
def index():
    if htmx:
        return render_block("confirm/index.html.j2", "content")
    else:
        return render_template("confirm/index.html.j2")
