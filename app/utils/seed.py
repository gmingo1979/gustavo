from app.db import db
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.funcion import Funcion
from app.models.usuario_rol import UsuarioRol
from app.models.rol_funcion import RolFuncion

def seed_data():
    # -------- ROLES --------
    admin_rol = Rol(nombre='admin')
    db.session.add(admin_rol)

    # -------- FUNCIONES --------
    funciones = [
        Funcion(nombre='Acceso total', ruta='*'),
    ]
    db.session.add_all(funciones)
    db.session.flush()

    # -------- ROL - FUNCION --------
    for f in funciones:
        db.session.add(RolFuncion(
            rol_id=admin_rol.id,
            funcion_id=f.id
        ))

    # -------- USUARIO ADMIN --------
    admin = Usuario(username='admin')
    admin.set_password('admin')
    db.session.add(admin)
    db.session.flush()

    # -------- USUARIO - ROL --------
    db.session.add(UsuarioRol(
        usuario_id=admin.id,
        rol_id=admin_rol.id
    ))

    db.session.commit()
