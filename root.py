from flask import Blueprint


bp = Blueprint("root", __name__, url_prefix="/root")


@bp.route("/", methods=["GET"])
def root():
    return "This is root page"
