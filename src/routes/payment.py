from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

from src.models import Payment

payments_bp = Blueprint("payments", __name__)


@payments_bp.get("/test")
@jwt_required()
def payment_test():
    return jsonify({
        "status": "success",
        "message": "Payment API is working"
    })