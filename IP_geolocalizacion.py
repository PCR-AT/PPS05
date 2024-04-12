
import os, requests

# Asignacion de variables.
listado_final = []
url = "https://reallyfreegeoip.org/json/"

with open(r"C:\Users\Pablo\Downloads\IPs_unicas.txt", "r") as listado:
    lineas = listado.readlines()
    for linea in lineas:
        ip = linea.strip()
        respuesta = requests.get(url + ip)
        respuesta.raise_for_status()
        listado_final.append(respuesta.json())

# Escritura del archivo resultante.
with open(r"C:\Users\Pablo\Downloads\IPs_y_geolocalizacion.txt", "w", encoding="utf-8") as archivo_final:
    for datos_ip in listado_final:
        archivo_final.write(str(datos_ip) + '\n')
