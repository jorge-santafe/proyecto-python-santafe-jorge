from persistencia import cargar_datos, guardar_datos


def buscar_paciente(identificacion):
    datos = cargar_datos()
    for paciente in datos["pacientes"]:
        if paciente["identificacion"] == identificacion:
            return paciente
    return None


def registrar_pacientes():
    print("\n======= REGISTRO DE PACIENTE =======")
    n_identificacion = input("Número de identificación: ").strip()
    if buscar_paciente(n_identificacion) is not None:
        print("El paciente ya se encuentra registrado")
        return
    nombres = input("Nombres: ").strip().upper()
    apellidos = input("Apellidos: ").strip().upper()
    telefono = input("Número de teléfono: ").strip()
    correo = input("Correo electrónico: ").strip().lower()
    direccion = input("Dirección: ").strip().lower()

    print(
        """
Seleccione el género:
1. Masculino
2. Femenino
3. Otro
          """
    )

    opcion_genero = int(input("Opción: "))
    match opcion_genero:
        case 1:
            genero = "masculino"
        case 2:
            genero = "femenino"
        case 3:
            genero = "otro"
        case _:
            print("Género no válido")
            return
    print(
        """
Seleccione el estado civil:
1. Soltero
2. Casado
3. Divorsiado
4. Viudo
          """
    )

    opcion_civil = int(input("Opción: "))
    match opcion_civil:
        case 1:
            estado_civil = "soltero"
        case 2:
            estado_civil = "casado"
        case 3:
            estado_civil = "divorciado"
        case 4:
            estado_civil = "viudo"
        case _:
            print("Estado civil no válido")
            return
    if not all([n_identificacion, nombres, apellidos, telefono, correo, direccion]):
        print("Error: todos los campos son obligatorios")
        return

    nuevo_paciente = {
        "identificacion": n_identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono": telefono,
        "correo": correo,
        "direccion": direccion,
        "genero": genero,
        "estado_civil": estado_civil,
    }

    datos = cargar_datos()
    datos["pacientes"].append(nuevo_paciente)
    guardar_datos(datos)
    print("\n Paciente registrado correctamente")
