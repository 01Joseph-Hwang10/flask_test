from flask import Blueprint


bp = Blueprint("root", __name__, url_prefix="/")


@bp.route("/", methods=["GET"])
def root():
    return "This is root page"
