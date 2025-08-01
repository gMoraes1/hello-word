import time
import psutil
import requests
from datetime import datetime

class Monitor:
    def __init__(self, url, log_file="monitor.log", cpu_alert=80.0, ram_alert=500):
        self.url = url
        self.log_file = log_file
        self.cpu_alert = cpu_alert
        self.ram_alert = ram_alert * 1024 * 1024  # MB -> bytes

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{timestamp}] {message}"
        print(line)
        with open(self.log_file, "a") as f:
            f.write(line + "\n")

    def check_health(self):
        try:
            r = requests.get(self.url, timeout=3)
            if r.status_code == 200:
                self.log(f"[OK] Endpoint {self.url} está respondendo.")
                return True
            else:
                self.log(f"[ALERTA] Endpoint {self.url} retornou status {r.status_code}")
                return False
        except requests.exceptions.RequestException as e:
            self.log(f"[ALERTA] Falha ao acessar {self.url}: {e}")
            return False

    def check_resources(self):
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().used

        if cpu > self.cpu_alert:
            self.log(f"[ALERTA] CPU alta: {cpu:.2f}%")
        else:
            self.log(f"[OK] CPU: {cpu:.2f}%")

        if ram > self.ram_alert:
            self.log(f"[ALERTA] RAM alta: {ram / 1024 / 1024:.2f} MB")
        else:
            self.log(f"[OK] RAM: {ram / 1024 / 1024:.2f} MB")

    def run(self, interval=5):
        self.log("🚀 Iniciando monitoramento...")
        while True:
            self.check_health()
            self.check_resources()
            time.sleep(interval)

if __name__ == "__main__":
    monitor = Monitor(url="http://localhost:8000")
    monitor.run(interval=5)
