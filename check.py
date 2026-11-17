import requests

urls = [
    "https://www.argentina.gob.ar",
    "https://www.arca.gob.ar",
    "https://www.tucuman.gob.ar",
    "https://sitio-que-no-existe-123.gob.ar",
    "https://httpbin.org/status/500"
]



for url in urls:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code < 400:
            print(
                f"[UP]   HTTP {r.status_code} | "
                f"{r.elapsed.total_seconds():.2f} s | {url}"
            )
        else:
            print(f"[DOWN] HTTP {r.status_code} | {url}")
    except requests.Timeout:
        print(f"[DOWN] TIMEOUT | {url}")
    except requests.ConnectionError:
        print(f"[DOWN] CONNECTION ERROR | {url}")
    except requests.RequestException:
        print(f"[DOWN] REQUEST ERROR | {url}")

print("=" * 80)