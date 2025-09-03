from models import Topic, User
from fastjson_db import TABLE_REGISTRY, JsonQuerier
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from dataclasses import asdict

@jwt_required()
def createTopic():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Invalid body"}), 400
    title, description = data.get("title"), data.get("description")
    if not title or not description:
        return jsonify({"error":"TItle and description are obrigatory"}), 400
    
    user_id = get_jwt_identity()
    user = TABLE_REGISTRY[User].get_by("_id", user_id)
    if not user:
        return jsonify({"error":"User not found"})
    
    new_topic = Topic(
        title=title,
        description=description
    )
    
    new_topic.user_id.set(user)
    TABLE_REGISTRY[Topic].insert(new_topic)
    TABLE_REGISTRY[Topic].flush()
    
    return jsonify({"topic":asdict(new_topic)})

def getTopics():
    return TABLE_REGISTRY[Topic].get_all()