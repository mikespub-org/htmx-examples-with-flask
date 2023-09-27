from flask import Blueprint, render_template, request
from jinja2_fragments.flask import render_block

from ..extensions import htmx

bp = Blueprint("dialogs_browser", __name__, url_prefix="/dialogs_browser")


@bp.route("/")
def index():
    if htmx:
        return render_block("dialogs_browser/index.html.j2", "content")
    else:
        return render_template("dialogs_browser/index.html.j2")


@bp.route("/submit", methods=("POST",))
def graph():
    response = request.headers["HX-Prompt"]
    # with flask-htmx
    # response = htmx.prompt
    return f"User entered <i>{response}</i>"
