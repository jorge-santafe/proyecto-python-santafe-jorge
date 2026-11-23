from persistencia import cargar_datos, guardar_datos


def registrar_usuario():
    print("\n======= REGISTRO DE USUARIOS =======")

    n_identificacion = input("Número de identificación: ").strip()
    nombres = input("Nombres: ").strip().lower()
    apellidos = input("Apellidos: ").strip().lower()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip().lower()
    direccion = input("Dirección: ").strip().lower()
    contrasena = input("Contraseña: ").strip()

    print(
        """
Seleccione el rol del usuario:
1. Médico
2. Administrativo
"""
    )
    if not all(
        [n_identificacion, nombres, apellidos, telefono, correo, direccion, contrasena]
    ):
        print("\n Error: todos los campos son obligatorios")
        return

    opcion = int(input("Opción: "))
    match opcion:
        case 1:
            rol = "medico"
        case 2:
            rol = "administrativo"
        case _:
            print("Usuario no valido")
            return

    datos = cargar_datos()

    for usuario in datos["usuarios"]:
        if usuario["identificacion"] == n_identificacion:
            print("No se puede registrar: el usuario ya existe")
            return

    nuevo_usuario = {
        "identificacion": n_identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "contrasena": contrasena,
        "rol": rol,
    }
    datos["usuarios"].append(nuevo_usuario)
    guardar_datos(datos)

    print("\nUsuario registrado correctamente")
