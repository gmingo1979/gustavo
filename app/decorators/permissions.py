from functools import wraps
from flask import session, redirect, url_for, flash
from app.models.usuario import Usuario


def require_permission(endpoint_requerido):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            user_id = session.get('user_id')
            if not user_id:
                flash("Debe iniciar sesión", "warning")
                return redirect(url_for('auth.login'))

            usuario = Usuario.query.get(user_id)
            if not usuario or not usuario.activo:
                flash("Usuario no válido", "danger")
                session.clear()
                return redirect(url_for('auth.login'))

            # SUPERADMIN
            for rol in usuario.roles:
                for funcion in rol.funciones:
                    if funcion.ruta == '__ALL__':
                        return func(*args, **kwargs)

            # Permiso específico
            for rol in usuario.roles:
                for funcion in rol.funciones:
                    if funcion.ruta == endpoint_requerido:
                        return func(*args, **kwargs)

            flash("No tiene permisos para esta acción", "danger")
            return redirect(url_for('main.index'))

        return wrapper
    return decorator
