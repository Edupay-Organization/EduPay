from datetime import datetime

from src.extensions import db


class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    amount = db.Column(
        db.Float,
        nullable=False
    )

    payment_reference = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    payment_method = db.Column(
        db.String(50),
        nullable=False,
        default="manual"
    )

    payment_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    student_id = db.Column(
        db.Integer,
        db.ForeignKey("students.id"),
        nullable=False
    )
