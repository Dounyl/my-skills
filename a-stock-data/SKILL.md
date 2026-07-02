---
name: a-stock-data
description: A股数据分析 skill。用于个股估值、实时行情、K线、研报检索、题材热点、北向资金、资金流向、龙虎榜、限售解禁、行业对比、两融、大宗交易、股东户数、分红、公告、ETF期权、互动易问答和市场热度分析。
origin: custom
version: 4.0.0
---

# A股数据分析 Skill

这个 skill 已按“渐进式暴露”重组。

先读本文件，只获取：
- 什么时候激活
- 先选哪类数据源
- 当前任务应该继续读哪一份 reference
- 什么时候需要脚本而不是把代码贴进上下文

不要默认继续读全部 `references/`。只读与你当前任务直接相关的那一份。

## 激活条件

用户要做下列任务时激活：
- 个股估值、PE/PB/PEG、一致预期、估值消化
- 实时行情、五档盘口、K线、逐笔成交、指数、ETF
- 研报检索、行业研报、PDF 下载、主题研报归纳
- 题材热点、概念归属、北向资金、资金流向、龙虎榜
- 限售解禁、两融、大宗交易、股东户数、分红、公告
- 涨停/炸板/跌停情绪、ETF 期权、互动易问答、人气热榜

## 先做路由，不要直接读大段实现

按用户任务选择后续文件：

| 任务 | 继续读取 |
|---|---|
| 依赖安装、环境变量、ticker 归一化、共用 helper | [references/setup-and-helpers.md](C:/Users/theD/Desktop/tempwork/references/setup-and-helpers.md) |
| 数据源选择、限流、防封、实现拆分规范 | [references/architecture-and-routing.md](C:/Users/theD/Desktop/tempwork/references/architecture-and-routing.md) |
| 行情、K线、指数、ETF | [references/domain-market.md](C:/Users/theD/Desktop/tempwork/references/domain-market.md) |
| 研报、一致预期、iwencai | [references/domain-research.md](C:/Users/theD/Desktop/tempwork/references/domain-research.md) |
| 热点、北向、概念、分钟级资金流 | [references/signals-overview.md](C:/Users/theD/Desktop/tempwork/references/signals-overview.md) |
| 龙虎榜、解禁、行业排名、打板、热榜 | [references/signals-trading-structure.md](C:/Users/theD/Desktop/tempwork/references/signals-trading-structure.md) |
| 财务、F10、个股基本面、财报三表 | [references/fundamentals-core.md](C:/Users/theD/Desktop/tempwork/references/fundamentals-core.md) |
| 新闻、公告、两融、大宗、股东户数、分红、期权、互动易 | [references/fundamentals-extended.md](C:/Users/theD/Desktop/tempwork/references/fundamentals-extended.md) |
| 单票调研、批量筛选、组合流程 | [references/workflows.md](C:/Users/theD/Desktop/tempwork/references/workflows.md) |

只有在下面两种情况，才读取旧大文档：
- 你要补某个冷门端点，而对应 domain reference 里还没有摘要
- 你需要核对历史实现细节或复制既有代码块

旧文档归档在：
- [references/legacy-full-skill.md](C:/Users/theD/Desktop/tempwork/references/legacy-full-skill.md)

## 核心路由规则

### 1. 先选数据源，再选实现

默认优先级：
1. `mootdx`
2. 腾讯财经
3. 新浪 / 巨潮 / 同花顺 / 百度股市通
4. 东财

含义：
- 行情、K线、实时价格、基础估值，优先走 `mootdx` 或腾讯
- 只有别处拿不到的数据，才走东财
- 一旦走东财，必须启用统一限流 helper

### 2. 先判断任务粒度

如果用户只是问“能不能查”或“怎么做”：
- 停在 reference 摘要层

如果用户要你真的实现、调用、封装：
- 读对应 domain reference
- 再决定是否调用 `scripts/` 中的脚本
- 不要把整段 sample code 全塞回主上下文

### 3. 共享逻辑不要散落在各 domain

这些逻辑统一收敛到共用 helper / script：
- ticker 归一化
- 市场前缀判断
- `mootdx` 客户端创建
- 东财 `Session`、限流、重试
- 通用 datacenter 查询
- PDF 下载、分页拉取、批量 sleep

## 推荐目录排布

```text
a-stock-data/
|- SKILL.md
|- references/
|  |- architecture-and-routing.md
|  |- setup-and-helpers.md
|  |- domain-market.md
|  |- domain-research.md
|  |- signals-overview.md
|  |- signals-trading-structure.md
|  |- fundamentals-core.md
|  |- fundamentals-extended.md
|  |- workflows.md
|  `- legacy-full-skill.md
`- scripts/
   |- shared/
   |  |- ticker.py
   |  |- tdx_client.py
   |  |- eastmoney_http.py
   |  `- pagination.py
   |- market/
   |- research/
   |- signals/
   `- fundamentals/
```

## script 和“衍生逻辑”的排布原则

`scripts/shared/`
- 放跨域复用且稳定的低自由度逻辑
- 例如 `normalize_ticker()`、`tdx_client()`、`em_get()`、通用分页器

`scripts/<domain>/`
- 放领域脚本，按输入输出明确分工
- 例如 `scripts/research/eastmoney_reports.py`
- 例如 `scripts/signals/dragon_tiger.py`

`references/*.md`
- 只放路由、使用时机、字段说明、数据源差异、注意事项
- 不放大段可执行代码，最多保留极短调用示意

“衍生逻辑”的推荐分层：
1. `routing` 层：在 `SKILL.md`，只决定读哪份 reference
2. `domain guide` 层：在 `references/*.md`，只决定选哪个端点或脚本
3. `shared helper` 层：在 `scripts/shared/`，承接跨域稳定逻辑
4. `endpoint implementation` 层：在 `scripts/<domain>/`
5. `workflow composition` 层：在 `references/workflows.md`，提供 checklist、验证点和失败回路

## 使用约束

- 不要一次性加载全部 reference
- 不要把旧版 2000+ 行实现直接复制进回答
- 不要在多个 domain 文件重复 helper 说明
- 东财相关请求必须统一走共享限流逻辑
- 批量任务优先调用脚本，避免在对话里重复生成相同代码

## 维护约束

新增功能时按下面顺序更新：
1. 先判断属于哪个 domain
2. 如是共享能力，进 `scripts/shared/`
3. 如是领域能力，进对应 `scripts/<domain>/`
4. 只在对应 `references/*.md` 增加入口说明
5. 仅当激活条件变化时才修改 `SKILL.md`

如果一个 reference 超过约 200 行，继续再拆，不要把它重新长成第二个大一统 skill。
