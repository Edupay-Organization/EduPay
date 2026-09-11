from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.get("/")
@jwt_required()
def dashboard():
    return jsonify({
        "status": "success",
        "message": "Dashboard API is working"
    })