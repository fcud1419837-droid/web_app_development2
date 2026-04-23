from .main import main_bp
from .subjects import subjects_bp
from .books import books_bp

def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(subjects_bp)
    app.register_blueprint(books_bp)
