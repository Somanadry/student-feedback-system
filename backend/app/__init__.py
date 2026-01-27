from flask import Flask
from .config import Config
from .extensions import db, cors, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from .models import Issue, StatusLog, User
        db.create_all()

    from .routes.student_routes import student_bp
    from .routes.admin_routes import admin_bp
    from .routes.auth_routes import auth_bp

    app.register_blueprint(student_bp, url_prefix="/api")
    app.register_blueprint(admin_bp, url_prefix="/api/admin")
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    return app
