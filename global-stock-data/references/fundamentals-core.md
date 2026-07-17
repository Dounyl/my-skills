# Fundamentals Core

## 这份文件何时读

用户要：
- 财务快照
- F10
- 个股基本面
- 财报三表

如果涉及新闻、公告、两融、大宗、股东户数、分红、期权、互动易或全球资讯，不读本文件，改读：
- [fundamentals-extended.md](fundamentals-extended.md)

## 能力路由

### 1. 财务快照 / F10

优先：
- `mootdx`

建议脚本：
- `scripts/fundamentals/mootdx_finance.py`
- `scripts/fundamentals/mootdx_f10.py`

### 2. 个股基本面

数据源：
- 东财 `push2`

建议脚本：
- `scripts/fundamentals/eastmoney_basics.py`

### 3. 财报三表

数据源：
- 新浪

建议脚本：
- `scripts/fundamentals/sina_statements.py`

## 边界

- 这里默认是 A 股基本面与财报能力
- 海外市场财报接口不在当前默认覆盖内；只有用户明确要扩展时再新增入口
