import typer
from picker.strategies.random_sampling import random_sample
from picker.strategies.heuristic_sampling import heuristic_sample
from picker.strategies.first_octet_bias import first_octet_bias
from picker.strategies.cluster_focus import cluster_focus
from picker.strategies.cloud_patterns import cloud_patterns
from picker.strategies.entropy_reduce import entropy_reduce
from picker.strategies.ttl_clustering import ttl_clustering
from picker.utils.report import save_report
from picker.utils.combo import apply_combined_strategies

STRATEGIES = {
    "random": random_sample,
    "heuristic": heuristic_sample,
    "first_octet_bias": first_octet_bias,
    "cluster_focus": cluster_focus,
    "cloud_patterns": cloud_patterns,
    "entropy_reduce": entropy_reduce,
    "ttl_clustering": ttl_clustering,
}

def pick(
    cidr: str = typer.Argument(..., help="CIDR network block to pick IPs from, e.g., 192.168.0.0/24."),
    strategy: str = typer.Option(
        "random",
        help="Strategy or combination of strategies to pick IPs."
    ),
    count: int = typer.Option(10, help="Number of IPs to pick."),
    input_file: str = typer.Option(None, help="Optional: input file for TTL or alive hosts."),
    ping_check: bool = typer.Option(True, help="Ping IPs and only return reachable ones."),
    timeout: int = typer.Option(1, help="Ping timeout in seconds per IP."),
    parallelism: int = typer.Option(100, help="Maximum concurrent pings."),
    output_file: str = typer.Option(None, help="Write a structured report to this file."),
):
    try:
        extra_args = {"known_hosts_file": input_file} if "cluster_focus" in strategy else {}
        ips = apply_combined_strategies(cidr, count, strategy, STRATEGIES, extra_args=extra_args)
    except ValueError as e:
        typer.echo(str(e))
        raise typer.Exit(code=1)

    if ping_check:
        from picker.utils.async_ping import filter_alive_ips
        import asyncio
        ips = asyncio.run(filter_alive_ips(ips, timeout=timeout, parallelism=parallelism))

    if output_file:
        save_report(ips, cidr, strategy, ping_check, output_file)
    else:
        typer.secho("\n[+] === Cherry Picker Result ===", bold=True, fg=typer.colors.BRIGHT_CYAN)
        typer.echo(f"[+] CIDR:      {cidr}")
        typer.echo(f"[++] Strategy:  {strategy}")
        typer.echo(f"[+++] Ping check: {'enabled' if ping_check else 'disabled'}")
        typer.echo(f"[+++] Total IPs: {len(ips)}\n")

        for ip in ips:
            typer.secho(f"• {ip}", fg=typer.colors.GREEN)

