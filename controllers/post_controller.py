from models import User, Topic, Post
from fastjson_db import TABLE_REGISTRY, JsonQuerier
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from dataclasses import asdict

@jwt_required()
def createPost():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Invalid body"}), 400
    title, description, topic_id = data.get("title"), data.get("text"), data.get("topic_id")
    if not title or not description or not topic_id:
        return jsonify({"error":"Title, topic id and description are obrigatory"}), 400
    
    user_id = get_jwt_identity()
    user = TABLE_REGISTRY[User].get_by("_id", user_id)
    if not user:
        return jsonify({"error":"User not found"})
    
    new_post = Post(
        title=title,
        text=description
    )
    
    new_post.user_id.set(user_id)
    new_post.topic_id.set(topic_id)
    
    TABLE_REGISTRY[Post].insert(new_post)
    TABLE_REGISTRY[Post].flush()
    
    return jsonify({"post":asdict(new_post)})

def getAllTopicPosts(id):
    return TABLE_REGISTRY[Post].get_by("topic_id", id)