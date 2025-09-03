from flask import Blueprint
from controllers.user_controller import createUser, login, getById

user_bp = Blueprint("users", __name__, url_prefix="/users")

@user_bp.route("/create")
def create_route():
    return createUser

@user_bp.route("/login")
def login_route():
    return login

@user_bp.route("/<int:id>")
def get_route():
    return getById()