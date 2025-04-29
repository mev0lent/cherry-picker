import ipaddress
from typing import List

def load_ip_list(filepath: str) -> List[ipaddress.IPv4Address]:
    """
    Loads a list of IPv4 addresses from a file.
    Supports plain text (one IP per line).
    """
    ips = []
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                ips.append(ipaddress.IPv4Address(line))
            except ValueError:
                continue
    return ips

def load_ip_ttl_map(filepath: str) -> dict[ipaddress.IPv4Address, int]:
    """
    Loads a mapping of IP -> TTL from a file. Format: 'IP TTL' per line.
    """
    result = {}
    with open(filepath, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) != 2:
                continue
            try:
                ip = ipaddress.IPv4Address(parts[0])
                ttl = int(parts[1])
                result[ip] = ttl
            except ValueError:
                continue
    return result
