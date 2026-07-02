"""Shared mootdx client bootstrap helpers."""

from __future__ import annotations

import socket
from typing import Iterable

from mootdx.quotes import Quotes


TDX_SERVERS: list[tuple[str, int]] = [
    ("119.97.185.59", 7709),
    ("124.70.133.119", 7709),
    ("116.205.183.150", 7709),
    ("123.60.73.44", 7709),
    ("116.205.163.254", 7709),
    ("121.36.225.169", 7709),
    ("123.60.70.228", 7709),
    ("124.71.9.153", 7709),
    ("110.41.147.114", 7709),
    ("124.71.187.122", 7709),
]


def probe_server(ip: str, port: int, timeout: float = 2.0) -> bool:
    """Return whether the target TDX server accepts a TCP handshake."""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except OSError:
        return False


def iter_reachable_servers(
    servers: Iterable[tuple[str, int]] = TDX_SERVERS,
    timeout: float = 2.0,
) -> Iterable[tuple[str, int]]:
    """Yield reachable TDX servers in the provided order."""
    for ip, port in servers:
        if probe_server(ip, port, timeout=timeout):
            yield ip, port


def tdx_client(market: str = "std") -> Quotes:
    """Create a mootdx client while avoiding the BESTIP empty-string issue."""
    for ip, port in iter_reachable_servers():
        return Quotes.factory(market=market, server=(ip, port))

    try:
        return Quotes.factory(market=market, bestip=True)
    except Exception:
        pass

    try:
        return Quotes.factory(market=market)
    except Exception as exc:
        raise RuntimeError(
            "all mootdx servers are unreachable; use a CN-accessible network or "
            "update TDX_SERVERS"
        ) from exc
