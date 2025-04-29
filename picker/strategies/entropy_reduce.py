"""
Strategy: Entropy Reduce
Selects IPs that appear more "structured" or human-chosen, by scoring and preferring
those with lower entropy (e.g., 10.0.0.1, 192.168.1.100).
"""

import ipaddress
from typing import List
import math

def octet_entropy(ip: ipaddress.IPv4Address) -> float:
    """
    Calculates a simple entropy score of an IP based on octet variation.
    Lower = more structured (e.g. 192.168.0.1), higher = more random.
    """
    octets = list(map(int, str(ip).split(".")))
    # Penalize high variation, favor repeated or rounded octets
    diffs = [abs(octets[i] - octets[i-1]) for i in range(1, 4)]
    roundness = sum(1 for o in octets if o in {0, 1, 10, 50, 100, 200, 254})
    variation_score = sum(diffs)
    return variation_score - (roundness * 2)  # round IPs are favored

def entropy_reduce(cidr: str, count: int) -> List[ipaddress.IPv4Address]:
    """
    Picks IPs from the network that have lower entropy scores,
    indicating likely structured or manually assigned addresses.
    """
    network = ipaddress.ip_network(cidr)
    all_hosts = list(network.hosts())

    scored = [(ip, octet_entropy(ip)) for ip in all_hosts]
    scored.sort(key=lambda x: x[1])  # lower score is better

    return [ip for ip, _ in scored[:count]]
