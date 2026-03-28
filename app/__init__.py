from flask import Flask
from app.core.config import Config
from app.core.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # type: ignore

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.assessment import assessment_bp
    from app.routes.admin import admin_bp
    from app.routes.pages import pages_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(assessment_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(pages_bp)
    
    # Ensure database tables are created (especially for PostgreSQL on Render)
    # Important: Move this AFTER blueprints are registered so models are imported
    with app.app_context():
        # Import models here to ensure they are known to SQLAlchemy
        from app.models.user import User
        from app.models.assessment import Assessment
        from app.models.result import Result
        db.create_all()

    return app

# Define 'app' instance at the module level to support 'gunicorn app:app'
app = create_app()