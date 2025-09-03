from fastjson_db import TABLE_REGISTRY, JsonQuerier
from models import User
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from dataclasses import asdict

def createUser():
    data = request.get_json()
    if not data:
        return jsonify({"error":"Invalid body"}), 400
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify({"error":"Username and password are obrigatory"}), 400
    
    new_user = User(
        name=username,
        _password=password
    )
    
    TABLE_REGISTRY[User].insert(new_user)
    TABLE_REGISTRY[User].flush()
    
    user_dict = asdict(new_user)
    user_dict.pop("_password", None)
    return jsonify({"user":user_dict})

def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid body"}), 400

    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify({"error": "Username and password are obligatory"}), 400

    querier = JsonQuerier(User)
    user_list = querier.filter(name=username)
    
    if not user_list:
        return jsonify({"error": "User not found"}), 404

    user = user_list[0]

    if not user.check_password(password):
        return jsonify({"error": "Invalid password"}), 401

    access_token = create_access_token(identity=user._id)

    return jsonify({
        "message": "Login successful",
        "access_token": access_token
    })
    