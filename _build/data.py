# -*- coding: utf-8 -*-
"""
审计应对 Check list —— 数据源
来源：《09:17审计日程和需提供的文件清单.xlsx》
原则：原文描述与顺序不做改写，仅作分类、分条拆分、补责任部门/责任人。
"""

# 人名 -> 责任部门（按承担工作推断，页面上可编辑覆盖）
PERSON_DEPT = {
    "马宏宇": "质量管理部",
    "许壮壮": "质量管理部",
    "张雅芳": "质量管理部",
    "高艳琼": "质量管理部",
    "洪老师": "质量管理部",
    "王会伟": "仓储运营部",
    "阮海贝": "仓储运营部",
    "范键楠": "仓储运营部",
    "赵宽宽": "运输管理部",
    "成建成": "运输管理部",
    "刘科": "运输管理部",
    "李超阳": "运输管理部",
    "王晓娜": "运营调度中心",
    "牛晨涛": "研发部（验证/校准）",
    "莫虎": "信息技术部",
    "魏慧": "客户服务部",
    "苏兰花": "客户服务部",
    "李冰燕": "客户服务部",
    "臧益岐": "供应链管理部",
}

DEPT_OPTIONS = [
    "质量管理部", "仓储运营部", "运输管理部", "运营调度中心",
    "研发部（验证/校准）", "信息技术部", "客户服务部", "供应链管理部",
    "人力资源部", "安全环保部（EHS）", "行政部", "总经办",
]

# ---------------------------------------------------------------------------
# 数据：cat = 分类；items = 审计条目
#   id    编号
#   en    英文原文
#   zh    中文翻译（原文照录）
#   subs  原文子项 [(en, zh), ...]
#   files 准备文件清单 [{"g":分组, "t":内容, "owner":责任人, "due":完成时间}, ...]
#   owner 条目级责任人（files 未单独指定时使用）
#   due   条目级完成时间
# ---------------------------------------------------------------------------

DATA = [
{
 "cat": "一、开场与公司／现场介绍（09:00–09:30）",
 "tag": "开场",
 "items": [
  {"id":"1.1","en":"Introduction of the involved people","zh":"相关人员介绍",
   "subs":[],"files":[],"owner":"","due":""},

  {"id":"1.2","en":"Opening Presentations from Site Management (about 30 min.)",
   "zh":"现场管理层开场报告（约30分钟），至少包含以下内容（如适用）：",
   "subs":[
     ("· Layout of facilities with area details (incl. total land, total number of buildings/blocks, built up area…)","· 设施布局及面积详情（含土地总面积、建筑/楼栋总数、建筑面积等）"),
     ("· List of products; List of vehicle","· 产品清单；车辆清单"),
     ("· Production description (with critical points)","· 生产描述（含关键点）"),
     ("· Organization charts","· 组织架构图"),
     ("· Flow of materials","· 物料流向"),
     ("· Inspections from Regulatory authorities with audit dates, scope & outcome","· 监管机构检查情况（含审计日期、范围及结果）"),
     ("· Total Headcount (department wise, incl. temporary / contract people)","· 总员工人数（按部门，含临时/合同人员）"),
     ("· Licenses & Certificates from local & international health authorities","· 国内外卫生监管机构颁发的许可证与证书"),
   ],
   "files":[
     {"g":"","t":"公司介绍ppt（须覆盖：设施布局及面积详情、产品清单、车辆清单、生产描述含关键点、组织架构图、物料流向、许可证与证书）","owner":"","due":""},
     {"g":"","t":"近三年无延伸检查","owner":"","due":""},
     {"g":"","t":"花名册","owner":"","due":""},
   ],"owner":"","due":""},

  {"id":"1.3","en":"Review of Audit Agenda","zh":"审计议程确认",
   "subs":[],"files":[{"g":"","t":"/","owner":"","due":""}],"owner":"","due":""},

  {"id":"1.4","en":"Progress on the corrective action plan from previous audit / inspection",
   "zh":"上次审计/检查纠正措施（CAPA）计划的进展",
   "subs":[],
   "files":[
     {"g":"","t":"整改附件","owner":"","due":""},
     {"g":"","t":"泰州审计整改附件","owner":"","due":""},
     {"g":"","t":"2022年华北区审计整改资料","owner":"","due":""},
   ],"owner":"马宏宇、张雅芳、洪老师","due":"9月11日前"},
 ]},

{
 "cat":"二、现场巡视与物料流向审计（09:30–12:00）",
 "tag":"现场",
 "items":[
  {"id":"2.1","en":"Site tour and audit following the material flow (temporary storage or lorry with its trailer), not limited to below:",
   "zh":"现场巡视并沿物料流向开展审计（临时仓储或带拖车的货车），检查内容不限于以下各项：",
   "subs":[
     ("· Receiving area","· 收货区域"),
     ("· Order Processing","· 订单处理"),
     ("· Inventory Control","· 库存控制"),
     ("· Storage areas, including cold chambers and secured area (narcotics, hazardous etc.)","· 存储区域，包括冷库及受控区域（麻醉药品、危险品等）"),
     ("· Order preparation and shipping areas","· 订单拣选和发货区域"),
     ("· Management and flow of specific products: i.e. products received \"on hold\" or \"under quarantine\", temperature controlled products, controlled products (e.g. narcotics) etc.",
      "· 特定产品的管理与流转：如处于“暂停放行”或“待检隔离”状态的产品、温控产品、受控产品（如麻醉药品）等"),
     ("· External warehouse (if applicable)","· 外部仓库（如适用）"),
     ("· Others","· 其他"),
   ],
   "files":[{"g":"","t":"现场检查，自查各区域标识、划分、现场卫生","owner":"","due":""}],
   "owner":"王会伟、阮海贝","due":"9月11日前"},

  {"id":"2.2","en":"· Premises (temporary storage): Security; Pest Control; Cleaning, Maintenance; Temperature management within areas (cool, cold, freezing areas)",
   "zh":"· 场所（临时存储）：安保；虫害控制；清洁、维护；区域内温度管理（阴凉、冷藏、冷冻区域）",
   "subs":[],
   "files":[
     {"g":"① 安保","t":"安保制度、门禁记录、监控点位图","owner":"","due":""},
     {"g":"② 虫害控制","t":"粘鼠板更换记录、灭蝇灯检查记录","owner":"","due":""},
     {"g":"③ 清洁","t":"库房清洁记录","owner":"","due":""},
   ],"owner":"王会伟、阮海贝","due":"9月11日前"},

  {"id":"2.3","en":"· Vehicle: Security; Cleaning / hygiene / conditions; Temperature control and monitoring; Communication system (e.g. GPS)",
   "zh":"· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；",
   "subs":[],
   "files":[
     {"g":"1","t":"赛诺菲使用所有车辆的完整台账","owner":"赵宽宽、成建成、刘科","due":"9月11日前"},
     {"g":"1","t":"赛诺菲使用所有车辆的清洁/卫生记录","owner":"赵宽宽、成建成、刘科","due":"9月11日前"},
     {"g":"1","t":"赛诺菲使用所有车辆的维护保养记录-并确认系统和线下的维保情况是否一致","owner":"赵宽宽、成建成、刘科","due":"9月11日前"},
     {"g":"1","t":"验证报告","owner":"赵宽宽、成建成、刘科","due":"9月11日前"},
     {"g":"1","t":"准备一辆车（需要有验证报告）和一位司机（可能现场回答问题）","owner":"赵宽宽、成建成、刘科","due":"9月11日前"},
     {"g":"2","t":"检查赛诺菲相关的超温报警是否都已经处理完成","owner":"王晓娜","due":"9月11日前"},
     {"g":"3","t":"自查封签发放、使用记录","owner":"高艳琼、张雅芳、洪老师","due":"9月11日前"},
   ],"owner":"赵宽宽、成建成、刘科","due":"9月11日前"},

  {"id":"2.4","en":"· Management of cool pack","zh":"· 蓄冷包/冰排管理",
   "subs":[],
   "files":[
     {"g":"1","t":"冰排出入库记录、预冷记录、泰州业务包装记录","owner":"阮海贝","due":"9月11日前"},
     {"g":"2","t":"广州保温罩预冷记录、出入库记录","owner":"高艳琼","due":"9月11日前"},
   ],"owner":"阮海贝","due":"9月11日前"},

  {"id":"2.5","en":"· Temperature controlled vehicle and its facilities and records",
   "zh":"· 温控车辆及其设施和记录",
   "subs":[],
   "files":[
     {"g":"","t":"温控车温度分布验证报告，区域提交研发部，经过审核后才可以提交客户查看。未经审核不能提供给客户。","owner":"","due":""},
     {"g":"","t":"在途温度记录仪数据","owner":"","due":""},
     {"g":"","t":"温度监测设备校准证书","owner":"","due":""},
   ],"owner":"牛晨涛","due":""},

  {"id":"2.6","en":"· Shipment service tracking system","zh":"· 运输服务追踪系统",
   "subs":[],
   "files":[
     {"g":"1","t":"安智、易流系统说明/演示","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"各系统权限清单，离职人员的权限是否已经关闭。赛诺菲关键人员的系统权限是否符合角色。","owner":"莫虎","due":"9月11日前"},
     {"g":"2","t":"异常处理记录","owner":"王晓娜","due":"9月14日"},
     {"g":"2","t":"24小时监控岗的系统操作日志中有无共用账号的情况","owner":"王晓娜","due":"9月14日"},
     {"g":"3","t":"至少检查2026年1月至现在的所有赛诺菲订单运输节点，使用的供应商是否是备案的供应商，由魏慧提供检查明细。","owner":"魏慧、苏兰花、李冰燕","due":"9月11日前"},
     {"g":"3","t":"每个订单在系统中的交付文件清单（随货同行单、温控记录单、签收单等），节点有无逻辑不通的问题","owner":"魏慧、苏兰花、李冰燕","due":"9月11日前"},
     {"g":"3","t":"有无使用客户账号上传的问题。","owner":"魏慧、苏兰花、李冰燕","due":"9月11日前"},
   ],"owner":"莫虎、王晓娜、魏慧、苏兰花、李冰燕","due":"9月11日前"},

  {"id":"2.7","en":"· Safety, security, environment monitoring","zh":"· 安全、安保、环境监测",
   "subs":[],"files":[{"g":"","t":"参考安全审计清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"2.8","en":"Lunch at your convenience","zh":"午餐（自行安排）",
   "subs":[],"files":[],"owner":"","due":""},
 ]},

{
 "cat":"三、文件审查 — 质量管理（13:00–16:30）",
 "tag":"质量",
 "items":[
  {"id":"3.1","en":"· Personnel – Training","zh":"· 人员——培训",
   "subs":[],
   "files":[
     {"g":"","t":"年度培训计划","owner":"","due":""},
     {"g":"","t":"培训记录（新员工、岗位、年度、专项培训）","owner":"","due":""},
     {"g":"","t":"培训考核记录","owner":"","due":""},
     {"g":"","t":"各岗位培训矩阵（岗位-技能-人员对应）","owner":"","due":""},
     {"g":"","t":"人员健康证/体检记录","owner":"","due":""},
     {"g":"","t":"各区域质量检查供应商月度安全培训记录，培训人员是否齐全","owner":"","due":""},
   ],"owner":"高艳琼、张雅芳、洪老师","due":"9月11日前"},

  {"id":"3.2","en":"· Hygiene and Safety (e.g. handling of flammable, hazardous, cytotoxics, wooden pallets)",
   "zh":"· 卫生与安全（如易燃物、危险品、细胞毒性药物的处理，木托盘）",
   "subs":[],
   "files":[{"g":"","t":"检查库房内所有木托盘是否都有熏蒸标识，如果没有熏蒸标识需要在库外暂存","owner":"","due":""}],
   "owner":"阮海贝、王会伟","due":"9月11日前"},

  {"id":"3.3","en":"· Document Management System, SOPs","zh":"· 文件管理系统、标准操作规程（SOP）",
   "subs":[],
   "files":[
     {"g":"1","t":"文件管理SOP","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"1","t":"受控文件清单/台账","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"1","t":"SOP目录","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"1","t":"文件分发/回收记录","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"1","t":"文件修订历史与审批记录","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"1","t":"作废文件管理记录","owner":"马宏宇、许壮壮","due":"9月11日前"},
     {"g":"2","t":"库房内的文件必须有发放记录现行有效版本","owner":"洪老师、张雅芳、高艳琼","due":"9月11日前"},
     {"g":"2","t":"库房内记录必须有打印序列号","owner":"洪老师、张雅芳、高艳琼","due":"9月11日前"},
   ],"owner":"马宏宇、许壮壮","due":"9月11日前"},

  {"id":"3.4","en":"· Deviation & Corrective and Preventive Action (CAPA)","zh":"· 偏差与纠正预防措施（CAPA）",
   "subs":[],
   "files":[
     {"g":"","t":"偏差处理SOP","owner":"","due":""},
     {"g":"","t":"偏差台账（含关闭状态）","owner":"","due":""},
     {"g":"","t":"偏差调查报告样本（含根因分析）","owner":"","due":""},
     {"g":"","t":"CAPA管理SOP","owner":"","due":""},
     {"g":"","t":"CAPA台账","owner":"","due":""},
     {"g":"","t":"CAPA有效性评估记录","owner":"","due":""},
   ],"owner":"许壮壮","due":"9月11日前"},

  {"id":"3.5","en":"· Change control","zh":"· 变更控制",
   "subs":[],
   "files":[
     {"g":"","t":"变更控制SOP","owner":"","due":""},
     {"g":"","t":"变更台账","owner":"","due":""},
     {"g":"","t":"变更评估与批准记录","owner":"","due":""},
     {"g":"","t":"变更实施与验证记录","owner":"","due":""},
   ],"owner":"马宏宇","due":"9月11日前"},

  {"id":"3.6","en":"· Transport complaint handling","zh":"· 运输投诉处理",
   "subs":[],
   "files":[
     {"g":"","t":"投诉处理SOP","owner":"","due":""},
     {"g":"","t":"投诉台账","owner":"","due":""},
     {"g":"","t":"投诉调查与处理记录（根因+纠正措施）","owner":"","due":""},
     {"g":"","t":"向客户反馈的记录","owner":"","due":""},
   ],"owner":"许壮壮","due":"9月11日前"},

  {"id":"3.7","en":"· Audits & Self-inspection","zh":"· 审计与自检",
   "subs":[],
   "files":[
     {"g":"","t":"自检SOP","owner":"","due":""},
     {"g":"","t":"自检计划（年度）","owner":"","due":""},
     {"g":"","t":"自检报告（含上次）","owner":"","due":""},
     {"g":"","t":"自检发现项CAPA","owner":"","due":""},
     {"g":"","t":"内审员资质证明","owner":"","due":""},
     {"g":"","t":"对供应商/分包商审计计划与报告","owner":"","due":""},
   ],"owner":"马宏宇","due":"9月12日前"},

  {"id":"3.8","en":"· Subcontractors' management","zh":"· 分包商管理",
   "subs":[],
   "files":[
     {"g":"","t":"分包商清单","owner":"","due":""},
     {"g":"","t":"赛诺菲在用供应商的分包协议/质量协议","owner":"","due":""},
     {"g":"","t":"分包商资质审计与评估记录","owner":"","due":""},
     {"g":"","t":"分包商绩效评估","owner":"","due":""},
   ],"owner":"臧益岐","due":"9月13日前"},

  {"id":"3.9","en":"· Customer related process: Determination & Review of customer-specific requirements related to material; Customer communication; Customer complaints",
   "zh":"· 客户相关流程：与物料相关的客户特殊要求的确定与评审；客户沟通；客户投诉",
   "subs":[],
   "files":[
     {"g":"","t":"项目操作手册","owner":"","due":""},
     {"g":"","t":"客户投诉台账与处理","owner":"","due":""},
   ],"owner":"","due":"9月11日前"},
 ]},

{
 "cat":"四、文件审查 — 车辆",
 "tag":"车辆",
 "items":[
  {"id":"4.1","en":"· Mapping Validation / Qualification","zh":"· 温控图/温度分布验证与确认",
   "subs":[],"files":[{"g":"","t":"参考温控车验证部分","owner":"","due":""}],"owner":"/","due":"/"},

  {"id":"4.2","en":"· Maintenance / renewal program","zh":"· 维护/更新计划",
   "subs":[],"files":[{"g":"","t":"赛诺菲使用车辆的维护保养记录","owner":"","due":""}],
   "owner":"","due":"9月11日前"},

  {"id":"4.3","en":"· Calibration","zh":"· 校准",
   "subs":[],
   "files":[
     {"g":"","t":"校准管理SOP","owner":"","due":""},
     {"g":"","t":"年度校准计划（线下台账）","owner":"","due":""},
     {"g":"","t":"校准证书（温度记录仪、探头、温湿度计）","owner":"","due":""},
   ],"owner":"牛晨涛","due":"9月11日前"},
 ]},

{
 "cat":"五、文件审查 — 运营",
 "tag":"运营",
 "items":[
  {"id":"5.1","en":"· Transport plan (including control points)","zh":"· 运输计划（含控制点）",
   "subs":[],
   "files":[
     {"g":"1","t":"可能需要现场演示调度系统、对应的记录（1）整车：订单-派车","owner":"赵宽宽","due":"9月11日前"},
     {"g":"1","t":"可能需要现场演示调度系统、对应的记录（2）零担：","owner":"李超阳","due":"9月11日前"},
     {"g":"2","t":"包含控制点的系统验证报告","owner":"","due":"9月11日前"},
   ],"owner":"赵宽宽、李超阳","due":"9月11日前"},

  {"id":"5.2","en":"· Loading and unloading report","zh":"· 装卸货报告",
   "subs":[],"files":[{"g":"","t":"待确定","owner":"","due":""}],"owner":"","due":""},

  {"id":"5.3","en":"· Tracking and tracing of vehicles and documentation (e.g. IS and back-up)",
   "zh":"· 车辆及文件的追踪与追溯（如信息系统和备份）",
   "subs":[],"files":[{"g":"","t":"数据备份记录演示","owner":"","due":""}],
   "owner":"莫虎","due":"9月11日演示"},

  {"id":"5.4","en":"· Delivery documentation","zh":"· 交付文件",
   "subs":[],"files":[{"g":"","t":"参考系统检查节点部分","owner":"","due":""}],"owner":"/","due":"/"},

  {"id":"5.5","en":"· Return process","zh":"· 退货流程",
   "subs":[],"files":[{"g":"","t":"退货SOP","owner":"","due":""}],"owner":"苏兰花","due":"/"},

  {"id":"5.6","en":"· Management of cool pack","zh":"· 蓄冷包/冰排管理",
   "subs":[],"files":[],"owner":"","due":""},

  {"id":"5.7","en":"· Equipment (e.g. generator) and their maintenance & calibration",
   "zh":"· 设备（如发电机）及其维护与校准",
   "subs":[],"files":[{"g":"","t":"参考安全审计清单","owner":"","due":""}],"owner":"/","due":"/"},
 ]},

{
 "cat":"六、文件审查 — 计算机化系统",
 "tag":"系统",
 "items":[
  {"id":"6.1","en":"· Inventory list of GxP computerized systems, System Description, validation, back-up, recovery Plan",
   "zh":"· GxP计算机化系统清单、系统描述、验证、备份、恢复计划",
   "subs":[],
   "files":[
     {"g":"1","t":"各系统权限清单（安智、易流、鼎为（深圳疫苗使用）、多协、国尚信）","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"验证文件（URS、IQ/OQ/PQ、验证报告）","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"权限管理记录","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"审计追踪说明","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"备份策略与备份记录","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"灾难恢复演练","owner":"莫虎","due":"9月11日前"},
     {"g":"1","t":"多协、鼎为的验证报告","owner":"莫虎","due":"9月11日前"},
     {"g":"2","t":"检查易流、安智验证报告数据完整性","owner":"马宏宇","due":"9月11日前"},
     {"g":"3","t":"检查国尚信报警是否已经处理","owner":"王会伟、阮海贝、范键楠","due":"9月11日前"},
   ],"owner":"莫虎","due":"9月11日前"},

  {"id":"6.2","en":"· Business continuity plan: Operation management","zh":"· 业务连续性计划：运营管理",
   "subs":[],"files":[{"g":"","t":"收集各区域应急演练报告","owner":"","due":""}],
   "owner":"许壮壮","due":"9月11日前"},
 ]},

{
 "cat":"七、收尾与其他",
 "tag":"收尾",
 "items":[
  {"id":"7.1","en":"Others","zh":"其他","subs":[],"files":[],"owner":"","due":""},
  {"id":"7.2","en":"Preparation time for auditors","zh":"审计员准备时间（16:30–17:00）","subs":[],"files":[],"owner":"","due":""},
  {"id":"7.3","en":"Closing meeting","zh":"末次会议（总结会议）（17:00–17:30）","subs":[],"files":[],"owner":"","due":""},
 ]},

{
 "cat":"八、附件 — 需提供文件清单（客户要求）",
 "tag":"附件",
 "items":[
  {"id":"8.1","en":"Site Master File","zh":"文件清单","cat_en":"法规 (Regulations)",
   "subs":[],"files":[{"g":"","t":"Site Master File（现场主文件）","owner":"","due":""}],
   "owner":"马宏宇","due":""},

  {"id":"8.2","en":"List of all batches produced in the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内生产的全部批次清单（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"产品（审计范围内）与工艺 (Products (in audit scope) and Processes)",
   "subs":[],"files":[{"g":"","t":"近两年内生产的全部批次清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.3","en":"List of batches reprocessed and reworked in the last two years (at a minimum)",
   "zh":"近两年内返工和再加工批次清单（至少两年）",
   "cat_en":"产品（审计范围内）与工艺 (Products (in audit scope) and Processes)",
   "subs":[],"files":[{"g":"","t":"近两年内返工和再加工批次清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.4","en":"Process flow diagrams","zh":"工艺流程图-项目操作手册",
   "cat_en":"产品（审计范围内）与工艺 (Products (in audit scope) and Processes)",
   "subs":[],"files":[{"g":"","t":"工艺流程图 —— 项目操作手册","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.5","en":"Schematic drawings of production areas, including zoning, personnel and material flows",
   "zh":"生产区域示意图，包括分区、人流和物流-参照安全",
   "cat_en":"场所/厂房 (Premises)",
   "subs":[],"files":[{"g":"","t":"生产区域示意图（分区、人流和物流）—— 参照安全","owner":"","due":""}],
   "owner":"阮海贝、王会伟","due":""},

  {"id":"8.6","en":"List of major changes in activities (facilities, manufacturing process, cleaning process, analytical methods, computerized systems, etc.) since last audit",
   "zh":"自上次审计以来发生的重大变更清单（设施、生产工艺、清洁工艺、分析方法、计算机化系统等）",
   "cat_en":"变更控制 (Change control)",
   "subs":[],"files":[{"g":"","t":"自上次审计以来重大变更清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.7","en":"List of deviations (including minor deviations) from the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内偏差清单（含微小偏差）（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"偏差/OOS (Deviations/OOS)",
   "subs":[],"files":[{"g":"","t":"近两年偏差清单（含微小偏差）","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.8","en":"List of OOS from the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内OOS（超标结果）清单（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"偏差/OOS (Deviations/OOS)",
   "subs":[],"files":[{"g":"","t":"近两年OOS（超标结果）清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.9","en":"List of Complaints from the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内投诉清单（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"投诉/退货/召回 (Complaints/Returns/Recalls)",
   "subs":[],"files":[{"g":"","t":"近两年投诉清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.10","en":"List of recalls for the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内召回清单（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"投诉/退货/召回 (Complaints/Returns/Recalls)",
   "subs":[],"files":[{"g":"","t":"近两年召回清单","owner":"","due":""}],"owner":"","due":""},

  {"id":"8.11","en":"List of returns for the last two years (at a minimum, more time frame can be considered depending on the supplier)",
   "zh":"近两年内退货清单（至少两年；可根据供应商情况考虑更长时间范围）",
   "cat_en":"投诉/退货/召回 (Complaints/Returns/Recalls)",
   "subs":[],"files":[{"g":"","t":"近两年退货清单","owner":"","due":""}],"owner":"","due":""},
 ]},
]
