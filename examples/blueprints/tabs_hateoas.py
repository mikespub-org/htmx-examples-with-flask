from flask import Blueprint, render_template
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("tabs_hateoas", __name__, url_prefix="/tabs_hateoas")


@bp.route("/")
def index():
    if htmx:
        return render_block("tabs_hateoas/index.html.j2", "content")
    else:
        return render_template("tabs_hateoas/index.html.j2")


@bp.route("/tab1/")
def tab1():
    return render_template("tabs_hateoas/tab1.html.j2")


@bp.route("/tab2/")
def tab2():
    return render_template("tabs_hateoas/tab2.html.j2")


@bp.route("/tab3/")
def tab3():
    return render_template("tabs_hateoas/tab3.html.j2")
