"""
Strategy: Cloud Patterns
Selects IPs from the given network that overlap with known cloud provider CIDR blocks.
Useful to focus on likely cloud-hosted services.
"""

import ipaddress
from typing import List

# Simplified cloud CIDR ranges — real ones are much longer, could be loaded from AWS JSON, etc.
CLOUD_CIDRS = [
    # AWS
    "3.0.0.0/8", "13.32.0.0/15", "15.230.0.0/16", "52.95.110.0/24",
    # Azure
    "20.33.0.0/16", "40.74.0.0/16",
    # Google Cloud
    "8.34.208.0/20", "8.35.192.0/20", "35.190.0.0/17",
]

cloud_networks = [ipaddress.ip_network(cidr) for cidr in CLOUD_CIDRS]

def cloud_patterns(cidr: str, count: int) -> List[ipaddress.IPv4Address]:
    """
    Picks IPs from the user's CIDR that match known cloud provider ranges.
    """
    network = ipaddress.ip_network(cidr)
    all_hosts = list(network.hosts())

    # Filter: only keep hosts that fall into one of the cloud CIDRs
    cloud_hosts = []
    for ip in all_hosts:
        for cloud_net in cloud_networks:
            if ip in cloud_net:
                cloud_hosts.append(ip)
                break
        if len(cloud_hosts) >= count:
            break

    # Fallback if not enough found
    if len(cloud_hosts) < count:
        rest = [ip for ip in all_hosts if ip not in cloud_hosts]
        cloud_hosts.extend(rest[: max(0, count - len(cloud_hosts))])

    return cloud_hosts
