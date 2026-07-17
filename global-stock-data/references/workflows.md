# Workflows

## 这份文件何时读

只有在用户要：
- 单票完整调研
- 批量筛选
- 多源交叉验证
- 组合型分析流程
- 全球市场联动观察

时才读这份文件。

## 使用方式

遇到复杂任务时：
1. 复制对应 checklist
2. 每完成一步就标记结果
3. 某一步失败时走该步骤下方的 validation / fallback
4. 不要跳过 validation 直接继续拼接结论

## 流程 A: 单票快速调研

Checklist:
- [ ] 读取 [domain-market.md](domain-market.md)，拿到基础行情与估值
- [ ] 读取 [domain-research.md](domain-research.md)，确认机构覆盖与研报
- [ ] 读取 [signals-overview.md](signals-overview.md)，确认概念归属与盘中资金
- [ ] 读取 [signals-trading-structure.md](signals-trading-structure.md)，补龙虎榜或解禁
- [ ] 读取 [fundamentals-core.md](fundamentals-core.md)，补财报和基本面
- [ ] 读取 [fundamentals-extended.md](fundamentals-extended.md)，补新闻、公告、互动易

Validation:
- 基础价格类数据优先来自 `mootdx` / 腾讯，而不是东财
- 如果结论依赖东财独有数据，确认请求频率已经降下来

Fallback:
- `mootdx` 不可达时，优先退到腾讯或其他 HTTP 源
- 东财异常时，先降频，再换低风险源补非独有字段

## 流程 B: 批量对比

Checklist:
- [ ] 先统一 ticker，调用 shared ticker helper
- [ ] 第一轮只跑低风险源
- [ ] 第二轮只对候选结果补东财独有指标
- [ ] 批量场景整体调大东财请求间隔

Validation:
- 不在对话里生成大循环代码
- 同类任务优先落到脚本，不要反复临时拼接

Fallback:
- 如果东财出现风控迹象，减少批量范围或拆批执行

## 流程 C: 主题研报检索

Checklist:
- [ ] 用 iwencai 做主题或问句检索
- [ ] 用东财补个股或行业研报
- [ ] 只下载需要精读的 PDF

Validation:
- 语义搜索需要 key 时先检查环境变量
- PDF 下载统一复用共享下载函数

## 流程 D: 情绪 + 资金联动

Checklist:
- [ ] 读取 [signals-overview.md](signals-overview.md)，拿热点和北向
- [ ] 读取 [signals-trading-structure.md](signals-trading-structure.md)，拿涨停池、炸板率、行业排名
- [ ] 必要时补分钟级个股资金流

Validation:
- 不要只看题材热度，要至少有一个资金侧信号交叉验证

Fallback:
- 分钟级资金流不稳定时，可先用板池和北向作为替代信号

## 流程 E: 全球市场联动 -> A 股映射

Checklist:
- [ ] 读取 [fundamentals-extended.md](fundamentals-extended.md)，先整理全球市场资讯和外围背景
- [ ] 明确哪些结论只是市场观察，哪些结论已经有 A 股数据验证
- [ ] 如果要落到具体 A 股板块或个股，再读取 [domain-market.md](domain-market.md) 或 [signals-overview.md](signals-overview.md)

Validation:
- 不要把“全球资讯”误写成“全球交易所级深度数据”
- A 股映射结论至少要有一个本地市场数据点支撑

Fallback:
- 如果缺少海外结构化数据，就停在“全球背景 + A 股已验证影响”这一层，不要继续猜测

## 这份文件不要承载什么

不要把 workflow 写成一堆具体实现代码。

这里只保留：
- checklist
- validation 点
- fallback
- 回跳到哪个 reference
