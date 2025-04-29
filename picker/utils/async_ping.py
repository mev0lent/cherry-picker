import asyncio
import platform
import ipaddress
from typing import List

async def ping(ip: str, timeout: int) -> bool:
    param = "-n" if platform.system().lower() == "windows" else "-c"
    timeout_param = "-w" if platform.system().lower() == "windows" else "-W"
    proc = await asyncio.create_subprocess_exec(
        "ping", param, "1", timeout_param, str(timeout), str(ip),
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    return (await proc.wait()) == 0

async def filter_alive_ips(ips: List[ipaddress.IPv4Address], timeout: int = 1, parallelism: int = 100) -> List[ipaddress.IPv4Address]:
    sem = asyncio.Semaphore(parallelism)

    async def sem_ping(ip):
        async with sem:
            return await ping(str(ip), timeout)

    tasks = [sem_ping(ip) for ip in ips]
    results = await asyncio.gather(*tasks)

    return [ip for ip, alive in zip(ips, results) if alive]
