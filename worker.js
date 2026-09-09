/* ============================================================
 * 审计应对 Check list —— 云端同步服务（Cloudflare Worker）
 * 由 _build/build.py 自动生成，请勿手改，改 _build/worker.template.js
 *
 * 职责：
 *   GET  /          读取当前全量状态
 *   POST /          提交改动（需姓名 + 个人口令）
 *
 * 环境变量（Cloudflare 后台 Settings → Variables 里填）：
 *   GITHUB_TOKEN  必填  GitHub 令牌，仅需对本仓库 Contents 读写
 *   GH_OWNER     默认 makacy-999
 *   GH_REPO      默认 audit-checklist
 *   GH_BRANCH    默认 main
 *   DATA_PATH    默认 data/audit-state.json
 *   SALT         选填  口令加盐，建议填一串随机字符
 * ============================================================ */

const OWNERS = {"1.1#-1": "", "1.2#0": "", "1.2#1": "", "1.2#2": "", "1.3#0": "", "1.4#0": "马宏宇、张雅芳、洪老师", "1.4#1": "马宏宇、张雅芳、洪老师", "1.4#2": "马宏宇、张雅芳、洪老师", "2.1#0": "王会伟、阮海贝", "2.2#0": "王会伟、阮海贝", "2.2#1": "王会伟、阮海贝", "2.2#2": "王会伟、阮海贝", "2.3#0": "赵宽宽、成建成、刘科", "2.3#1": "赵宽宽、成建成、刘科", "2.3#2": "赵宽宽、成建成、刘科", "2.3#3": "赵宽宽、成建成、刘科", "2.3#4": "赵宽宽、成建成、刘科", "2.3#5": "王晓娜", "2.3#6": "高艳琼、张雅芳、洪老师", "2.4#0": "阮海贝", "2.4#1": "高艳琼", "2.5#0": "牛晨涛", "2.5#1": "牛晨涛", "2.5#2": "牛晨涛", "2.6#0": "莫虎", "2.6#1": "莫虎", "2.6#2": "王晓娜", "2.6#3": "王晓娜", "2.6#4": "魏慧、苏兰花、李冰燕", "2.6#5": "魏慧、苏兰花、李冰燕", "2.6#6": "魏慧、苏兰花、李冰燕", "2.7#0": "", "2.8#-1": "", "3.1#0": "高艳琼、张雅芳、洪老师", "3.1#1": "高艳琼、张雅芳、洪老师", "3.1#2": "高艳琼、张雅芳、洪老师", "3.1#3": "高艳琼、张雅芳、洪老师", "3.1#4": "高艳琼、张雅芳、洪老师", "3.1#5": "高艳琼、张雅芳、洪老师", "3.2#0": "阮海贝、王会伟", "3.3#0": "马宏宇、许壮壮", "3.3#1": "马宏宇、许壮壮", "3.3#2": "马宏宇、许壮壮", "3.3#3": "马宏宇、许壮壮", "3.3#4": "马宏宇、许壮壮", "3.3#5": "马宏宇、许壮壮", "3.3#6": "洪老师、张雅芳、高艳琼", "3.3#7": "洪老师、张雅芳、高艳琼", "3.4#0": "许壮壮", "3.4#1": "许壮壮", "3.4#2": "许壮壮", "3.4#3": "许壮壮", "3.4#4": "许壮壮", "3.4#5": "许壮壮", "3.5#0": "马宏宇", "3.5#1": "马宏宇", "3.5#2": "马宏宇", "3.5#3": "马宏宇", "3.6#0": "许壮壮", "3.6#1": "许壮壮", "3.6#2": "许壮壮", "3.6#3": "许壮壮", "3.7#0": "马宏宇", "3.7#1": "马宏宇", "3.7#2": "马宏宇", "3.7#3": "马宏宇", "3.7#4": "马宏宇", "3.7#5": "马宏宇", "3.8#0": "臧益岐", "3.8#1": "臧益岐", "3.8#2": "臧益岐", "3.8#3": "臧益岐", "3.9#0": "", "3.9#1": "", "4.1#0": "/", "4.2#0": "", "4.3#0": "牛晨涛", "4.3#1": "牛晨涛", "4.3#2": "牛晨涛", "5.1#0": "赵宽宽", "5.1#1": "李超阳", "5.1#2": "赵宽宽、李超阳", "5.2#0": "", "5.3#0": "莫虎", "5.4#0": "/", "5.5#0": "苏兰花", "5.6#-1": "", "5.7#0": "/", "6.1#0": "莫虎", "6.1#1": "莫虎", "6.1#2": "莫虎", "6.1#3": "莫虎", "6.1#4": "莫虎", "6.1#5": "莫虎", "6.1#6": "莫虎", "6.1#7": "马宏宇", "6.1#8": "王会伟、阮海贝、范键楠", "6.2#0": "许壮壮", "7.1#-1": "", "7.2#-1": "", "7.3#-1": "", "8.1#0": "马宏宇", "8.2#0": "", "8.3#0": "", "8.4#0": "", "8.5#0": "阮海贝、王会伟", "8.6#0": "", "8.7#0": "", "8.8#0": "", "8.9#0": "", "8.10#0": "", "8.11#0": ""};
const SEQ = {"1.1#-1": "001", "1.2#0": "002", "1.2#1": "003", "1.2#2": "004", "1.3#0": "005", "1.4#0": "006", "1.4#1": "007", "1.4#2": "008", "2.1#0": "009", "2.2#0": "010", "2.2#1": "011", "2.2#2": "012", "2.3#0": "013", "2.3#1": "014", "2.3#2": "015", "2.3#3": "016", "2.3#4": "017", "2.3#5": "018", "2.3#6": "019", "2.4#0": "020", "2.4#1": "021", "2.5#0": "022", "2.5#1": "023", "2.5#2": "024", "2.6#0": "025", "2.6#1": "026", "2.6#2": "027", "2.6#3": "028", "2.6#4": "029", "2.6#5": "030", "2.6#6": "031", "2.7#0": "032", "2.8#-1": "033", "3.1#0": "034", "3.1#1": "035", "3.1#2": "036", "3.1#3": "037", "3.1#4": "038", "3.1#5": "039", "3.2#0": "040", "3.3#0": "041", "3.3#1": "042", "3.3#2": "043", "3.3#3": "044", "3.3#4": "045", "3.3#5": "046", "3.3#6": "047", "3.3#7": "048", "3.4#0": "049", "3.4#1": "050", "3.4#2": "051", "3.4#3": "052", "3.4#4": "053", "3.4#5": "054", "3.5#0": "055", "3.5#1": "056", "3.5#2": "057", "3.5#3": "058", "3.6#0": "059", "3.6#1": "060", "3.6#2": "061", "3.6#3": "062", "3.7#0": "063", "3.7#1": "064", "3.7#2": "065", "3.7#3": "066", "3.7#4": "067", "3.7#5": "068", "3.8#0": "069", "3.8#1": "070", "3.8#2": "071", "3.8#3": "072", "3.9#0": "073", "3.9#1": "074", "4.1#0": "075", "4.2#0": "076", "4.3#0": "077", "4.3#1": "078", "4.3#2": "079", "5.1#0": "080", "5.1#1": "081", "5.1#2": "082", "5.2#0": "083", "5.3#0": "084", "5.4#0": "085", "5.5#0": "086", "5.6#-1": "087", "5.7#0": "088", "6.1#0": "089", "6.1#1": "090", "6.1#2": "091", "6.1#3": "092", "6.1#4": "093", "6.1#5": "094", "6.1#6": "095", "6.1#7": "096", "6.1#8": "097", "6.2#0": "098", "7.1#-1": "099", "7.2#-1": "100", "7.3#-1": "101", "8.1#0": "102", "8.2#0": "103", "8.3#0": "104", "8.4#0": "105", "8.5#0": "106", "8.6#0": "107", "8.7#0": "108", "8.8#0": "109", "8.9#0": "110", "8.10#0": "111", "8.11#0": "112"};
const ZH = {"1.1#-1": "相关人员介绍", "1.2#0": "现场管理层开场报告（约30分钟），至少包含以下内容（如适用）：", "1.2#1": "现场管理层开场报告（约30分钟），至少包含以下内容（如适用）：", "1.2#2": "现场管理层开场报告（约30分钟），至少包含以下内容（如适用）：", "1.3#0": "审计议程确认", "1.4#0": "上次审计/检查纠正措施（CAPA）计划的进展", "1.4#1": "上次审计/检查纠正措施（CAPA）计划的进展", "1.4#2": "上次审计/检查纠正措施（CAPA）计划的进展", "2.1#0": "现场巡视并沿物料流向开展审计（临时仓储或带拖车的货车），检查内容不限于以下各项：", "2.2#0": "· 场所（临时存储）：安保；虫害控制；清洁、维护；区域内温度管理（阴凉、冷藏、冷冻区域）", "2.2#1": "· 场所（临时存储）：安保；虫害控制；清洁、维护；区域内温度管理（阴凉、冷藏、冷冻区域）", "2.2#2": "· 场所（临时存储）：安保；虫害控制；清洁、维护；区域内温度管理（阴凉、冷藏、冷冻区域）", "2.3#0": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#1": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#2": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#3": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#4": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#5": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.3#6": "· 车辆：安保；清洁/卫生/状态；温度控制与监测；通信系统（如GPS）；", "2.4#0": "· 蓄冷包/冰排管理", "2.4#1": "· 蓄冷包/冰排管理", "2.5#0": "· 温控车辆及其设施和记录", "2.5#1": "· 温控车辆及其设施和记录", "2.5#2": "· 温控车辆及其设施和记录", "2.6#0": "· 运输服务追踪系统", "2.6#1": "· 运输服务追踪系统", "2.6#2": "· 运输服务追踪系统", "2.6#3": "· 运输服务追踪系统", "2.6#4": "· 运输服务追踪系统", "2.6#5": "· 运输服务追踪系统", "2.6#6": "· 运输服务追踪系统", "2.7#0": "· 安全、安保、环境监测", "2.8#-1": "午餐（自行安排）", "3.1#0": "· 人员——培训", "3.1#1": "· 人员——培训", "3.1#2": "· 人员——培训", "3.1#3": "· 人员——培训", "3.1#4": "· 人员——培训", "3.1#5": "· 人员——培训", "3.2#0": "· 卫生与安全（如易燃物、危险品、细胞毒性药物的处理，木托盘）", "3.3#0": "· 文件管理系统、标准操作规程（SOP）", "3.3#1": "· 文件管理系统、标准操作规程（SOP）", "3.3#2": "· 文件管理系统、标准操作规程（SOP）", "3.3#3": "· 文件管理系统、标准操作规程（SOP）", "3.3#4": "· 文件管理系统、标准操作规程（SOP）", "3.3#5": "· 文件管理系统、标准操作规程（SOP）", "3.3#6": "· 文件管理系统、标准操作规程（SOP）", "3.3#7": "· 文件管理系统、标准操作规程（SOP）", "3.4#0": "· 偏差与纠正预防措施（CAPA）", "3.4#1": "· 偏差与纠正预防措施（CAPA）", "3.4#2": "· 偏差与纠正预防措施（CAPA）", "3.4#3": "· 偏差与纠正预防措施（CAPA）", "3.4#4": "· 偏差与纠正预防措施（CAPA）", "3.4#5": "· 偏差与纠正预防措施（CAPA）", "3.5#0": "· 变更控制", "3.5#1": "· 变更控制", "3.5#2": "· 变更控制", "3.5#3": "· 变更控制", "3.6#0": "· 运输投诉处理", "3.6#1": "· 运输投诉处理", "3.6#2": "· 运输投诉处理", "3.6#3": "· 运输投诉处理", "3.7#0": "· 审计与自检", "3.7#1": "· 审计与自检", "3.7#2": "· 审计与自检", "3.7#3": "· 审计与自检", "3.7#4": "· 审计与自检", "3.7#5": "· 审计与自检", "3.8#0": "· 分包商管理", "3.8#1": "· 分包商管理", "3.8#2": "· 分包商管理", "3.8#3": "· 分包商管理", "3.9#0": "· 客户相关流程：与物料相关的客户特殊要求的确定与评审；客户沟通；客户投诉", "3.9#1": "· 客户相关流程：与物料相关的客户特殊要求的确定与评审；客户沟通；客户投诉", "4.1#0": "· 温控图/温度分布验证与确认", "4.2#0": "· 维护/更新计划", "4.3#0": "· 校准", "4.3#1": "· 校准", "4.3#2": "· 校准", "5.1#0": "· 运输计划（含控制点）", "5.1#1": "· 运输计划（含控制点）", "5.1#2": "· 运输计划（含控制点）", "5.2#0": "· 装卸货报告", "5.3#0": "· 车辆及文件的追踪与追溯（如信息系统和备份）", "5.4#0": "· 交付文件", "5.5#0": "· 退货流程", "5.6#-1": "· 蓄冷包/冰排管理", "5.7#0": "· 设备（如发电机）及其维护与校准", "6.1#0": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#1": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#2": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#3": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#4": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#5": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#6": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#7": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.1#8": "· GxP计算机化系统清单、系统描述、验证、备份、恢复计划", "6.2#0": "· 业务连续性计划：运营管理", "7.1#-1": "其他", "7.2#-1": "审计员准备时间（16:30–17:00）", "7.3#-1": "末次会议（总结会议）（17:00–17:30）", "8.1#0": "文件清单", "8.2#0": "近两年内生产的全部批次清单（至少两年；可根据供应商情况考虑更长时间范围）", "8.3#0": "近两年内返工和再加工批次清单（至少两年）", "8.4#0": "工艺流程图-项目操作手册", "8.5#0": "生产区域示意图，包括分区、人流和物流-参照安全", "8.6#0": "自上次审计以来发生的重大变更清单（设施、生产工艺、清洁工艺、分析方法、计算机化系统等）", "8.7#0": "近两年内偏差清单（含微小偏差）（至少两年；可根据供应商情况考虑更长时间范围）", "8.8#0": "近两年内OOS（超标结果）清单（至少两年；可根据供应商情况考虑更长时间范围）", "8.9#0": "近两年内投诉清单（至少两年；可根据供应商情况考虑更长时间范围）", "8.10#0": "近两年内召回清单（至少两年；可根据供应商情况考虑更长时间范围）", "8.11#0": "近两年内退货清单（至少两年；可根据供应商情况考虑更长时间范围）"};
const MIG = '（旧版迁移）';
const SLAB = { todo: '未开始', doing: '准备中', done: '已就绪', na: '不适用' };
const DEFAULT_ADMINS = ['马宏宇'];

const CORS = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
  'Access-Control-Allow-Headers': 'Content-Type',
  'Access-Control-Max-Age': '86400',
};

function json(obj, status) {
  return new Response(JSON.stringify(obj), {
    status: status || 200,
    headers: Object.assign({ 'Content-Type': 'application/json; charset=utf-8' }, CORS),
  });
}

/* ---------- base64（UTF-8 安全） ---------- */
function toB64(str) {
  const bytes = new TextEncoder().encode(str);
  let bin = '';
  for (let i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
  return btoa(bin);
}
function fromB64(b64) {
  const bin = atob(String(b64).replace(/\s/g, ''));
  const bytes = new Uint8Array(bin.length);
  for (let i = 0; i < bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder().decode(bytes);
}

/* ---------- GitHub ---------- */
function api(env) {
  return 'https://api.github.com/repos/' + env.GH_OWNER + '/' + env.GH_REPO + '/contents/' + env.DATA_PATH;
}
function ghHeaders(env) {
  return {
    Authorization: 'Bearer ' + env.GITHUB_TOKEN,
    Accept: 'application/vnd.github+json',
    'User-Agent': 'audit-checklist-worker',
    'Content-Type': 'application/json',
  };
}
function blank() {
  return { v: 3, users: {}, admins: DEFAULT_ADMINS.slice(), S: {}, N: {}, D: {}, LOG: [] };
}
async function readState(env) {
  const r = await fetch(api(env) + '?ref=' + env.GH_BRANCH, { headers: ghHeaders(env) });
  if (r.status === 404) return { state: blank(), sha: null };
  if (!r.ok) throw new Error('读取 GitHub 失败: ' + r.status + ' ' + (await r.text()).slice(0, 200));
  const j = await r.json();
  let st;
  try { st = JSON.parse(fromB64(j.content)); } catch (e) { st = blank(); }
  st.users = st.users || {};
  st.admins = st.admins && st.admins.length ? st.admins : DEFAULT_ADMINS.slice();
  st.S = st.S || {}; st.N = st.N || {}; st.D = st.D || {}; st.LOG = st.LOG || [];
  return { state: st, sha: j.sha };
}
async function writeState(env, state, sha) {
  const body = { message: 'checklist: ' + new Date().toISOString(), content: toB64(JSON.stringify(state)), branch: env.GH_BRANCH };
  if (sha) body.sha = sha;
  const r = await fetch(api(env), { method: 'PUT', headers: ghHeaders(env), body: JSON.stringify(body) });
  if (!r.ok) throw new Error('写入 GitHub 失败: ' + r.status + ' ' + (await r.text()).slice(0, 200));
  return true;
}

/* ---------- 口令 ---------- */
async function hashOf(name, code, env) {
  const raw = String(name) + '::' + String(code) + '::' + (env.SALT || 'audit2026');
  const buf = new TextEncoder().encode(raw);
  const h = await crypto.subtle.digest('SHA-256', buf);
  return Array.from(new Uint8Array(h)).map(b => b.toString(16).padStart(2, '0')).join('');
}

/* ---------- 权限（服务端强制） ---------- */
function ownersOf(key) {
  return String(OWNERS[key] || '').split(/[、,，]/).map(s => s.trim()).filter(Boolean);
}
function isAdmin(state, name) {
  return (state.admins || []).indexOf(name) >= 0;
}
function canEdit(state, key, name) {
  if (isAdmin(state, name)) return true;
  if (ownersOf(key).indexOf(name) < 0) return false;
  const rec = state.S[key];
  if (rec && rec.by && rec.by !== name && rec.by !== MIG) return false;
  return true;
}
function stamp() {
  const d = new Date(), p = n => String(n).padStart(2, '0');
  return d.getFullYear() + '-' + p(d.getMonth() + 1) + '-' + p(d.getDate()) + ' ' + p(d.getHours()) + ':' + p(d.getMinutes());
}

/* ---------- 应用改动 ---------- */
function applyOps(state, name, ops) {
  const applied = [], denied = [];
  for (const op of (ops || [])) {
    const key = op.key;
    if (!key || !(key in OWNERS)) { denied.push({ key: key, why: '未知条目' }); continue; }

    if (op.type === 'clear') {
      if (!isAdmin(state, name)) { denied.push({ key: key, why: '仅管理员可清除' }); continue; }
      const o = state.S[key], n = state.N[key];
      delete state.S[key]; delete state.N[key];
      state.LOG.push({ t: stamp(), who: name + '（管理员）', seq: SEQ[key], id: key.split('#')[0],
        zh: ZH[key] || '', field: '清除记录',
        from: (o ? SLAB[o.v] || o.v : '未开始') + (n && n.v ? ' / ' + n.v.slice(0, 30) : ''), to: '（已清除）' });
      applied.push(key);
      continue;
    }

    if (!canEdit(state, key, name)) {
      denied.push({ key: key, why: isAdmin(state, name) ? '无权限' : '非你负责或他人已改' });
      continue;
    }

    if (op.field === 'status') {
      const v = op.value;
      if (!SLAB[v]) { denied.push({ key: key, why: '状态值非法' }); continue; }
      const old = state.S[key] ? (state.S[key].v || 'todo') : 'todo';
      state.S[key] = { v: v, by: name, at: stamp() };
      if (old !== v) state.LOG.push({ t: stamp(), who: name, seq: SEQ[key], id: key.split('#')[0],
        zh: ZH[key] || '', field: '状态', from: SLAB[old], to: SLAB[v] });
      applied.push(key);
    } else if (op.field === 'note') {
      const v = String(op.value || '');
      const old = state.N[key] ? (state.N[key].v || '') : '';
      if (old === v) continue;
      state.N[key] = { v: v, by: name, at: stamp() };
      state.LOG.push({ t: stamp(), who: name, seq: SEQ[key], id: key.split('#')[0],
        zh: ZH[key] || '', field: '备注', from: old.slice(0, 40), to: v.slice(0, 40) });
      applied.push(key);
    } else if (op.field === 'dept') {
      const v = String(op.value || '');
      const p = OWNERS[key] || '';
      const k = 'P::' + p;
      const old = state.D[k] || '';
      if (old === v) continue;
      state.D[k] = v;
      state.LOG.push({ t: stamp(), who: name, seq: SEQ[key], id: key.split('#')[0],
        zh: ZH[key] || '', field: '责任部门', from: old, to: v });
      applied.push(key);
    } else {
      denied.push({ key: key, why: '未知字段' });
    }
  }
  if (state.LOG.length > 4000) state.LOG = state.LOG.slice(-4000);
  return { applied: applied, denied: denied };
}

/* ---------- 主入口 ---------- */
export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') return new Response(null, { headers: CORS, status: 204 });

    env.GH_OWNER = env.GH_OWNER || 'makacy-999';
    env.GH_REPO = env.GH_REPO || 'audit-checklist';
    env.GH_BRANCH = env.GH_BRANCH || 'main';
    env.DATA_PATH = env.DATA_PATH || 'data/audit-state.json';

    if (!env.GITHUB_TOKEN) return json({ error: '服务端未配置 GITHUB_TOKEN' }, 500);

    /* ---- GET：读全量 ---- */
    if (request.method === 'GET') {
      try {
        const { state } = await readState(env);
        return json({ ok: true, state: state, admins: state.admins, users: Object.keys(state.users) });
      } catch (e) {
        return json({ error: String(e && e.message || e) }, 500);
      }
    }

    /* ---- POST：提交 ---- */
    if (request.method !== 'POST') return json({ error: 'method not allowed' }, 405);

    let body;
    try { body = await request.json(); } catch (e) { return json({ error: '请求体不是合法 JSON' }, 400); }
    const name = String(body.name || '').trim();
    const code = String(body.code || '');
    if (!name) return json({ error: '缺少姓名' }, 400);
    if (!code) return json({ error: '缺少口令' }, 400);

    // 冲突重试：最多 3 次
    for (let attempt = 0; attempt < 3; attempt++) {
      try {
        const { state, sha } = await readState(env);
        const h = await hashOf(name, code, env);

        // 注册 or 校验
        if (!state.users[name]) {
          if (body.register !== true) return json({ error: '该姓名尚未设置口令，请先注册', needRegister: true }, 401);
          state.users[name] = h;
        } else if (state.users[name] !== h) {
          return json({ error: '口令不正确' }, 403);
        }

        // 管理员自提（口令正确 + 在 admins 名单里即管理员）
        const admin = isAdmin(state, name);

        let result = { applied: [], denied: [] };
        if (body.op === 'resetAll') {
          if (!admin) return json({ error: '仅管理员可清空' }, 403);
          state.S = {}; state.N = {}; state.D = {}; state.LOG = [];
          state.LOG.push({ t: stamp(), who: name + '（管理员）', seq: '-', id: '-',
            zh: '清空全部数据', field: '清空', from: '', to: '' });
        } else if (body.op === 'clearLog') {
          if (!admin) return json({ error: '仅管理员可清空日志' }, 403);
          state.LOG = [];
        } else {
          result = applyOps(state, name, body.ops || []);
        }

        await writeState(env, state, sha);
        return json({ ok: true, admin: admin, state: state,
                      applied: result.applied, denied: result.denied });
      } catch (e) {
        const msg = String(e && e.message || e);
        if (msg.indexOf('409') >= 0 || msg.indexOf('sha') >= 0) { continue; }  // 冲突，重试
        return json({ error: msg }, 500);
      }
    }
    return json({ error: '提交冲突，请重试' }, 409);
  },
};
