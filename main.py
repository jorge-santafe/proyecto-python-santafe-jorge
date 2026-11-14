from autenticacion import iniciar_sesion
from usuarios import registrar_usuario
from pacientes import registrar_pacientes
from diagnosticos import registrar_diagnostico
from historia_clinica import consultar_historia_clinica


def mostrar_menu(usuario):
    while True:
        print("""
======= CLÍNICA ACME =======
1. Registrar usuario
2. Registrar paciente
3. Diagnosticar paciente
4. Consultar historia clínica
5. Cerrar sesión
        """)

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                if usuario["rol"] == "administrativo":
                    registrar_usuario()
                else:
                    print("No tiene permisos para registrar usuarios.")

            case "2":
                registrar_pacientes()

            case "3":
                if usuario["rol"] == "medico":
                    registrar_diagnostico(usuario)
                else:
                    print("Solo los médicos pueden registrar diagnósticos.")

            case "4":
                consultar_historia_clinica()

            case "5":
                print("Sesión cerrada correctamente.")
                break

            case _:
                print("Opción no válida.")


def main():
    while True:
        print("""
======= BIENVENIDO A CLÍNICA ACME =======
1. Iniciar sesión
2. Salir
        """)

        opcion = input("Seleccione una opción: ").strip()

        match opcion:
            case "1":
                usuario = iniciar_sesion()

                if usuario is not None:
                    mostrar_menu(usuario)

            case "2":
                print("Gracias por utilizar el sistema.")
                break

            case _:
                print("Opción no válida.")


main()
