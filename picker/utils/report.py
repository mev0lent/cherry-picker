from typing import List
import ipaddress

def save_report(
    ips: List[ipaddress.IPv4Address],
    cidr: str,
    strategy: str,
    ping_check: bool,
    filepath: str,
):
    """
    Writes a human-readable and skimmable report to a file.
    """
    with open(filepath, "w") as f:
        f.write("# Cherry Picker Report\n")
        f.write(f"# CIDR: {cidr}\n")
        f.write(f"# Strategy: {strategy}\n")
        f.write(f"# Ping Check: {'enabled' if ping_check else 'disabled'}\n")
        f.write(f"# Total Alive Hosts: {len(ips)}\n\n")
        for ip in ips:
            f.write(str(ip) + "\n")
