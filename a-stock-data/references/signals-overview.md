# Signals Overview

## 这份文件何时读

用户要：
- 热点题材
- 北向资金
- 概念归属
- 分钟级资金流

如果涉及龙虎榜、解禁、行业排名、涨停池、热榜，不读本文件，改读：
- [signals-trading-structure.md](C:/Users/theD/Desktop/tempwork/references/signals-trading-structure.md)

## 能力路由

### 1. 热点题材

建议脚本：
- `scripts/signals/ths_hot.py`

用途：
- 强势股
- 题材归因

### 2. 北向资金

建议脚本：
- `scripts/signals/northbound_flow.py`

用途：
- 实时分钟流向
- 收盘后缓存历史

### 3. 概念 / 行业 / 地域归属

数据源：
- 东财 `slist`

建议脚本：
- `scripts/signals/eastmoney_blocks.py`

### 4. 分钟级资金流

数据源：
- 东财 `push2`

建议脚本：
- `scripts/signals/eastmoney_fund_flow.py`

## 共享约束

- 东财相关脚本统一复用 `scripts/shared/eastmoney_http.py`
- 本地缓存逻辑抽到 shared，不要写死在单个脚本里
