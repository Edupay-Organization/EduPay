from flask import Flask
from config import Config

from src.extensions import db, jwt, cors


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)

    from src.routes.auth import auth_bp
    from src.routes.admin import admin_bp
    from src.routes.teacher import teacher_bp
    from src.routes.payment import payments_bp
    from src.routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(teacher_bp, url_prefix="/api/teacher")
    app.register_blueprint(payments_bp, url_prefix="/api/payments")
    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")

    with app.app_context():
        from src.models import (
            school,
            user,
            classroom,
            student,
            payment
        )

        db.create_all()

    return app