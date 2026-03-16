# Network Scanning Automation

This project implements automated network scanning tools using Python. 
The programs execute system commands like Ping, ARP, and Nmap and analyze their outputs to gather network information.

## Tools Implemented

1. Ping Scanner
2. ARP Scanner
3. Nmap Scanner

## Requirements

Python 3  
Nmap

Install Nmap:

sudo apt install nmap

## How to Run the Programs

Ping Scanner

python3 ping_scanner.py

ARP Scanner

python3 arp_scanner.py

Nmap Scanner

python3 nmap_scanner.py

## Project Structure

network-scanning-tools
│
├── ping_scanner.py
├── arp_scanner.py
├── nmap_scanner.py
├── README.md
│
└── screenshots
    ├── ping_output.png
    ├── arp_output.png
    └── nmap_output.png

## Example Usage

Ping Scanner  
Input: google.com  
Output: Host reachable with response time.

ARP Scanner  
Displays IP and MAC address mappings from the system ARP table.

Nmap Scanner  
Input: 127.0.0.1  
Output: Shows detected ports and services.

## Author

Tejaswini H L  
Cybersecurity Course – CampusPe
