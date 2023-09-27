from flask import Blueprint, render_template, request
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("bulk_update", __name__, url_prefix="/bulk_update")

data = [
    {
        "name": "Joe Smith",
        "email": "joe@smith.org",
        "status": "Active",
    },
    {
        "name": "Angie MacDowell",
        "email": "angie@macdowell.org",
        "status": "Active",
    },
    {
        "name": "Fuqua Tarkenton",
        "email": "fuqua@tarkenton.org",
        "status": "Active",
    },
    {
        "name": "Kim Yee",
        "email": "kim@yee.org",
        "status": "Inactive",
    },
]


@bp.route("/")
def index():
    if htmx:
        return render_block("bulk_update/index.html.j2", "content", contacts=data)
    else:
        return render_template("bulk_update/index.html.j2", contacts=data)


@bp.route("/activate", methods=("PUT",))
def activate():
    for id in request.form.getlist("ids", type=int):
        data[id]["status"] = "Active"

    return index()


@bp.route("/deactivate", methods=("PUT",))
def deactivate():
    for id in request.form.getlist("ids", type=int):
        data[id]["status"] = "Inactive"

    return index()
