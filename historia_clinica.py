from persistencia import cargar_datos
from pacientes import buscar_paciente


def mostrar_datos_paciente(paciente):
    print("\n======= DATOS DEL PACIENTE =======")
    print(f"Identificación: {paciente['identificacion']}")
    print(f"Nombres: {paciente['nombres']}")
    print(f"Apellidos: {paciente['apellidos']}")
    print(f"Teléfono: {paciente['telefono']}")
    print(f"Correo: {paciente['correo']}")
    print(f"Dirección: {paciente['direccion']}")
    print(f"Género: {paciente['genero']}")
    print(f"Estado civil: {paciente['estado_civil']}")


def obtener_consultas(identificacion, datos):
    consultas = []

    for diagnostico in datos["diagnosticos"]:
        if diagnostico["paciente"] == identificacion:
            consultas.append(diagnostico)

    return consultas


def mostrar_consultas(consultas, datos):
    print("\n======= HISTORIAL MÉDICO =======")

    for consulta in consultas:
        print(f"\nFecha: {consulta['fecha']}")

        for usuario in datos["usuarios"]:
            if usuario["identificacion"] == consulta["medico"]:
                print(f"Médico: {usuario['nombres']} {usuario['apellidos']}")
                break
        else:
            print(f"Médico (identificación): {consulta['medico']}")

        print("\nSíntomas:")
        for sintoma in consulta["sintomas"]:
            print(f"- {sintoma}")

        print(f"\nDiagnóstico: {consulta['diagnostico']}")

        print("\nPrescripción médica:")
        for medicamento in consulta["prescripcion"]:
            print(f"Medicamento: {medicamento['medicamento']}")
            print(f"Cantidad: {medicamento['cantidad']}")
            print(f"Dosis diaria: {medicamento['dosis']}")
            print(f"Tiempo de aplicación: {medicamento['tiempo_aplicacion']} días")
            print("-----------------------------")


def consultar_historia_clinica():
    print("\n======= HISTORIA CLÍNICA =======")

    identificacion = input("Identificación del paciente: ").strip()

    paciente = buscar_paciente(identificacion)

    if paciente is None:
        print("El paciente no se encuentra registrado.")
        return

    datos = cargar_datos()

    mostrar_datos_paciente(paciente)

    consultas = obtener_consultas(identificacion, datos)

    if not consultas:
        print("\nEl paciente no tiene consultas registradas.")
        return

    mostrar_consultas(consultas, datos)
