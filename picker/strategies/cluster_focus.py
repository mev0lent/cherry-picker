"""
Strategy: Cluster Focus
Expands IP selection around known "hit" IPs (e.g. alive hosts),
to focus on nearby addresses in the same subnet.
"""

import ipaddress
from typing import List, Optional
from picker.utils.data_loader import load_ip_list

def cluster_focus(cidr: str, count: int, known_hosts_file: Optional[str] = None) -> List[ipaddress.IPv4Address]:
    """
    Selects IPs close to known active ones, expanding from each in both directions.
    Requires known hosts input file.
    """
    if known_hosts_file is None:
        raise ValueError("cluster_focus requires --input-file with known active IPs.")

    known_ips = load_ip_list(known_hosts_file)
    network = ipaddress.ip_network(cidr)
    all_hosts = list(network.hosts())

    host_set = set(all_hosts)
    selected = []
    RADIUS = 5

    for ip in known_ips:
        base_int = int(ip)
        for offset in range(-RADIUS, RADIUS + 1):
            candidate = ipaddress.IPv4Address(base_int + offset)
            if candidate in host_set and candidate not in selected:
                selected.append(candidate)
                if len(selected) >= count:
                    return selected

    # Fallback: fill from remaining IPs
    remaining = [ip for ip in all_hosts if ip not in selected]
    selected.extend(remaining[: max(0, count - len(selected))])
    return selected
