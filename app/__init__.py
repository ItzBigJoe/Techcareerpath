from flask import Flask
from app.core.config import Config
from app.core.extensions import db, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Init extensions
    db.init_app(app)
    
    # Ensure database tables are created (especially for PostgreSQL on Render)
    with app.app_context():
        db.create_all()
        
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

    return app