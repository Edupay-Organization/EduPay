from src.extensions import db


class ClassRoom(db.Model):
    __tablename__ = "classes"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(100),
        nullable=False
    )

    school_id = db.Column(
        db.Integer,
        db.ForeignKey("schools.id"),
        nullable=False
    )

    students = db.relationship(
        "Student",
        backref="classroom",
        lazy=True
    )

    teachers = db.relationship(
        "User",
        backref="assigned_class",
        lazy=True,
        foreign_keys="User.class_id"
    )