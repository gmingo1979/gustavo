from flask import session, request, redirect, url_for, flash
from app.models.usuario import Usuario


RUTAS_PUBLICAS = [
    'auth.login',
    'auth.logout',
    'static'
]


def verificar_permisos():
    endpoint = request.endpoint

    # =========================
    # Rutas públicas
    # =========================
    if endpoint is None:
        return

    if endpoint.startswith('static'):
        return

    if endpoint in RUTAS_PUBLICAS:
        return

    # =========================
    # Usuario logueado
    # =========================
    user_id = session.get('user_id')
    if not user_id:
        flash("Debe iniciar sesión", "warning")
        return redirect(url_for('auth.login'))

    usuario = Usuario.query.get(user_id)
    if not usuario or not usuario.activo:
        flash("Usuario no válido", "danger")
        session.clear()
        return redirect(url_for('auth.login'))

    # =========================
    # Cambio de password obligatorio
    # =========================
    if usuario.must_change_password and endpoint != 'auth.change_password':
        return redirect(url_for('auth.change_password'))

    # =========================
    # SUPERADMIN => acceso total
    # =========================
    for rol in usuario.roles:
        for funcion in rol.funciones:
            if funcion.ruta == '__ALL__':
                return

    # =========================
    # Permiso por ruta
    # =========================
    if not tiene_permiso(usuario, endpoint):
        flash("No tiene permisos para acceder", "danger")
        return redirect(url_for('main.index'))


def tiene_permiso(usuario, endpoint):
    for rol in usuario.roles:
        for funcion in rol.funciones:
            if funcion.ruta == endpoint:
                return True
    return False


