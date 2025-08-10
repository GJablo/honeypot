import socket
import requests
import time
from datetime import datetime
import json
import sys

# Log file configuration
LOG_FILE = "honeypot_log.txt"

def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json", timeout=5)
        if response.status_code == 200:
            return response.json().get("ip", "127.0.0.1")
    except:
        pass
    return "127.0.0.1"

def get_geolocation(ip):
    if ip == "127.0.0.1":
        return "Localhost"
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=5)
        if response.status_code == 200:
            data = response.json()
            city = data.get("city", "Unknown")
            country = data.get("country", "Unknown")
            return f"{city}, {country}"
    except:
        pass
    return "Unknown"

def log_attempt(ip, username, password, user_agent):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    location = get_geolocation(ip)
    log_entry = f"[{timestamp}] IP: {ip} | Location: {location} | User-Agent: {user_agent} | Username: {username} | Password: {password}\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def fake_login_prompt():
    print("Welcome to Secure System. Unauthorized access is prohibited.")
    print("Enter 'exit' as the username to quit.\n")
    ip = get_public_ip()
    user_agent = "Terminal Honeypot"

    while True:
        try:
            username = input("username: ").strip()
            if username.lower() == "exit":
                print("Exiting honeypot...")
                break
            password = input("password: ").strip()
            time.sleep(1)  # Mimic authentication delay
            print("Login failed: Invalid credentials\n")
            log_attempt(ip, username, password, user_agent)
        except KeyboardInterrupt:
            print("\nHoneypot terminated by user.")
            break
        except Exception as e:
            print(f"Error: {e}. Continuing...")

if __name__ == "__main__":
    fake_login_prompt()
