#!/usr/bin/env python3

import requests
import socket
import ipaddress
import json
import argparse
import os
import configparser
from colorama import init, Fore, Style

init(autoreset=True)

# ====== Tool Metadata ======
VERSION = "1.0.0"
AUTHOR = "Galmx"
GITHUB = "https://github.com/yourrepo/VeilStrike"

# ====== Colors ======
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE

# ====== Banner ======
banner = r'''
██╗   ██╗███████╗██╗██╗     ███████╗████████╗██████╗ ██╗██╗  ██╗███████╗
██║   ██║██╔════╝██║██║     ██╔════╝╚══██╔══╝██╔══██╗██║██║ ██╔╝██╔════╝
██║   ██║█████╗  ██║██║     ███████╗   ██║   ██████╔╝██║█████╔╝ █████╗
╚██╗ ██╔╝██╔══╝  ██║██║     ╚════██║   ██║   ██╔══██╗██║██╔═██╗ ██╔══╝
 ╚████╔╝ ███████╗██║███████╗███████║   ██║   ██║  ██║██║██║  ██╗███████╗
  ╚═══╝  ╚══════╝╚═╝╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚══════╝

        CDN Exposure & Origin Intelligence Scanner
'''

def print_banner():
    print(f"{R}{banner}{W}")
    print(f"{G}[+] {Y}Version      : {W}{VERSION}")
    print(f"{G}[+] {Y}Author       : {W}{AUTHOR}")
    print(f"{G}[+] {Y}GitHub       : {W}{GITHUB}")
    print(f"{G}[+] {Y}Module       : {W}CDN Detection | Origin Resolution\n")

# ====== Load Config ======
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.ini")
config = configparser.ConfigParser()
config.read(CONFIG_PATH)

SECURITYTRAILS_API_KEY = config.get("API_KEYS", "SECURITYTRAILS_API_KEY", fallback=None)

# ====== Cloudflare IP Ranges ======
CLOUDFLARE_RANGES = [
    "173.245.48.0/20",
    "103.21.244.0/22",
    "103.22.200.0/22",
    "103.31.4.0/22",
    "141.101.64.0/18",
    "108.162.192.0/18",
    "190.93.240.0/20",
    "188.114.96.0/20",
    "197.234.240.0/22",
    "198.41.128.0/17",
    "162.158.0.0/15",
    "104.16.0.0/13",
    "104.24.0.0/14",
    "172.64.0.0/13",
    "131.0.72.0/22"
]

# ====== Functions ======
def resolve_domain(domain):
    """Resolve IPv4 and IPv6 addresses"""
    results = {"ipv4": [], "ipv6": []}
    try:
        infos = socket.getaddrinfo(domain, None)
        for info in infos:
            addr = info[4][0]
            if ":" in addr:
                if addr not in results["ipv6"]:
                    results["ipv6"].append(addr)
            else:
                if addr not in results["ipv4"]:
                    results["ipv4"].append(addr)
    except Exception as e:
        print(f"[!] DNS resolution failed: {e}")
    return results

def is_cloudflare_ip(ip):
    ip_obj = ipaddress.ip_address(ip)
    for cidr in CLOUDFLARE_RANGES:
        if ip_obj in ipaddress.ip_network(cidr):
            return True
    return False

def check_cloudflare(domain):
    """Check if a domain is using Cloudflare via IPs and headers"""
    dns = resolve_domain(domain)
    cloudflare_detected = False
    for ip in dns["ipv4"]:
        if is_cloudflare_ip(ip):
            cloudflare_detected = True
    try:
        r = requests.head(f"https://{domain}", timeout=5)
        headers = r.headers
        server_header = headers.get("server", "").lower()
        if "cloudflare" in server_header:
            cloudflare_detected = True
        if "cf-ray" in headers:
            cloudflare_detected = True
    except:
        pass
    return cloudflare_detected

def detect_web_server(domain):
    """Detect web server header"""
    try:
        r = requests.head(f"https://{domain}", timeout=5)
        return r.headers.get("Server", "UNKNOWN")
    except:
        return "UNKNOWN"

def analyze(domain, json_output=False):
    dns = resolve_domain(domain)
    cloudflare = check_cloudflare(domain)
    server = detect_web_server(domain)

    data = {
        "domain": domain,
        "cloudflare_detected": cloudflare,
        "web_server": server,
        "ipv4": dns["ipv4"],
        "ipv6": dns["ipv6"]
    }

    if json_output:
        print(json.dumps(data, indent=4))
    else:
        print(f"{C}Target: {W}{domain}")
        print(f"{C}Cloudflare Detected: {W}{cloudflare}")
        print(f"{C}Web Server: {W}{server}")
        print(f"{C}IPv4: {W}{', '.join(dns['ipv4']) if dns['ipv4'] else 'NONE'}")
        print(f"{C}IPv6: {W}{', '.join(dns['ipv6']) if dns['ipv6'] else 'NONE'}")

# ====== Main ======
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="VeilStrike - CDN & Origin Intelligence Scanner")
    parser.add_argument("domain", help="Target domain to scan")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    args = parser.parse_args()

    print_banner()
    analyze(args.domain, args.json)