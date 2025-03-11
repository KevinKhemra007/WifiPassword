import subprocess
import os
import time
import colorama
from colorama import Fore

# Initialize colorama
colorama.init(autoreset=True)

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.RED + r"""
     ⠀⠀⠀⠀⠀⢀⣤⣾⡿⠃⠀⠀⠠⠾⠦⠤⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⢀⡴⢻⣿⡟⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⣼⠁⠀⠹⡇⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⡏⠀⠀⣴⣷⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⡇⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⢠⡇⠀⠀⠈⠉⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⢸⠁⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠈⣇⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
     ⠀⠀⠘⢆⠀⠀⠀⠀⠀⠈⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    """)
    print(Fore.YELLOW + "="*50)
    os.system("figlet -f slant 'WIFI PASSWORD TOOL'")
    print(Fore.YELLOW + "="*50)
    print(Fore.CYAN + "[1] Show All Saved WiFi Passwords")
    print(Fore.CYAN + "[2] Export WiFi Passwords to File")
    print(Fore.CYAN + "[3] Exit")
    print(Fore.YELLOW + "="*50)
    print(Fore.GREEN + "GitHub: https://github.com/KevinKhemra007")
    print(Fore.GREEN + "Telegram: https://t.me/hackisreal007")
    print(Fore.YELLOW + "="*50)

def run_command(command):
    """Run a command in the Windows shell and return the output."""
    result = subprocess.run(command, capture_output=True, text=True, shell=True, encoding="utf-8", errors="ignore")
    return result.stdout.strip()

def get_wifi_passwords():
    """Retrieve saved Wi-Fi passwords"""
    profiles_output = run_command("netsh wlan show profiles")

    wifi_names = []
    for line in profiles_output.split("\n"):
        if "All User Profile" in line:
            wifi_name = line.split(":")[-1].strip()
            wifi_names.append(wifi_name)

    if not wifi_names:
        print(Fore.RED + "[❌] No saved Wi-Fi networks found.")
        return []

    wifi_passwords = []
    for wifi_name in wifi_names:
        wifi_password_info = run_command(f'netsh wlan show profiles name="{wifi_name}" key=clear')
        password = "Not Found"
        for line in wifi_password_info.split("\n"):
            if "Key Content" in line:
                password = line.split(":")[-1].strip()
                break
        
        wifi_passwords.append((wifi_name, password))

    return wifi_passwords

def show_wifi_passwords():
    """Display saved Wi-Fi passwords"""
    wifi_passwords = get_wifi_passwords()

    if wifi_passwords:
        print(Fore.YELLOW + "="*50)
        for wifi_name, password in wifi_passwords:
            print(Fore.GREEN + f"Wi-Fi: {wifi_name} | Password: {password}")
        print(Fore.YELLOW + "="*50)
    
    input(Fore.YELLOW + "[⏎] Press Enter to return to menu...")

def export_wifi_passwords():
    """Save Wi-Fi passwords to a file"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "wifi_passwords.txt")

    wifi_passwords = get_wifi_passwords()

    with open(file_path, "w", encoding="utf-8") as file:
        file.write("Saved Wi-Fi Networks and Passwords:\n\n")
        for wifi_name, password in wifi_passwords:
            file.write(f"Wi-Fi: {wifi_name} | Password: {password}\n")

    print(Fore.GREEN + f"[✅] Wi-Fi passwords saved to: {file_path}")
    input(Fore.YELLOW + "[⏎] Press Enter to return to menu...")

while True:
    banner()
    choice = input(Fore.YELLOW + "[📌] Enter your choice: ")

    if choice == "1":
        show_wifi_passwords()
    elif choice == "2":
        export_wifi_passwords()
    elif choice == "3":
        print(Fore.YELLOW + "[🛑] Exiting...")
        time.sleep(1)
        break
    else:
        print(Fore.RED + "[❌] Invalid option! Try again.")
    
    time.sleep(2)
