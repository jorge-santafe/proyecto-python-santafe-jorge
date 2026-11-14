from persistencia import cargar_datos


def iniciar_sesion():
    print("\n======= INICIO DE SESIÓN =======")
    correo = input("Correo electrónico: ").strip().lower()
    contrasena = input("Contraseña: ").strip()

    if not all([correo, contrasena]):
        print("Todos los campos son obligatorios.")
        return

    datos = cargar_datos()

    for usuario in datos["usuarios"]:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            print(f"\nBienvenido, {usuario['nombres']} {usuario['apellidos']}")
            return usuario

    print("Correo electrónico o contraseña incorrectos.")
    return None
