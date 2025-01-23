import requests
import sys
import signal
from concurrent.futures import ThreadPoolExecutor
import argparse
from tqdm import tqdm    
from colorama import Fore, Style, init

init(autoreset=True)

found_vulnerability = False

def handle_interrupt(signal, frame):
    print(f"\n\n{Fore.RED}[!] Process interrupted by user. Exiting...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

def load_payloads(file_path):
    try:
        with open(file_path, "r") as file:
            payloads = file.read().splitlines()
        return payloads
    except Exception as e:
        print(f"{Fore.RED}[!] Error reading file: {e}{Style.RESET_ALL}")
        return []

def test_xss(payload, base_url, progress_bar):
    global found_vulnerability
    if found_vulnerability:   
        return
    url = base_url + requests.utils.quote(payload)   
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and payload in response.text:
            found_vulnerability = True
            progress_bar.close()   
            print(f"\n\n{Fore.GREEN}[!] XSS Vulnerability Detected!{Style.RESET_ALL}")
            print(f"{Fore.CYAN}    [+] Payload: {Fore.YELLOW}{payload}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}    [+] Affected URL: {Fore.YELLOW}{url}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}    [+] HTTP Status Code: {Fore.YELLOW}{response.status_code}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}    [+] Response Length: {Fore.YELLOW}{len(response.text)} bytes{Style.RESET_ALL}")
            print(f"\n{Fore.RED}[!] Stopping further testing as vulnerability was detected.{Style.RESET_ALL}")
        elif response.status_code != 200:
            pass 
    except Exception as e:
        print(f"\n{Fore.RED}[!] Error testing payload '{payload}': {e}{Style.RESET_ALL}")
    finally:
        progress_bar.update(1)   

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced XSS Testing Tool")
    parser.add_argument("-u","--url", required=True, help="The base URL to test, e.g., 'https://example.com/search?q='")
    parser.add_argument("-p","--payload", required=True, help="The file containing XSS payloads to test")
    args = parser.parse_args()
    base_url = args.url
    payload_file = args.payload

    payloads = load_payloads(payload_file)
    if not payloads:
        print(f"{Fore.RED}[!] No payloads found. Exiting...{Style.RESET_ALL}")
    else:
        print(f"{Fore.MAGENTA}[#] @e5t3hb4r47 [#]{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[*] Loaded {len(payloads)} payloads from {payload_file}{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[*] Starting XSS tests...\n{Style.RESET_ALL}")
        
        with tqdm(total=len(payloads), desc="Testing Payloads", unit="payload") as progress_bar:
            with ThreadPoolExecutor(max_workers=10) as executor:
                executor.map(lambda payload: test_xss(payload, base_url, progress_bar), payloads)
        
        if not found_vulnerability:
            print(f"\n{Fore.YELLOW}[-] No XSS vulnerabilities detected after testing all payloads.{Style.RESET_ALL}")
