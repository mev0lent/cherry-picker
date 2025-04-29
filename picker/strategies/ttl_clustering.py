"""
Strategy: TTL Clustering
Groups IPs by similar TTL values (from prior ping scan data) and selects from the dominant TTL group.
"""

import ipaddress
from typing import List, Optional
from collections import defaultdict
from picker.utils.data_loader import load_ip_ttl_map

def ttl_clustering(cidr: str, count: int, ttl_file: Optional[str] = None) -> List[ipaddress.IPv4Address]:
    """
    Selects IPs grouped by most common TTL cluster.
    Requires a TTL input file.
    """
    if ttl_file is None:
        raise ValueError("ttl_clustering requires --input-file with TTL data (IP TTL per line).")

    ttl_map = load_ip_ttl_map(ttl_file)

    # Group IPs by TTL value
    ttl_groups = defaultdict(list)
    for ip, ttl in ttl_map.items():
        ttl_groups[ttl].append(ip)

    if not ttl_groups:
        return []

    # Find largest group
    largest_group = max(ttl_groups.values(), key=len)

    return largest_group[:count]
