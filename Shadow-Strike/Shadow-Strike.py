import requests
import socket
import threading
import time
import datetime
import urllib3
import re

# SSL Warnings बंद करण्यासाठी
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def show_master_logo():
    print("=" * 90)
    print(f"{'OFFENSIVE CYBER SECURITY FRAMEWORK':^90}")
    print("=" * 90)
    logo = """
    ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗    ███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
    ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║    ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
    ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║    ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗  
    ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║    ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝  
    ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝    ███████║   ██║   ██║  ██║██║██║  ██╗███████╗
    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝     ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝
                                                                           
                                  [ VERSION: 2.0 - STRIKE MODE ]
                                  [ DEVELOPED BY: TUSHAR PATIL ]
    """
    print(logo)
    print(f"[*] SESSION STARTED: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"[*] TARGETING SYSTEM: ASSET DISCOVERY + VULNERABILITY CHAINING")
    print("=" * 90)

class ShadowStrike:
    def __init__(self, domain):
        self.domain = domain
        self.found_assets = []
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Shadow-Strike/2.0'}
        self.keywords = ['api', 'dev', 'staging', 's3', 'bucket', 'admin', 'jenkins', 'git', 'v1', 'v2', 'test', 'portal']

    def extract_sensitive_info(self, text):
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        return emails[0] if emails else "None"

    def analyze_vulnerability(self, url):
        print(f"\n[~] Launching Strike on: {url}")
        try:
            response = requests.get(url, headers=self.headers, timeout=5, verify=False)
            
            # 1. Directory Hunting
            dangerous_paths = ['/.git/', '/.env', '/admin/', '/backup/', '/config.php']
            for path in dangerous_paths:
                test_url = url + path
                res = requests.get(test_url, headers=self.headers, timeout=3, verify=False)
                if res.status_code == 200:
                    print(f"    [!!!] CRITICAL EXPOSURE: {test_url}")

            # 2. Header & Tech Analysis
            server = response.headers.get('Server', 'Hidden')
            email_found = self.extract_sensitive_info(response.text)
            
            print(f"    [+] Infrastructure: {server}")
            print(f"    [+] Public Intel  : {email_found}")
            
            # 3. Security Risk Assessment
            if 'X-Frame-Options' not in response.headers:
                print(f"    [!] VULNERABILITY: Clickjacking Risk Detected!")
            if 'Content-Security-Policy' not in response.headers:
                print(f"    [!] VULNERABILITY: XSS Injection Possible!")

        except:
            print(f"    [-] Strike Failed: Connection Refused.")

    def scan_asset(self, sub):
        target = f"{sub}.{self.domain}"
        url = f"https://{target}"
        try:
            response = requests.get(url, headers=self.headers, timeout=4, verify=False)
            if response.status_code != 404:
                ip = socket.gethostbyname(target)
                print(f"[+] ASSET UNEARTHED: {url} | IP: {ip}")
                self.found_assets.append(url)
        except:
            pass

    def launch_framework(self):
        show_master_logo()
        print(f"[*] Initiating Reconnaissance on {self.domain}...")
        
        # Engine 1: Khalnayak (Discovery)
        threads = []
        for sub in self.keywords:
            t = threading.Thread(target=self.scan_asset, args=(sub,))
            threads.append(t)
            t.start()
        for t in threads: t.join()

        if not self.found_assets:
            print("\n[-] No assets found. Strike cancelled.")
            return

        print(f"\n[*] Recon Complete. {len(self.found_assets)} assets detected.")
        print(f"[*] Handing over to Shadow-Strike Engine for Offensive Analysis...")
        time.sleep(2)

        # Engine 2: Shadow-Strike (Analysis)
        for asset in self.found_assets:
            self.analyze_vulnerability(asset)

        print("\n" + "=" * 90)
        print(f"{'MISSION SUCCESSFUL - TUSHAR PATIL SIGNING OFF':^90}")
        print("=" * 90)

if __name__ == "__main__":
    target = input("\nEnter Target Domain (e.g., example.com): ").strip()
    strike = ShadowStrike(target)
    strike.launch_framework()