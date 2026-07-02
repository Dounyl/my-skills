# Architecture And Routing

## 这份文件何时读

当你需要判断：
- 哪个数据源优先
- 东财什么时候能用
- script 和 reference 怎么分工
- 新功能应该放到哪里

## 数据源优先级

1. `mootdx`
2. 腾讯财经
3. 新浪 / 巨潮 / 同花顺 / 百度股市通
4. 东财

判断规则：
- 行情、K线、实时价、盘口、部分估值：优先 `mootdx` / 腾讯
- 东财只处理独有数据：龙虎榜、解禁、两融、大宗、东财研报、东财新闻、部分资金流和板块归属

## 东财相关约束

东财接口统一视为高风险源：
- 不并发
- 请求间隔至少 1 秒，批量任务提高到 1.5 到 2 秒
- 统一复用 `Session`
- 带正常 `User-Agent` 和 `Referer`
- `403` 视为风控信号，优先降频，不要盲目重试

因此：
- 东财 HTTP 逻辑统一进 `scripts/shared/eastmoney_http.py`
- 任何 domain 脚本都不应直接各自实现一套 `requests.get`

## 目录责任

`SKILL.md`
- 激活条件
- 路由规则
- 文件导航

`references/domain-*.md`
- 该领域有哪些能力
- 每种能力优先用哪个源
- 关键字段与注意事项
- 需要哪个脚本

`scripts/shared/*`
- 跨域稳定基础设施

`scripts/<domain>/*`
- 具体端点封装

## 衍生逻辑怎么排

不建议把“衍生逻辑”写成一个超长说明节。更好的方式是按决策深度拆：

1. 入口衍生逻辑
   只回答“这是哪个 domain 的问题”

2. 域内衍生逻辑
   只回答“这个 domain 里该选哪个端点”

3. 实现衍生逻辑
   只回答“这个端点是否依赖共享 helper、分页、限流、缓存”

4. 组合衍生逻辑
   只回答“多个端点如何串成 workflow”

这样每层只做一类判断，模型不会在激活时一次性读完整棵树。

## 建议新增的脚本布局

```text
scripts/
|- shared/
|  |- ticker.py
|  |- tdx_client.py
|  |- eastmoney_http.py
|  |- download_pdf.py
|  `- cache_io.py
|- market/
|- research/
|- signals/
`- fundamentals/
```

示例：
- `scripts/shared/ticker.py`: 代码归一化、市场前缀
- `scripts/shared/tdx_client.py`: mootdx 连接和探测
- `scripts/shared/eastmoney_http.py`: session、限流、重试、通用请求
- `scripts/research/eastmoney_reports.py`: 研报查询和 PDF 下载
- `scripts/signals/board_blocks.py`: 概念/行业/地域归属
- `scripts/fundamentals/cninfo_announcements.py`: 公告查询
