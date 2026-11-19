import requests
from datetime import datetime


def save_logs(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open("results.log", "a", encoding="utf-8") as log_file:
        log_file.write(line + "\n")

def read_sites(path):
    with open(path, "r", encoding="utf-8") as file:
        urls = [line.strip() for line in file if line.strip()]
    return urls



def check_site(url):
    try:
        r = requests.get(url, timeout=5)
        if r.status_code < 400:
            return (
                f"[UP]   HTTP {r.status_code} | "
                f"{r.elapsed.total_seconds():.2f} s | {url}"
            )
        return f"[DOWN] HTTP {r.status_code} | {url}"
    except requests.Timeout:
        return f"[DOWN] TIMEOUT | {url}"
    except requests.ConnectionError:
        return f"[DOWN] CONNECTION ERROR | {url}"
    except requests.RequestException:
        return f"[DOWN] REQUEST ERROR | {url}"
    

def main():
    urls = read_sites("sites.txt")
    for url in urls:
        save_logs(check_site(url))

if __name__ == "__main__":
    main()