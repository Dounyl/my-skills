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

适用：
- A 股个股新闻
- 全球市场快讯
- 外围市场背景和跨市场联动分析

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

## 全球请求的处理规则

- 如果用户只要“全球股市今天发生了什么”或“外围市场怎么影响 A 股”，优先从这里进入
- 如果用户要的是海外交易所专有结构化数据，不要把“全球资讯”误写成“全市场行情接口”
- 先给出现有覆盖，再说明哪些部分需要新增脚本

## 共享约束

- datacenter 类请求统一复用 `eastmoney_datacenter()`
- 东财新闻、公告等请求统一复用 `em_get()`
