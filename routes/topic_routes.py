from flask import Blueprint
from controllers.topic_controller import createTopic, getTopics

topic_bp = Blueprint("topics", __name__, url_prefix="/topics")

@topic_bp.route("/create")
def create_route():
    return createTopic

@topic_bp.route("/")
def login_route():
    return getTopics