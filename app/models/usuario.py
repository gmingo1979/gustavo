from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model, UserMixin):
    __tablename__ = 'usuarios'
    __table_args__ = {'mysql_engine': 'InnoDB'}  # 🔹 fuerza el motor InnoDB
    
    id = db.Column(db.Integer, primary_key=True)
    apellido=db.Column(db.String(50), nullable=False)
    nombre=db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)
    password_hash = db.Column(db.String(200), nullable=False)
    estado = db.Column(db.Enum("Activo", "Bloqueado", "Retirado"), default="Activo")
    auth_origen = db.Column(db.Enum("Local", "Entra"), default="Local", nullable=False)
    fecha_alta = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    es_viajante = db.Column(db.Boolean, default=False)

    roles = db.relationship(
        "Rol",
        secondary="usuario_rol",
        backref="usuarios"
    )

    def puede_ingresar(self):
        return self.estado.lower() == 'activo'

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    @property
    def profile_pic(self):
        return f"uploads/profile_pics/user_{self.id}.jpg"
    
    @property
    def nombre_completo(self):
        return f"{self.apellido}, {self.nombre}"