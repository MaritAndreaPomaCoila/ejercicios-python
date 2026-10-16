import socket
from urllib.parse import urlsplit, parse_qs

# 1. Obtención de IP local
print("localhost ->", socket.gethostbyname("localhost"))

print("-" * 40)

# 2. Anatomía de una URL
url = "https://agencia-titicaca.test:443/paquetes/islas?destino=uros&personas=4#precios"
partes = urlsplit(url)

print("Esquema (protocolo):", partes.scheme)
print("Dominio (host):     ", partes.hostname)
print("Puerto:             ", partes.port)
print("Ruta:               ", partes.path)
print("Parámetros:         ", parse_qs(partes.query))
print("Fragmento:          ", partes.fragment)