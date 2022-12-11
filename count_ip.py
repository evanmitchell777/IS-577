#!/usr/bin/env python3

import re

# Open the log file
with open('logfile.txt') as f:
    log = f.read()

# Find all IP addresses in the log file using a regular expression
ip_regex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'
ip_addresses = re.findall(ip_regex, log)

# Count the occurrences of each IP address
ip_counts = {}
for ip in ip_addresses:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

# Print the IP addresses and their counts
for ip, count in ip_counts.items():
    print(f'{ip}: {count}')
