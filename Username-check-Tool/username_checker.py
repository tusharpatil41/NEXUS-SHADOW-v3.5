import requests
import datetime

def show_logo():
    print("*" * 80)
    print("* *")
    print("* PRESENTED BY: TUSHAR PATIL                                                  *")
    print("* *")
    print("*" * 80)
    
    logo = """
     ██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
     ██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
     ██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  
     ██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
     ╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
      ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
    
                 [ SOCIAL MEDIA USERNAME AVAILABILITY CHECKER ]
    """
    print(logo)
    print(f"[!] Scan Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 80)

def check_username():
    show_logo()
    username = input("\nEnter Username to scan: ").strip()
    
    # सोशल मीडिया प्लॅटफॉर्म्स आणि त्यांच्या URL स्ट्रक्चर्सची यादी
    platforms = {
        "Instagram": f"https://www.instagram.com/{username}/",
        "Twitter": f"https://twitter.com/{username}",
        "GitHub": f"https://github.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "YouTube": f"https://www.youtube.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}/",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
    }

    print(f"\n[~] Searching for '{username}' across platforms...\n")
    print(f"{'PLATFORM':<15} | {'STATUS':<15} | {'PROFILE LINK'}")
    print("-" * 80)

    for name, url in platforms.items():
        try:
            # आपण वेबसाईटला रिक्वेस्ट पाठवून चेक करतो की ती प्रोफाईल अस्तित्वात आहे की नाही
            response = requests.get(url, timeout=5, headers={'User-Agent': 'Mozilla/5.0'})
            
            if response.status_code == 200:
                print(f"{name:<15} | [ FOUND ]       | {url}")
            elif response.status_code == 404:
                print(f"{name:<15} | [ NOT FOUND ]   | -")
            else:
                print(f"{name:<15} | [ ERROR {response.status_code} ] | -")
                
        except requests.exceptions.RequestException:
            print(f"{name:<15} | [ CONNECTION ERR ]| -")

    print("-" * 80)
    print("[!] Scan Completed.")

if __name__ == "__main__":
    check_username()