import os
import time
import socket
import requests
from datetime import datetime

# --- UI CONSTANTS ---
class UI:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

def show_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = f"""
{UI.CYAN}    ######################################################################
    #                                                                    #
    #   ███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗              #
    #   ██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║              #
    #   ███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║              #
    #   ╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║              #
    #   ███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝              #
    #   ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝               #
    #                                                                    #
    #         >> OFFENSIVE SECURITY & VULNERABILITY FRAMEWORK <<         #
    #              DEVELOPED BY: TUSHAR PATIL (HI-TECH IT)               #
    ######################################################################{UI.RESET}
    """
    print(banner)

def status_msg(msg, type="info"):
    if type == "info":
        print(f"{UI.YELLOW}[*] {msg}...{UI.RESET}")
    elif type == "success":
        print(f"{UI.GREEN}[+] {msg}{UI.RESET}")
    elif type == "danger":
        print(f"{UI.RED}[!!!] {msg}{UI.RESET}")

def professional_scanner():
    show_banner()
    
    # 1. User Input
    print(f"{UI.BOLD}STEP 1: TARGET SPECIFICATION{UI.RESET}")
    target = input(f"Enter Domain Name (e.g., target.com): ").strip()
    
    if not target:
        status_msg("Invalid target! Exiting", "danger")
        return

    # 2. Phase 1: Reconnaissance (KHALNAYAK ENGINE)
    print(f"\n{UI.BOLD}STEP 2: INFRASTRUCTURE RECONNAISSANCE{UI.RESET}")
    status_msg("Resolving Target IP Address")
    time.sleep(1)
    
    try:
        ip_addr = socket.gethostbyname(target)
        status_msg(f"Target Identified: {target} [{ip_addr}]", "success")
    except:
        status_msg("Target resolution failed. Please check internet connection", "danger")
        return

    # 3. Phase 2: Attack Simulation (SHADOW ENGINE)
    print(f"\n{UI.BOLD}STEP 3: SECURITY VULNERABILITY SCANNING{UI.RESET}")
    time.sleep(1)

    # List of sensitive files to simulate an attack
    vulnerabilities = {
        '/.env': 'CRITICAL: Database configuration exposed',
        '/.git/': 'HIGH: Git repository directory accessible',
        '/admin/': 'MEDIUM: Administrator control panel found',
        '/backup/': 'HIGH: System backup files detected'
    }

    found_list = []

    for path, risk in vulnerabilities.items():
        print(f"  > Scanning path: {path}", end="\r")
        time.sleep(0.5)
        
        try:
            # Checking the path using HTTP GET request
            url = f"https://{target}{path}"
            response = requests.get(url, timeout=3, verify=False)
            
            if response.status_code == 200:
                status_msg(f"EXPOSED: {path} | {risk}", "danger")
                found_list.append(path)
            else:
                print(f"{UI.GREEN}  [SAFE] {path} is not public.{UI.RESET}")
        except:
            print(f"{UI.YELLOW}  [SKIP] Connection timed out for {path}{UI.RESET}")

    # 4. Final Audit Report
    print(f"\n{UI.CYAN}{'='*70}{UI.RESET}")
    print(f"{UI.BOLD}FINAL SECURITY AUDIT REPORT{UI.RESET}")
    print(f"Target Domain  : {target}")
    print(f"Scan Completed : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total Risks    : {UI.RED}{len(found_list)}{UI.RESET}")
    print(f"Lead Auditor   : {UI.BOLD}TUSHAR PATIL{UI.RESET}")
    print(f"{UI.CYAN}{'='*70}{UI.RESET}")

if __name__ == "__main__":
    try:
        professional_scanner()
    except KeyboardInterrupt:
        print(f"\n{UI.RED}[!] Scan aborted by user.{UI.RESET}")