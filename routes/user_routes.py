from flask import Blueprint
from controllers.user_controller import createUser, login, getById

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/create", methods=["POST"])
def create_route():
    return createUser()

@user_bp.route("/login", methods=["POST"])
def login_route():
    return login()

@user_bp.route("/<int:id>", methods=["GET"])
def get_route():
    return getById()