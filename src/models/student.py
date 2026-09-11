from src.extensions import db


class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    student_id = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    name = db.Column(
        db.String(150),
        nullable=False
    )

    parent_name = db.Column(
        db.String(150)
    )

    parent_phone = db.Column(
        db.String(30)
    )

    total_fee = db.Column(
        db.Float,
        nullable=False,
        default=0
    )

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False
    )

    class_id = db.Column(
        db.Integer,
        db.ForeignKey("classes.id"),
        nullable=False
    )

    payments = db.relationship(
        "Payment",
        backref="student",
        lazy=True,
        cascade="all, delete-orphan"
    )

    @property
    def amount_paid(self):
        return sum(payment.amount for payment in self.payments)

    @property
    def balance(self):
        return max(self.total_fee - self.amount_paid, 0)

    @property
    def payment_status(self):
        if self.amount_paid <= 0:
            return "Unpaid"

        if self.amount_paid < self.total_fee:
            return "Partially Paid"

        return "Paid"