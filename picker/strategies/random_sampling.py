import ipaddress
import random

def random_sample(cidr: str, count: int):
    network = ipaddress.ip_network(cidr)
    all_ips = list(network.hosts())
    return random.sample(all_ips, min(count, len(all_ips)))
