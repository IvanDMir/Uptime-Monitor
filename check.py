import requests

urls = [
    "https://www.argentina.gob.ar",
    "https://www.arca.gob.ar",
    "https://www.tucuman.gob.ar",
    "https://sitio-que-no-existe-123.gob.ar"
]
for url in urls:
    try:
        r = requests.get(url, timeout=5)
        print(f"URL: {url}")
        print(f"Código HTTP: {r.status_code}")
        print(f"Tiempo de respuesta: {r.elapsed.total_seconds()} segundos")
    except requests.Timeout:
        print(f"CAÍDO (timeout): {url}")
    except requests.ConnectionError:
        print(f"CAÍDO (sin conexión): {url}")
    except requests.RequestException:
        print(f"CAÍDO (error en la solicitud): {url}")
    print("-" * 40)