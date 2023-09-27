from flask import Blueprint, render_template, request
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("value_select", __name__, url_prefix="/value_select")

data = {
    "audi": {"models": ["A1", "A4", "A6"]},
    "toyota": {"models": ["Landcruiser", "Tacoma", "Yaris"]},
    "bmw": {"models": ["325i", "325ix", "X5"]},
}


@bp.route("/")
def index():
    current_make = "audi"
    if htmx:
        return render_block(
            "value_select/index.html.j2",
            "content",
            makes=data.keys(),
            current_make=current_make,
            models=data[current_make]["models"],
        )
    else:
        return render_template(
            "value_select/index.html.j2",
            makes=data.keys(),
            current_make=current_make,
            models=data[current_make]["models"],
        )


@bp.route("/models/")
def models():
    current_make = request.args["make"]
    return render_block(
        "value_select/index.html.j2",
        "models",
        makes=data.keys(),
        current_make=current_make,
        models=data[current_make]["models"],
    )
