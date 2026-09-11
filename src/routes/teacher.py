from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from src.models import User

teacher_bp = Blueprint("teacher", __name__)


@teacher_bp.get("/class")
@jwt_required()
def assigned_class():
    user_id = get_jwt_identity()

    teacher = User.query.get(user_id)

    if not teacher or teacher.role != "teacher":
        return jsonify({
            "status": "error",
            "message": "Teacher access required"
        }), 403

    if not teacher.class_id:
        return jsonify({
            "status": "error",
            "message": "No class assigned"
        }), 404

    return jsonify({
        "status": "success",
        "class_id": teacher.class_id
    })