def register_blueprints(app):
    from .health import health_bp
    app.register_blueprint(health_bp)
