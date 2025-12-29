from app import db

rol_funcion = db.Table(
    "rol_funcion",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("rol_id", db.Integer, db.ForeignKey("roles.id")),
    db.Column("funcion_id", db.Integer, db.ForeignKey("funciones.id")),
    mysql_engine='InnoDB'  # si querés forzar engine
)

usuario_rol = db.Table(
    "usuario_rol",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("usuario_id", db.Integer, db.ForeignKey("usuarios.id")),
    db.Column("rol_id", db.Integer, db.ForeignKey("roles.id")),
    mysql_engine='InnoDB'  # si querés forzar engine
)
