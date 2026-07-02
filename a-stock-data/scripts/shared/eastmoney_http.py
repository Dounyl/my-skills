"""Shared Eastmoney HTTP helpers with throttling and retries."""

from __future__ import annotations

import random
import re
import time
from pathlib import Path
from typing import Any

import requests

try:
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except Exception:  # pragma: no cover
    HTTPAdapter = None
    Retry = None


UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
DATACENTER_URL = "https://datacenter-web.eastmoney.com/api/data/v1/get"
PDF_TPL = "https://pdf.dfcfw.com/pdf/H3_{info_code}_1.pdf"

EM_SESSION = requests.Session()
EM_SESSION.headers.update({"User-Agent": UA})

if HTTPAdapter and Retry:
    adapter = HTTPAdapter(
        max_retries=Retry(
            total=3,
            connect=3,
            backoff_factor=0.6,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
        )
    )
    EM_SESSION.mount("https://", adapter)
    EM_SESSION.mount("http://", adapter)

EM_MIN_INTERVAL = 1.0
_em_last_call = [0.0]


def em_get(
    url: str,
    params: dict[str, Any] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int = 15,
    **kwargs: Any,
) -> requests.Response:
    """Issue a throttled GET request for Eastmoney endpoints."""
    wait = EM_MIN_INTERVAL - (time.time() - _em_last_call[0])
    if wait > 0:
        time.sleep(wait + random.uniform(0.1, 0.5))
    try:
        return EM_SESSION.get(url, params=params, headers=headers, timeout=timeout, **kwargs)
    finally:
        _em_last_call[0] = time.time()


def eastmoney_datacenter(
    report_name: str,
    columns: str = "ALL",
    filter_str: str = "",
    page_size: int = 50,
    sort_columns: str = "",
    sort_types: str = "-1",
) -> list[dict[str, Any]]:
    """Query Eastmoney datacenter with shared throttling."""
    params = {
        "reportName": report_name,
        "columns": columns,
        "filter": filter_str,
        "pageNumber": "1",
        "pageSize": str(page_size),
        "sortColumns": sort_columns,
        "sortTypes": sort_types,
        "source": "WEB",
        "client": "WEB",
    }
    response = em_get(DATACENTER_URL, params=params, timeout=15)
    payload = response.json()
    if payload.get("result") and payload["result"].get("data"):
        return payload["result"]["data"]
    return []


def download_pdf(record: dict[str, Any], target_dir: str = "./reports") -> str | None:
    """Download a single Eastmoney research PDF and return the local path."""
    info_code = record.get("infoCode", "")
    if not info_code:
        return None

    date = (record.get("publishDate") or "")[:10]
    org = re.sub(r'[\\/:*?"<>|]', "_", record.get("orgSName") or "unknown")[:40]
    title = re.sub(r'[\\/:*?"<>|]', "_", record.get("title", ""))[:80]
    filename = f"{date}_{org}_{title}.pdf"
    target = Path(target_dir) / filename
    if target.exists():
        return str(target)

    response = em_get(
        PDF_TPL.format(info_code=info_code),
        headers={"Referer": "https://data.eastmoney.com/"},
        timeout=60,
    )
    if response.status_code == 200 and len(response.content) >= 1024:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(response.content)
        return str(target)
    return None
