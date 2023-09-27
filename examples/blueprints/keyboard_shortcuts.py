from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("keyboard_shortcuts", __name__, url_prefix="/keyboard_shortcuts")


@bp.route("/")
def index():
    if htmx:
        return render_block("keyboard_shortcuts/index.html.j2", "content")
    else:
        return render_template("keyboard_shortcuts/index.html.j2")


@bp.route("/doit", methods=("POST",))
def do_it():
    return "Did it!"
