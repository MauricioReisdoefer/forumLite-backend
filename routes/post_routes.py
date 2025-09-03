from flask import Blueprint
from controllers.post_controller import createPost, getAllTopicPosts

post_bp = Blueprint("posts", __name__, url_prefix="/posts")

@post_bp.route("/create")
def create_route():
    return createPost

@post_bp.route("/<int:id>")
def login_route():
    return getAllTopicPosts