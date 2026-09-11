from src.extensions import db


class School(db.Model):
    __tablename__ = "schools"

    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.String(20), unique=True, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone = db.Column(db.String(30))
    address = db.Column(db.String(255))

    users = db.relationship(
        "User",
        backref="school",
        lazy=True,
        cascade="all, delete-orphan"
    )

    classes = db.relationship(
        "ClassRoom",
        backref="school",
        lazy=True,
        cascade="all, delete-orphan"
    )

    students = db.relationship(
        "Student",
        backref="school",
        lazy=True,
        cascade="all, delete-orphan"
    )