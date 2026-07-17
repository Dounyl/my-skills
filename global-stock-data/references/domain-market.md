# Domain Market

## 这份文件何时读

用户要：
- K 线
- 五档盘口
- 逐笔成交
- 实时报价
- 指数 / ETF 行情
- 带均线的 K 线
- A 股市场快照

## 能力路由

### 1. A 股 K 线 / 五档 / 逐笔

优先：
- `mootdx`

原因：
- 不依赖东财
- 适合高频读取

建议脚本：
- `scripts/shared/tdx_client.py`
- `scripts/market/mootdx_quotes.py`

### 2. A 股 PE / PB / 市值 / 换手率 / 涨跌停 / 指数 / ETF

优先：
- 腾讯财经

建议脚本：
- `scripts/market/tencent_quotes.py`

### 3. 带 MA5/10/20 的 K 线

可选：
- 百度股市通

建议脚本：
- `scripts/market/baidu_kline.py`

### 4. 全球市场观察

如果用户只是要：
- 全球主要指数涨跌
- 外围市场对 A 股的影响
- 市场背景或快讯摘要

做法：
- 先跳到 [fundamentals-extended.md](fundamentals-extended.md) 读取全球资讯入口
- 再按 [workflows.md](workflows.md) 的“全球市场联动”流程组织回答

如果用户要：
- 非 A 股交易所级深度行情
- 海外个股逐笔、盘口、交易所专有字段

做法：
- 先说明当前 skill 没有默认覆盖该接口
- 仅在用户明确要求扩展时新增脚本，不要临时虚构端点
