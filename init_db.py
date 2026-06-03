#!/usr/bin/env python
"""Script para inicializar o banco de dados SQLite"""

from app import create_app, db

if __name__ == '__main__':
    app = create_app()
    
    with app.app_context():
        db.create_all()
        print("✓ Database initialized successfully at app.db")
