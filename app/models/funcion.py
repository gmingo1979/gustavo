from app import db

class Funcion(db.Model):
    __tablename__ = "funciones"
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 🔹 fuerza el motor InnoDB

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    endpoint=db.Column(db.String(100), unique=True, nullable=False)
    descripcion = db.Column(db.Text)
    icono = db.Column(db.String(100))
    categoria = db.Column(db.String(100))
    es_menu = db.Column(db.Boolean, default=False)
    ubicacion_menu = db.Column(db.String(20), default='sidebar')