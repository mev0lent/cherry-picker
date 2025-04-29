from typing import List
import ipaddress

def apply_combined_strategies(cidr: str, count: int, strategy_str: str, strategies: dict, extra_args: dict = None) -> List[ipaddress.IPv4Address]:
    """
    Parses a strategy string like "heuristic+random" or "heuristic:0.7+random:0.3"
    and returns a combined list of IPs (deduplicated).
    """
    strategy_chunks = strategy_str.split("+")
    parsed = []

    total_weight = 0.0
    for chunk in strategy_chunks:
        parts = chunk.split(":")
        name = parts[0]
        weight = float(parts[1]) if len(parts) == 2 else 1.0
        if name not in strategies:
            raise ValueError(f"Unknown strategy: {name}")
        parsed.append((name, weight))
        total_weight += weight

    if total_weight == 0:
        raise ValueError("Total strategy weight must be > 0.")

    all_ips = []
    seen = set()
    assigned_counts = []

    # Split
    for i, (name, weight) in enumerate(parsed):
        portion = (weight / total_weight) * count
        rounded = int(round(portion))
        assigned_counts.append(rounded)

    # Adjustment so that sum equals `count`
    diff = count - sum(assigned_counts)
    if diff != 0:
        # Correct first strategy top/bottom
        assigned_counts[0] += diff

    for (name, _), strategy_count in zip(parsed, assigned_counts):
        picker = strategies[name]
        if extra_args:
            picked = picker(cidr, strategy_count, **extra_args)
        else:
            picked = picker(cidr, strategy_count)

        for ip in picked:
            if ip not in seen:
                seen.add(ip)
                all_ips.append(ip)

    return all_ips
