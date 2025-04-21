import re

log = "Client IP: 192.168.0.1 - Request received from 10.0.0.1 - Server IP: 172.16.0.1"

ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
ips = re.findall(ip_pattern, log)

print(ips)