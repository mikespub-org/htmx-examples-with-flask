from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("lazy_loading", __name__, url_prefix="/lazy_loading")


@bp.route("/")
def index():
    if htmx:
        return render_block("lazy_loading/index.html.j2", "content")
    else:
        return render_template("lazy_loading/index.html.j2")


@bp.route("/graph")
def graph():
    return render_template("lazy_loading/image.html.j2")
