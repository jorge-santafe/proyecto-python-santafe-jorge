from persistencia import cargar_datos, guardar_datos
from pacientes import buscar_paciente
from datetime import date


def registrar_diagnostico(medico):
    print("\n======= DIAGNÓSTICO DE PACIENTES =======")

    id_paciente = input("Identificación del paciente: ").strip()
    paciente = buscar_paciente(id_paciente)

    if paciente is None:
        print("El paciente no se encuentra registrado.")
        return

    print(f"Paciente: {paciente['nombres']} {paciente['apellidos']}")

    sintomas = []
    while True:
        sintoma = input("Ingrese un síntoma (Presione entrer para terminar): ").strip()
        if not sintoma:
            break
        sintomas.append(sintoma)

    if not sintomas:
        print("Debe registrar al menos un síntoma.")
        return

    diagnostico = input("Ingrese el diagnostico: ").strip()
    if not diagnostico:
        print("El diagnostico es obligatorio")
        return

    medicamentos = []
    while True:
        print("\n======= PRESCRIPCIÓN MÉDICA =======")

        medicamento = input("Medicamento: ").strip()
        cantidad = input("Cantidad: ").strip()
        dosis = input("Dosis diaria: ").strip()
        tiempo = input("Tiempo de aplicación (días): ").strip()

        if not all([medicamento, cantidad, dosis, tiempo]):
            print("Todos los campos son obligatorios")
            return

        if not tiempo.isdigit() or int(tiempo) <= 0:
            print("El tiempo debe ser un número positivo.")
            return

        nueva_prescripcion = {
            "medicamento": medicamento,
            "cantidad": cantidad,
            "dosis": dosis,
            "tiempo_aplicacion": int(tiempo),
        }
        medicamentos.append(nueva_prescripcion)

        print("""
¿Desea agregar otro medicamento?
1. Si
2. No
              """)
        opcion = int(input("Opcion: "))

        match opcion:
            case 1:
                continue
            case 2:
                break
            case _:
                print("Opción no válida")
                return

    nuevo_diagnostico = {
        "fecha": date.today().isoformat(),
        "paciente": id_paciente,
        "medico": medico["identificacion"],
        "sintomas": sintomas,
        "diagnostico": diagnostico,
        "prescripcion": medicamentos,
    }

    datos = cargar_datos()
    datos["diagnosticos"].append(nuevo_diagnostico)
    guardar_datos(datos)
    print("\nDiagnóstico registrado correctamente.")
