---
name: a-stock-data
description: A鑲″叏鏍堟暟鎹伐鍏峰寘 鈥?瑕嗙洊琛屾儏(mootdx+鑵捐+鐧惧害K绾?銆佺爺鎶?涓滆储+鍚岃姳椤?iwencai)銆佷俊鍙?鍚岃姳椤虹儹鐐?鍖楀悜+榫欒檸姒?瑙ｇ+琛屼笟)銆佽祫閲戦潰(铻嶈祫铻嶅埜+澶у畻浜ゆ槗+鑲′笢鎴锋暟+鍒嗙孩+璧勯噾娴佸垎閽熺骇+璧勯噾娴?20鏃?銆佹柊闂?涓滆储涓偂+鍏ㄧ悆璧勮)銆佸熀纭€鏁版嵁(mootdx璐㈠姟/F10+涓滆储+鏂版氮涓夎〃)銆佸叕鍛?宸ㄦ疆)銆佹墦鏉?娑ㄥ仠姹?杩炴澘姊槦/鐐告澘鐜?璺屽仠)銆丒TF鏈熸潈(T鍨嬫姤浠?甯岃厞瀛楁瘝/IV)銆佽垎鎯呬簰鍔?浜掑姩鏄撻棶绛?鐑/浜烘皵姒?鍗佸眰鏁版嵁婧愶紝鍐呭祵鍏ㄩ儴璋冪敤浠ｇ爜锛岃嚜鍖呭惈闆朵緷璧栧閮ㄦ枃浠躲€備紭鍏堢敤閫氳揪淇?mootdx)/鑵捐(涓嶅皝IP)锛屼笢璐㈡帴鍙ｅ凡鍐呯疆闄愭祦闃插皝銆傞€傜敤浜庝釜鑲′及鍊笺€佺爺鎶ユ绱€侀鏉愬綊鍥犮€侀緳铏庢璺熻釜銆佽В绂侀璀︺€佽涓氳疆鍔ㄣ€佽瀺璧勮瀺鍒歌窡韪€佺鐮佸垎鏋愩€佷骇涓氶摼璋冪爺銆佹壒閲忕瓫閫夈€佹墦鏉挎儏缁窡韪€丒TF鏈熸潈绛栫暐銆佹姇璧勮€呬簰鍔ㄩ棶绛斻€佸競鍦虹儹搴﹂€夐绛夊満鏅€?origin: custom
version: 3.3.0
---

> 馃摝 椤圭洰涓婚〉锛歨ttps://github.com/simonlin1212/a-stock-data 鈥?鏇存柊銆佸弽棣堛€佹敮鎸佷綔鑰?> 
> 浣滆€咃細Simon 鏋?路 鎶栭煶銆孲imon鏋椼€嵚?鍏紬鍙枫€岀鍩轰笘绾€?
# A鑲″叏鏍堟暟鎹伐鍏峰寘 V3.3.0

鍗佸眰鏁版嵁鏋舵瀯锛?0 涓鐐瑰疄娴嬪彲鐢紙2026-06 楠岃瘉锛涜储鑱旂ぞ蹇宸蹭笅绾匡紝璇﹁ 搂5.2锛夛紝瑕嗙洊涓绘澘/涓皬鏉?绉戝垱鏉?ST銆?
> **V3.2.3锛堣涓氱爺鎶ユ柊澧烇級锛?*
> - **搂2.1 涓滆储琛屼笟鐮旀姤 `eastmoney_industry_reports()`**锛氱爺鎶ュ眰琛ヤ笂琛屼笟鐮旀姤绔偣锛堟鍓嶅彧鏈変釜鑲＄爺鎶ワ級銆備笌涓偂鐮旀姤**鍚岀鐐?* `reportapi.eastmoney.com/report/list`锛屼粎 `qType=1`锛沗industry_code="*"` 鎷夊叏琛屼笟銆佷紶涓滆储琛屼笟鐮侊紙濡?`1238`=IT鏈嶅姟鈪★級绮剧‘杩囨护锛孭DF 澶嶇敤 `download_pdf()`锛岃蛋 `em_get` 闄愭祦銆傜鐐规暟 27 鈫?28銆?> - 瀹炴祴锛?026-06-20锛夛細鍏ㄨ涓?`hits=47928`銆佹寜琛屼笟鐮?`1238` 杩囨护 `hits=1863`锛岄绡?PDF `H3_{infoCode}_1.pdf` 涓嬭浇鎴愬姛锛?.5MB锛宍%PDF` 澶达級锛涜涓氱爜琛ㄧ鐐癸紙`bxpa` 绛夛級404 涓嶅瓨鍦紝鐢?`"*"` 鎷夊彇鍚庝粠缁撴灉鍙嶆煡琛屼笟鐮併€?
> **V3.2.2锛堝け鏁堟帴鍙ｆ浛鎹?+ 闅愯棌 Bug 淇锛夛細**
> - **搂3.3 姒傚康鏉垮潡褰掑睘锛?18锛?*锛氱櫨搴?PAE `getrelatedblock` 澶辨晥锛坄ResultCode 10003` + 绌烘暟缁勶級鈫?鏀圭敤涓滆储 `slist`锛坄spt=3`锛塦eastmoney_concept_blocks()`锛屼竴娆¤姹傛嬁鍏ㄤ釜鑲℃墍灞炴澘鍧楋紙琛屼笟/姒傚康/鍦板煙 + BK鐮?+ 娑ㄨ穼骞?+ 榫欏ご鑲★級锛岄浂閴存潈璧?`em_get` 闄愭祦銆?> - **搂7.1 宸ㄦ疆鍏憡 orgId锛?19锛?*锛氱‖缂栫爜 `gssx0{code}` 鑷村ぇ閲?601xxx 鑲＄エ `totalAnnouncement=0` 鈫?鏂板 `_cninfo_orgid()` 鍔ㄦ€佹煡瀹樻柟鏄犲皠琛?`szse_stock.json`锛?198 鍙偂锛屾ā鍧楃骇缂撳瓨锛夛紝纭紪鐮侀檷涓?fallback銆?> - **缁煎悎绀轰緥淇**锛氱ず渚嬩粛璋冪敤 v3.1 宸插垹鐨?`baidu_fund_flow_history` 鈫?鏀?`eastmoney_fund_flow_minute`銆?> - **搂4.5/搂5.1 椋庢帶璇存槑**锛氶儴鍒嗗ぇ闄嗕綇瀹?IP 琚笢璐㈤棿姝囬鎺э紙`HTTP 000`/绌猴級闈炰唬鐮?Bug锛屽姞閲嶈瘯/鎹㈢綉缁滄彁绀恒€?> - 鏂颁唬鐮佸師鏍?exec smoke test 瀹炴祴锛氭澘鍧楀綊灞?鑼呭彴27/浜旂伯娑?8/缁跨殑璋愭尝21锛涘叕鍛?骞冲畨601318/宸ヨ601398 鍘熷け鏁堣偂鎭㈠銆?>
> **V3.2.1锛圔ug 淇锛夛細** 淇涓や釜鍐呭祵鍑芥暟鐨勮В鏋愰€昏緫锛堥鍏堝瓨鍦紝闈?V3.2 寮曞叆锛夆€斺€?> - **搂5.1 涓滆储涓偂鏂伴椈**锛氫笢璐㈠疄闄呰繑鍥為噷 `result.cmsArticleWebOld` 鐩存帴灏辨槸鏂囩珷鍒楄〃锛屾棫鍐欐硶瀵?list 璋?`.get("list")` 瑙﹀彂 AttributeError / 杩斿洖绌?鈫?鏀逛负閬嶅巻 `cmsArticleWebOld` 鍒楄〃鏈韩銆?> - **搂6.4 鏂版氮璐㈡姤涓夎〃**锛氭柊娴疄闄呯粨鏋勬槸 `result.data.report_list`锛堟寜鎶ュ憡鏈熶负閿殑 dict锛屾瘡鏈?`data` 鎵嶆槸琛岄」鍒楄〃锛夛紝鏃у啓娉曞彇 `result.data.{lrb}` 姘镐箙杩斿洖绌?鈫?鏀逛负閬嶅巻 `report_list` 鏈熸銆佷粠姣忔湡 `data` 鎸?`item_title` 鎻愬彇銆?> - 涓ゅ嚱鏁板潎鐢ㄨ寘鍙?600519 鍏紑 API锛堥浂 key锛夊疄娴嬭繑鍥為潪绌恒€佸瓧娈垫纭€?>
> **V3.2锛堥槻灏?+ 澶辨晥淇锛夛細**
> - **鏁版嵁婧愪紭鍏堢骇 + 涓滆储闃插皝**锛氭槑纭€岄€氳揪淇?mootdx)/鑵捐涓嶅皝IP 浼樺厛鐢紝涓滆储浠呯敤浜庡叾鐙湁鏁版嵁銆嶅師鍒欙紱鏂板缁熶竴鑺傛祦鍏ュ彛 `em_get()`锛屾墍鏈変笢璐㈡帴鍙ｅ唴缃覆琛岄檺娴侊紙闂撮殧鈮?s+闅忔満鎶栧姩锛? 浼氳瘽澶嶇敤锛孉I 鎶勪唬鐮佸嵆鑷甫闃插皝銆傝瑙併€屾暟鎹簮浼樺厛绾?& 涓滆储闃插皝銆嶇珷鑺傘€?> - **璐㈣仈绀惧揩璁笅绾匡紙#14锛?*锛歚cls.cn` 鏃?API 鍏ㄩ潰 404锛屾爣娉ㄥ純鐢ㄥ苟鏀圭敤涓滆储鍏ㄧ悆璧勮銆?>
> **V3.1 淇锛?* 鏇挎崲 4 涓け鏁堟帴鍙ｏ紙鐧惧害 PAE 璧勯噾娴佲啋涓滆储 push2銆佸ぇ瀹椾氦鏄?RPT 鎶ヨ〃鍚嶆洿鏂般€佹満鏋勫腑浣嶆敼鐢?BUY/SELL 鏄庣粏绛涢€夛級+ 淇涓滆储鍏ㄧ悆璧勮 req_trace 鍙傛暟 + 淇宸ㄦ疆鍏憡 orgId 鏍煎紡銆?>
> **V3.0 Breaking Change**锛氬交搴曠Щ闄?akshare 渚濊禆锛屾墍鏈夋暟鎹簮鏀逛负鐩磋繛 HTTP API锛堥浂绗笁鏂规暟鎹緷璧栵紝浠?mootdx 淇濈暀 TCP锛夈€?
**浣跨敤鏂瑰紡锛?* 灏嗘湰鏂囦欢鏀惧叆 `~/.claude/skills/a-stock-data/SKILL.md`锛孋laude Code 浼氳嚜鍔ㄨ瘑鍒苟鍦?A 鑲＄浉鍏冲璇濅腑婵€娲汇€?
```
琛屾儏灞傦紙瀹炴椂锛屼笉灏両P锛?鈹溾攢鈹€ mootdx        鈫?K绾?+ 浜旀。鐩樺彛 + 閫愮瑪鎴愪氦 (TCP 7709)
鈹溾攢鈹€ 鑵捐璐㈢粡 API   鈫?PE/PB/甯傚€?鎹㈡墜鐜?娑ㄨ穼鍋?鎸囨暟/ETF (HTTP)
鈹斺攢鈹€ 鐧惧害鑲″競閫?    鈫?K绾垮甫MA5/10/20 (V3.0 鏂板锛孒TTP)

鐮旀姤灞?鈹溾攢鈹€ 涓滆储 reportapi 鈫?涓偂鐮旀姤 + 琛屼笟鐮旀姤 + PDF涓嬭浇 + 璇勭骇 + 涓夊勾EPS
鈹溾攢鈹€ 鍚岃姳椤?THS     鈫?涓€鑷撮鏈烢PS (鐩磋繛 basic.10jqka.com.cn)
鈹斺攢鈹€ iwencai        鈫?NL璇箟鎼滅储鐮旀姤 (鍞竴鑳藉姏锛岄渶X-Claw)

淇″彿灞?鈹溾攢鈹€ 鍚岃姳椤虹儹鐐?    鈫?褰撴棩寮哄娍鑲?+ 棰樻潗褰掑洜 reason tags (闆堕壌鏉?73ms)
鈹溾攢鈹€ 鍚岃姳椤哄寳鍚?    鈫?hgt/sgt 鍒嗛挓璧勯噾娴佸悜 + 鏈湴鑷紦瀛樺巻鍙?鈹溾攢鈹€ 涓滆储 slist     鈫?涓偂鎵€灞炴澘鍧?姒傚康褰掑睘 (V3.2.2 鏇挎崲鐧惧害PAE)
鈹溾攢鈹€ 涓滆储 push2     鈫?涓偂璧勯噾娴佸悜 鍒嗛挓绾?(V3.1 鏇挎崲鐧惧害PAE)
鈹溾攢鈹€ 榫欒檸姒滃腑浣?    鈫?涓婃璁板綍 + 涔板崠甯綅 TOP5 + 鏈烘瀯鍔ㄥ悜 (datacenter-web)
鈹溾攢鈹€ 鍏ㄥ競鍦洪緳铏庢   鈫?姣忔棩鍏ㄥ競鍦轰笂姒滆偂绁?+ 鍑€涔伴鎺掑悕 (datacenter-web)
鈹溾攢鈹€ 闄愬敭瑙ｇ鏃ュ巻   鈫?鍘嗗彶瑙ｇ + 鏈潵90澶╁緟瑙ｇ (datacenter-web)
鈹斺攢鈹€ 琛屼笟鏉垮潡鎺掑悕   鈫?涓滆储琛屼笟娑ㄨ穼/涓婃定涓嬭穼瀹舵暟 (V3.0 鏇挎崲鍚岃姳椤?

璧勯噾闈?/ 绛圭爜灞?鈹溾攢鈹€ 铻嶈祫铻嶅埜鏄庣粏   鈫?鏃ョ骇铻嶈祫浣欓/涔板叆/鍋胯繕 + 铻嶅埜 (datacenter-web)
鈹溾攢鈹€ 澶у畻浜ゆ槗       鈫?鎴愪氦浠?閲?+ 涔板崠鏂硅惀涓氶儴 (datacenter-web)
鈹溾攢鈹€ 鑲′笢鎴锋暟鍙樺寲   鈫?瀛ｅ害鑲′笢鎴锋暟 + 鐜瘮鍙樺寲 (datacenter-web)
鈹溾攢鈹€ 鍒嗙孩閫佽浆       鈫?鍘嗗彶姣忚偂娲炬伅/閫佽偂/杞 (datacenter-web)
鈹斺攢鈹€ 涓偂璧勯噾娴?20鏃?鈫?涓诲姏/澶у崟/涓崟/灏忓崟 鏃ョ骇鍑€娴佸叆 (push2his)

鏂伴椈灞?鈹溾攢鈹€ 涓滆储涓偂鏂伴椈   鈫?涓偂鐩稿叧鏂伴椈 (search-api-web JSONP)
鈹溾攢鈹€ 璐㈣仈绀惧揩璁?    鈫?鈿狅笍 宸蹭笅绾?(cls.cn 杩?Next.js锛屾棫API 404)
鈹斺攢鈹€ 涓滆储鍏ㄧ悆璧勮   鈫?7脳24 璐㈢粡蹇 (np-weblist锛岃储鑱旂ぞ鏇夸唬)

鍩虹鏁版嵁灞?鈹溾攢鈹€ mootdx finance 鈫?瀛ｆ姤蹇収 (37瀛楁, EPS/ROE/鍑€鍒?
鈹溾攢鈹€ mootdx F10     鈫?鍏徃璧勬枡 (9澶х被鏂囨湰)
鈹溾攢鈹€ 涓滆储涓偂淇℃伅   鈫?琛屼笟/鎬昏偂鏈?娴侀€氳偂/甯傚€?涓婂競鏃ユ湡 (push2)
鈹斺攢鈹€ 鏂版氮璐㈡姤涓夎〃   鈫?璧勪骇璐熷€鸿〃/鍒╂鼎琛?鐜伴噾娴侀噺琛?(quotes.sina.cn)

鍏憡灞?鈹溾攢鈹€ 宸ㄦ疆 cninfo    鈫?鍏憡鍏ㄦ枃妫€绱?涓嬭浇 (cninfo.com.cn)
鈹斺攢鈹€ mootdx F10     鈫?鏈€鏂板叕鍛婃憳瑕?
鎵撴澘灞?(V3.3 鏂板)
鈹溾攢鈹€ 涓滆储娑ㄥ仠姹?    鈫?杩炴澘鏁?鍑犲ぉ鍑犳澘/灏佹澘璧勯噾/鐐告澘娆℃暟/琛屼笟 (push2ex)
鈹溾攢鈹€ 涓滆储鐐告澘姹?    鈫?娑ㄥ仠鍚庡紑鏉?+ 鎸箙/娑ㄩ€?(push2ex)
鈹溾攢鈹€ 涓滆储璺屽仠姹?    鈫?灏佸崟璧勯噾/杩炵画璺屽仠/寮€鏉挎鏁?(push2ex)
鈹溾攢鈹€ 涓滆储鏄ㄦ定鍋滄睜   鈫?鏄ㄦ定鍋滀粖琛ㄧ幇锛岀畻鏅嬬骇鐜?璧氶挶鏁堝簲 (push2ex)
鈹斺攢鈹€ 鍚岃姳椤烘定鍋滄彮绉?鈫?娑ㄥ仠鍘熷洜棰樻潗/灏佹澘鎴愬姛鐜?鏉垮瀷 (10jqka)

ETF鏈熸潈灞?(V3.3 鏂板)
鈹溾攢鈹€ 鍚堢害娓呭崟       鈫?50ETF/300ETF/绉戝垱50/500ETF 鍚勬湀璁よ喘璁ゆ步 (鏂版氮)
鈹溾攢鈹€ T鍨嬫姤浠?       鈫?涔板崠浜旀。/鎸佷粨閲?琛屾潈浠?鏈€鏂颁环 (鏂版氮)
鈹斺攢鈹€ 甯岃厞瀛楁瘝+IV    鈫?Delta/Gamma/Theta/Vega/闅愬惈娉㈠姩鐜?(鏂版氮)

鑸嗘儏浜掑姩灞?(V3.3 鏂板)
鈹溾攢鈹€ 浜掑姩鏄撻棶绛?    鈫?鎶曡祫鑰呮彁闂?鍏徃鍥炲 (宸ㄦ疆锛孉I闂瓟鐙)
鈹溾攢鈹€ 鍚岃姳椤虹儹姒?    鈫?浜烘皵鍊?姒傚康鏍囩/鎺掑悕鍙樺寲 (10jqka)
鈹溾攢鈹€ 涓滆储浜烘皵姒?    鈫?鎺掑悕+鎺掑悕鍙樺寲+鍚嶇О浠锋牸 (emappdata)
鈹斺攢鈹€ 涓滆储姒傚康鍛戒腑   鈫?涓偂琚綊鍒板摢浜涙蹇靛湪鐐?鐑害 (emappdata)
```

## 鏁版嵁婧愪紭鍏堢骇 & 涓滆储闃插皝锛堥噸瑕侊紝鍏堣锛?
### 浼樺厛绾у師鍒欙細鑳界敤閫氳揪淇?鑵捐锛屽氨鍒敤涓滆储

| 浼樺厛绾?| 鏁版嵁婧?| 鍗忚 | 灏?IP 椋庨櫓 | 瑕嗙洊 |
|--------|--------|------|-----------|------|
| **1锛堥閫夛級** | **mootdx锛堥€氳揪淇★級** | TCP 7709 浜岃繘鍒?| **涓嶅皝 IP** | K绾裤€佷簲妗ｇ洏鍙ｃ€侀€愮瑪鎴愪氦銆佽储鍔″揩鐓с€丗10 |
| **2** | **鑵捐璐㈢粡** | HTTP GBK | **涓嶅皝 IP** | 瀹炴椂浠枫€丳E/PB/甯傚€?鎹㈡墜鐜?娑ㄨ穼鍋溿€佹寚鏁般€丒TF |
| **3** | 鏂版氮 / 宸ㄦ疆 / 鍚岃姳椤?| HTTP | 浣?| 璐㈡姤涓夎〃銆佸叕鍛娿€佷竴鑷撮鏈?鐑偣 |
| **4锛堜粎鐙湁鏁版嵁鎵嶇敤锛?* | **涓滆储 eastmoney** | HTTP | **鏈夐鎺э紝浼氬皝 IP** | 瑙佷笅 |

**鍑℃槸琛屾儏 / K绾?/ 瀹炴椂浠?/ 甯傚€?/ 璐㈠姟涓夎〃鑳戒粠 mootdx 鎴栬吘璁嬁鍒扮殑锛屼竴寰嬭蛋瀹冧滑**鈥斺€擳CP 鍗忚鍜岃吘璁帴鍙ｅ疄娴嬩笉灏?IP锛屽彲鏀惧績楂橀璋冪敤銆?
### 涓滆储鍙敤浜庡畠銆岀嫭鏈夈€佸埆澶勬嬁涓嶅埌銆嶇殑鏁版嵁

涓嬪垪鏁版嵁**鍙湁涓滆储鏈?*锛岄€氳揪淇?鑵捐/鏂版氮閮芥病鏈夛紝蹇呴』鐢ㄤ笢璐紙浣嗚闄愭祦锛夛細

> 榫欒檸姒滃腑浣?路 鍏ㄥ競鍦洪緳铏庢 路 闄愬敭瑙ｇ鏃ュ巻 路 铻嶈祫铻嶅埜 路 澶у畻浜ゆ槗 路 鑲′笢鎴锋暟 路 鍒嗙孩閫佽浆 路 涓偂璧勯噾娴佸悜锛堝垎閽?鏃ョ骇锛壜?琛屼笟鏉垮潡鎺掑悕 路 鐮旀姤鍒楄〃/PDF 路 涓偂鏂伴椈 路 鍏ㄧ悆璧勮

### 涓滆储椋庢帶闃堝€硷紙绀惧尯瀹炴祴锛?026-05锛?
| 琛屼负 | 瑙﹀彂灏佺鐨勯槇鍊?| 椋庨櫓 |
|------|---------------|------|
| 姣忕璇锋眰鏁?| > 5 娆?绉?| 楂?|
| 鍗?IP 骞跺彂杩炴帴 | 鈮?10 | 楂?|
| 1 鍒嗛挓璇锋眰鎬绘暟 | 鈮?200 娆?| 涓珮 |
| 5 鍒嗛挓璇锋眰鎬绘暟 | 鈮?300 娆?| 瑙﹀彂灏佺 |
| User-Agent | 绌?UA / 鏃犳祻瑙堝櫒鐗瑰緛 | 涓?|

琚皝琛ㄧ幇锛氳繛缁姹傚悗 `403` / `429` / 杩炴帴瓒呮椂 / 杩斿洖绌烘暟鎹€備复鏃跺皝绂侀€氬父鍑犲垎閽熷埌鍑犲皬鏃躲€?
### 闃插皝閾佸緥锛堣皟鐢ㄤ笢璐㈡椂蹇呴』閬靛畧锛?
1. **涓茶锛屼笉骞跺彂**鈥斺€旂粷涓嶅涓滆储寮€澶氱嚎绋?鍗忕▼骞跺彂璇锋眰
2. **姣忔闂撮殧 鈮?1 绉?+ 闅忔満鎶栧姩**锛圦PS 鈮?2锛夛紝鎵归噺绛涢€夋椂璋冨ぇ鍒?1.5~2 绉?3. **澶嶇敤 HTTP 浼氳瘽**锛圞eep-Alive锛夛紝涓嶈姣忔鏂板缓杩炴帴
4. **甯︽甯?UA + Referer**锛堟湰 SKILL 鍚勭鐐瑰凡閰嶅ソ锛?5. **鎵归噺鍦烘櫙姣忓彧鑲＄エ涔嬮棿 sleep**鈥斺€擜I 璺戞壒閲忓惊鐜紙濡傜瓫閫?100 鍙偂閫愪釜鎷夐緳铏庢/璧勯噾娴侊級鏄灏佺殑澶村彿鍏冨嚩

### 宸插唴缃檺娴侊細鎵€鏈変笢璐㈣姹傝蛋 `em_get()`

鏈?SKILL 鎻愪緵缁熶竴鐨勮妭娴佸叆鍙?`em_get()`锛堝畾涔夎涓嬫柟銆屼笢璐㈡暟鎹腑蹇冪粺涓€鏌ヨ锛堝叡鐢?helper锛夈€嶏級锛屽畠鑷姩鍋氬埌锛氫覆琛岄檺娴侊紙鏈€灏忛棿闅?`EM_MIN_INTERVAL=1.0s` + 闅忔満鎶栧姩锛? 澶嶇敤 `EM_SESSION`锛圞eep-Alive锛? 榛樿 UA銆?*鎵€鏈?`eastmoney.com` 绔偣鐨勪唬鐮佸潡閮藉凡鏀圭敤 `em_get` 鑰岄潪瑁?`requests.get`**锛孉I 鐩存帴鎶勪唬鐮佸嵆鑷甫闃插皝銆傛壒閲忎换鍔℃妸 `EM_MIN_INTERVAL` 璋冨ぇ鍗冲彲杩涗竴姝ラ檷閫熴€?
> 娉細`em_get` / `EM_SESSION` / `EM_MIN_INTERVAL` 鏄墍鏈変笢璐唬鐮佸潡鍏辩敤鐨勫墠缃畾涔夛紝浣跨敤浠讳竴涓滆储绔偣鍓嶉渶鍏堟墽琛屻€屽叡鐢?helper銆嶄唬鐮佸潡銆?
---

## When to Activate

- 鐢ㄦ埛瑕佹煡 A 鑲′釜鑲′及鍊硷紙涓€鑷撮鏈?/ PE / PEG / PE娑堝寲锛?- 鐢ㄦ埛瑕佹媺瀹炴椂琛屾儏锛堜环鏍?/ 浜旀。鐩樺彛 / K绾?/ 娑ㄨ穼鍋滀环锛?- 鐢ㄦ埛瑕佹悳鐮旀姤锛堟寜涓婚 / 鎸夋爣鐨?/ 鎸夎涓?/ 涓嬭浇PDF锛?- 鐢ㄦ埛瑕佺湅**褰撴棩寮哄娍鑲?/ 棰樻潗褰掑洜 / 姒傚康鐑偣**
- 鐢ㄦ埛瑕佺湅**鍖楀悜璧勯噾鍔ㄥ悜**锛堟勃鑲￠€?娣辫偂閫氬垎閽熸祦鍚戯級
- 鐢ㄦ埛瑕佺湅**姒傚康鏉垮潡褰掑睘**锛堣涓?姒傚康/鍦板煙锛?- 鐢ㄦ埛瑕佺湅**涓偂璧勯噾娴佸悜**锛堜富鍔?鏁ｆ埛/瓒呭ぇ鍗?澶у崟鍒嗛挓绾э級
- 鐢ㄦ埛瑕佺湅**榫欒檸姒滃腑浣?*锛堣惀涓氶儴 + 鏈烘瀯涔板崠锛?- 鐢ㄦ埛瑕佺湅**鍏ㄥ競鍦洪緳铏庢**锛堝綋鏃ユ墍鏈変笂姒滆偂绁?+ 鍑€涔伴鎺掑悕锛?- 鐢ㄦ埛瑕佺湅**闄愬敭瑙ｇ鏃ュ巻**锛堝巻鍙茶В绂?+ 鏈潵寰呰В绂侊級
- 鐢ㄦ埛瑕佸仛**琛屼笟妯悜瀵规瘮**锛堟定璺屾帓鍚?/ 璧勯噾娴佸叆 / 棰嗘定鑲★級
- 鐢ㄦ埛瑕佺湅**铻嶈祫铻嶅埜 / 涓よ瀺鏁版嵁**锛堣瀺璧勪綑棰?+ 铻嶅埜浣欓锛?- 鐢ㄦ埛瑕佺湅**澶у畻浜ゆ槗**锛堟垚浜や环/閲?+ 涔板崠鏂硅惀涓氶儴锛?- 鐢ㄦ埛瑕佺湅**鑲′笢鎴锋暟鍙樺寲**锛堢鐮侀泦涓害锛?- 鐢ㄦ埛瑕佺湅**鍒嗙孩閫佽浆鍘嗗彶**锛堟瘡鑲℃淳鎭?+ 閫佽偂 + 杞锛?- 鐢ㄦ埛瑕佺湅**鎸囨暟/ETF琛屾儏**锛堜笂璇佹寚鏁?/ 娌繁300 / 鍒涗笟鏉挎寚 / ETF锛?- 鐢ㄦ埛瑕佺湅**娑ㄥ仠 / 鎵撴澘鎯呯华**锛堟定鍋滄睜 / 杩炴澘姊槦 / 鐐告澘鐜?/ 璺屽仠 / 娑ㄥ仠鍘熷洜棰樻潗锛?- 鐢ㄦ埛瑕佺湅**ETF 鏈熸潈**锛圱鍨嬫姤浠?/ 甯岃厞瀛楁瘝 Delta路Gamma路Theta路Vega / 闅愬惈娉㈠姩鐜?IV锛?- 鐢ㄦ埛瑕佺湅**鎶曡祫鑰呬簰鍔ㄩ棶绛?*锛堝叕鍙稿浣曞洖搴旀煇浼犻椈/鍒╁ソ 路 浜掑姩鏄擄級
- 鐢ㄦ埛瑕佺湅**甯傚満鐑害 / 浜烘皵姒?*锛堝悓鑺遍『鐑 / 涓滆储浜烘皵姒?/ 涓偂姒傚康鍛戒腑锛?- 鐢ㄦ埛瑕佺湅鏂伴椈璧勮锛堜釜鑲℃柊闂?/ 璐㈣仈绀惧揩璁?/ 鍏ㄧ悆璧勮锛?- 鐢ㄦ埛瑕佹煡鍏憡锛堝法娼叕鍛婂叏鏂囷級
- 鐢ㄦ埛瑕佸仛浜т笟閾捐皟鐮?/ 鎵归噺妯悜瀵规瘮
- 鍏抽敭璇嶏細浼板€笺€佷竴鑷撮鏈熴€佹満鏋勯娴嬨€佸競鐩堢巼銆丳EG銆佸競鍊笺€佺爺鎶ャ€佷骇涓氶摼銆佽涓氱爺绌躲€並绾裤€佺洏鍙ｃ€佸叕鍛娿€佹柊闂汇€?*寮哄娍鑲°€侀鏉愩€佺儹鐐广€佹蹇靛綊鍥犮€佸寳鍚戣祫閲戙€佹勃鑲￠€氥€佹繁鑲￠€氥€佹蹇垫澘鍧椼€佽祫閲戞祦鍚戙€佷富鍔涖€侀緳铏庢銆佸腑浣嶃€佽惀涓氶儴銆佸叏甯傚満榫欒檸姒溿€佸噣涔板叆銆佽В绂併€侀檺鍞€佽涓氬姣斻€佽涓氳疆鍔ㄣ€佽瀺璧勮瀺鍒搞€佷袱铻嶃€佸ぇ瀹椾氦鏄撱€佽偂涓滄埛鏁般€佺鐮侀泦涓€佸垎绾€佹淳鎭€侀€佽偂銆佹寚鏁般€丒TF銆佹定鍋溿€佹墦鏉裤€佽繛鏉裤€佺偢鏉裤€佽穼鍋溿€佹定鍋滃師鍥犮€佸皝鏉裤€佹檵绾х巼銆丒TF鏈熸潈銆佸笇鑵婂瓧姣嶃€侀殣鍚尝鍔ㄧ巼銆佷簰鍔ㄦ槗銆佹姇璧勮€呭叧绯汇€佺儹姒溿€佷汉姘旀銆佸競鍦虹儹搴?*

---

## Prerequisites

```bash
pip install mootdx requests pandas stockstats
```

| 渚濊禆 | 鐗堟湰瑕佹眰 | 鐢ㄩ€?|
|------|---------|------|
| mootdx | >= 0.10 | TCP琛屾儏+璐㈠姟+F10锛堝敮涓€闈濰TTP渚濊禆锛夛紱0.11.x 鐢?`tdx_client()` 瑙勯伩 BESTIP bug锛岃涓婅妭 |
| requests | any | 鎵€鏈塇TTP API鐩磋繛 |
| pandas | any | 鏁版嵁澶勭悊+HTML琛ㄦ牸瑙ｆ瀽 |
| stockstats | any | 鎶€鏈寚鏍囪绠楋紙RSI/MACD/BOLL绛夛級 |

> **V3.0 鏋舵瀯锛?* 闄?mootdx锛圱CP 浜岃繘鍒跺崗璁級澶栵紝鎵€鏈夋暟鎹簮鍧囦负鐩磋繛 HTTP API锛岄浂绗笁鏂规暟鎹皝瑁呬緷璧栥€傛瘡涓鐐圭殑搴曞眰 URL/鍙傛暟瀹屽叏鏆撮湶锛屾柟渚胯皟璇曞拰瀹氬埗銆?
### iwencai API Key锛堜粎璇箟鎼滅储闇€瑕侊級

```bash
# 鐜鍙橀噺鏂瑰紡
export IWENCAI_API_KEY="your_key_here"
export IWENCAI_BASE_URL="https://openapi.iwencai.com"

# 鐢宠鍦板潃: https://www.iwencai.com/skillhub
# 娉ㄥ唽鍚庡畨瑁?SkillHub CLI锛屽啀瀹夎 report-search 鎶€鑳藉嵆鍙幏寰?Key
```

鍏朵粬鏁版嵁婧愶紙mootdx / 鑵捐 / 涓滆储 / 鍚岃姳椤?/ 鐧惧害鑲″競閫?/ 鏂版氮 / 宸ㄦ疆锛夊叏閮ㄥ厤璐癸紝鏃犻渶 key銆?
### mootdx 瀹㈡埛绔紙蹇呰锛岃閬?0.11.x BESTIP 绌轰覆 bug锛?
> **宸茬煡 bug锛坢ootdx 0.11.x锛夛細** 鍏ㄦ柊瀹夎鍚?`Quotes.factory(market='std')` 瑁歌皟鐢ㄥ彲鑳芥姏 `ValueError: not enough values to unpack (expected 2, got 0)`銆?> 鏍瑰洜锛歚~/.mootdx/config.json` 鐨?`BESTIP.HQ` 鍒濆鏄┖瀛楃涓?`""`锛堜笉鏄己澶遍敭锛夛紝mootdx 鐢?`dict.get(key, default)` 鍙栦笉鍒?default锛屾媶鍖呭け璐ャ€?*鑰佺敤鎴凤紙config 鏇惧～鍏呰繃 IP锛変笉浼氳Е鍙戯紝鎵€浠ュ鏄撴紡娴嬨€?*
> **涓嶈闈犻攣鐗堟湰瑙ｅ喅锛?* 閿?`mootdx==0.10.12` 鍦ㄩ儴鍒嗙幆澧冿紙濡傚共鍑€鐨?Python 3.9锛変笅 `import mootdx` 浼氬洜 numpy/pandas 浜岃繘鍒朵笉鍏煎鐩存帴宕┿€傛纭仛娉曟槸鐢ㄤ笅闈㈢殑 `tdx_client()`鈥斺€旀樉寮忎紶 server 缁曡繃 BESTIP锛屽 0.10 / 0.11 閮介€傜敤銆?
**缁熶竴鐢ㄤ互涓?helper 鍒涘缓瀹㈡埛绔紙鎵€鏈?mootdx 璋冪敤閮借蛋瀹冿級锛?*

```python
import socket
from mootdx.quotes import Quotes

# 瀹炴祴鍙敤鐨勫閫夋湇鍔″櫒锛堟寜寤惰繜鎺掑簭锛?026-06 楠岃瘉锛?_TDX_SERVERS = [
    ('119.97.185.59', 7709), ('124.70.133.119', 7709), ('116.205.183.150', 7709),
    ('123.60.73.44', 7709),  ('116.205.163.254', 7709), ('121.36.225.169', 7709),
    ('123.60.70.228', 7709), ('124.71.9.153', 7709),    ('110.41.147.114', 7709),
    ('124.71.187.122', 7709),
]

def _probe(ip, port, timeout=2.0):
    """TCP 鎻℃墜鎺㈡祴锛屽垽鏂湇鍔″櫒鏄惁鍙揪"""
    try:
        with socket.create_connection((ip, port), timeout=timeout):
            return True
    except Exception:
        return False

def tdx_client(market='std'):
    """
    鍒涘缓 mootdx 瀹㈡埛绔紝瑙勯伩 0.11.x BESTIP.HQ 绌轰覆 bug銆?    椤哄簭鍏滃簳锛屼繚璇?IP 鍒楄〃鑰佸寲/鎹㈢綉鏃朵粛鑳藉伐浣滐細
      1) 椤哄簭鎺㈡祴 _TDX_SERVERS锛岀敤绗竴涓?TCP 鍙揪鐨勬樉寮?server锛?      2) 鍏ㄩ儴涓嶅彲杈?鈫?鍥為€€ mootdx 鑷甫 bestip 娴嬮€熼€変紭锛?      3) 鍐嶄笉琛?鈫?鍥為€€瑁?factory锛堣€佺敤鎴?config 宸叉湁鍙敤 BESTIP 鏃舵垚绔嬶級锛?      4) 浠嶅け璐?鈫?鎶?RuntimeError锛屾槑纭姤閿欒€岄潪姝荤瓑銆?    """
    for ip, port in _TDX_SERVERS:
        if _probe(ip, port):
            return Quotes.factory(market=market, server=(ip, port))
    try:
        return Quotes.factory(market=market, bestip=True)   # fallback 1
    except Exception:
        pass
    try:
        return Quotes.factory(market=market)                # fallback 2
    except Exception as e:
        raise RuntimeError(
            "鎵€鏈?mootdx 鏈嶅姟鍣ㄥ潎涓嶅彲杈俱€傛捣澶栫綉缁滈€氬父鍏ㄩ儴瓒呮椂锛圱CP 7709锛夛紝"
            "璇疯蛋鍥藉唴浠ｇ悊鎴栨洿鏂?_TDX_SERVERS 鍒楄〃銆傚師濮嬮敊璇細%s" % e
        )

# 鐢ㄦ硶锛歝lient = tdx_client()   # 鏇夸唬鎵€鏈?Quotes.factory(market='std')
```

> **娴峰 IP 鐢ㄦ埛锛?* mootdx 璧伴€氳揪淇?TCP 7709锛屾捣澶栫幆澧冮€氬父鍏ㄩ儴瓒呮椂銆俙tdx_client()` 浼氬揩閫熷け璐ョ粰鍑烘槑纭姤閿欙紝鑰岄潪姝荤瓑銆?
### 甯傚満鍓嶇紑瑙勫垯锛堝叏灞€閫氱敤锛?
```python
def get_prefix(code: str) -> str:
    """6浣嶄唬鐮?鈫?甯傚満鍓嶇紑"""
    if code.startswith(("6", "9")):
        return "sh"
    elif code.startswith("8"):
        return "bj"
    else:
        return "sz"
```

### Ticker 鏍煎紡褰掍竴鍖?
鎵€鏈夋帴鍙ｇ粺涓€鏀寔澶氱杈撳叆鏍煎紡锛屽唴閮ㄥ綊涓€鍖栦负绾?6 浣嶆暟瀛楋細

| 杈撳叆 | 褰掍竴鍖栫粨鏋?|
|------|-----------|
| `688017` | `688017` |
| `SH688017` / `sh688017` | `688017` |
| `688017.SH` / `688017.sh` | `688017` |
| `SZ000001` | `000001` |
| `BJ832000` | `832000` |

### 涓滆储鏁版嵁涓績缁熶竴鏌ヨ锛堝叡鐢?helper锛?
榫欒檸姒?瑙ｇ/铻嶈祫铻嶅埜/澶у畻浜ゆ槗/鑲′笢鎴锋暟/鍒嗙孩 鍏辩敤鍚屼竴 base URL锛?
```python
import time
import random
import requests

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
DATACENTER_URL = "https://datacenter-web.eastmoney.com/api/data/v1/get"

# 鈹€鈹€ 涓滆储闃插皝锛氬叏灞€鑺傛祦 + 浼氳瘽澶嶇敤 鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€
# 涓滆储绯?HTTP 鎺ュ彛锛坧ush2 / datacenter / reportapi / search / np-weblist锛夋湁椋庢帶锛?#   姣忕 >5 娆?/ 鍗?IP 骞跺彂 鈮?0 / 1 鍒嗛挓 鈮?00 娆? 鈫? 涓存椂灏?IP銆?# 鎵€鏈?eastmoney.com 璇锋眰涓€寰嬭蛋 em_get()锛氫覆琛岄檺娴侊紙鏈€灏忛棿闅?+ 闅忔満鎶栧姩锛? 澶嶇敤
# Keep-Alive 浼氳瘽锛屾壒閲忚皟鐢ㄦ椂鑷姩闄嶉€燂紝閬垮厤琚皝銆傝瑙併€屾暟鎹簮浼樺厛绾?& 涓滆储闃插皝銆嶇珷鑺傘€?EM_SESSION = requests.Session()
EM_SESSION.headers.update({"User-Agent": UA})
# 杩炴帴绾ц嚜鍔ㄩ噸璇曪細鐬€佽繛鎺ラ敊璇?/ 429 / 5xx 鎸囨暟閫€閬块噸璇曪紙浣忓畢IP鍋跺彂椋庢帶鏇寸ǔ锛夈€?# 娉ㄦ剰锛?03 涓嶉噸璇曪紙涓滆储椋庢帶淇″彿锛岄噸璇曟棤鐩婂弽鑰屽姞閲嶏紱鎸変笅鏂?EM_MIN_INTERVAL 闄嶉搴斿锛夈€?try:
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
    _em_adapter = HTTPAdapter(max_retries=Retry(
        total=3, connect=3, backoff_factor=0.6,
        status_forcelist=[429, 500, 502, 503, 504], allowed_methods=["GET"]))
    EM_SESSION.mount("https://", _em_adapter)
    EM_SESSION.mount("http://", _em_adapter)
except Exception:
    pass  # 鑰佺増鏈?urllib3 缂?allowed_methods 绛夊弬鏁版椂闄嶇骇涓烘棤閲嶈瘯锛屼笉褰卞搷涓绘祦绋?EM_MIN_INTERVAL = 1.0          # 涓ゆ涓滆储璇锋眰鏈€灏忛棿闅?绉?锛涙壒閲忕瓫閫夊缓璁皟澶у埌 1.5~2
_em_last_call = [0.0]          # 妯″潡绾т笂娆¤姹傛椂闂存埑

def em_get(url: str, params: dict | None = None, headers: dict | None = None,
           timeout: int = 15, **kwargs):
    """涓滆储缁熶竴璇锋眰鍏ュ彛锛氳嚜鍔ㄨ妭娴?+ 澶嶇敤 session + 榛樿 UA銆?    鎵€鏈?eastmoney.com 鎺ュ彛閮藉簲閫氳繃瀹冭姹傦紝閬垮厤楂橀琚皝 IP銆?""
    wait = EM_MIN_INTERVAL - (time.time() - _em_last_call[0])
    if wait > 0:
        time.sleep(wait + random.uniform(0.1, 0.5))
    try:
        return EM_SESSION.get(url, params=params, headers=headers, timeout=timeout, **kwargs)
    finally:
        _em_last_call[0] = time.time()

def eastmoney_datacenter(report_name: str, columns: str = "ALL",
                          filter_str: str = "", page_size: int = 50,
                          sort_columns: str = "", sort_types: str = "-1") -> list[dict]:
    """涓滆储鏁版嵁涓績缁熶竴鏌ヨ 鈥?榫欒檸姒?瑙ｇ/铻嶈祫铻嶅埜/澶у畻浜ゆ槗/鑲′笢鎴锋暟/鍒嗙孩 鍏辩敤锛堝凡鍐呯疆闄愭祦锛?""
    params = {
        "reportName": report_name, "columns": columns,
        "filter": filter_str, "pageNumber": "1", "pageSize": str(page_size),
        "sortColumns": sort_columns, "sortTypes": sort_types,
        "source": "WEB", "client": "WEB",
    }
    r = em_get(DATACENTER_URL, params=params, timeout=15)
    d = r.json()
    if d.get("result") and d["result"].get("data"):
        return d["result"]["data"]
    return []
```

---

## Layer 1: 琛屾儏灞傦紙瀹炴椂锛屼笉灏両P锛?
### 1.1 mootdx 鈥?K绾?+ 浜旀。鐩樺彛 + 閫愮瑪鎴愪氦

TCP 浜岃繘鍒跺崗璁紝杩為€氳揪淇℃湇鍔″櫒(7709)锛屾棤闇€娉ㄥ唽锛屼笉灏両P銆?
```python
from mootdx.quotes import Quotes

client = tdx_client()  # 瑙?Prerequisites 鐨?tdx_client() helper锛堣閬?0.11.x BESTIP bug锛涚瓑浠?Quotes.factory(market='std')锛?
# === K绾挎暟鎹?===
# 鈿狅笍 鍙傛暟鍚嶆槸 frequency锛堜笉鏄?category锛佷紶 category 浼氳 **kwargs 闈欓粯鍚炴帀锛?#    姘歌繙閫€鍖栨垚榛樿 frequency=9 鏃ョ嚎锛屾嬁涓嶅埌鍒嗛挓鏁版嵁锛夈€?# mootdx 0.11.7 瀹炴祴棰戠巼鍊艰〃锛?#   0=5鍒嗛挓  1=15鍒嗛挓  2=30鍒嗛挓  3=60鍒嗛挓(1灏忔椂)  4=鏃ョ嚎  5=鍛ㄧ嚎  6=鏈堢嚎
#   8=1鍒嗛挓  9=鏃ョ嚎(榛樿)  10=瀛ｇ嚎  11=骞寸嚎        锛?=1鍒嗛挓闄ゆ潈鍙ｅ緞,灏戠敤锛?klines = client.bars(symbol='688017', frequency=9, offset=10)    # 鏃ョ嚎
min1   = client.bars(symbol='688017', frequency=8, offset=240)   # 1鍒嗛挓锛堜竴涓氦鏄撴棩鈮?40鏍癸級
min5   = client.bars(symbol='688017', frequency=0, offset=48)    # 5鍒嗛挓
# 杩斿洖: open, close, high, low, vol, amount, datetime
# 鈿狅笍 澶嶆潈锛歜ars 杩斿洖銆愪笉澶嶆潈銆戝師濮嬩环锛堥€氳揪淇″師濮嬫暟鎹紝鏃?adjust 鍙傛暟锛夈€?#    璺ㄩ櫎鏉冮櫎鎭棩鍋氫及鍊?鍥炴祴鍓嶉渶鑷澶嶆潈锛屾垨鏀圭敤甯﹀墠澶嶆潈鐨勬棩K鏁版嵁婧愶紙鑵捐璐㈢粡锛夈€?
# === 瀹炴椂鎶ヤ环 ===
quotes = client.quotes(symbol=['688017', '300476'])
# 杩斿洖 46 涓瓧娈?
#   price(鐜颁环), open, high, low, last_close(鏄ㄦ敹)
#   bid1~bid5, ask1~ask5, bid_vol1~bid_vol5, ask_vol1~ask_vol5
#   vol(鎴愪氦閲?, amount(鎴愪氦棰?, servertime

# === 閫愮瑪鎴愪氦锛堥潪浜ゆ槗鏃堕棿杩斿洖绌猴級===
trades = client.transaction(symbol='688017', date='20260502')
# 杩斿洖: time, price, vol, num, buyorsell(0涔?1鍗?2涓€?
```

**mootdx 涓嶆彁渚?PE / PB / 甯傚€?/ 鎹㈡墜鐜?/ 娑ㄨ穼鍋滀环** 鈥?杩欎簺璧拌吘璁储缁忋€?
### 1.2 鑵捐璐㈢粡 API 鈥?PE/PB/甯傚€?鎹㈡墜鐜?娑ㄨ穼鍋?鎸囨暟/ETF

HTTP GET锛孏BK 缂栫爜锛宍~` 鍒嗛殧 88 涓瓧娈碉紝涓嶅皝IP銆?
```python
import urllib.request

def tencent_quote(codes: list[str]) -> dict[str, dict]:
    """
    鎵归噺鎷夊彇鑵捐璐㈢粡瀹炴椂琛屾儏銆?    codes: ["688017", "300476", "002463"]
    涔熸敮鎸佹寚鏁? ["000001", "000300", "399006"]
    涔熸敮鎸丒TF: ["510050", "510300"]
    杩斿洖: {code: {name, price, pe_ttm, pb, mcap, ...}}
    """
    prefixed = []
    for c in codes:
        if c.startswith(("6", "9")):
            prefixed.append(f"sh{c}")
        elif c.startswith("8"):
            prefixed.append(f"bj{c}")
        else:
            prefixed.append(f"sz{c}")

    url = "https://qt.gtimg.cn/q=" + ",".join(prefixed)
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0")
    resp = urllib.request.urlopen(req, timeout=10)
    data = resp.read().decode("gbk")

    result = {}
    for line in data.strip().split(";"):
        if not line.strip() or "=" not in line or '"' not in line:
            continue
        key = line.split("=")[0].split("_")[-1]
        vals = line.split('"')[1].split("~")
        if len(vals) < 53:
            continue
        code = key[2:]
        result[code] = {
            "name":         vals[1],
            "price":        float(vals[3]) if vals[3] else 0,
            "last_close":   float(vals[4]) if vals[4] else 0,
            "open":         float(vals[5]) if vals[5] else 0,
            "change_amt":   float(vals[31]) if vals[31] else 0,
            "change_pct":   float(vals[32]) if vals[32] else 0,
            "high":         float(vals[33]) if vals[33] else 0,
            "low":          float(vals[34]) if vals[34] else 0,
            "amount_wan":   float(vals[37]) if vals[37] else 0,
            "turnover_pct": float(vals[38]) if vals[38] else 0,
            "pe_ttm":       float(vals[39]) if vals[39] else 0,
            "amplitude_pct":float(vals[43]) if vals[43] else 0,
            "mcap_yi":      float(vals[44]) if vals[44] else 0,
            "float_mcap_yi":float(vals[45]) if vals[45] else 0,
            "pb":           float(vals[46]) if vals[46] else 0,
            "limit_up":     float(vals[47]) if vals[47] else 0,
            "limit_down":   float(vals[48]) if vals[48] else 0,
            "vol_ratio":    float(vals[49]) if vals[49] else 0,
            "pe_static":    float(vals[52]) if vals[52] else 0,
        }
    return result

# 鐢ㄦ硶: 涓偂
quotes = tencent_quote(["688017", "300476", "002463"])
for code, q in quotes.items():
    print(f"{q['name']}({code}): {q['price']}鍏?PE={q['pe_ttm']} PB={q['pb']} 甯傚€?{q['mcap_yi']}浜?)

# 鐢ㄦ硶: 鎸囨暟 鈥?sh000001=涓婅瘉鎸囨暟, sh000300=娌繁300, sz399006=鍒涗笟鏉挎寚
index_quotes = tencent_quote(["000001", "000300", "399006"])

# 鐢ㄦ硶: ETF 鈥?sh510050=涓婅瘉50ETF, sh510300=娌繁300ETF
etf_quotes = tencent_quote(["510050", "510300"])
```

#### 鑵捐璐㈢粡瀛楁绱㈠紩閫熸煡锛堝疄娴嬫牎鍑?2026-05-03锛?
| 绱㈠紩 | 鍚箟 | 绀轰緥 |
|------|------|------|
| 1 | 鍚嶇О | 缁跨殑璋愭尝 |
| 3 | 褰撳墠浠?| 224.12 |
| 4 | 鏄ㄦ敹 | 215.01 |
| 5 | 浠婂紑 | 214.10 |
| 9-18 | 涔颁竴~涔颁簲(浠?閲? | |
| 19-28 | 鍗栦竴~鍗栦簲(浠?閲? | |
| 31 | 娑ㄨ穼棰?| 9.11 |
| 32 | 娑ㄨ穼骞? | 4.24 |
| 33 | 鏈€楂?| 229.62 |
| 34 | 鏈€浣?| 214.10 |
| 37 | 鎴愪氦棰?涓? | 187040 |
| 38 | 鎹㈡墜鐜? | 4.55 |
| **39** | **PE(TTM)** | 300.45 |
| **43** | **鎸箙%锛堜笉鏄疨B锛侊級** | 7.22 |
| **44** | **鎬诲競鍊?浜?** | 410.88 |
| **45** | **娴侀€氬競鍊?浜?** | 410.88 |
| **46** | **PB(甯傚噣鐜?** | 11.51 |
| **47** | **娑ㄥ仠浠?* | 258.01 |
| **48** | **璺屽仠浠?* | 172.01 |
| 49 | 閲忔瘮 | 1.20 |
| **52** | **PE(闈?** | 314.76 |

> **韪╁潙鎻愰啋锛?* 缃戜笂寰堝鏁欑▼鎶婄储寮?43 鍐欐垚 PB锛屽疄娴嬫槸鎸箙%銆侾B 鍦ㄧ储寮?46銆?
### 1.3 鐧惧害鑲″競閫?K绾?鈥?甯A5/MA10/MA20锛圴3.0 鏂板锛?
**鏍稿績浠峰€硷細** 杩斿洖鏃惰嚜甯﹀潎绾挎暟鎹紝鏃犻渶鏈湴璁＄畻銆?
```python
import requests

def baidu_kline_with_ma(code: str, start_time: str = "") -> dict:
    """鐧惧害鑲″競閫欿绾?鈥?鐙湁鑳藉姏: 杩斿洖鏃惰嚜甯?ma5/ma10/ma20 鍧囦环"""
    url = "https://finance.pae.baidu.com/selfselect/getstockquotation"
    params = {
        "all": "1", "isIndex": "false", "isBk": "false", "isBlock": "false",
        "isFutures": "false", "isStock": "true", "newFormat": "1",
        "group": "quotation_kline_ab", "finClientType": "pc",
        "code": code, "start_time": start_time, "ktype": "1",
    }
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/vnd.finance-web.v1+json",
        "Origin": "https://gushitong.baidu.com",
        "Referer": "https://gushitong.baidu.com/",
    }
    r = requests.get(url, params=params, headers=headers, timeout=10)
    d = r.json()
    result = d.get("Result", {})
    md = result.get("newMarketData", {})
    keys = md.get("keys", [])  # includes: ma5avgprice, ma10avgprice, ma20avgprice
    rows = md.get("marketData", "").split(";")
    return {"keys": keys, "rows": rows}

# 鐢ㄦ硶
data = baidu_kline_with_ma("600519")
print("瀛楁:", data["keys"][:10])
print("鏈€杩?鏍筀绾?", data["rows"][-5:])
# keys 鍖呭惈: time, open, close, high, low, volume, amount, ma5avgprice, ma10avgprice, ma20avgprice 绛?```

---

## Layer 2: 鐮旀姤灞?
### 2.1 涓滆储鐮旀姤 API 鈥?鐮旀姤鍒楄〃 + PDF涓嬭浇锛堜富鍔涳級

A绾ф帴鍙ｏ紙鍏紑JSON API锛夛紝reportapi.eastmoney.com锛屽厤璐规棤key銆?
```python
import requests
import re
import time
from pathlib import Path

REPORT_API = "https://reportapi.eastmoney.com/report/list"
PDF_TPL = "https://pdf.dfcfw.com/pdf/H3_{info_code}_1.pdf"
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"

def eastmoney_reports(code: str, max_pages: int = 5) -> list[dict]:
    """鎷夊彇鎸囧畾鑲＄エ鐨勭爺鎶ュ垪琛?""
    all_records = []
    for page in range(1, max_pages + 1):
        params = {
            "industryCode": "*", "pageSize": "100", "industry": "*",
            "rating": "*", "ratingChange": "*",
            "beginTime": "2000-01-01", "endTime": "2030-01-01",
            "pageNo": str(page), "fields": "", "qType": "0",
            "orgCode": "", "code": code, "rcode": "",
            "p": str(page), "pageNum": str(page), "pageNumber": str(page),
        }
        r = em_get(REPORT_API, params=params,
                   headers={"Referer": "https://data.eastmoney.com/"}, timeout=30)  # 宸插唴缃檺娴?        d = r.json()
        rows = d.get("data") or []
        if not rows:
            break
        all_records.extend(rows)
        if page >= (d.get("TotalPage", 1) or 1):
            break
    return all_records

def download_pdf(record: dict, target_dir: str = "./reports") -> str | None:
    """涓嬭浇鍗曚唤鐮旀姤PDF锛岃繑鍥炰繚瀛樿矾寰勬垨None"""
    info_code = record.get("infoCode", "")
    if not info_code:
        return None
    date = (record.get("publishDate") or "")[:10]
    org = re.sub(r'[\\/:*?"<>|]', "_", record.get("orgSName") or "鏈煡")[:40]
    title = re.sub(r'[\\/:*?"<>|]', "_", record.get("title", ""))[:80]
    fname = f"{date}_{org}_{title}.pdf"
    target = Path(target_dir) / fname
    if target.exists():
        return str(target)
    url = PDF_TPL.format(info_code=info_code)
    r = em_get(url, headers={"Referer": "https://data.eastmoney.com/"}, timeout=60)
    if r.status_code == 200 and len(r.content) >= 1024:
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(r.content)
        return str(target)
    return None

# 鐢ㄦ硶
reports = eastmoney_reports("688017")
print(f"鍏?{len(reports)} 绡囩爺鎶?)
for r in reports[:5]:
    print(f"  {r.get('publishDate','')[:10]} | {r.get('orgSName')} | {r.get('title','')[:60]}")
```

#### 鐮旀姤 record 鍏抽敭瀛楁

| 瀛楁 | 鍚箟 |
|------|------|
| title | 鐮旀姤鏍囬 |
| publishDate | 鍙戝竷鏃ユ湡 |
| orgSName | 鏈烘瀯绠€绉?|
| infoCode | 鐢ㄤ簬鎷?PDF URL |
| predictThisYearEps | 浠婂勾EPS棰勬祴 |
| predictNextYearEps | 鏄庡勾EPS棰勬祴 |
| predictNextTwoYearEps | 鍚庡勾EPS棰勬祴 |
| emRatingName | 璇勭骇(涔板叆/澧炴寔/...) |
| indvInduName | 琛屼笟鍒嗙被 |

#### 琛屼笟鐮旀姤鍒楄〃锛坬Type=1锛?
涓庝釜鑲＄爺鎶?*鍚屼竴绔偣**锛坄reportapi.eastmoney.com/report/list`锛夛紝浠?`qType` 涓嶅悓锛歚qType=0` 涓偂鐮旀姤锛宍qType=1` 琛屼笟鐮旀姤銆傝繑鍥?record 鍙洿鎺ュ杺缁欎笂闈㈢殑 `download_pdf()`锛圥DF 妯℃澘閫氱敤锛夈€?
```python
def eastmoney_industry_reports(industry_code: str = "*", max_pages: int = 5,
                               begin: str = "2024-01-01") -> list[dict]:
    """鎷夊彇琛屼笟鐮旀姤鍒楄〃锛坬Type=1锛夈€?    industry_code="*" = 鍏ㄨ涓氾紱浼犱笢璐㈣涓氱爜锛堝 "1238"=IT鏈嶅姟鈪★級= 鍗曡涓氥€?    琛屼笟鍚?/ 琛屼笟鐮佸湪姣忔潯 record 鐨?industryName / industryCode 瀛楁銆?""
    all_records = []
    for page in range(1, max_pages + 1):
        params = {
            "industryCode": industry_code, "pageSize": "100", "industry": "*",
            "rating": "*", "ratingChange": "*",
            "beginTime": begin, "endTime": "2030-01-01",
            "pageNo": str(page), "fields": "", "qType": "1",
        }
        r = em_get(REPORT_API, params=params,
                   headers={"Referer": "https://data.eastmoney.com/"}, timeout=30)  # 宸插唴缃檺娴?        d = r.json()
        rows = d.get("data") or []
        if not rows:
            break
        all_records.extend(rows)
        if page >= (d.get("TotalPage", 1) or 1):
            break
    return all_records

# 鐢ㄦ硶
# 1) 鍏ㄨ涓氭渶鏂扮爺鎶?reports = eastmoney_industry_reports("*", max_pages=2)
print(f"鍏?{len(reports)} 绡囪涓氱爺鎶?)
for r in reports[:5]:
    print(f"  {r.get('publishDate','')[:10]} | {r.get('industryName')} | {r.get('orgSName')} | {r.get('title','')[:50]}")

# 2) 鍗曡涓氾紙IT鏈嶅姟鈪★紝琛屼笟鐮?1238锛? 涓嬭浇棣栫瘒 PDF锛堝鐢?2.1 鐨?download_pdf锛?it = eastmoney_industry_reports("1238", max_pages=1)
if it:
    download_pdf(it[0])
```

琛屼笟鐮旀姤鐗规湁/甯哥敤瀛楁锛堝叾浣欏瓧娈靛悓 2.1 涓偂鐮旀姤锛夛細

| 瀛楁 | 鍚箟 |
|------|------|
| industryName | 琛屼笟鍚嶇О锛堝 IT鏈嶅姟鈪°€侀鐢佃澶囥€佸厜浼忚澶囷級 |
| industryCode | 涓滆储琛屼笟浠ｇ爜锛堢敤浜?`industry_code` 绮剧‘杩囨护锛?|
| emRatingName | 琛屼笟璇勭骇锛堜拱鍏?澧炴寔/涓€?...锛?|
| reportType | 鎶ュ憡绫诲瀷 |
| attachPages / attachSize | PDF 椤垫暟 / 澶у皬(KB) |
| infoCode | 鍠傜粰 `download_pdf()` 鎷?PDF URL |

> **琛屼笟鐮佹€庝箞鎷匡細** 涓滆储琛屼笟鐮佷笉鏄€氱敤璁板繂鐮侊紝娌℃湁鍏紑鐨勭爜琛ㄧ鐐癸紙`bxpa` 绛夊凡 404锛夈€傚父鐢ㄥ仛娉曪細鍏堢敤 `industry_code="*"` 鎷変竴鎵癸紝浠庣粨鏋滅殑 `industryName`/`industryCode` 鎵惧埌鐩爣琛屼笟鐨勭爜锛屽啀鐢ㄨ鐮佺簿纭繃婊ゃ€?
### 2.2 鍚岃姳椤轰竴鑷撮鏈烢PS锛堢洿杩?basic.10jqka.com.cn锛?
```python
import requests
import pandas as pd
from io import StringIO

def ths_eps_forecast(code: str) -> pd.DataFrame:
    """
    鍚岃姳椤烘満鏋勪竴鑷撮鏈烢PS銆?    鐩磋繛 basic.10jqka.com.cn锛岃В鏋怘TML琛ㄦ牸銆?    杩斿洖 DataFrame: 骞村害, 棰勬祴鏈烘瀯鏁? 鏈€灏忓€? 鍧囧€? 鏈€澶у€?    "鍧囧€? = 鏈烘瀯涓€鑷撮鏈烢PS
    """
    url = f"https://basic.10jqka.com.cn/new/{code}/worth.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
        "Referer": "https://basic.10jqka.com.cn/",
    }
    r = requests.get(url, headers=headers, timeout=15)
    r.encoding = "gbk"
    dfs = pd.read_html(StringIO(r.text))
    # 鎵惧惈"姣忚偂鏀剁泭"鐨勮〃鏍?    for df in dfs:
        cols = [str(c) for c in df.columns]
        if any("姣忚偂鏀剁泭" in c or "鍧囧€? in c for c in cols):
            return df
    # fallback: 杩斿洖绗竴涓〃
    return dfs[0] if dfs else pd.DataFrame()

# 鐢ㄦ硶
df = ths_eps_forecast("688017")
print(df)
# "棰勬祴鏈烘瀯鏁? < 3 鐨勮璋ㄦ厧
```

### 2.3 iwencai 鈥?NL璇箟鎼滅储鐮旀姤锛堝敮涓€鑳藉姏锛?
闇€瑕?API Key + X-Claw Headers锛圫killHub 2.0 寮哄埗瑕佹眰锛夈€?
```python
import os
import json
import secrets
import requests

IWENCAI_BASE = os.environ.get("IWENCAI_BASE_URL", "https://openapi.iwencai.com")
IWENCAI_KEY = os.environ.get("IWENCAI_API_KEY", "")

def _claw_headers(call_type: str = "normal") -> dict:
    """SkillHub 2.0 蹇呴』鐨?X-Claw 閴存潈澶?""
    return {
        "X-Claw-Call-Type": call_type,
        "X-Claw-Skill-Id": "report-search",
        "X-Claw-Skill-Version": "2.0.0",
        "X-Claw-Plugin-Id": "none",
        "X-Claw-Plugin-Version": "none",
        "X-Claw-Trace-Id": secrets.token_hex(32),
    }

def iwencai_search(query: str, channel: str = "report", size: int = 50) -> list[dict]:
    """
    iwencai 璇箟鎼滅储銆?    channel: "report"(鐮旀姤) / "announcement"(鍏憡) / "news"(鏂伴椈)
    size: 榛樿10, 瀹炴祴鍙皟鍒?0锛堥殣钘忓弬鏁帮級
    """
    headers = {
        "Authorization": f"Bearer {IWENCAI_KEY}",
        "Content-Type": "application/json",
        **_claw_headers(),
    }
    payload = {
        "channels": [channel],
        "app_id": "AIME_SKILL",
        "query": query,
        "size": size,
    }
    r = requests.post(
        f"{IWENCAI_BASE}/v1/comprehensive/search",
        json=payload, headers=headers, timeout=30,
    )
    if r.status_code != 200:
        raise RuntimeError(f"iwencai HTTP {r.status_code}: {r.text[:200]}")
    data = r.json()
    if data.get("status_code", 0) != 0:
        raise RuntimeError(f"iwencai error: {data.get('status_msg', '')}")
    return data.get("data") or []

def iwencai_query(query: str, page: int = 1, limit: int = 50) -> list[dict]:
    """
    iwencai NL鏁版嵁鏌ヨ锛堢粨鏋勫寲瀛楁锛夈€?    渚? "璐靛窞鑼呭彴 ROE" 鈫?DataFrame-like rows
    """
    headers = {
        "Authorization": f"Bearer {IWENCAI_KEY}",
        "Content-Type": "application/json",
        **_claw_headers(),
    }
    payload = {
        "query": query,
        "page": str(page),
        "limit": str(limit),
        "is_cache": "1",
        "expand_index": "true",
    }
    r = requests.post(
        f"{IWENCAI_BASE}/v1/query2data",
        json=payload, headers=headers, timeout=30,
    )
    if r.status_code != 200:
        raise RuntimeError(f"iwencai HTTP {r.status_code}: {r.text[:200]}")
    data = r.json()
    if data.get("status_code", 0) != 0:
        raise RuntimeError(f"iwencai error: {data.get('status_msg', '')}")
    return data.get("datas") or []

def dedup_articles(articles: list[dict]) -> list[dict]:
    """鍚屼竴uid浠呬繚鐣檚core鏈€楂樼殑娈佃惤"""
    best = {}
    for a in articles:
        uid = a.get("uid", "") or f"{a.get('title','')}|{a.get('publish_date','')}"
        score = float(a.get("score", 0))
        if uid not in best or score > float(best[uid].get("score", 0)):
            best[uid] = a
    return sorted(best.values(), key=lambda x: x.get("publish_date", ""), reverse=True)

# 鐢ㄦ硶: NL璇箟鎼滅储鐮旀姤
articles = iwencai_search("浜哄舰鏈哄櫒浜?琛屾槦婊氭煴涓濇潬 2026", channel="report", size=50)
articles = dedup_articles(articles)
for a in articles[:5]:
    extra = a.get("extra") or {}
    if isinstance(extra, str):
        extra = json.loads(extra)
    print(f"{a.get('publish_date','')[:10]} | {extra.get('organization','')} | {a.get('title','')[:60]}")
```

**iwencai 鐨勫敮涓€浠峰€硷細** NL 涓婚鎼滅储銆?浜哄舰鏈哄櫒浜?琛屾槦婊氭煴涓濇潬" 杩欑璺ㄤ富棰樻绱㈠彧鏈?iwencai 鑳藉仛銆傛寜鏍囩殑鎼滅爺鎶ヨ蛋涓滆储 reportapi 鏇寸ǔ瀹氥€?
---

## Layer 3: 淇″彿灞?
### 3.1 鍚岃姳椤虹儹鐐?鈥?褰撴棩寮哄娍鑲?+ 棰樻潗褰掑洜 reason tags锛堢嫭瀹讹級

**鏍稿績浠峰€硷細** 涓嶅彧鍛婅瘔浣?鍝簺璧板己"锛岃繕鍛婅瘔浣?*"涓轰粈涔堣蛋寮?** 鈥斺€?鍚岃姳椤虹紪杈戦儴浜哄伐杩愯惀鐨勯鏉愭爣绛俱€?
```python
import requests
import pandas as pd

def ths_hot_reason(date: str = None) -> pd.DataFrame:
    """
    鍚岃姳椤哄綋鏃ュ己鍔胯偂褰掑洜銆?    date: 'YYYY-MM-DD' 鏍煎紡锛孨one=浠婂ぉ
    杩斿洖 DataFrame锛屽惈姣忓彧鑲＄エ鐨勯鏉愭爣绛?(reason)銆?
    瀹炴祴: 73ms 鎷垮埌 ~125 鍙?+ 瀹屾暣瀛楁
    """
    from datetime import date as _date
    if date is None:
        date = _date.today().strftime("%Y-%m-%d")

    url = (
        f"http://zx.10jqka.com.cn/event/api/getharden/"
        f"date/{date}/orderby/date/orderway/desc/charset/GBK/"
    )
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "Chrome/117.0.0.0 Safari/537.36"
        )
    }
    r = requests.get(url, headers=headers, timeout=10)
    data = r.json()
    if data.get("errocode", 0) != 0:
        raise RuntimeError(f"鍚岃姳椤虹儹鐐归敊璇? {data.get('errormsg', '')}")

    rows = data.get("data") or []
    df = pd.DataFrame(rows)
    if df.empty:
        return df

    # 瀛楁閲嶅懡鍚嶏紙涓枃鍙嬪ソ锛?    rename_map = {
        "name": "鍚嶇О", "code": "浠ｇ爜", "reason": "棰樻潗褰掑洜",
        "close": "鏀剁洏浠?, "zhangdie": "娑ㄨ穼棰?, "zhangfu": "娑ㄥ箙%",
        "huanshou": "鎹㈡墜鐜?", "chengjiaoe": "鎴愪氦棰?,
        "chengjiaoliang": "鎴愪氦閲?, "ddejingliang": "澶у崟鍑€閲?,
        "market": "甯傚満",
    }
    df = df.rename(columns=rename_map)
    return df

# 鐢ㄦ硶
df = ths_hot_reason("2026-05-09")
print(f"褰撴棩寮哄娍鑲? {len(df)} 鍙?)
print(df[["浠ｇ爜", "鍚嶇О", "娑ㄥ箙%", "棰樻潗褰掑洜"]].head(10))
```

#### 鍚岃姳椤虹儹鐐瑰瓧娈甸€熸煡

| 鍘熷瓧娈?| 涓枃 | 璇存槑 |
|---|---|---|
| code | 浠ｇ爜 | 6 浣嶈偂绁ㄤ唬鐮?|
| name | 鍚嶇О | 绠€绉?|
| **reason** | **棰樻潗褰掑洜** | **鏍稿績瀛楁锛屼汉宸ヨ繍钀?tags锛屽"绠楀姏绉熻祦+Token宸ュ巶+AI鏀垮姟"** |
| zhangfu | 娑ㄥ箙% | 褰撴棩娑ㄥ箙 |
| huanshou | 鎹㈡墜鐜? | 褰撴棩鎹㈡墜 |
| chengjiaoe | 鎴愪氦棰?| 鍏?|
| chengjiaoliang | 鎴愪氦閲?| 鑲?|
| ddejingliang | 澶у崟鍑€閲?| 涓诲姏鍑€娴佸叆鎸囨爣 |
| close | 鏀剁洏浠?| 鍏?|
| zhangdie | 娑ㄨ穼棰?| 鍏?|
| market | 甯傚満 | 娌?娣?鍖?|

### 3.2 鍚岃姳椤哄寳鍚戣祫閲?鈥?hsgtApi 瀹炴椂鍒嗛挓娴佸悜 + 鏈湴鑷紦瀛樺巻鍙?
> **宸茬煡琛屼笟鎬ч棶棰橈細** eastmoney 鍏ㄧ郴鍖楀悜鏁版嵁鑷?2024-08 鍚庡噣涔伴瀛楁杩斿洖 NaN/0锛屽睘涓婃父鏂緵銆傚凡鏀逛负**鏈湴 CSV 鑷紦瀛樻ā寮?*鈥斺€旀瘡娆℃媺瀹炴椂鏁版嵁鍚庤嚜鍔ㄥ啓鍏ユ湰鍦?CSV锛屽巻鍙茶秺璺戣秺涓板瘜銆?
```python
import requests
import pandas as pd
from pathlib import Path

HSGT_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "Chrome/117.0.0.0 Safari/537.36"
    ),
    "Host": "data.hexin.cn",
    "Referer": "https://data.hexin.cn/",
}

def hsgt_realtime() -> pd.DataFrame:
    """
    娌繁鑲￠€氬綋鏃ュ疄鏃跺垎閽熸祦鍚戯紙鍚泦鍚堢珵浠?09:10鈥?5:00锛?62 涓椂闂寸偣锛夈€?    杩斿洖瀛楁: time, hgt(娌偂閫氱疮璁″噣涔板叆), sgt(娣辫偂閫氱疮璁″噣涔板叆)
    鍗曚綅: 浜垮厓
    """
    url = "https://data.hexin.cn/market/hsgtApi/method/dayChart/"
    r = requests.get(url, headers=HSGT_HEADERS, timeout=10)
    d = r.json()
    times = d.get("time", [])
    hgt = d.get("hgt", [])
    sgt = d.get("sgt", [])

    n = len(times)
    return pd.DataFrame({
        "time": times,
        "hgt_yi": hgt[:n] + [None] * (n - len(hgt)),
        "sgt_yi": sgt[:n] + [None] * (n - len(sgt)),
    })

# === 鑷紦瀛樿緟鍔╁嚱鏁?===

def _northbound_cache_path() -> Path:
    """鍖楀悜璧勯噾鏈湴 CSV 缂撳瓨璺緞"""
    p = Path.home() / ".tradingagents" / "cache" / "northbound_daily.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    return p

def _save_northbound_snapshot(date: str, hgt: float, sgt: float):
    """鍐欏叆/鏇存柊褰撳ぉ鍖楀悜鏀剁洏鏁版嵁鍒?CSV"""
    path = _northbound_cache_path()
    rows = {}
    if path.exists():
        for line in path.read_text().strip().split("\n")[1:]:
            parts = line.split(",")
            if len(parts) == 3:
                rows[parts[0]] = line
    rows[date] = f"{date},{hgt},{sgt}"
    with open(path, "w") as f:
        f.write("date,hgt,sgt\n")
        for d in sorted(rows.keys()):
            f.write(rows[d] + "\n")

def _load_northbound_history(n: int = 20) -> pd.DataFrame:
    """璇诲彇鏈€杩?N 澶╁寳鍚戝巻鍙?""
    path = _northbound_cache_path()
    if not path.exists():
        return pd.DataFrame()
    df = pd.read_csv(path)
    return df.tail(n)

# 鐢ㄦ硶 1: 瀹炴椂鍒嗛挓娴佸悜
df = hsgt_realtime()
print(f"鍒嗛挓鐐规暟: {len(df)}")
print(df.tail(5))

# 鐢ㄦ硶 2: 鑷姩缂撳瓨浠婃棩鏀剁洏鏁版嵁
if not df.empty:
    last = df.dropna().iloc[-1]
    _save_northbound_snapshot("2026-05-17", last["hgt_yi"], last["sgt_yi"])

# 鐢ㄦ硶 3: 璇诲彇鍘嗗彶
hist = _load_northbound_history(20)
print(hist)
```

### 3.3 涓滆储 slist 鈥?涓偂鎵€灞炴澘鍧?姒傚康褰掑睘锛圴3.2.2 鏇挎崲鐧惧害锛?
**鏍稿績浠峰€硷細** 涓€娆¤皟鐢ㄦ嬁鍒颁釜鑲℃墍灞炵殑鍏ㄩ儴鏉垮潡锛堣涓?+ 姒傚康 + 鍦板煙娣峰悎锛夛紝鍚澘鍧椾唬鐮侊紙BK鐮侊級銆佸綋鏃ユ定璺屽箙銆佹澘鍧楅緳澶磋偂銆傞鏉愬綊鍥犮€佹澘鍧楄仈鍔ㄥ垎鏋愬繀澶囥€?
> **V3.2.2 鏇挎崲璇存槑锛?* 鐧惧害 PAE `getrelatedblock` 鎺ュ彛宸插け鏁堬紙瀹炴祴杩斿洖 `ResultCode 10003` + 绌烘暟缁勶紝#18锛夛紝鏀圭敤涓滆储 `slist` 涓偂鎵€灞炴澘鍧楁帴鍙ｏ紙`spt=3`锛屼竴娆¤姹傛嬁鍏紝闆堕壌鏉冿級銆備笢璐㈡妸琛屼笟/姒傚康/鍦板煙娣峰湪**涓€涓垪琛?*閲岃繑鍥烇紝鏉垮潡鍚嶆湰韬凡鑷В閲婏紙濡傘€岄鍝侀ギ鏂欍€嶆槸琛屼笟銆併€岃吹宸炴澘鍧椼€嶆槸鍦板煙銆併€岄吙閰掓蹇点€嶆槸姒傚康锛夛紝AI 鐩存帴鐢ㄦ澘鍧楀悕鍋氶鏉愬綊鍥犲嵆鍙€?
```python
def eastmoney_concept_blocks(code: str) -> dict:
    """
    涓偂鎵€灞炴澘鍧?姒傚康褰掑睘锛堜笢璐?slist锛屼竴娆¤姹傛嬁鍏紝宸插唴缃檺娴侊級銆?    杩斿洖: {total, boards: [{name, code(BK鐮?, change_pct, lead_stock}], concept_tags: [鏉垮潡鍚?..]}
    boards 娣峰悎 琛屼笟/姒傚康/鍦板煙锛屾澘鍧楀悕鑷В閲婏紱concept_tags 鏄墍鏈夋澘鍧楀悕鐨勪究鎹峰垪琛ㄣ€?    """
    market_code = 1 if code.startswith("6") else 0
    params = {
        "fltt": "2", "invt": "2",
        "secid": f"{market_code}.{code}",
        "spt": "3", "pi": "0", "pz": "200", "po": "1",
        "fields": "f12,f14,f3,f128",
    }
    headers = {"User-Agent": UA, "Referer": "https://quote.eastmoney.com/"}
    try:
        r = em_get("https://push2.eastmoney.com/api/qt/slist/get",
                   params=params, headers=headers, timeout=15)
        d = r.json()
    except Exception as e:
        print(f"[WARN] 涓滆储鏉垮潡褰掑睘璇锋眰澶辫触: {e}")
        return {"total": 0, "boards": [], "concept_tags": []}

    diff = (d.get("data") or {}).get("diff") or {}
    items = diff.values() if isinstance(diff, dict) else diff
    boards = []
    for it in items:
        boards.append({
            "name": it.get("f14", ""),         # 鏉垮潡鍚?            "code": it.get("f12", ""),         # BK 鏉垮潡浠ｇ爜
            "change_pct": it.get("f3", ""),    # 鏉垮潡褰撴棩娑ㄨ穼骞?            "lead_stock": it.get("f128", ""),  # 鏉垮潡榫欏ご鑲?        })
    return {
        "total": len(boards),
        "boards": boards,
        "concept_tags": [b["name"] for b in boards],
    }

# 鐢ㄦ硶
blocks = eastmoney_concept_blocks("600519")
print(f"鍏?{blocks['total']} 涓澘鍧?)
print("鏉垮潡褰掑睘:", blocks["concept_tags"])
# 鈫?['椋熷搧楗枡', '鐧介厭鈪?, '鐧介厭鈪?, '璐靛窞鏉垮潡', '閰块厭姒傚康', 'HS300_', ...]
```

> **娉ㄦ剰锛?* 涓滆储涓嶅尯鍒嗚涓?姒傚康/鍦板煙绫诲瀷锛堟贩鍦ㄤ竴涓垪琛ㄨ繑鍥烇級銆傚闇€绮剧‘鍒嗙被鍙寜鏉垮潡鍚嶅垽鏂紝鎴栧彟鏌ュ叏甯傚満鏉垮潡娓呭崟锛坄clist` + `m:90+t:1/2/3`锛夆€斺€斾絾鍚庤€呮瘡娆￠渶澶氬彂璇锋眰銆佸ぇ椤垫槗瑙﹀彂椋庢帶锛屼笉鎺ㄨ崘鍦ㄦ壒閲忓満鏅敤銆?
### 3.4 涓滆储 push2 鈥?涓偂璧勯噾娴佸悜锛堝垎閽熺骇锛?
鐩樹腑瀹炴椂鍒嗛挓绾ц祫閲戞祦锛堜富鍔?澶у崟/涓崟/灏忓崟/瓒呭ぇ鍗曞噣娴佸叆锛夈€?
> **V3.1 鏇挎崲璇存槑锛?* 鐧惧害 PAE `fundflow` 鍜?`fundsortlist` 鎺ュ彛宸蹭簬 2026-05 涓嬬嚎锛堣繑鍥?null锛夛紝鏀圭敤涓滆储 push2 璧勯噾娴?API銆傛棩绾ц祫閲戞祦瑙?Layer 4.5 `stock_fund_flow_120d()`銆?
```python
import requests

def eastmoney_fund_flow_minute(code: str) -> list[dict]:
    """
    涓偂璧勯噾娴佸悜锛堝垎閽熺骇锛屽綋鏃ョ洏涓級銆?    code: 6浣嶈偂绁ㄤ唬鐮?    杩斿洖: [{time, main_net, small_net, mid_net, large_net, super_net}, ...]
    鍗曚綅: 鍏?    """
    secid = f"1.{code}" if code.startswith("6") else f"0.{code}"
    url = "https://push2.eastmoney.com/api/qt/stock/fflow/kline/get"
    params = {
        "secid": secid, "klt": 1,
        "fields1": "f1,f2,f3,f7",
        "fields2": "f51,f52,f53,f54,f55,f56,f57",
    }
    headers = {
        "User-Agent": UA,
        "Referer": "https://quote.eastmoney.com/",
        "Origin": "https://quote.eastmoney.com",
    }
    try:
        r = em_get(url, params=params, headers=headers, timeout=10)
        d = r.json()
    except Exception as e:
        print(f"[WARN] push2 璧勯噾娴佽姹傚け璐? {e}")
        return []

    rows = []
    for line in d.get("data", {}).get("klines", []):
        parts = line.split(",")
        if len(parts) >= 6:
            rows.append({
                "time": parts[0],
                "main_net": float(parts[1]),
                "small_net": float(parts[2]),
                "mid_net": float(parts[3]),
                "large_net": float(parts[4]),
                "super_net": float(parts[5]),
            })
    return rows

# 鐢ㄦ硶: 鍒嗛挓绾у疄鏃惰祫閲戞祦
realtime = eastmoney_fund_flow_minute("000858")
if realtime:
    last = realtime[-1]
    signal = "bullish" if last["main_net"] > 0 else "bearish"
    print(f"涓诲姏鍑€娴佸叆: {last['main_net']:.0f}鍏?鈫?{signal}")
    # 缁熻鍏ㄥぉ涓诲姏鍑€娴佸叆
    total = sum(r["main_net"] for r in realtime)
    print(f"鍏ㄥぉ涓诲姏绱: {total/1e4:.0f}涓囧厓")
```

> **娉ㄦ剰锛?* push2 璧勯噾娴侀噾棰濆崟浣嶆槸**鍏?*锛堥潪涓囧厓锛夛紝浣跨敤鏃舵敞鎰忔崲绠椼€俙klt=1` 鍒嗛挓绾э紝`klt=101` 鏃ョ骇銆?
### 3.5 榫欒檸姒滃腑浣?鈥?涓偂涓婃璁板綍 + 涔板崠甯綅 TOP5 + 鏈烘瀯鍔ㄥ悜

鐩磋繛涓滆储 datacenter API锛屼笉渚濊禆绗笁鏂瑰皝瑁呫€?
```python
import requests
from datetime import datetime, timedelta

def dragon_tiger_board(code: str, trade_date: str, look_back: int = 30) -> dict:
    """
    榫欒檸姒滄暟鎹仛鍚堛€?    trade_date: YYYY-MM-DD
    look_back: 鍥炵湅澶╂暟
    杩斿洖: {records: [...], seats: {buy: [...], sell: [...]}, institution: {...}}
    """
    start = datetime.strptime(trade_date, "%Y-%m-%d") - timedelta(days=look_back)
    start_str = start.strftime("%Y-%m-%d")

    # 1. 涓婃璁板綍
    records = []
    data = eastmoney_datacenter(
        "RPT_DAILYBILLBOARD_DETAILSNEW",
        filter_str=f"(TRADE_DATE>='{start_str}')(TRADE_DATE<='{trade_date}')(SECURITY_CODE=\"{code}\")",
        page_size=50,
        sort_columns="TRADE_DATE", sort_types="-1",
    )
    for row in data:
        records.append({
            "date": str(row.get("TRADE_DATE", ""))[:10],
            "reason": row.get("EXPLANATION", ""),
            "net_buy": round((row.get("BILLBOARD_NET_AMT") or 0) / 10000, 1),
            "turnover": round(float(row.get("TURNOVERRATE") or 0), 2),
        })

    # 2. 鏈€杩戜笂姒滅殑涔板崠甯綅
    seats = {"buy": [], "sell": []}
    if records:
        latest_date = records[0]["date"]
        # 涔板叆甯綅
        buy_data = eastmoney_datacenter(
            "RPT_BILLBOARD_DAILYDETAILSBUY",
            filter_str=f"(TRADE_DATE='{latest_date}')(SECURITY_CODE=\"{code}\")",
            page_size=10,
            sort_columns="BUY", sort_types="-1",
        )
        for row in buy_data[:5]:
            seats["buy"].append({
                "name": row.get("OPERATEDEPT_NAME", ""),
                "buy_amt": round((row.get("BUY") or 0) / 10000, 1),
                "sell_amt": round((row.get("SELL") or 0) / 10000, 1),
                "net": round((row.get("NET") or 0) / 10000, 1),
            })
        # 鍗栧嚭甯綅
        sell_data = eastmoney_datacenter(
            "RPT_BILLBOARD_DAILYDETAILSSELL",
            filter_str=f"(TRADE_DATE='{latest_date}')(SECURITY_CODE=\"{code}\")",
            page_size=10,
            sort_columns="SELL", sort_types="-1",
        )
        for row in sell_data[:5]:
            seats["sell"].append({
                "name": row.get("OPERATEDEPT_NAME", ""),
                "buy_amt": round((row.get("BUY") or 0) / 10000, 1),
                "sell_amt": round((row.get("SELL") or 0) / 10000, 1),
                "net": round((row.get("NET") or 0) / 10000, 1),
            })

    # 3. 鏈烘瀯涔板崠缁熻锛堜粠涔板崠甯綅鏄庣粏涓瓫閫?OPERATEDEPT_CODE="0" 鍗虫満鏋勪笓鐢ㄥ腑浣嶏級
    institution = {"buy_amt": 0, "sell_amt": 0, "net_amt": 0}
    for detail_data, side in [(buy_data, "buy"), (sell_data, "sell")]:
        for row in detail_data:
            if str(row.get("OPERATEDEPT_CODE", "")) == "0":
                amt = (row.get("BUY") or 0) if side == "buy" else (row.get("SELL") or 0)
                if side == "buy":
                    institution["buy_amt"] += amt
                else:
                    institution["sell_amt"] += amt
    institution["buy_amt"] = round(institution["buy_amt"] / 10000, 1)
    institution["sell_amt"] = round(institution["sell_amt"] / 10000, 1)
    institution["net_amt"] = round(institution["buy_amt"] - institution["sell_amt"], 1)

    return {"records": records, "seats": seats, "institution": institution}

# 鐢ㄦ硶
data = dragon_tiger_board("002475", "2026-05-17")
print(f"杩?0鏃ヤ笂姒?{len(data['records'])} 娆?)
for r in data["records"]:
    print(f"  {r['date']}: {r['reason']}")
if data["seats"]["buy"]:
    print("涔板叆甯綅 TOP5:")
    for s in data["seats"]["buy"]:
        print(f"  {s['name']}: 涔皗s['buy_amt']}涓?鍗杮s['sell_amt']}涓?鍑€{s['net']}涓?)
```

> **ST 鑲℃敞鎰忥細** 5% 娑ㄨ穼鍋滄洿瀹规槗瑙﹀彂榫欒檸姒滐紙"杩炵画涓夋棩鍋忕鍊肩疮璁¤揪12%"锛夛紝绉戝垱鏉?20% 娑ㄨ穼鍋滃垯杈冨皯瑙﹀彂銆?
### 3.6 闄愬敭瑙ｇ鏃ュ巻 鈥?鍘嗗彶瑙ｇ + 鏈潵 90 澶╁緟瑙ｇ

```python
from datetime import datetime, timedelta

def lockup_expiry(code: str, trade_date: str, forward_days: int = 90) -> dict:
    """
    闄愬敭瑙ｇ鏃ュ巻銆?    杩斿洖: {history: [...], upcoming: [...]}
    """
    # 1. 鍘嗗彶瑙ｇ璁板綍
    history_data = eastmoney_datacenter(
        "RPT_LIFT_STAGE",
        filter_str=f"(SECURITY_CODE=\"{code}\")",
        page_size=15,
        sort_columns="FREE_DATE", sort_types="-1",
    )
    history = []
    for row in history_data:
        history.append({
            "date": str(row.get("FREE_DATE", ""))[:10],
            "type": row.get("LIMITED_STOCK_TYPE", ""),
            "shares": row.get("FREE_SHARES_NUM", 0),
            "ratio": row.get("FREE_RATIO", 0),
        })

    # 2. 鏈潵寰呰В绂?    end_date = datetime.strptime(trade_date, "%Y-%m-%d") + timedelta(days=forward_days)
    end_str = end_date.strftime("%Y-%m-%d")
    upcoming_data = eastmoney_datacenter(
        "RPT_LIFT_STAGE",
        filter_str=f"(SECURITY_CODE=\"{code}\")(FREE_DATE>='{trade_date}')(FREE_DATE<='{end_str}')",
        page_size=20,
        sort_columns="FREE_DATE", sort_types="1",
    )
    upcoming = []
    for row in upcoming_data:
        upcoming.append({
            "date": str(row.get("FREE_DATE", ""))[:10],
            "type": row.get("LIMITED_STOCK_TYPE", ""),
            "shares": row.get("FREE_SHARES_NUM", 0),
            "ratio": row.get("FREE_RATIO", 0),
        })

    return {"history": history, "upcoming": upcoming}

# 鐢ㄦ硶
data = lockup_expiry("002475", "2026-05-17")
print(f"鍘嗗彶瑙ｇ {len(data['history'])} 鎵?)
for h in data["history"][:5]:
    print(f"  {h['date']}: {h['type']} 鏁伴噺={h['shares']}")
if data["upcoming"]:
    print(f"鏈潵90澶╁緟瑙ｇ {len(data['upcoming'])} 鎵?)
else:
    print("鏈潵90澶╂棤寰呰В绂?)
```

**闄愬敭鑲＄被鍨嬪弬鑰冿細**
- 棣栧彂鍘熻偂涓滈檺鍞偂浠斤紙IPO 鍚?1-3 骞达級
- 棣栧彂鏈烘瀯閰嶅敭鑲′唤锛圛PO 鎴樼暐閰嶅敭锛?- 瀹氬悜澧炲彂鏈烘瀯閰嶅敭鑲′唤锛?-18 涓湀锛?- 鑲℃潈婵€鍔遍檺鍞偂浠?
### 3.7 琛屼笟鏉垮潡鎺掑悕锛圴3.0 鏀圭敤涓滆储 鈥?鍚岃姳椤哄姞浜嗗弽鐖?01锛?
涓滆储琛屼笟鏉垮潡娑ㄨ穼骞呮帓鍚嶏紝涓€娆¤皟鐢ㄧ湅鍏ㄥ競鍦鸿涓氳疆鍔ㄣ€?
```python
import requests

def industry_comparison(top_n: int = 20) -> dict:
    """
    鍏ㄨ涓氭定璺屽箙鎺掑悕锛堜笢璐㈣涓氭澘鍧楋紝~100 涓涓氾級銆?    杩斿洖: {top: [...], bottom: [...], total: int}
    """
    url = "https://push2.eastmoney.com/api/qt/clist/get"
    params = {
        "pn": "1", "pz": "100", "po": "1", "np": "1",
        "fltt": "2", "invt": "2",
        "fs": "m:90+t:2",
        "fields": "f2,f3,f4,f12,f13,f14,f104,f105,f128,f136,f140,f141,f207",
    }
    headers = {"User-Agent": UA}
    r = em_get(url, params=params, headers=headers, timeout=15)
    d = r.json()
    items = d.get("data", {}).get("diff", [])
    if not items:
        return {"top": [], "bottom": [], "total": 0}

    rows = []
    for i, item in enumerate(items):
        rows.append({
            "rank": i + 1,
            "name": item.get("f14", ""),
            "change_pct": item.get("f3", 0),
            "code": item.get("f12", ""),
            "up_count": item.get("f104", 0),
            "down_count": item.get("f105", 0),
            "leader": item.get("f140", ""),
            "leader_change": item.get("f136", 0),
        })

    return {
        "top": rows[:top_n],
        "bottom": rows[-top_n:],
        "total": len(rows),
    }

# 鐢ㄦ硶
data = industry_comparison(20)
print(f"鍏?{data['total']} 涓涓?)
print("\nTOP 10 娑ㄥ箙:")
for r in data["top"][:10]:
    print(f"  {r['rank']}. {r['name']}: {r['change_pct']}% 娑▄r['up_count']}璺寋r['down_count']} 棰嗘定{r['leader']}")
print("\nBOTTOM 5 璺屽箙:")
for r in data["bottom"][-5:]:
    print(f"  {r['rank']}. {r['name']}: {r['change_pct']}%")
```

### 3.8 鍏ㄥ競鍦洪緳铏庢

姣忔棩鍏ㄥ競鍦洪緳铏庢姹囨€烩€斺€斿綋鏃ユ墍鏈夎Е鍙戦緳铏庢鐨勮偂绁?+ 涓婃鍘熷洜 + 涔板崠鍑€棰?+ 鎹㈡墜鐜囥€?
```python
from datetime import datetime

def daily_dragon_tiger(trade_date: str = None, min_net_buy: float = None) -> dict:
    """
    鍏ㄥ競鍦洪緳铏庢銆?    trade_date: YYYY-MM-DD锛堥粯璁ゅ綋鏃ワ級
    min_net_buy: 鍑€涔板叆涓嬮檺锛堜竾鍏冿級锛孨one 涓嶈繃婊?    杩斿洖: {date, total_records, stocks: [{code, name, reason, close, change_pct,
           net_buy_wan, buy_wan, sell_wan, turnover_pct}]}
    """
    if trade_date is None:
        trade_date = datetime.now().strftime("%Y-%m-%d")

    data = eastmoney_datacenter(
        "RPT_DAILYBILLBOARD_DETAILSNEW",
        filter_str=f"(TRADE_DATE>='{trade_date}')(TRADE_DATE<='{trade_date}')",
        page_size=500,
        sort_columns="BILLBOARD_NET_AMT", sort_types="-1",
    )
    if not data:
        return {"date": trade_date, "total_records": 0, "stocks": [],
                "note": "鏃犳暟鎹紙闈炰氦鏄撴棩鎴栫洏鍚庢湭鏇存柊锛?}

    actual_date = str(data[0].get("TRADE_DATE", ""))[:10] if data else trade_date
    stocks = []
    for row in data:
        net_buy = (row.get("BILLBOARD_NET_AMT") or 0) / 10000
        if min_net_buy is not None and net_buy < min_net_buy:
            continue
        stocks.append({
            "code": row.get("SECURITY_CODE", ""),
            "name": row.get("SECURITY_NAME_ABBR", ""),
            "reason": row.get("EXPLANATION", ""),
            "close": row.get("CLOSE_PRICE") or 0,
            "change_pct": round(float(row.get("CHANGE_RATE") or 0), 2),
            "net_buy_wan": round(net_buy, 1),
            "buy_wan": round((row.get("BILLBOARD_BUY_AMT") or 0) / 10000, 1),
            "sell_wan": round((row.get("BILLBOARD_SELL_AMT") or 0) / 10000, 1),
            "turnover_pct": round(float(row.get("TURNOVERRATE") or 0), 2),
        })
    return {"date": actual_date, "total_records": len(stocks), "stocks": stocks}

# 鐢ㄦ硶
data = daily_dragon_tiger("2026-05-16")
print(f"{data['date']} 榫欒檸姒滃叡 {data['total_records']} 鏉¤褰?)
for s in data["stocks"][:10]:
    print(f"  {s['code']} {s['name']}: {s['reason']} | 鍑€涔皗s['net_buy_wan']}涓?娑ㄨ穼{s['change_pct']}%")

# 鍙湅鍑€涔板叆 > 5000 涓囩殑
data = daily_dragon_tiger("2026-05-16", min_net_buy=5000)
print(f"\n鍑€涔板叆 > 5000涓? {data['total_records']} 鏉?)
```

### 3.9 淇″彿灞傜粍鍚堢敤娉曪細棰樻潗鐑害 + 璧勯噾楠岃瘉

```python
# 鎷夊綋鏃ュ己鍔胯偂 reason
df_hot = ths_hot_reason()

# 璇嶉缁熻 reason 鍒楅噷鐨勯鏉愬叧閿瘝
from collections import Counter
all_tags = []
for r in df_hot["棰樻潗褰掑洜"].dropna():
    tags = [t.strip() for t in str(r).split("+") if t.strip()]
    all_tags.extend(tags)

cnt = Counter(all_tags)
print("褰撴棩 TOP 10 棰樻潗鐑害:")
for tag, n in cnt.most_common(10):
    print(f"  {tag}: {n} 鍙?)

# 鍚屾椂鎷夊寳鍚戝綋鏃ユ祦鍚戯紝鐪嬭祫閲戞祦鏂瑰悜鏄惁瀵瑰簲棰樻潗
df_north = hsgt_realtime()
hgt_close = df_north["hgt_yi"].dropna().iloc[-1] if not df_north.empty else 0
sgt_close = df_north["sgt_yi"].dropna().iloc[-1] if not df_north.empty else 0
print(f"\n鍖楀悜鏀剁洏绱: 娌偂閫?{hgt_close} 浜?/ 娣辫偂閫?{sgt_close} 浜?)

# V3.0: 鍙犲姞琛屼笟瀵规瘮锛岀湅鍝簺琛屼笟璧勯噾鍦ㄦ祦鍏?comp = industry_comparison(10)
print("\n琛屼笟娑ㄥ箙 TOP 5:")
for r in comp["top"][:5]:
    print(f"  {r['name']}: {r['change_pct']}% 娑▄r['up_count']}璺寋r['down_count']}")
```

---

## Layer 4: 璧勯噾闈?/ 绛圭爜灞傦紙V3.0 鏂板锛?
### 4.1 铻嶈祫铻嶅埜鏄庣粏

```python
def margin_trading(code: str, page_size: int = 30) -> list[dict]:
    """
    铻嶈祫铻嶅埜鏄庣粏锛堟棩绾э級銆?    杩斿洖: [{date, rzye(铻嶈祫浣欓), rzmre(铻嶈祫涔板叆), rqye(铻嶅埜浣欓), ...}]
    """
    data = eastmoney_datacenter(
        "RPTA_WEB_RZRQ_GGMX",
        filter_str=f'(SCODE="{code}")',
        page_size=page_size,
        sort_columns="DATE", sort_types="-1",
    )
    rows = []
    for row in data:
        rows.append({
            "date": str(row.get("DATE", ""))[:10],
            "rzye": row.get("RZYE", 0),       # 铻嶈祫浣欓(鍏?
            "rzmre": row.get("RZMRE", 0),      # 铻嶈祫涔板叆棰?            "rzche": row.get("RZCHE", 0),      # 铻嶈祫鍋胯繕棰?            "rqye": row.get("RQYE", 0),        # 铻嶅埜浣欓(鍏?
            "rqmcl": row.get("RQMCL", 0),      # 铻嶅埜鍗栧嚭閲?            "rqchl": row.get("RQCHL", 0),      # 铻嶅埜鍋胯繕閲?            "rzrqye": row.get("RZRQYE", 0),    # 铻嶈祫铻嶅埜浣欓鍚堣
        })
    return rows

# 鐢ㄦ硶
data = margin_trading("600519")
for d in data[:5]:
    print(f"{d['date']}: 铻嶈祫浣欓={d['rzye']/1e8:.2f}浜?铻嶅埜浣欓={d['rqye']/1e8:.2f}浜?)
```

### 4.2 澶у畻浜ゆ槗

```python
def block_trade(code: str, page_size: int = 20) -> list[dict]:
    """
    澶у畻浜ゆ槗璁板綍銆?    杩斿洖: [{date, price, vol, amount, buyer, seller, premium_pct}]
    """
    data = eastmoney_datacenter(
        "RPT_DATA_BLOCKTRADE",
        filter_str=f'(SECURITY_CODE="{code}")',
        page_size=page_size,
        sort_columns="TRADE_DATE", sort_types="-1",
    )
    rows = []
    for row in data:
        close = row.get("CLOSE_PRICE") or 0
        deal_price = row.get("DEAL_PRICE") or 0
        premium = ((deal_price / close - 1) * 100) if close else 0
        rows.append({
            "date": str(row.get("TRADE_DATE", ""))[:10],
            "price": deal_price,
            "close": close,
            "premium_pct": round(premium, 2),
            "vol": row.get("DEAL_VOLUME", 0),
            "amount": row.get("DEAL_AMT", 0),
            "buyer": row.get("BUYER_NAME", ""),
            "seller": row.get("SELLER_NAME", ""),
        })
    return rows

# 鐢ㄦ硶
data = block_trade("600519")
for d in data[:5]:
    print(f"{d['date']}: 浠锋牸={d['price']} 婧环={d['premium_pct']}% 涔版柟={d['buyer']}")
```

### 4.3 鑲′笢鎴锋暟鍙樺寲

```python
def holder_num_change(code: str, page_size: int = 10) -> list[dict]:
    """
    鑲′笢鎴锋暟鍙樺寲锛堝搴︾骇锛夈€?    杩斿洖: [{date, holder_num, change_num, change_ratio, avg_shares}]
    """
    data = eastmoney_datacenter(
        "RPT_HOLDERNUMLATEST",
        filter_str=f'(SECURITY_CODE="{code}")',
        page_size=page_size,
        sort_columns="END_DATE", sort_types="-1",
    )
    rows = []
    for row in data:
        rows.append({
            "date": str(row.get("END_DATE", ""))[:10],
            "holder_num": row.get("HOLDER_NUM", 0),
            "change_num": row.get("HOLDER_NUM_CHANGE", 0),
            "change_ratio": row.get("HOLDER_NUM_RATIO", 0),  # 鐜瘮%
            "avg_shares": row.get("AVG_FREE_SHARES", 0),     # 鎴峰潎鎸佽偂
        })
    return rows

# 鐢ㄦ硶
data = holder_num_change("600519")
for d in data[:5]:
    print(f"{d['date']}: 鑲′笢鏁?{d['holder_num']} 鍙樺寲={d['change_ratio']}% 鎴峰潎={d['avg_shares']}")
# 鑲′笢鎴锋暟鎸佺画鍑忓皯 = 绛圭爜闆嗕腑 = 涓诲姏鍚哥淇″彿
```

### 4.4 鍒嗙孩閫佽浆鍘嗗彶

```python
def dividend_history(code: str, page_size: int = 20) -> list[dict]:
    """
    鍒嗙孩閫佽浆鍘嗗彶銆?    杩斿洖: [{date, bonus_rmb(姣忚偂娲炬伅), transfer_ratio(杞姣斾緥), bonus_ratio(閫佽偂姣斾緥)}]
    """
    data = eastmoney_datacenter(
        "RPT_SHAREBONUS_DET",
        filter_str=f'(SECURITY_CODE="{code}")',
        page_size=page_size,
        sort_columns="EX_DIVIDEND_DATE", sort_types="-1",
    )
    rows = []
    for row in data:
        rows.append({
            "date": str(row.get("EX_DIVIDEND_DATE", ""))[:10],
            "bonus_rmb": row.get("PRETAX_BONUS_RMB", 0),    # 姣忚偂娲炬伅(绋庡墠)
            "transfer_ratio": row.get("TRANSFER_RATIO", 0),  # 姣?0鑲¤浆澧?            "bonus_ratio": row.get("BONUS_RATIO", 0),        # 姣?0鑲￠€佽偂
            "plan": row.get("ASSIGN_PROGRESS", ""),           # 杩涘害
        })
    return rows

# 鐢ㄦ硶
data = dividend_history("600519")
for d in data[:5]:
    print(f"{d['date']}: 姣忚偂娲炬伅={d['bonus_rmb']}鍏?杞={d['transfer_ratio']} 閫?{d['bonus_ratio']}")
```

### 4.5 涓偂璧勯噾娴侊紙120鏃ワ紝鏃ョ骇锛?
```python
import requests

def stock_fund_flow_120d(code: str) -> list[dict]:
    """
    涓偂璧勯噾娴侊紙鏃ョ骇锛屾渶杩?20涓氦鏄撴棩锛夈€?    杩斿洖: [{date, main_net(涓诲姏鍑€娴佸叆), small_net, mid_net, large_net, super_net}]
    鍗曚綅: 鍏?    """
    market_code = 1 if code.startswith("6") else 0
    url = "https://push2his.eastmoney.com/api/qt/stock/fflow/daykline/get"
    params = {
        "secid": f"{market_code}.{code}",
        "fields1": "f1,f2,f3,f7",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61,f62,f63,f64,f65",
        "lmt": "120",
    }
    headers = {
        "User-Agent": UA,
        "Referer": "https://quote.eastmoney.com/",
        "Origin": "https://quote.eastmoney.com",
    }
    try:
        r = em_get(url, params=params, headers=headers, timeout=15)
        d = r.json()
    except Exception as e:
        print(f"[WARN] push2 璧勯噾娴佽姹傚け璐? {e}")
        return []
    klines = d.get("data", {}).get("klines", [])

    rows = []
    for line in klines:
        parts = line.split(",")
        if len(parts) >= 7:
            rows.append({
                "date": parts[0],
                "main_net": float(parts[1]) if parts[1] != "-" else 0,
                "small_net": float(parts[2]) if parts[2] != "-" else 0,
                "mid_net": float(parts[3]) if parts[3] != "-" else 0,
                "large_net": float(parts[4]) if parts[4] != "-" else 0,
                "super_net": float(parts[5]) if parts[5] != "-" else 0,
            })
    return rows

# 鐢ㄦ硶
data = stock_fund_flow_120d("600519")
for d in data[-5:]:
    print(f"{d['date']}: 涓诲姏鍑€娴佸叆={d['main_net']/1e4:.0f}涓?瓒呭ぇ鍗?{d['super_net']/1e4:.0f}涓?)

# 缁熻杩?0鏃ヤ富鍔涘噣娴佸叆
recent_20 = data[-20:]
total_main = sum(d["main_net"] for d in recent_20)
print(f"\n杩?0鏃ヤ富鍔涚疮璁″噣娴佸叆: {total_main/1e8:.2f}浜?)
```

> **鈿狅笍 澶ч檰浣忓畢 IP 闂存瓏灏侀攣锛?18锛夛細** push2/push2his 绯诲垪瀵?*閮ㄥ垎澶ч檰浣忓畢瀹藉甫 IP** 鏈夎繛鎺ョ骇椋庢帶锛岃〃鐜颁负鍋跺彂 `HTTP 000`锛堣繛鎺ヨ鎷?瓒呮椂锛夋垨杩斿洖绌衡€斺€?*杩欎笉鏄唬鐮侀棶棰?*锛堝悓涓€浠ｇ爜鍦ㄥ叾浠栫綉缁?鏃舵瀹炴祴姝ｅ父锛夈€傞亣鍒版椂锛氣憼 闅斿嚑鍒嗛挓閲嶈瘯锛涒憽 鎹㈢綉缁滅幆澧冿紙濡傛墜鏈虹儹鐐癸級锛涒憿 闄嶄綆璇锋眰棰戠巼锛堣皟澶?`EM_MIN_INTERVAL`锛夈€傛棩绾ц祫閲戞祦鍔″疄鏇夸唬锛氫粛鍙敤 mootdx 绠楅噺浠凤紝鎴栨崲鏃舵閲嶈瘯銆?
---

## Layer 5: 鏂伴椈灞?
### 5.1 涓滆储涓偂鏂伴椈锛堢洿杩?search-api-web锛?
```python
import requests
import re
import json

def eastmoney_stock_news(code: str, page_size: int = 20) -> list[dict]:
    """
    涓滆储涓偂鏂伴椈锛圝SONP 鎺ュ彛锛夈€?    杩斿洖: [{title, content, time, source, url}]
    """
    # 鏋勯€?JSONP 鍙傛暟
    cb = "jQuery_news"
    url = "https://search-api-web.eastmoney.com/search/jsonp"
    inner_params = json.dumps({
        "uid": "",
        "keyword": code,
        "type": ["cmsArticleWebOld"],
        "client": "web",
        "clientType": "web",
        "clientVersion": "curr",
        "param": {"cmsArticleWebOld": {"searchScope": "default", "sort": "default",
                  "pageIndex": 1, "pageSize": page_size, "preTag": "", "postTag": ""}},
    }, separators=(',', ':'))
    params = {"cb": cb, "param": inner_params}
    headers = {"User-Agent": UA, "Referer": "https://so.eastmoney.com/"}
    r = em_get(url, params=params, headers=headers, timeout=15)

    # 瑙ｆ瀽 JSONP
    text = r.text
    json_str = text[text.index("(") + 1 : text.rindex(")")]
    d = json.loads(json_str)

    rows = []
    # 涓滆储瀹為檯杩斿洖閲?result.cmsArticleWebOld 鐩存帴灏辨槸鏂囩珷鍒楄〃锛堥潪 {list:[...]} 宓屽锛?    articles = d.get("result", {}).get("cmsArticleWebOld", []) or []
    for a in articles:
        rows.append({
            "title": re.sub(r'<[^>]+>', '', a.get("title", "")),
            "content": re.sub(r'<[^>]+>', '', a.get("content", ""))[:200],
            "time": a.get("date", ""),
            "source": a.get("mediaName", ""),
            "url": a.get("url", ""),
        })
    return rows

# 鐢ㄦ硶
news = eastmoney_stock_news("688017")
for n in news[:5]:
    print(f"  {n['time']} | {n['source']} | {n['title']}")
```

> **鈿狅笍 闂存瓏鎬ц繑鍥炵┖锛?18锛夛細** 閮ㄥ垎澶ч檰浣忓畢 IP 璋冩湰鎺ュ彛浼氬彧鎷垮埌 `passportWeb`锛堣偂姘戣祫鏂欙級鑰屾棤 `cmsArticleWebOld`锛堟枃绔犲垪琛級鈥斺€旇繖鏄笢璐㈠璇?IP 鐨勯棿姝囬鎺э紝闈炰唬鐮侀棶棰樸€備唬鐮佸凡瀵圭┖缁撴灉瀹夊叏杩斿洖 `[]`锛涢亣鍒版椂闅斿嚑鍒嗛挓鎴栨崲缃戠粶閲嶈瘯鍗冲彲銆?
### 5.2 璐㈣仈绀惧揩璁紙鐩磋繛 cls.cn锛夆€?鈿狅笍 宸蹭笅绾匡紝鏀圭敤 搂5.3

> **鈿狅笍 2026-05 宸插け鏁堬紙#14锛夛細** 璐㈣仈绀剧綉绔欒縼绉诲埌 Next.js 鏋舵瀯锛屾棫鐗堝叕寮€鎺ュ彛
> `cls.cn/nodeapi/telegraphList` 鍏ㄩ潰涓嬬嚎锛堣繑鍥?404锛夛紝鏂扮増 API 闇€绛惧悕璁よ瘉锛屾棤娉?> 鍏紑 HTTP 璋冪敤銆?*鍏ㄥ競鍦哄疄鏃跺揩璁鏀圭敤 搂5.3銆屼笢璐㈠叏鐞冭祫璁€?*锛?脳24 婊氬姩锛屽厤璐规棤 key锛夈€?> 涓嬮潰浠ｇ爜浠呬綔鍘嗗彶鍙傝€冿紝宸蹭笉鍙敤銆?
```python
import requests

def cls_telegraph(page_size: int = 50) -> list[dict]:
    """
    璐㈣仈绀剧數鎶ワ紙鍏ㄥ競鍦哄疄鏃跺揩璁級銆?    杩斿洖: [{title, content, time}]
    """
    url = "https://www.cls.cn/nodeapi/telegraphList"
    params = {"rn": str(page_size), "page": "1"}
    headers = {"User-Agent": UA, "Referer": "https://www.cls.cn/"}
    r = requests.get(url, params=params, headers=headers, timeout=10)
    d = r.json()

    rows = []
    for item in d.get("data", {}).get("roll_data", []):
        rows.append({
            "title": item.get("title", "") or item.get("brief", ""),
            "content": item.get("content", "") or item.get("brief", ""),
            "time": item.get("ctime", ""),
        })
    return rows

# 鐢ㄦ硶
news = cls_telegraph()
for n in news[:10]:
    print(f"  {n['time']} | {n['title'][:60]}")
```

### 5.3 涓滆储鍏ㄧ悆璧勮锛?x24锛?
```python
import requests

import uuid

def eastmoney_global_news(page_size: int = 50) -> list[dict]:
    """
    涓滄柟璐㈠瘜鍏ㄧ悆璐㈢粡璧勮锛?x24 婊氬姩锛夈€?    杩斿洖: [{title, summary, time}]
    """
    url = "https://np-weblist.eastmoney.com/comm/web/getFastNewsList"
    params = {
        "client": "web", "biz": "web_724",
        "fastColumn": "102", "sortEnd": "",
        "pageSize": str(page_size),
        "req_trace": str(uuid.uuid4()),
    }
    headers = {"User-Agent": UA, "Referer": "https://kuaixun.eastmoney.com/"}
    r = em_get(url, params=params, headers=headers, timeout=10)
    d = r.json()

    rows = []
    for item in d.get("data", {}).get("fastNewsList", []):
        rows.append({
            "title": item.get("title", ""),
            "summary": item.get("summary", "")[:200],
            "time": item.get("showTime", ""),
        })
    return rows

# 鐢ㄦ硶
news = eastmoney_global_news()
for n in news[:10]:
    print(f"  {n['time']} | {n['title']}")
```

---

## Layer 6: 鍩虹鏁版嵁灞?
### 6.1 mootdx 璐㈠姟蹇収锛?7瀛楁瀛ｆ姤鏁版嵁锛?
```python
from mootdx.quotes import Quotes

client = tdx_client()  # 瑙?Prerequisites 鐨?tdx_client() helper锛堣閬?0.11.x BESTIP bug锛涚瓑浠?Quotes.factory(market='std')锛?
# market: 0=娣卞湷, 1=涓婃捣
fin = client.finance(symbol='688017')
# 杩斿洖 37 涓瓧娈电殑瀛ｆ姤蹇収:
#   liutongguben(娴侀€氳偂鏈?, zongguben(鎬昏偂鏈?
#   eps(姣忚偂鏀剁泭), bvps(姣忚偂鍑€璧勪骇), roe(鍑€璧勪骇鏀剁泭鐜?)
#   profit(鍑€鍒╂鼎), income(涓昏惀鏀跺叆)
#   meigujingzichan(姣忚偂鍑€璧勪骇), meigugongjijin(姣忚偂鍏Н閲?
#   meiguweifeipeili(姣忚偂鏈垎閰嶅埄娑?
#   绛?7涓鎶ヨ储鍔″瓧娈?```

### 6.2 mootdx F10锛堝叕鍙告枃鏈祫鏂欙級

```python
from mootdx.quotes import Quotes

client = tdx_client()  # 瑙?Prerequisites 鐨?tdx_client() helper锛堣閬?0.11.x BESTIP bug锛涚瓑浠?Quotes.factory(market='std')锛?
# 9 澶х被鏂囨湰鏁版嵁:
categories = [
    "鏈€鏂版彁绀?, "鍏徃姒傚喌", "璐㈠姟鍒嗘瀽",
    "鑲′笢鐮旂┒", "鑲℃湰缁撴瀯", "璧勬湰杩愪綔",
    "涓氬唴鐐硅瘎", "琛屼笟鍒嗘瀽", "鍏徃澶т簨",
]
for cat in categories:
    text = client.F10(symbol='688017', name=cat)
    print(f"=== {cat} ===")
    print(text[:200] if text else "(绌?")
```

> **浼樺寲鎻愮ず锛?* "鑲′笢鐮旂┒" 涓殑銆?.鑲′笢鍙樺寲銆戠珷鑺傚惈澶ч噺鍘嗗彶鍗佸ぇ鑲′笢鍒楄〃锛屽疄娴?16000+ chars銆傚缓璁彧淇濈暀鏈€鏂颁竴鏈燂紙-70% token锛夈€?
### 6.3 涓滆储涓偂鍩烘湰闈紙鐩磋繛 push2 API锛?
```python
import requests

def eastmoney_stock_info(code: str) -> dict:
    """
    涓滆储涓偂鍩烘湰闈俊鎭€?    杩斿洖: {code, name, industry, total_shares, float_shares, mcap, float_mcap, list_date}
    """
    market_code = 1 if code.startswith("6") else 0
    url = "https://push2.eastmoney.com/api/qt/stock/get"
    params = {
        "fltt": "2", "invt": "2",
        "fields": "f57,f58,f84,f85,f127,f116,f117,f189,f43",
        "secid": f"{market_code}.{code}",
    }
    headers = {"User-Agent": UA}
    r = em_get(url, params=params, headers=headers, timeout=10)
    d = r.json().get("data", {})
    return {
        "code": d.get("f57", ""),
        "name": d.get("f58", ""),
        "industry": d.get("f127", ""),
        "total_shares": d.get("f84", 0),     # 鎬昏偂鏈?鑲?
        "float_shares": d.get("f85", 0),     # 娴侀€氳偂(鑲?
        "mcap": d.get("f116", 0),            # 鎬诲競鍊?鍏?
        "float_mcap": d.get("f117", 0),      # 娴侀€氬競鍊?鍏?
        "list_date": str(d.get("f189", "")), # 涓婂競鏃ユ湡 YYYYMMDD
        "price": d.get("f43", 0),
    }

# 鐢ㄦ硶
info = eastmoney_stock_info("688017")
print(f"{info['name']}({info['code']}): 琛屼笟={info['industry']} 鎬诲競鍊?{info['mcap']/1e8:.0f}浜?涓婂競={info['list_date']}")
```

### 6.4 鏂版氮璐㈡姤涓夎〃锛堣祫浜ц礋鍊鸿〃/鍒╂鼎琛?鐜伴噾娴侀噺琛級

```python
import requests

def sina_financial_report(code: str, report_type: str = "lrb", num: int = 8) -> list[dict]:
    """
    鏂版氮璐㈡姤涓夎〃銆?    code: 6浣嶄唬鐮?    report_type: "fzb"(璧勪骇璐熷€鸿〃) / "lrb"(鍒╂鼎琛? / "llb"(鐜伴噾娴侀噺琛?
    num: 鍙栨渶杩?N 鏈燂紙榛樿 8 鏈燂級
    杩斿洖: 鎸夋姤鍛婃湡鍊掑簭鐨勮褰曞垪琛紝姣忔湡涓€鏉?dict锛?          {"鎶ュ憡鏈?: "2026-03-31", "<绉戠洰>": "<鍊?", "<绉戠洰>_鍚屾瘮": <鍚屾瘮>, ...}
          锛坕tem_value 涓烘柊娴師濮嬪瓧绗︿覆鏁板€硷紝浠呭湪鏈夊悓姣旀椂闄?"_鍚屾瘮" 閿級
    """
    prefix = "sh" if code.startswith("6") else "sz"
    paper_code = f"{prefix}{code}"
    url = "https://quotes.sina.cn/cn/api/openapi.php/CompanyFinanceService.getFinanceReport2022"
    params = {
        "paperCode": paper_code,
        "source": report_type,
        "type": "0",
        "page": "1",
        "num": str(num),
    }
    headers = {"User-Agent": UA}
    r = requests.get(url, params=params, headers=headers, timeout=15)
    # 鏂版氮瀹為檯缁撴瀯: result.data.report_list 鏄€屾寜鎶ュ憡鏈?濡?'20260331')涓洪敭銆嶇殑 dict,
    # 姣忔湡瀵硅薄鐨?data 瀛楁鎵嶆槸琛岄」鍒楄〃 [{item_title, item_value, item_tongbi}]銆?    report_list = r.json().get("result", {}).get("data", {}).get("report_list", {}) or {}

    rows = []
    for period in sorted(report_list.keys(), reverse=True)[:num]:
        obj = report_list[period]
        rec = {"鎶ュ憡鏈?: f"{period[:4]}-{period[4:6]}-{period[6:8]}"}
        for it in obj.get("data", []) or []:
            title = it.get("item_title", "")
            if not title or it.get("item_value") is None:
                continue
            rec[title] = it.get("item_value")
            tongbi = it.get("item_tongbi")
            if tongbi not in (None, ""):
                rec[title + "_鍚屾瘮"] = tongbi
        rows.append(rec)
    return rows

# 鐢ㄦ硶: 鍒╂鼎琛?lrb = sina_financial_report("600519", "lrb")
for item in lrb[:3]:
    print(f"鎶ュ憡鏈? {item.get('鎶ュ憡鏈?, '')} 鍑€鍒╂鼎: {item.get('鍑€鍒╂鼎', '')}")

# 鐢ㄦ硶: 璧勪骇璐熷€鸿〃
fzb = sina_financial_report("600519", "fzb")

# 鐢ㄦ硶: 鐜伴噾娴侀噺琛?llb = sina_financial_report("600519", "llb")
```

---

## Layer 7: 鍏憡灞?
### 7.1 宸ㄦ疆鍏憡锛堢洿杩?cninfo.com.cn锛?
```python
import requests
from datetime import datetime

def _cninfo_ts_to_date(ts):
    """宸ㄦ疆 announcementTime 杩斿洖 Unix 姣鏁存暟锛岄渶杞崲涓烘棩鏈熷瓧绗︿覆銆?""
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts / 1000).strftime("%Y-%m-%d")
    return str(ts)[:10] if ts else ""

# 宸ㄦ疆 鑲＄エ鈫抩rgId 鏄犲皠锛堟ā鍧楃骇缂撳瓨锛岄娆¤皟鐢ㄦ椂鎷夊彇涓€娆★紝鍏ㄧ▼澶嶇敤锛?_CNINFO_ORGID_MAP = {}

def _cninfo_orgid(code: str) -> str:
    """鏌ヨ偂绁ㄧ湡瀹?orgId銆傚法娼?orgId 骞堕潪缁熶竴 `gssx0{code}` 鏍煎紡锛堝 601318鈫?900002221銆?    601398鈫抝jxt0000019銆?88017鈫?900041602锛夛紝纭紪鐮佷細瀵艰嚧澶ч噺鑲＄エ锛堝挨鍏?601xxx 娈碉級
    杩斿洖 totalAnnouncement=0銆佹煡涓嶅埌鍏憡锛?19锛夈€備紭鍏堝姩鎬佹煡瀹樻柟鏄犲皠琛紝鏌ヤ笉鍒板啀鍥為€€纭紪鐮併€?""
    global _CNINFO_ORGID_MAP
    if not _CNINFO_ORGID_MAP:
        try:
            r = requests.get("http://www.cninfo.com.cn/new/data/szse_stock.json",
                             headers={"User-Agent": UA}, timeout=15)
            _CNINFO_ORGID_MAP = {s["code"]: s["orgId"]
                                 for s in r.json().get("stockList", [])}
        except Exception as e:
            print(f"[WARN] 宸ㄦ疆 orgId 鏄犲皠琛ㄦ媺鍙栧け璐ワ紝鍥為€€纭紪鐮佽鍒? {e}")
    org = _CNINFO_ORGID_MAP.get(code)
    if org:
        return org
    # fallback锛氳€佹牸寮忥紙浠呴儴鍒嗚€佽偂绁ㄥ 600519/600036 閫傜敤锛?    if code.startswith("6"):
        return f"gssh0{code}"
    elif code.startswith("8") or code.startswith("4"):
        return f"gsbj0{code}"
    return f"gssz0{code}"

def cninfo_announcements(code: str, page_size: int = 30) -> list[dict]:
    """
    宸ㄦ疆鍏憡鍏ㄦ枃妫€绱€?    杩斿洖: [{title, type, date, url}]
    """
    url = "https://www.cninfo.com.cn/new/hisAnnouncement/query"
    org_id = _cninfo_orgid(code)   # 鍔ㄦ€佹煡鐪熷疄 orgId锛?19 淇锛岃嚜甯︾‖缂栫爜 fallback锛?
    payload = {
        "stock": f"{code},{org_id}",
        "tabName": "fulltext",
        "pageSize": str(page_size),
        "pageNum": "1",
        "column": "",
        "category": "",
        "plate": "",
        "seDate": "",
        "searchkey": "",
        "secid": "",
        "sortName": "",
        "sortType": "",
        "isHLtitle": "true",
    }
    headers = {
        "User-Agent": UA,
        "Content-Type": "application/x-www-form-urlencoded",
        "Referer": "https://www.cninfo.com.cn/new/disclosure",
        "Origin": "https://www.cninfo.com.cn",
    }
    r = requests.post(url, data=payload, headers=headers, timeout=15)
    d = r.json()

    rows = []
    for item in d.get("announcements", []) or []:
        rows.append({
            "title": item.get("announcementTitle", ""),
            "type": item.get("announcementTypeName", ""),
            "date": _cninfo_ts_to_date(item.get("announcementTime")),
            "url": f"https://www.cninfo.com.cn/new/disclosure/detail?annoId={item.get('announcementId', '')}",
        })
    return rows

# 鐢ㄦ硶
anns = cninfo_announcements("688017")
for a in anns[:10]:
    print(f"  {a['date']} | {a['type']} | {a['title']}")
```

### 7.2 mootdx F10 鍏憡鎽樿

```python
from mootdx.quotes import Quotes
client = tdx_client()  # 瑙?Prerequisites 鐨?tdx_client() helper锛堣閬?0.11.x BESTIP bug锛涚瓑浠?Quotes.factory(market='std')锛?text = client.F10(symbol='688017', name='鏈€鏂版彁绀?)
# 鍖呭惈鏈€杩戠殑鍏憡/鍒嗙孩/鑲′笢澶т細鍐宠绛夋憳瑕?```

---

## Layer 8: 鎵撴澘灞傦紙娑ㄥ仠 / 鐐告澘 / 璺屽仠 / 棰樻潗鎯呯华锛孷3.3.0 鏂板锛?
> 杩炴澘姊槦銆佺偢鏉跨巼銆佹檵绾х巼銆佹定鍋滃師鍥犻鏉愨€斺€旀墦鏉夸笌棰樻潗璺熻釜鐨勯珮棰戦渶姹傦紙#23 / #15锛夈€備笢璐㈠洓姹犺蛋 `push2ex.eastmoney.com`锛堜笌鐜版湁 push2 鍚屾簮锛屽凡绾冲叆 `em_get()` 闄愭祦锛夛紱娑ㄥ仠鍘熷洜棰樻潗澧炲己鐢ㄥ悓鑺遍『銆?*鍏ㄩ儴鍏嶇櫥褰曘€侀浂閴存潈銆?*

### 8.1 涓滆储娑ㄥ仠鏉挎睜 鈥?娑ㄥ仠 / 鐐告澘 / 璺屽仠 / 鏄ㄦ棩娑ㄥ仠

```python
import requests

ZTB_UT = "7eea3edcaed734bea9cbfc24409ed989"

def _fmt_zt_time(t) -> str:
    """娑ㄥ仠鏉挎椂闂存暣鏁?鈫?HH:MM:SS锛?2500 鈫?09:25:00锛夈€?""
    s = str(t).zfill(6)
    return f"{s[0:2]}:{s[2:4]}:{s[4:6]}"

def _em_zt_api(endpoint: str, sort: str, date: str) -> list[dict]:
    """涓滆储娑ㄥ仠鏉胯鎯呬腑蹇冮€氱敤璇锋眰锛坧ush2ex锛岃蛋 em_get 闄愭祦锛夈€?    endpoint: getTopicZTPool / getTopicZBPool / getTopicDTPool / getYesterdayZTPool
    杩斿洖 data.pool 鍘熷鍒楄〃锛坉ata 涓?null = 闈炰氦鏄撴棩 / 鍙傛暟閿欙級銆?""
    url = f"https://push2ex.eastmoney.com/{endpoint}"
    params = {"ut": ZTB_UT, "dpt": "wz.ztzt", "Pageindex": 0,
              "pagesize": 10000, "sort": sort, "date": date}
    headers = {"User-Agent": UA, "Referer": "https://quote.eastmoney.com/"}
    try:
        r = em_get(url, params=params, headers=headers, timeout=10)
        return (r.json().get("data") or {}).get("pool") or []
    except Exception as e:
        print(f"[WARN] 娑ㄥ仠鏉挎睜 {endpoint} 璇锋眰澶辫触: {e}")
        return []

def em_zt_pool(date: str) -> list[dict]:
    """娑ㄥ仠姹犮€俤ate=YYYYMMDD锛堜氦鏄撴棩锛夈€?    杩斿洖姣忓彧: code/name/price/pct/amount/float_cap/turnover/limit_days(杩炴澘鏁?/
    first_seal/last_seal(灏佹澘鏃堕棿)/seal_fund(灏佹澘璧勯噾,鍏?/break_times(鐐告澘娆℃暟)/
    industry/zt_stat(N澶㎝鏉?"""
    out = []
    for p in _em_zt_api("getTopicZTPool", "fbt:asc", date):
        out.append({"code": p["c"], "name": p["n"], "price": p["p"] / 1000,
            "pct": round(p["zdp"], 2), "amount": p["amount"], "float_cap": p["ltsz"],
            "turnover": round(p["hs"], 2), "limit_days": p["lbc"],
            "first_seal": _fmt_zt_time(p["fbt"]), "last_seal": _fmt_zt_time(p["lbt"]),
            "seal_fund": p["fund"], "break_times": p["zbc"], "industry": p.get("hybk", ""),
            "zt_stat": f'{(p.get("zttj") or {}).get("days","?")}澶﹞(p.get("zttj") or {}).get("ct","?")}鏉?})
    return out

def em_zb_pool(date: str) -> list[dict]:
    """鐐告澘姹狅紙娑ㄥ仠鍚庡紑鏉匡級銆傝繑鍥?code/name/price/limit_price(娑ㄥ仠浠?/pct/turnover/
    first_seal/break_times/amplitude(鎸箙)/speed(娑ㄩ€?/industry/zt_stat"""
    out = []
    for p in _em_zt_api("getTopicZBPool", "fbt:asc", date):
        out.append({"code": p["c"], "name": p["n"], "price": p["p"] / 1000,
            "limit_price": p["ztp"] / 1000, "pct": round(p["zdp"], 2),
            "turnover": round(p["hs"], 2), "first_seal": _fmt_zt_time(p["fbt"]),
            "break_times": p["zbc"], "amplitude": round(p["zf"], 2),
            "speed": round(p["zs"], 2), "industry": p.get("hybk", ""),
            "zt_stat": f'{(p.get("zttj") or {}).get("days","?")}澶﹞(p.get("zttj") or {}).get("ct","?")}鏉?})
    return out

def em_dt_pool(date: str) -> list[dict]:
    """璺屽仠姹犮€傝繑鍥?code/name/price/pct/turnover/pe/seal_fund(灏佸崟璧勯噾)/last_seal/
    board_amount(鏉夸笂鎴愪氦棰?/dt_days(杩炵画璺屽仠)/open_times(寮€鏉挎鏁?/industry"""
    out = []
    for p in _em_zt_api("getTopicDTPool", "fund:asc", date):
        out.append({"code": p["c"], "name": p["n"], "price": p["p"] / 1000,
            "pct": round(p["zdp"], 2), "turnover": round(p["hs"], 2), "pe": p.get("pe"),
            "seal_fund": p["fund"], "last_seal": _fmt_zt_time(p["lbt"]),
            "board_amount": p.get("fba"), "dt_days": p.get("days"),
            "open_times": p.get("oc"), "industry": p.get("hybk", "")})
    return out

def em_yzt_pool(date: str) -> list[dict]:
    """鏄ㄦ棩娑ㄥ仠姹狅紙鏄ㄦ定鍋滀粖琛ㄧ幇锛岀畻鏅嬬骇鐜?璧氶挶鏁堝簲锛夈€傝繑鍥?code/name/price/
    pct(浠婃棩娑ㄥ箙)/turnover/amplitude/speed/y_first_seal(鏄ㄥ皝鏉挎椂闂?/
    y_limit_days(鏄ㄨ繛鏉?/industry/zt_stat"""
    out = []
    for p in _em_zt_api("getYesterdayZTPool", "zs:desc", date):
        out.append({"code": p["c"], "name": p["n"], "price": p["p"] / 1000,
            "pct": round(p["zdp"], 2), "turnover": round(p["hs"], 2),
            "amplitude": round(p["zf"], 2), "speed": round(p["zs"], 2),
            "y_first_seal": _fmt_zt_time(p["yfbt"]), "y_limit_days": p["ylbc"],
            "industry": p.get("hybk", ""), "zt_stat": f'{(p.get("zttj") or {}).get("days","?")}澶﹞(p.get("zttj") or {}).get("ct","?")}鏉?})
    return out

# 鐢ㄦ硶
zt = em_zt_pool("20260626")
print(f"浠婃棩娑ㄥ仠 {len(zt)} 鍙?)
for s in zt[:3]:
    print(f"  {s['name']} {s['zt_stat']} 灏佹澘{s['seal_fund']/1e8:.2f}浜?{s['industry']}")
```

> **鍧戯細** 鈶?浠锋牸瀛楁 `price`/`limit_price` 宸?梅1000锛堝師濮嬪€兼槸 脳1000 鏁存暟锛夈€傗憽 鍥涙睜鍙湁 `sort` 涓嶅悓锛堟定鍋?鐐告澘=`fbt:asc`銆佽穼鍋?`fund:asc`銆佹槰娑ㄥ仠=`zs:desc`锛夛紝`dpt` 閮芥槸 `wz.ztzt`銆傗憿 `date` 蹇呴』浼犱氦鏄撴棩锛岄潪浜ゆ槗鏃?`data` 杩斿洖 null銆傗懀 閲戦鍗曚綅鍧囦负**鍏?*銆?
### 8.2 鍚岃姳椤烘定鍋滄彮绉?鈥?娑ㄥ仠鍘熷洜棰樻潗 + 灏佹澘鎴愬姛鐜?+ 鏉垮瀷

```python
from datetime import datetime

def ths_limit_up_pool(date: str) -> list[dict]:
    """鍚岃姳椤烘定鍋滄彮绉橈紙娑ㄥ仠鍘熷洜 + 灏佹澘璐ㄩ噺澧炲己婧愶級銆俤ate=YYYYMMDD銆?    杩斿洖姣忓彧: code/name/price/pct/reason(娑ㄥ仠鍘熷洜棰樻潗)/board_type(鎹㈡墜鏉?涓€瀛楁澘/T瀛楁澘)/
    seal_rate(灏佹澘鎴愬姛鐜?0~1)/break_times(鐐告澘娆℃暟)/seal_amount(灏佸崟棰?鍏?/
    high_days(鍑犲ぉ鍑犳澘)/first_time(棣栨娑ㄥ仠鏃堕棿)/is_again(鏄惁鍥炲皝 0/1)"""
    url = "https://data.10jqka.com.cn/dataapi/limit_up/limit_up_pool"
    params = {"page": 1, "limit": 200,
              "field": "199112,10,9001,330323,330324,330325,9002,330329,133971,133970,1968584,3475914,9003,9004",
              "filter": "HS,GEM2STAR", "order_field": "330324", "order_type": "0", "date": date}
    try:
        r = requests.get(url, params=params, headers={"User-Agent": UA}, timeout=10)
        info = (r.json().get("data") or {}).get("info", [])
    except Exception as e:
        print(f"[WARN] 鍚岃姳椤烘定鍋滄彮绉樿姹傚け璐? {e}")
        return []
    out = []
    for it in info:
        ft = it.get("first_limit_up_time")
        out.append({"code": it.get("code"), "name": it.get("name"),
            "price": it.get("latest"), "pct": it.get("change_rate"),
            "reason": it.get("reason_type", ""), "board_type": it.get("limit_up_type", ""),
            "seal_rate": it.get("limit_up_suc_rate"), "break_times": it.get("open_num") or 0,
            "seal_amount": it.get("order_amount"), "high_days": it.get("high_days", ""),
            "first_time": datetime.fromtimestamp(int(ft)).strftime("%H:%M:%S") if ft else "",
            "is_again": it.get("is_again_limit")})
    return out

# 鐢ㄦ硶: 娑ㄥ仠鍘熷洜棰樻潗褰掑洜
for s in ths_limit_up_pool("20260626")[:5]:
    print(f"  {s['name']} {s['high_days']} | {s['reason']} | 灏佹澘鐜噞s['seal_rate']}")
```

> **鍧戯細** `first_limit_up_time` 鏄?**Unix 绉掓椂闂存埑**锛堣 `datetime.fromtimestamp`锛夛紝涓嶆槸 HHMMSS銆俙field` 閭ｄ覆鏄悓鑺遍『鍐呴儴瀛楁 ID锛岀収鎶勫嵆鍙€俙filter=HS,GEM2STAR` 鎺у埗鏉垮潡鑼冨洿锛堟勃娣变富鏉?+ 鍒涗笟鏉?+ 绉戝垱鏉匡級銆?
### 8.3 鎵撴澘鎯呯华閫熺畻 鈥?鐐告澘鐜?/ 杩炴澘楂樺害 / 杩炴澘姊槦

```python
def limit_up_sentiment(date: str) -> dict:
    """鎵撴澘鎯呯华娓╁害璁★細杩炴澘姊槦 + 鐐告澘鐜?+ 娑ㄨ穼鍋滃姣斻€?""
    zt, zb, dt = em_zt_pool(date), em_zb_pool(date), em_dt_pool(date)
    ladder = {}
    for s in zt:
        ladder[s["limit_days"]] = ladder.get(s["limit_days"], 0) + 1
    zt_n, zb_n = len(zt), len(zb)
    return {"date": date, "zt_count": zt_n, "zb_count": zb_n, "dt_count": len(dt),
        "break_rate": round(zb_n / (zt_n + zb_n) * 100, 1) if (zt_n + zb_n) else 0,  # 鐐告澘鐜?
        "max_height": max((s["limit_days"] for s in zt), default=0),                 # 鏈€楂樿繛鏉?        "ladder": dict(sorted(ladder.items()))}                                       # 杩炴澘姊槦 {鏉挎暟:瀹舵暟}

# 鐢ㄦ硶
s = limit_up_sentiment("20260626")
print(f"娑ㄥ仠{s['zt_count']} 鐐告澘{s['zb_count']}(鐐告澘鐜噞s['break_rate']}%) "
      f"璺屽仠{s['dt_count']} 鏈€楂榹s['max_height']}杩炴澘")
print(f"杩炴澘姊槦: {s['ladder']}")
```

> 鏅嬬骇鐜囷紙鏄ㄦ定鍋滀粖浠嶆定鍋?/ 鏄ㄦ定鍋滄€绘暟锛夊彲鐢?`em_yzt_pool()` 鐨?`pct >= 9.8` 璁℃暟闄や互鎬绘暟鑷畻銆?
---

## Layer 9: ETF 鏈熸潈灞傦紙T鍨嬫姤浠?+ 甯岃厞瀛楁瘝 + IV锛孷3.3.0 鏂板锛?
> 50ETF / 300ETF / 绉戝垱50ETF / 500ETF 鏈熸潈锛?13锛夈€傝蛋鏂版氮婧愨€斺€?*T鍨嬫姤浠枫€佸笇鑵婂瓧姣嶃€侀殣鍚尝鍔ㄧ巼鍧囩敱浜ゆ槗鎵€/鏂版氮棰勫厛绠楀ソ锛屾棤闇€鏈湴绠?BSM**銆傚厤璐圭洿杩烇紝鍞竴娉ㄦ剰甯?`Referer`銆?
### 9.1 鍚堢害娓呭崟 + T鍨嬫姤浠?+ 甯岃厞瀛楁瘝

```python
import requests

SINA_OPT_HDR = {"Referer": "https://stock.finance.sina.com.cn/", "User-Agent": UA}

def _opt_f(x):
    try: return float(x)
    except Exception: return x

def _sina_opt_list(param: str) -> list:
    """鏂版氮 hq.sinajs.cn 鍙栧€硷紙GBK锛岄€楀彿鍒嗛殧锛屽幓 var hq_str_XXX="..." 澹筹級銆?""
    r = requests.get(f"https://hq.sinajs.cn/list={param}", headers=SINA_OPT_HDR, timeout=10)
    r.encoding = "gbk"
    t = r.text
    return t.split('"')[1].split(",") if '"' in t else []

def sina_option_codes(underlying: str = "510050", call: bool = True) -> dict:
    """ETF鏈熸潈鍚堢害娓呭崟銆倁nderlying: 510050/510300/588000/510500銆俢all=True璁よ喘/False璁ゆ步銆?    杩斿洖 {鏈堜唤YYMM: [鍚堢害浠ｇ爜,...]}锛岀涓€涓?key 鍗宠繎鏈堛€?""
    cate = {"510050": "50ETF", "510300": "300ETF",
            "588000": "绉戝垱50ETF", "510500": "500ETF"}.get(underlying, "50ETF")
    url = ("https://stock.finance.sina.com.cn/futures/api/openapi.php/"
           f"StockOptionService.getStockName?exchange=null&cate={cate}")
    try:
        months = requests.get(url, headers=SINA_OPT_HDR, timeout=10).json()["result"]["data"]["contractMonth"]
    except Exception as e:
        print(f"[WARN] 鏈熸潈鏈堜唤鑾峰彇澶辫触: {e}")
        return {}
    months = [m.replace("-", "")[2:] for m in months[1:]]  # 涓㈤涓紝杞?YYMM
    flag = "OP_UP_" if call else "OP_DOWN_"
    out = {}
    for m in months:
        codes = [c.replace("CON_OP_", "") for c in _sina_opt_list(f"{flag}{underlying}{m}")
                 if c.startswith("CON_OP_")]
        if codes:
            out[m] = codes
    return out

def sina_option_tquote(code: str) -> dict:
    """鏈熸潈T鍨嬫姤浠枫€傝繑鍥?bid_vol/bid/last/ask/ask_vol/open_interest(鎸佷粨閲?/pct/
    strike(琛屾潈浠?/prev_close/open/limit_up/limit_down/name/amplitude/high/low/volume/amount銆?""
    v = _sina_opt_list(f"CON_OP_{code}")
    if len(v) < 43:
        return {}
    return {"bid_vol": _opt_f(v[0]), "bid": _opt_f(v[1]), "last": _opt_f(v[2]),
        "ask": _opt_f(v[3]), "ask_vol": _opt_f(v[4]), "open_interest": _opt_f(v[5]),
        "pct": _opt_f(v[6]), "strike": _opt_f(v[7]), "prev_close": _opt_f(v[8]),
        "open": _opt_f(v[9]), "limit_up": _opt_f(v[10]), "limit_down": _opt_f(v[11]),
        "name": v[37], "amplitude": _opt_f(v[38]), "high": _opt_f(v[39]),
        "low": _opt_f(v[40]), "volume": _opt_f(v[41]), "amount": _opt_f(v[42])}

def sina_option_greeks(code: str) -> dict:
    """鏈熸潈甯岃厞瀛楁瘝 + 闅愬惈娉㈠姩鐜囥€傝繑鍥?name/volume/delta/gamma/theta/vega/
    iv(闅愬惈娉㈠姩鐜?灏忔暟)/high/low/trade_code/strike/last/theory(鐞嗚浠峰€?銆?""
    raw = _sina_opt_list(f"CON_SO_{code}")
    if len(raw) < 16:
        return {}
    v = [raw[0]] + raw[4:]  # 鈿狅笍 raw[1:4] 鏄?3 涓┖涓诧紝蹇呴』璺宠繃鍚﹀垯瀛楁閿欎綅
    return {"name": v[0], "volume": _opt_f(v[1]), "delta": _opt_f(v[2]),
        "gamma": _opt_f(v[3]), "theta": _opt_f(v[4]), "vega": _opt_f(v[5]),
        "iv": _opt_f(v[6]), "high": _opt_f(v[7]), "low": _opt_f(v[8]),
        "trade_code": v[9], "strike": _opt_f(v[10]), "last": _opt_f(v[11]), "theory": _opt_f(v[12])}

# 鐢ㄦ硶: 鍙?50ETF 杩戞湀骞冲€奸檮杩戜竴妗ｇ殑 T鍨嬫姤浠?+ 甯岃厞瀛楁瘝
codes = sina_option_codes("510050", call=True)
near = list(codes)[0]                       # 杩戞湀
c = codes[near][len(codes[near]) // 2]      # 涓棿妗ｂ増骞冲€奸檮杩?q, g = sina_option_tquote(c), sina_option_greeks(c)
print(f"{q['name']} 琛屾潈浠穥q['strike']} 鏈€鏂皗q['last']} 鎸佷粨{q['open_interest']:.0f}")
print(f"  Delta={g['delta']} Gamma={g['gamma']} Theta={g['theta']} Vega={g['vega']} IV={g['iv']:.2%}")
```

> **鍧戯細** 鈶?鏂版氮婧?**GBK 缂栫爜**銆?*閫楀彿鍒嗛殧**銆侀渶鍘?`var hq_str_XXX="..."` 澹炽€傗憽 蹇呭甫 `Referer: https://stock.finance.sina.com.cn/`锛屽惁鍒?403銆傗憿 甯岃厞瀛楁瘝瑙ｆ瀽 **`[raw[0]] + raw[4:]`**鈥斺€擿raw[1:4]` 鏄?3 涓┖涓诧紝涓嶈烦杩囧垯 Delta/IV 鍏ㄩ敊浣嶃€傗懀 `iv` 鏄皬鏁帮紙0.1735 = 17.35%锛夈€傗懁 300ETF(510300)銆佺鍒?0ETF(588000) 鍚岀悊锛屾崲 `underlying` 鍗冲彲銆?
---

## Layer 10: 鑸嗘儏浜掑姩灞傦紙浜掑姩鏄撻棶绛?+ 鐑 + 浜烘皵姒滐紝V3.3.0 鏂板锛?
> 鎶曡祫鑰呬簰鍔ㄩ棶绛?+ 甯傚満鐑害鈥斺€擜I 闂瓟涓庨€夐鐨勭嫭瀹朵俊婧愩€?*浜掑姩鏄?*锛堝法娼級鑳界瓟"鍏徃鎬庝箞鍥炲簲鏌愪紶闂?鍒╁ソ"锛屽埆澶勬嬁涓嶅埌锛?*鍚岃姳椤虹儹姒?/ 涓滆储浜烘皵姒?*缁?褰撲笅鏈€鐑釜鑲?+ 琚綊鍒颁粈涔堟蹇靛湪鐐?銆傚叏閮ㄥ厤鐧诲綍銆侀浂閴存潈銆?
### 10.1 浜掑姩鏄撻棶绛旓紙宸ㄦ疆 鈥?鎶曡祫鑰呮彁闂?+ 鍏徃鍥炲锛?
```python
import requests
from datetime import datetime

def cninfo_irm(code: str, page_size: int = 30, page_num: int = 1) -> list[dict]:
    """浜掑姩鏄撻棶绛旓紙娣辨勃缁熶竴璧板法娼級銆俢ode: 6浣嶄唬鐮併€?    杩斿洖姣忔潯: code/company/question(鎶曡祫鑰呮彁闂?/answer(鍏徃鍥炲,None=鏈洖澶?/
    answerer(鍥炵瓟鏂?/ask_time銆?""
    try:
        r1 = requests.post("https://irm.cninfo.com.cn/newircs/index/queryKeyboardInfo",
            data={"keyWord": code}, headers={"User-Agent": UA}, timeout=10)
        d1 = r1.json().get("data") or []
        if not d1:
            return []
        org_id = d1[0].get("secid")
        # 鈿狅笍 绗簩姝ュ弬鏁板繀椤绘斁 query string锛圥OST 浣?body 绌猴級锛屽惁鍒?HTTP 400
        params = {"_t": 1, "stockcode": code, "orgId": org_id, "pageSize": page_size,
                  "pageNum": page_num, "keyWord": "", "startDay": "", "endDay": ""}
        r2 = requests.post("https://irm.cninfo.com.cn/newircs/company/question",
            params=params, headers={"User-Agent": UA}, timeout=10)
        rows = r2.json().get("rows") or []
    except Exception as e:
        print(f"[WARN] 浜掑姩鏄撹姹傚け璐? {e}")
        return []
    out = []
    for it in rows:
        pd = it.get("pubDate")
        out.append({"code": it.get("stockCode"), "company": it.get("companyShortName"),
            "question": it.get("mainContent"), "answer": it.get("attachedContent"),
            "answerer": it.get("attachedAuthor"),
            "ask_time": datetime.fromtimestamp(pd / 1000).strftime("%Y-%m-%d %H:%M") if pd else ""})
    return out

# 鐢ㄦ硶: 鐪嬪叕鍙告€庝箞鍥炲簲鎶曡祫鑰呭叧鍒?for q in cninfo_irm("002594", page_size=30):
    if q["answer"]:
        print(f"  Q: {q['question'][:30]}\n  A[{q['answerer']}]: {q['answer'][:50]}")
```

> **鍧戯細** 鈶?绗簩姝ュ弬鏁版斁 **query string**锛堜笉鏄?body锛夛紝鍚﹀垯 400銆傗憽 `orgId` 鍙栬嚜绗竴姝ョ殑 `secid`锛堝嵆渚垮墠缂€鏄?`gshk`锛岄潬 `stockcode` 杩囨护鐓ф牱鎷?A 鑲￠棶绛旓級銆傗憿 鏈€鏂版彁闂父鏈洖澶嶏紙`answer=None`锛夛紝鍥炲鐜囧洜鍏徃鑰屽紓锛堝疄娴嬬珛璁簿瀵?002475 鍥炲澶氥€佷含涓滄柟 000725 鍑犱箮涓嶅洖锛夈€傗懀 鏃堕棿鏄绉掓椂闂存埑銆?
### 10.2 鍚岃姳椤虹儹姒?+ 涓滆储浜烘皵姒滐紙甯傚満鐑害 + 姒傚康鍛戒腑锛?
```python
EM_HOT_BODY = {"appId": "appId01", "globalId": "786e4c21-70dc-435a-93bb-38"}

def ths_hot_list(period: str = "hour") -> list[dict]:
    """鍚岃姳椤虹儹姒滐紙鍗曟帴鍙ｆ嬁鍚嶇О+浜烘皵+姒傚康鏍囩+鎺掑悕鍙樺寲锛夈€俻eriod: hour/day銆?    杩斿洖姣忓彧: rank/code/name/heat(浜烘皵鍊?/pct/rank_chg(鎺掑悕鍙樺寲)/concepts(姒傚康鏍囩)/tag銆?""
    try:
        r = requests.get("https://dq.10jqka.com.cn/fuyao/hot_list_data/out/hot_list/v1/stock",
            params={"stock_type": "a", "type": period, "list_type": "normal"},
            headers={"User-Agent": UA}, timeout=10)
        lst = (r.json().get("data") or {}).get("stock_list") or []
    except Exception as e:
        print(f"[WARN] 鍚岃姳椤虹儹姒滃け璐? {e}")
        return []
    out = []
    for it in lst:
        tag = it.get("tag") or {}
        out.append({"rank": it.get("order"), "code": it.get("code"), "name": it.get("name"),
            "heat": it.get("rate"), "pct": it.get("rise_and_fall"), "rank_chg": it.get("hot_rank_chg"),
            "concepts": tag.get("concept_tag") or [], "tag": tag.get("popularity_tag", "")})
    return out

def em_hot_rank(top: int = 50) -> list[dict]:
    """涓滆储浜烘皵姒滐紙鎺掑悕 + 鎺掑悕鍙樺寲 + 鍚嶇О/浠锋牸锛夈€傝繑鍥?rank/code/name/price/pct/rank_chg銆?""
    try:
        r = requests.post("https://emappdata.eastmoney.com/stockrank/getAllCurrentList",
            json={**EM_HOT_BODY, "marketType": "", "pageNo": 1, "pageSize": top},
            headers={"User-Agent": UA}, timeout=10)
        data = r.json().get("data") or []
        if not data:
            return []
        # 浜烘皵姒滃彧缁欏甫鍓嶇紑浠ｇ爜锛岀敤 push2 ulist.np 鎵归噺琛ュ悕绉?浠锋牸
        secids = [("0." if it["sc"].startswith("SZ") else "1.") + it["sc"][2:] for it in data]
        u = requests.get("https://push2.eastmoney.com/api/qt/ulist.np/get",
            params={"ut": "f057cbcbce2a86e2866ab8877db1d059", "fltt": 2, "invt": 2,
                    "fields": "f14,f3,f12,f2", "secids": ",".join(secids)},
            headers={"User-Agent": UA, "Referer": "https://quote.eastmoney.com/"}, timeout=10)
        diff = (u.json().get("data") or {}).get("diff") or []
        if isinstance(diff, dict):                       # push2 鐨?diff 鏈夋椂鏄?dict
            diff = list(diff.values())
        nm = {x["f12"]: (x.get("f14"), x.get("f2"), x.get("f3")) for x in diff}
    except Exception as e:
        print(f"[WARN] 涓滆储浜烘皵姒滃け璐? {e}")
        return []
    out = []
    for it in data:
        code = it["sc"][2:]
        name, price, pct = nm.get(code, ("", None, None))
        out.append({"rank": it["rk"], "code": code, "name": name,
            "price": price, "pct": pct, "rank_chg": it.get("hisRc")})
    return out

def em_hot_concept(code: str) -> list[dict]:
    """涓滆储涓偂鐑棬姒傚康鍛戒腑锛堣繖鍙エ褰撲笅琚競鍦哄綊鍒板摢浜涙蹇靛湪鐐掞級銆?    杩斿洖 [{concept, bk, hit(鍛戒腑鐑害)}, ...]锛屾寜鐑害闄嶅簭銆?""
    try:
        prefix = "SH" if code.startswith("6") else "SZ"
        r = requests.post("https://emappdata.eastmoney.com/stockrank/getHotStockRankList",
            json={**EM_HOT_BODY, "srcSecurityCode": prefix + code},
            headers={"User-Agent": UA}, timeout=10)
        data = r.json().get("data") or []
    except Exception as e:
        print(f"[WARN] 涓滆储涓偂姒傚康澶辫触: {e}")
        return []
    return [{"concept": x.get("conceptName"), "bk": x.get("conceptId"),
             "hit": x.get("hitCount")} for x in data]

# 鐢ㄦ硶
for s in ths_hot_list()[:5]:
    print(f"  #{s['rank']} {s['name']} 鐑害{s['heat']} {s['concepts']} {s['tag']}")
hot = em_hot_rank(10)        # 涓滆储浜烘皵姒?TOP10
print("浜烘皵绗竴:", hot[0]["name"], "姒傚康鍛戒腑:", em_hot_concept(hot[0]["code"])[:3])
```

> **鍧戯細** 鈶?涓滆储浜烘皵姒?`getAllCurrentList` 鍙繑鍥炲甫鍓嶇紑浠ｇ爜锛圫Z/SH锛夛紝鍚嶇О瑕佸啀璧?`ulist.np` 琛ワ紙`SZ`鈫抈0.`銆乣SH`鈫抈1.`锛夈€傗憽 `ulist.np` 鐨?`diff` 鍋跺皵鏄?dict锛堟寜搴忓彿涓洪敭锛夛紝宸插仛 `list(values())` 褰掍竴鍖栥€傗憿 鍚岃姳椤虹儹姒?`type` 鍙€?`hour`/`day`銆?
---

## 浼板€艰绠楀叕寮?
### 鍓嶅悜PE

```python
def forward_pe(price: float, eps_forecast: float) -> float:
    """鍓嶅悜PE = 褰撳墠鑲′环 / 鏈潵骞村害涓€鑷撮鏈烢PS"""
    if eps_forecast <= 0:
        return float("inf")
    return price / eps_forecast
```

### PE娑堝寲鏃堕棿

```python
import math

def pe_digestion(current_pe: float, cagr: float, target_pe: float = 30) -> float:
    """
    褰撳墠PE娑堝寲鍒扮洰鏍嘝E闇€瑕佸灏戝勾銆?    target_pe 鍥哄畾30x锛圓鑲℃垚闀胯偂鍚堢悊浼板€奸敋鐐癸級銆?    cagr: 鐢?涓嬩竴骞碋PS / 褰撳勾EPS - 1
    """
    if current_pe <= target_pe:
        return 0.0
    if cagr <= 0:
        return float("inf")
    return math.log(current_pe / target_pe) / math.log(1 + cagr)
```

### PEG

```python
def calc_peg(pe: float, cagr: float) -> float:
    """
    PEG = 鍓嶅悜PE / (CAGR * 100)
    PEG < 1   鈫?渚垮疁
    PEG 1-1.5 鈫?鍚堢悊
    PEG > 1.5 鈫?璐?    """
    if cagr <= 0:
        return float("inf")
    return pe / (cagr * 100)
```

### 鎶曡祫妗嗘灦閫熸煡

```
澹佸瀿 鈫?澧為€?鈫?PE娑堝寲 鈫?PEG鏍￠獙

1. 鏈夊鍨掑悧锛?tech_moat / capacity_moat) 鈫?娌℃湁鍒欐帓闄?2. 澧為€熷灏戯紵(CAGR > 30% 鎵嶆湁鎰忎箟)
3. PE澶氫箙娑堝寲鍒?0x锛?< 2骞村悎鐞? > 4骞村お璐?
4. PEG澶氬皯锛?< 1 渚垮疁, 1-1.5 鍚堢悊, > 1.5 璐?

30x PE 閿氱偣: A鑲℃垚闀胯偂鐨勫悎鐞嗕及鍊奸噸鍔涚嚎锛屾墍鏈夎涓氱粺涓€鐢?0x銆?鏈熸潈瀹氫环渚嬪: PEG > 3 浣嗗鍨掓瀬娣辨椂锛屾湰璐ㄦ槸鐪嬫定鏈熸潈锛屼笉閫傜敤PEG妗嗘灦銆?```

---

## 瀹屾暣璋冪爺娴佺▼

### 娴佺▼ A: 鍗曠エ瀹屾暣浼板€硷紙30绉掞級

```python
import requests
import urllib.request
import math
import pandas as pd

def full_valuation(code: str) -> dict:
    """鍗曠エ瀹屾暣浼板€煎垎鏋?""
    # 1. 鑵捐瀹炴椂琛屾儏
    prefix = "sh" if code.startswith(("6","9")) else ("bj" if code.startswith("8") else "sz")
    url = f"https://qt.gtimg.cn/q={prefix}{code}"
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0")
    resp = urllib.request.urlopen(req, timeout=10)
    data = resp.read().decode("gbk")
    vals = data.split('"')[1].split("~")
    price = float(vals[3])
    mcap = float(vals[44])
    pe_ttm = float(vals[39]) if vals[39] else 0
    pb = float(vals[46]) if vals[46] else 0

    # 2. 鏈烘瀯涓€鑷撮鏈燂紙鐩磋繛鍚岃姳椤猴級
    df = ths_eps_forecast(code)
    eps_cur = eps_next = None
    analyst_count = 0
    if not df.empty and len(df.columns) >= 3:
        # 鎸夊垪鍚嶅彇銆屽潎鍊笺€?鏈烘瀯涓€鑷撮鏈烢PS锛堣 ths_eps_forecast 鏂囨。锛夈€?        # 涓嶆寜 iloc 浣嶇疆鍙栤€斺€斿悓鑺遍『琛ㄦ牸鍒楀簭浼氬彉锛涗笖鏃х増璇敤 iloc[2]锛濄€屾渶灏忓€笺€?        # 褰撴垚涓€鑷撮鏈燂紝瀵艰嚧 pe_forward/PEG 绯荤粺鎬у亸宸紝姝ゅ涓€骞朵慨姝ｃ€?        def _pick(row, name):
            for c in df.columns:
                if name in str(c):
                    return row.get(c)
            return None
        try:
            r0 = df.iloc[0]
            v = _pick(r0, "鍧囧€?);          eps_cur = float(v) if pd.notna(v) else None
            cnt = _pick(r0, "棰勬祴鏈烘瀯鏁?);  analyst_count = int(cnt) if pd.notna(cnt) else 0
            if len(df) >= 2:
                vn = _pick(df.iloc[1], "鍧囧€?); eps_next = float(vn) if pd.notna(vn) else None
        except (ValueError, TypeError) as e:
            print(f"[WARN] full_valuation EPS 瑙ｆ瀽澶辫触({e})锛屼及鍊煎彲鑳戒笉瀹屾暣")

    # 3. 浼板€兼寚鏍?    pe_fwd = price / eps_cur if eps_cur else float("inf")
    cagr = (eps_next / eps_cur - 1) if (eps_cur and eps_next) else 0
    peg = pe_fwd / (cagr * 100) if cagr > 0 else float("inf")
    digest = (
        math.log(pe_fwd / 30) / math.log(1 + cagr)
        if pe_fwd > 30 and cagr > 0 else 0
    )

    return {
        "name": vals[1],
        "price": price,
        "mcap_yi": mcap,
        "pe_ttm": pe_ttm,
        "pb": pb,
        "eps_cur": eps_cur,
        "eps_next": eps_next,
        "pe_fwd": round(pe_fwd, 1) if eps_cur else None,
        "cagr_pct": round(cagr * 100, 0) if cagr else None,
        "peg": round(peg, 2) if peg != float("inf") else None,
        "digest_years": round(digest, 1),
        "analyst_count": analyst_count,
    }

# 鐢ㄦ硶
result = full_valuation("688017")
print(result)
```

### 娴佺▼ B: 鎵归噺浼板€煎姣?
```python
stocks = ["688017", "300308", "300476", "002463"]
for code in stocks:
    try:
        r = full_valuation(code)
        print(f"{r['name']}({code}): PE_fwd={r['pe_fwd']}x PEG={r['peg']} 娑堝寲={r['digest_years']}骞?瑕嗙洊={r['analyst_count']}瀹?)
    except Exception as e:
        print(f"{code}: 澶辫触 - {e}")
```

### 娴佺▼ C: 涓婚鐮旀姤鎵归噺妫€绱?
```python
# Step 1: iwencai 澶?query 璇箟鎼滅储
queries = [
    "浜哄舰鏈哄櫒浜轰骇涓氶摼娣卞害 2026",
    "浜哄舰鏈哄櫒浜哄噺閫熷櫒 涓濇潬",
    "鐗规柉鎷塐ptimus 鍥戒骇渚涘簲閾?,
]
seen_uids = set()
all_articles = []
for q in queries:
    arts = iwencai_search(q, channel="report", size=50)
    for a in arts:
        uid = a.get("uid", "")
        if uid not in seen_uids:
            seen_uids.add(uid)
            all_articles.append(a)
print(f"鍏?{len(all_articles)} 绡囧幓閲嶅悗鐮旀姤")

# Step 2: 涓滆储琛ュ厖鍚屾爣鐨勭爺鎶?+ PDF
for a in all_articles[:10]:
    stocks = a.get("stock_infos") or []
    for s in stocks:
        stock_code = s.get("code", "")
        if stock_code:
            em = eastmoney_reports(stock_code, max_pages=1)
            print(f"  {stock_code}: 涓滆储 {len(em)} 绡?)
```

### 娴佺▼ D: 鏂版爣鐨勫揩閫熻皟鐮旓紙V3.0 澧炲己鐗堬級

```python
code = "688017"

# 1. 鏈夋棤鏈烘瀯瑕嗙洊锛?forecast = ths_eps_forecast(code)
print(f"鏈烘瀯瑕嗙洊: {'鏈? if not forecast.empty else '鏃?}")

# 2. 瀹炴椂浼板€?quotes = tencent_quote([code])
q = quotes[code]
print(f"PE={q['pe_ttm']} PB={q['pb']} 甯傚€?{q['mcap_yi']}浜?)

# 3. PE娑堝寲 鈫?鐢?full_valuation()
# 4. PEG鏍￠獙

# 5. 姒傚康鏉垮潡褰掑睘
blocks = eastmoney_concept_blocks(code)
print(f"鏉垮潡: {', '.join(blocks['concept_tags'][:10])}")

# 6. 璧勯噾娴佸悜锛堝垎閽熺骇锛屽綋鏃ョ洏涓級
flow = eastmoney_fund_flow_minute(code)
if flow:
    total = sum(f["main_net"] for f in flow)
    print(f"褰撴棩涓诲姏绱鍑€娴佸叆: {total/1e4:.0f}涓?)

# 7. 璧勯噾娴佸悜锛堜笢璐?20鏃ワ級
flow_120 = stock_fund_flow_120d(code)
if flow_120:
    total = sum(d["main_net"] for d in flow_120[-20:])
    print(f"杩?0鏃ヤ富鍔涚疮璁″噣娴佸叆: {total/1e8:.2f}浜?)

# 8. 榫欒檸姒?dtb = dragon_tiger_board(code, "2026-05-17")
print(f"杩?0鏃ヤ笂榫欒檸姒? {len(dtb['records'])} 娆?)

# 9. 瑙ｇ棰勮
lockup = lockup_expiry(code, "2026-05-17")
print(f"鏈潵90澶╁緟瑙ｇ: {len(lockup['upcoming'])} 鎵?)

# 10. 铻嶈祫铻嶅埜
margin = margin_trading(code, page_size=5)
if margin:
    print(f"鏈€鏂拌瀺璧勪綑棰? {margin[0]['rzye']/1e8:.2f}浜?)

# 11. 鑲′笢鎴锋暟
holders = holder_num_change(code)
if holders:
    print(f"鏈€鏂拌偂涓滄暟: {holders[0]['holder_num']} 鐜瘮{holders[0]['change_ratio']}%")
```

---

## 鏁版嵁婧愪紭鍏堢骇

| 浼樺厛绾?| 鏁版嵁婧?| 鐢ㄩ€?| 鍙潬鎬?| 灏両P椋庨櫓 |
|--------|--------|------|--------|---------|
| 1 | **mootdx** (TCP) | K绾?浜旀。鐩樺彛+閫愮瑪鎴愪氦+璐㈠姟蹇収+F10 | 鏋佺ǔ瀹?| 鏋佷綆 |
| 2 | **鑵捐璐㈢粡** (HTTP) | 瀹炴椂PE/PB/甯傚€?鎹㈡墜鐜?娑ㄨ穼鍋?鎸囨暟/ETF | 绋冲畾 | 浣?|
| 3 | **涓滆储 datacenter** (HTTP) | 榫欒檸姒?瑙ｇ/铻嶈祫铻嶅埜/澶у畻浜ゆ槗/鑲′笢鎴锋暟/鍒嗙孩/涓偂淇℃伅 | 绋冲畾 | 浣?|
| 4 | **涓滆储 push2/push2his** (HTTP) | 琛屼笟鏉垮潡/涓偂璧勯噾娴佸垎閽熺骇+120鏃?| 绋冲畾 | 浣?|
| 5 | **iwencai** (OpenAPI) | NL涓婚鎼滅储鐮旀姤(鍞竴鑳藉姏) | 闇€X-Claw Header | 浣?|
| 6 | **涓滆储 reportapi/PDF** (HTTP) | 瀹屾暣鐮旀姤鍥捐〃銆佽瘎绾?| 绋冲畾 | 浣?|
| 7 | **鍚岃姳椤虹儹鐐?* (HTTP) | 褰撴棩寮哄娍鑲?棰樻潗褰掑洜 reason tags | 绋冲畾 73ms | 鏋佷綆锛堥浂閴存潈锛?|
| 8 | **鍚岃姳椤?hsgtApi** (HTTP) | 鍖楀悜璧勯噾鍒嗛挓绾?鑷紦瀛樺巻鍙?| 绋冲畾 | 鏋佷綆锛堥浂閴存潈锛?|
| 9 | **鐧惧害鑲″競閫?* (HTTP) | 姒傚康鏉垮潡+K绾垮甫MA | 绋冲畾 | 鏋佷綆锛堥浂閴存潈锛?|
| 10 | **鏂版氮璐㈢粡** (HTTP) | 璧勪骇璐熷€鸿〃/鍒╂鼎琛?鐜伴噾娴侀噺琛?| 绋冲畾 | 浣?|
| 11 | **鍚岃姳椤?basic** (HTTP) | 涓€鑷撮鏈烢PS | 绋冲畾(闇€UA) | 浣?|
| 12 | **璐㈣仈绀?* (HTTP) | 鍏ㄥ競鍦哄疄鏃剁數鎶?| 绋冲畾 | 浣?|
| 13 | **宸ㄦ疆 cninfo** (HTTP) | 鍏憡鍏ㄦ枃妫€绱?涓嬭浇 | 绋冲畾 | 浣?|

**鍘熷垯锛?* 琛屾儏璧?mootdx+鑵捐锛堜笉灏両P锛夛紝鐮旀姤璧颁笢璐?iwencai锛岃祫閲戦潰璧颁笢璐?datacenter+push2锛?*淇″彿灞傝蛋鍚岃姳椤?鐧惧害+涓滆储鐩磋繛鎺ュ彛**銆傚叏閮ㄧ洿杩?HTTP锛岄浂绗笁鏂规暟鎹皝瑁呬緷璧栥€?
---

## FAQ

### Q: mootdx 鍜岃吘璁湁浠€涔堝尯鍒紵
A: 浜掕ˉ鍏崇郴銆俶ootdx = 浜ゆ槗灞傦紙浠锋牸+鐩樺彛+K绾匡級锛岃吘璁?= 浼板€煎眰锛圥E/PB/甯傚€?鎹㈡墜鐜?娑ㄨ穼鍋滀环锛夈€備袱鑰呴兘涓嶅皝IP銆?
### Q: V3.0 涓轰粈涔堢Щ闄?akshare锛?A: akshare 鏈川鏄涓滆储/鍚岃姳椤?鏂版氮绛夊叕寮€ API 鐨勫皝瑁咃紝涓棿灞傚鍔犱簡鏁呴殰鐐癸紙鐗堟湰鍏煎 bug銆乸andas 3.0 ArrowInvalid 绛夛級銆俈3.0 鐩磋繛搴曞眰 HTTP API锛岄浂涓棿渚濊禆锛屾洿绋冲畾鍙帶銆?
### Q: iwencai 杩斿洖 401
A: 妫€鏌ヤ袱鐐癸細(1) API Key 鏄惁鏈夋晥 (2) 鏄惁鎼哄甫浜?X-Claw-* Headers銆係killHub 2.0 鍚庡繀椤诲甫 X-Claw Headers锛屽惁鍒欎竴寰?401銆?
### Q: 鍚岃姳椤轰竴鑷撮鏈?ths_eps_forecast 杩斿洖绌?A: 璇ヨ偂绁ㄦ棤鏈烘瀯瑕嗙洊銆傚皬鐩?娆℃柊/ST 鑲″父瑙併€傚彲 fallback 鍒颁笢璐?reportapi 閲岀殑 predictThisYearEps 瀛楁銆?
### Q: 涓滆储 PDF 涓嬭浇 403
A: 蹇呴』甯?`Referer: https://data.eastmoney.com/` header銆?
### Q: 鑵捐 API 杩斿洖涔辩爜
A: 缂栫爜鏄?GBK锛屽繀椤?`decode("gbk")`銆?
### Q: 鑵捐 API 瀛楁 43 鏄?PB 鍚楋紵
A: **涓嶆槸锛?* 43=鎸箙%锛?6=PB銆傜綉涓婂緢澶氭暀绋嬪啓閿欎簡锛岃繖閲屾槸瀹炴祴鏍″噯缁撴灉銆?
### Q: iwencai search 杩斿洖鏉℃暟澶皯
A: `size` 鍙傛暟榛樿 10锛岃皟鍒?50銆傞殣钘忓弬鏁帮紝鏂囨。鏈啓鏄庝絾瀹炴祴鍙敤銆?
### Q: 鍝簺鏁版嵁婧愰渶瑕?API Key锛?A: 鍙湁 iwencai 闇€瑕併€俶ootdx / 鑵捐 / 涓滆储 / 鍚岃姳椤?/ 鐧惧害鑲″競閫?/ 鏂版氮 / 宸ㄦ疆 / 璐㈣仈绀惧叏閮ㄥ厤璐规棤 key銆?
### Q: 鍚岃姳椤虹儹鐐规帴鍙ｉ渶瑕?cookie 鍚楋紵
A: **涓嶉渶瑕?*銆備粎 User-Agent 鍗冲彲锛岄浂閴存潈 73ms 鎷垮埌 ~125 鍙綋鏃ュ己鍔胯偂銆備絾**涓嶈鍘绘墦 search.10jqka.com.cn 鐨?iwencai NL 閫夎偂鎺ュ彛** 鈥斺€?閭ｄ釜鏈?hexin-v cookie JS 绛惧悕閴存潈锛岃窡鐑偣鎺ュ彛瀹屽叏涓ょ爜浜嬨€?
### Q: 鐧惧害鑲″競閫?ResultCode 鏈夋椂鏄?0 鏈夋椂鏄?"0"锛?A: 宸茬煡鍧戙€俙ResultCode` 杩斿洖绫诲瀷涓嶇ǔ瀹氣€斺€旀湁鏃?int锛屾湁鏃?string銆備唬鐮侀噷蹇呴』鐢?`str(d.get("ResultCode", -1)) != "0"` 缁熶竴姣旇緝銆?
### Q: 鍖楀悜璧勯噾鍘嗗彶鏁版嵁涓轰粈涔堝彧鏈夋渶杩戝嚑澶╋紵
A: 鏈湴鑷紦瀛樻ā寮忋€俥astmoney 鍏ㄧ郴鍖楀悜鏁版嵁鑷?2024-08 璧锋柇渚涳紙鍑€涔伴瀛楁杩斿洖 NaN/0锛夈€傛瘡娆¤皟鐢ㄥ疄鏃?API 鍚庤嚜鍔ㄥ啓鍏ユ湰鍦?CSV锛屽巻鍙茶秺璺戣秺涓板瘜銆?
### Q: 琛屼笟鏉垮潡涓轰粈涔堜粠鍚岃姳椤烘崲鎴愪笢璐紵
A: 鍚岃姳椤?`stock_board_industry_summary_ths` 鎺ュ彛 2026 骞村垵鍔犱簡鍙嶇埇 401锛堥渶瑕佺櫥褰曟€侊級銆備笢璐?push2 琛屼笟鏉垮潡鏁版嵁锛坄m:90+t:2`锛夋槸瀹岀編鏇夸唬锛岄浂閴存潈涓斿瓧娈垫洿涓板瘜銆?
### Q: 鍦ㄦ捣澶栨湇鍔″櫒璺戯紝mootdx 鎺ュ彛瓒呮椂锛?A: mootdx 璧?TCP 鐩磋繛閫氳揪淇¤鎯呮湇鍔″櫒锛岄渶鍥藉唴 IP 鎵嶇ǔ瀹氥€傛捣澶栫幆澧冨缓璁蛋浠ｇ悊銆傝吘璁储缁忓拰鐧惧害鑲″競閫氫笉鍙楀奖鍝嶃€?
### Q: 涓嶇敤 Claude Code锛岃兘鐢ㄥ悧锛?A: 鑳姐€係KILL.md 鏈川鏄?Markdown + 鍐呭祵 Python 浠ｇ爜銆侰odex銆丱penClaw 鎴栦换浣?AI 缂栫▼鍔╂墜閮借兘璇诲彇銆備綘涔熷彲浠ョ洿鎺ユ妸 Python 浠ｇ爜娈靛鍒跺嚭鏉ュ湪鑷繁鐨勮剼鏈噷璺戙€?
---

## 瀹夎璇存槑

```bash
# 1. 鍒涘缓 skill 鐩綍
mkdir -p ~/.claude/skills/a-stock-data

# 2. 灏嗘湰鏂囦欢澶嶅埗涓?SKILL.md
cp SKILL.md ~/.claude/skills/a-stock-data/SKILL.md

# 3. 瀹夎 Python 渚濊禆
pip install mootdx requests pandas stockstats

# 4. (鍙€? 閰嶇疆 iwencai API Key
export IWENCAI_API_KEY="your_key_here"

# 5. 鍚姩 Claude Code锛岃"鏌ヤ竴涓?88017鐨勪及鍊?鍗冲彲鑷姩婵€娲?```

---

> 馃摝 https://github.com/simonlin1212/a-stock-data 鈥?Star 猸?鏄渶濂界殑鏀寔
