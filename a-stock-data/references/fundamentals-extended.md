# Fundamentals Extended

## 这份文件何时读

用户要：
- 个股新闻
- 全球资讯
- 公告
- 两融
- 大宗交易
- 股东户数
- 分红
- ETF 期权
- 互动易问答

## 能力路由

### 1. 新闻

建议脚本：
- `scripts/fundamentals/stock_news.py`
- `scripts/fundamentals/global_news.py`

### 2. 公告

建议脚本：
- `scripts/fundamentals/cninfo_announcements.py`
- `scripts/fundamentals/f10_announcements.py`

### 3. 两融 / 大宗 / 股东户数 / 分红

建议脚本：
- `scripts/fundamentals/margin_trading.py`
- `scripts/fundamentals/block_trades.py`
- `scripts/fundamentals/shareholder_counts.py`
- `scripts/fundamentals/dividends.py`

### 4. ETF 期权

建议脚本：
- `scripts/fundamentals/etf_options.py`

### 5. 互动易

建议脚本：
- `scripts/fundamentals/irm_qa.py`

## 共享约束

- datacenter 类请求统一复用 `eastmoney_datacenter()`
- 东财新闻、公告等请求统一复用 `em_get()`
