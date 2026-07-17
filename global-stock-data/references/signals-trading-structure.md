# Signals Trading Structure

## 这份文件何时读

用户要：
- 龙虎榜
- 全市场龙虎榜
- 限售解禁
- 行业板块排名
- 涨停 / 炸板 / 跌停 / 连板情绪
- 热榜 / 人气榜

## 能力路由

### 1. 龙虎榜 / 全市场龙虎榜

数据源：
- 东财 `datacenter`

建议脚本：
- `scripts/signals/dragon_tiger.py`

### 2. 限售解禁

数据源：
- 东财 `datacenter`

建议脚本：
- `scripts/signals/unlock_calendar.py`

### 3. 行业板块排名

数据源：
- 东财

建议脚本：
- `scripts/signals/industry_rank.py`

### 4. 打板情绪

建议拆分：
- `scripts/signals/limit_up_pool.py`
- `scripts/signals/limit_up_reason.py`
- `scripts/signals/board_sentiment.py`

### 5. 热榜 / 人气榜

建议脚本：
- `scripts/signals/heat_rank.py`

## 共享约束

- 交易结构类东财请求优先走 `eastmoney_datacenter()`
- 如果需要组合“题材热度 + 资金验证”，跳转 [workflows.md](workflows.md)

## 边界

- 这些能力默认都面向 A 股交易结构
- 如果用户要全球市场情绪对比，先做资讯或指数层观察，再决定是否扩展结构化脚本
