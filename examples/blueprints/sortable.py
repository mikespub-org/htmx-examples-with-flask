from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("sortable", __name__, url_prefix="/sortable")


@bp.route("/")
def index():
    if htmx:
        return render_block("sortable/index.html.j2", "content")
    else:
        return render_template("sortable/index.html.j2")


@bp.route("/items", methods=("POST",))
def items():
    # store order of items here
    return ("", 204)
