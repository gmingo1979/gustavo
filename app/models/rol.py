from app import db

class Rol(db.Model):
    __tablename__ = "roles"
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 🔹 fuerza el motor InnoDB


    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), unique=True, nullable=False)

    funciones = db.relationship(
        "Funcion",
        secondary="rol_funcion",
        backref="roles"
    )