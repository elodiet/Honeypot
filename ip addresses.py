import json
import re

# Load the JSON file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/log files/cowrie.json.2023-04-16', 'r') as f:
    data = f.read()

# Extract IP addresses using regex
ip_addresses = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', data)

# Remove duplicates
unique_ips = list(set(ip_addresses))

# Save unique IPs to a new file
with open('C:/Users/etana/OneDrive/Documents/Forensic Investigations/ipaddresses-logfiles/ipaddressoutput0416', 'a') as f:
    for ip in unique_ips:
        f.write(ip + '\n')
