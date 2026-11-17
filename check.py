import requests

url = "https://www.argentina.gob.ar"
r = requests.get(url, timeout=5)

print(f"Código HTTP: {r.status_code}")
print(f"Tiempo de respuesta: {r.elapsed.total_seconds()} segundos")