from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt

admin_bp = Blueprint("admin", __name__)


@admin_bp.get("/test")
@jwt_required()
def admin_test():
    claims = get_jwt()

    if claims["role"] != "admin":
        return jsonify({
            "status": "error",
            "message": "Admin access required"
        }), 403

    return jsonify({
        "status": "success",
        "message": "Admin API is working"
    })