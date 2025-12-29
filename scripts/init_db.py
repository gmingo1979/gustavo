import os
import sys

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from app import create_app
from app.db import db
from app.utils.seed import seed_data


def main():
    app = create_app()

    with app.app_context():
        print("📦 Creando tablas...")
        db.create_all()

        print("🌱 Insertando datos iniciales...")
        seed_data()

        print("✅ Base inicializada correctamente")


if __name__ == "__main__":
    main()
