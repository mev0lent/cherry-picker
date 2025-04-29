"""
Strategy: First Octet Bias
This strategy prioritizes IP addresses typically associated with important infrastructure,
such as .1 (gateway), .10 (management), and .254 (special devices).
"""

import ipaddress
from picker.utils.selection import select_first_octet_bias

def first_octet_bias(cidr: str, count: int):
    network = ipaddress.ip_network(cidr)
    hosts = list(network.hosts())
    prioritized_ips = select_first_octet_bias(hosts)

    # Fallback: when there are fewer IPs than the requested count
    if len(prioritized_ips) < count:
        return prioritized_ips
    else:
        return prioritized_ips[:count]
