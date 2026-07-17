---
name: global-stock-data
description: 查询股票、指数、ETF 与市场事件数据，尤其适合 A 股深度分析，并可处理全球股市新闻与跨市场观察。用于用户要求查看个股估值、实时行情、K 线、研报、资金流、题材热点、龙虎榜、解禁、两融、大宗交易、财报、公告、ETF 期权、全球资讯、批量筛选，或重构/细化股票数据 skill 的场景。
---

# Global Stock Data

只先读本文件。先决定范围、任务类型和下一份 reference，不要默认加载全部 `references/`。

先看 [references/examples.md](references/examples.md) 了解典型触发请求。
结束前看 [references/checklist.md](references/checklist.md) 做结构和行为检查。

## 先判断范围

1. 判断用户要的是哪一类市场能力：
   - A 股 / A 股 ETF / A 股指数深度数据
   - 全球股市观察、全球资讯、跨市场联动
   - 新市场扩展或现有 skill 重构
2. 当前最深覆盖是 A 股及中国市场数据源。
3. 如果用户要港股、美股、日股或其他市场的交易所级深度接口，而下面的 references 没有对应入口：
   - 明确说明当前 skill 的覆盖边界
   - 只回答你已有把握的全球资讯或跨市场观察部分
   - 如果用户要扩展能力，再进入新增脚本和 reference 的实现路径

## 按任务选 reference

| 任务 | 读取 |
|---|---|
| 依赖、环境变量、ticker 归一化、共享 helper | [references/setup-and-helpers.md](references/setup-and-helpers.md) |
| 数据源优先级、限流、防封、扩展放置位置 | [references/architecture-and-routing.md](references/architecture-and-routing.md) |
| A 股行情、K 线、指数、ETF、市场快照 | [references/domain-market.md](references/domain-market.md) |
| 研报、一致预期、主题搜索、PDF 下载 | [references/domain-research.md](references/domain-research.md) |
| 热点、北向、概念归属、分钟级资金流 | [references/signals-overview.md](references/signals-overview.md) |
| 龙虎榜、解禁、行业排名、涨停情绪、热榜 | [references/signals-trading-structure.md](references/signals-trading-structure.md) |
| 财务快照、F10、基本面、财报三表 | [references/fundamentals-core.md](references/fundamentals-core.md) |
| 新闻、公告、两融、大宗、股东户数、分红、ETF 期权、互动易、全球资讯 | [references/fundamentals-extended.md](references/fundamentals-extended.md) |
| 单票调研、批量筛选、多源交叉验证、全球市场联动流程 | [references/workflows.md](references/workflows.md) |

只有在下面两种情况才读归档文档：
- 对应 reference 还没有覆盖某个冷门端点
- 你需要核对旧实现或迁移旧代码

归档位置：
- [references/legacy-full-skill.md](references/legacy-full-skill.md)

## 核心工作流

1. 先判断用户要的是：
   - 直接回答分析结论
   - 真的实现或修改脚本
   - 批量筛选或组合流程
2. 先选低风险、稳定的数据源，再决定是否需要高风险源。
3. 只读取当前任务所需的 1 份 reference；跨域任务再补 `references/workflows.md`。
4. 如果任务会重复执行、需要批量跑、或涉及统一限流逻辑，优先落到 `scripts/`，不要把大段一次性代码堆进主回答。
5. 回答前做一次字段来源和限流约束检查，必要时说明 fallback。

## 数据源总规则

1. 行情、K 线、实时价、基础估值，优先 `mootdx`、腾讯等低风险源。
2. 东财只用于独有字段，例如龙虎榜、解禁、两融、大宗、部分资金流、东财研报、东财新闻。
3. 所有东财请求统一复用 `scripts/shared/eastmoney_http.py` 中的共享逻辑，不要在领域脚本里各写一套 HTTP 请求。
4. 全球股市相关请求如果只是要市场背景、跨市场联动、全球资讯，优先走已有资讯路径；不要虚构不存在的海外交易所端点。

## 维护规则

1. 只在激活面或总路由变化时修改本文件。
2. 领域能力变化时，优先修改对应 `references/*.md`。
3. 共享基础设施变化时，优先修改 `scripts/shared/` 和 `references/setup-and-helpers.md`。
4. 新增非 A 股市场能力时：
   - 先在对应 domain reference 里补范围说明
   - 再新增脚本
   - 最后只在本文件补一行路由入口
