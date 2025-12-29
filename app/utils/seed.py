from app import db
from app.models.usuario import Usuario
from app.models.rol import Rol
from app.models.funcion import Funcion
from app.models.relaciones import usuario_rol, rol_funcion
from werkzeug.security import generate_password_hash


def seed_data():
    print("▶ Iniciando seed de datos...")

    # =========================
    # 1️⃣ ROL ADMIN
    # =========================
    admin_rol = Rol.query.filter_by(nombre="ADMIN").first()
    if not admin_rol:
        admin_rol = Rol(nombre="ADMIN", descripcion="Administrador del sistema")
        db.session.add(admin_rol)
        db.session.commit()
        print("✔ Rol ADMIN creado")
    else:
        print("ℹ Rol ADMIN ya existe")

    # =========================
    # 2️⃣ FUNCION SUPERADMIN
    # =========================
    super_funcion = Funcion.query.filter_by(nombre="SUPERADMIN").first()
    if not super_funcion:
        super_funcion = Funcion(
            nombre="SUPERADMIN",
            descripcion="Acceso total al sistema",
            ruta="__ALL__"
        )
        db.session.add(super_funcion)
        db.session.commit()
        print("✔ Función SUPERADMIN creada")
    else:
        print("ℹ Función SUPERADMIN ya existe")

    # =========================
    # 3️⃣ ASOCIAR FUNCION AL ROL
    # =========================
    existe_relacion = db.session.execute(
        rol_funcion.select().where(
            (rol_funcion.c.rol_id == admin_rol.id) &
            (rol_funcion.c.funcion_id == super_funcion.id)
        )
    ).first()

    if not existe_relacion:
        db.session.execute(
            rol_funcion.insert().values(
                rol_id=admin_rol.id,
                funcion_id=super_funcion.id
            )
        )
        db.session.commit()
        print("✔ Función SUPERADMIN asignada al rol ADMIN")
    else:
        print("ℹ Relación rol-función ya existe")

    # =========================
    # 4️⃣ USUARIO ADMIN
    # =========================
    admin_user = Usuario.query.filter_by(username="admin").first()
    if not admin_user:
        admin_user = Usuario(
            username="admin",
            password=generate_password_hash("admin"),
            must_change_password=True
        )
        db.session.add(admin_user)
        db.session.commit()
        print("✔ Usuario admin creado")
    else:
        print("ℹ Usuario admin ya existe")

    # =========================
    # 5️⃣ ASOCIAR ROL AL USUARIO
    # =========================
    existe_usuario_rol = db.session.execute(
        usuario_rol.select().where(
            (usuario_rol.c.usuario_id == admin_user.id) &
            (usuario_rol.c.rol_id == admin_rol.id)
        )
    ).first()

    if not existe_usuario_rol:
        db.session.execute(
            usuario_rol.insert().values(
                usuario_id=admin_user.id,
                rol_id=admin_rol.id
            )
        )
        db.session.commit()
        print("✔ Rol ADMIN asignado al usuario admin")
    else:
        print("ℹ Relación usuario-rol ya existe")

    print("✅ Seed finalizado correctamente")
