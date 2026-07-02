# Domain Market

## 这份文件何时读

用户要：
- K线
- 五档盘口
- 逐笔成交
- 实时报价
- 指数 / ETF 行情
- 带均线的 K 线

## 能力路由

### 1. K线 / 五档 / 逐笔

优先：
- `mootdx`

原因：
- 不依赖东财
- 适合高频读取

实现建议：
- 共用 `scripts/shared/tdx_client.py`
- 领域封装放 `scripts/market/mootdx_quotes.py`

### 2. PE / PB / 市值 / 换手率 / 涨跌停 / 指数 / ETF

优先：
- 腾讯财经

实现建议：
- `scripts/market/tencent_quotes.py`

### 3. 带 MA5/10/20 的 K 线

可选：
- 百度股市通

实现建议：
- `scripts/market/baidu_kline.py`

## 保留在 reference 的信息

- 优先级
- 适用场景
- 字段差异
- 是否可高频调用

## 不放在 reference 的信息

- 大段可执行示例
- 完整字段索引表
- 各种异常处理实现

那些内容应转进脚本内部注释或测试。
