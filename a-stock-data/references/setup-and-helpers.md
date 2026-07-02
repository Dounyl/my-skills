# Setup And Helpers

## 这份文件何时读

当你需要：
- 安装依赖
- 配置 iwencai key
- 统一 ticker 格式
- 创建 `mootdx` 客户端
- 使用东财共享 helper

## 依赖

```bash
pip install mootdx requests pandas stockstats
```

## iwencai

只有语义搜索研报时需要：

```bash
export IWENCAI_API_KEY="your_key_here"
export IWENCAI_BASE_URL="https://openapi.iwencai.com"
```

## ticker 归一化

所有输入先归一化成 6 位数字代码。

接受的常见格式：
- `688017`
- `SH688017`
- `688017.SH`
- `SZ000001`
- `BJ832000`

市场前缀规则：
- `6` 或 `9` 开头 -> `sh`
- `8` 开头 -> `bj`
- 其余 -> `sz`

这部分放进：
- `scripts/shared/ticker.py`

## mootdx helper

`mootdx` 客户端初始化应独立为共享脚本，不要在每个示例里重复定义。

建议职责：
- 维护候选服务器列表
- 探测 TCP 可达性
- 显式传入 `server` 规避 `BESTIP` 空串问题
- 提供统一的 `tdx_client()` 工厂

建议文件：
- `scripts/shared/tdx_client.py`

## 东财 helper

所有东财请求共享：
- `Session`
- 最小请求间隔
- 随机抖动
- 重试策略

建议文件：
- `scripts/shared/eastmoney_http.py`

建议暴露的方法：
- `em_get()`
- `eastmoney_datacenter()`
- `download_pdf()`

## 这里不要放什么

不要在这份文件里堆各领域端点细节：
- 研报字段
- 龙虎榜字段
- 新闻字段
- 两融字段

这些都应回到各自 `domain-*.md`。
