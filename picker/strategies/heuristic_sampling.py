import ipaddress

def heuristic_sample(cidr: str, count: int):
    network = ipaddress.ip_network(cidr)
    all_ips = list(network.hosts())

    # Beispiel: always take the first x IPs
    return all_ips[:count]
