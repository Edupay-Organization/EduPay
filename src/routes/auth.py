from flask import Blueprint, request, jsonify
from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity
)

from src.models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.post("/login")
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({
            "status": "error",
            "message": "Email and password are required"
        }), 400

    user = User.query.filter_by(email=email).first()

    if not user or not user.check_password(password):
        return jsonify({
            "status": "error",
            "message": "Invalid email or password"
        }), 401

    token = create_access_token(
        identity=str(user.id),
        additional_claims={
            "role": user.role,
            "school_id": user.school_id
        }
    )

    return jsonify({
        "status": "success",
        "message": "Login successful",
        "access_token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "school_id": user.school_id
        }
    }), 200


@auth_bp.get("/me")
@jwt_required()
def current_user():
    user_id = get_jwt_identity()

    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    return jsonify({
        "status": "success",
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "role": user.role,
            "school_id": user.school_id
        }
    })