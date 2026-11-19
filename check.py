import requests
from datetime import datetime


def save_logs(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open("results.log", "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")

with open("sites.txt", "r", encoding="utf-8") as file:
    urls = [line.strip() for line in file if line.strip()]



for url in urls:
    try:
        r = requests.get(url, timeout=5)
        if r.status_code < 400:
            save_logs(
                f"[UP]   HTTP {r.status_code} | "
                f"{r.elapsed.total_seconds():.2f} s | {url}"
            )
        else:
            save_logs(f"[DOWN] HTTP {r.status_code} | {url}")
    except requests.Timeout:
        save_logs(f"[DOWN] TIMEOUT | {url}")
    except requests.ConnectionError:
        save_logs(f"[DOWN] CONNECTION ERROR | {url}")
    except requests.RequestException:
        save_logs(f"[DOWN] REQUEST ERROR | {url}")
