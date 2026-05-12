import platform
import os

print("=== NOCTYRA CORE ===")

sistema = platform.system()

print(f"Sistema detectado: {sistema}")

while True:
    comando = input(">>> ")

    if comando == "firefox":

        if sistema == "Linux":
            os.system("firefox")

        elif sistema == "Windows":
            os.system("start firefox")

    elif comando == "sair":
        break

    else:
        print("Comando desconhecido.")