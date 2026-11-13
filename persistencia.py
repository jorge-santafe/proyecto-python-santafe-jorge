import json

ruta = "/Users/jorge-santafe/Desktop/proyecto-python-santafe-jorge/"
archivo = "datos.json"


def cargar_datos():
    with open(ruta + archivo, "r", encoding="utf-8") as arch:
        return json.load(arch)


def guardar_datos(informacion):
    with open(ruta + archivo, "w", encoding="utf-8") as arch:
        json.dump(informacion, arch, indent=4, ensure_ascii=False)
