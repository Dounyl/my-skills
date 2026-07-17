# Domain Research

## 这份文件何时读

用户要：
- 个股研报
- 行业研报
- 研报 PDF
- 一致预期 EPS
- 主题 / 自然语言研报搜索

## 能力路由

### 1. 东财研报列表 + PDF

用途：
- 标准研报抓取主入口

注意：
- 属于东财源，必须走共享限流 helper

建议脚本：
- `scripts/research/eastmoney_reports.py`

建议职责：
- 个股研报查询
- 行业研报查询
- 分页
- PDF 下载

### 2. 同花顺一致预期 EPS

用途：
- 看机构覆盖和一致预期

建议脚本：
- `scripts/research/ths_forecast.py`

### 3. iwencai 语义搜索

用途：
- 主题驱动、问句式搜索

前提：
- 需要 API key

建议脚本：
- `scripts/research/iwencai_search.py`

## 推荐读取顺序

1. 先判断用户是“标准研报检索”还是“主题语义搜索”
2. 标准检索优先东财
3. 一致预期单独走同花顺
4. 主题性搜索再补 iwencai

## 边界

- 这份文件主要覆盖 A 股和中国市场研报入口
- 如果用户要的是全球市场新闻脉络，不读这里，改读 [fundamentals-extended.md](fundamentals-extended.md)
- 如果用户要海外卖方数据库或海外交易所披露文件，先说明当前 skill 未默认覆盖
