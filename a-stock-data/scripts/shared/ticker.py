"""Ticker normalization helpers for A-share symbols."""

from __future__ import annotations

import re


_TICKER_RE = re.compile(r"^\d{6}$")


def normalize_ticker(raw: str) -> str:
    """Normalize common A-share ticker formats to a 6-digit code."""
    if raw is None:
        raise ValueError("ticker is required")

    value = str(raw).strip().upper()
    value = value.replace(".SH", "").replace(".SZ", "").replace(".BJ", "")
    value = value.removeprefix("SH").removeprefix("SZ").removeprefix("BJ")

    if not _TICKER_RE.fullmatch(value):
        raise ValueError(f"unsupported ticker format: {raw}")

    return value


def get_prefix(code: str) -> str:
    """Map a 6-digit A-share ticker to its market prefix."""
    code = normalize_ticker(code)
    if code.startswith(("6", "9")):
        return "sh"
    if code.startswith("8"):
        return "bj"
    return "sz"


def with_prefix(code: str) -> str:
    """Return normalized ticker with exchange prefix, such as sh600519."""
    normalized = normalize_ticker(code)
    return f"{get_prefix(normalized)}{normalized}"
