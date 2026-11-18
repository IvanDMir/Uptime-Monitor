import requests
from datetime import datetime


def print_line(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open("results.log", "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")

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
            print_line(
                f"[UP]   HTTP {r.status_code} | "
                f"{r.elapsed.total_seconds():.2f} s | {url}"
            )
        else:
            print_line(f"[DOWN] HTTP {r.status_code} | {url}")
    except requests.Timeout:
        print_line(f"[DOWN] TIMEOUT | {url}")
    except requests.ConnectionError:
        print_line(f"[DOWN] CONNECTION ERROR | {url}")
    except requests.RequestException:
        print_line(f"[DOWN] REQUEST ERROR | {url}")

print_line("=" * 80)