import streamlit as st
import pandas as pd
import json, os, io
from datetime import datetime
import urllib.parse

st.set_page_config(
    page_title="منصة الأستاذة إسلام البرماوي",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@300;400;500;700;800;900&display=swap');

:root {
    --bg:           #F0F4FF;
    --surface:      #FFFFFF;
    --border:       #DDE3F0;
    --blue:         #4361EE;
    --blue-light:   #EEF2FF;
    --blue-dark:    #2D46CC;
    --blue-glow:    rgba(67,97,238,0.18);
    --green:        #06D6A0;
    --green-light:  #D4F7ED;
    --green-dark:   #05A67D;
    --red:          #EF233C;
    --red-light:    #FDEDF0;
    --amber:        #F8961E;
    --amber-light:  #FEF3E2;
    --purple:       #7209B7;
    --purple-light: #F0E6FA;
    --teal:         #4CC9F0;
    --teal-light:   #E4F7FD;
    --pink:         #F72585;
    --pink-light:   #FDEDF8;
    --text-dark:    #0A0F2C;
    --text-mid:     #4A5280;
    --text-light:   #9AA3C9;
    --sh-sm: 0 2px 8px rgba(67,97,238,0.07), 0 1px 3px rgba(10,15,44,0.04);
    --sh-md: 0 8px 24px rgba(67,97,238,0.12), 0 2px 8px rgba(10,15,44,0.05);
    --sh-lg: 0 16px 48px rgba(67,97,238,0.18), 0 4px 16px rgba(10,15,44,0.06);
    --radius: 16px;
    --radius-sm: 10px;
}

* { font-family:'Tajawal',sans-serif !important; box-sizing:border-box; }
html,body,.stApp { background:var(--bg) !important; direction:rtl; color:var(--text-dark); }
#MainMenu,footer,header { visibility:hidden; }
section[data-testid="stSidebar"] { display:none !important; }

.block-container { padding:0 1.2rem 6rem !important; max-width:1100px !important; margin:auto; }

/* ═══ TOP HEADER BAR ═══ */
.top-bar {
    background:linear-gradient(135deg,#0A0F2C 0%,#1a1f4e 40%,#2d3680 100%);
    border-radius:0 0 28px 28px;
    padding:20px 28px 16px;
    margin-bottom:24px;
    position:sticky;
    top:0;
    z-index:998;
    overflow:hidden;
    box-shadow:0 8px 32px rgba(10,15,44,0.25);
}
.top-bar::before {
    content:'';
    position:absolute;top:0;left:0;right:0;bottom:0;
    background:url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%234361EE' fill-opacity='0.06'%3E%3Cpath d='M36 34v-4h-2v4h-4v2h4v4h2v-4h4v-2h-4zm0-30V0h-2v4h-4v2h4v4h2V6h4V4h-4zM6 34v-4H4v4H0v2h4v4h2v-4h4v-2H6zM6 4V0H4v4H0v2h4v4h2V6h4V4H6z'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
}
.top-bar::after {
    content:'';
    position:absolute;top:-60px;right:-60px;
    width:200px;height:200px;
    background:radial-gradient(circle,rgba(67,97,238,0.3) 0%,transparent 70%);
    border-radius:50%;
}
.top-bar-inner {
    position:relative;z-index:1;
    display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:14px;
}
.top-bar-logo {
    display:flex;align-items:center;gap:14px;
}
.top-logo-ic {
    width:52px;height:52px;
    background:linear-gradient(135deg,#4361EE,#7209B7);
    border-radius:15px;
    display:flex;align-items:center;justify-content:center;
    font-size:1.5rem;
    box-shadow:0 4px 16px rgba(67,97,238,0.4),0 0 0 2px rgba(255,255,255,0.12);
}
.top-bar-title h1 {
    color:white !important;
    font-size:1.15rem !important;
    font-weight:900 !important;
    margin:0 0 2px !important;
    line-height:1.2 !important;
}
.top-bar-title p {
    color:rgba(255,255,255,0.55);
    font-size:0.72rem;
    margin:0;
    font-weight:600;
    letter-spacing:1px;
    text-transform:uppercase;
}
.top-bar-stats {
    display:flex;gap:20px;align-items:center;
}
.tbs {
    text-align:center;
    padding:8px 16px;
    background:rgba(255,255,255,0.07);
    border-radius:12px;
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter:blur(8px);
}
.tbs-v { color:white;font-size:1.4rem;font-weight:900;line-height:1; }
.tbs-l { color:rgba(255,255,255,0.55);font-size:0.62rem;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-top:2px; }

/* ═══ PAGE HEADER ═══ */
.ph {
    background:var(--surface);
    border:1px solid var(--border);
    border-radius:var(--radius);
    padding:20px 24px;
    margin-bottom:20px;
    display:flex;align-items:center;gap:14px;
    box-shadow:var(--sh-sm);
    position:relative;overflow:hidden;
}
.ph::before {
    content:'';position:absolute;top:0;left:0;right:0;height:3px;
    background:linear-gradient(90deg,var(--blue),var(--purple),var(--pink));
    border-radius:var(--radius) var(--radius) 0 0;
}
.ph-ic {
    width:48px;height:48px;border-radius:13px;
    display:flex;align-items:center;justify-content:center;
    font-size:1.3rem;flex-shrink:0;
}
.ph-ic.bl { background:var(--blue-light);color:var(--blue); }
.ph-ic.gr { background:var(--green-light);color:var(--green-dark); }
.ph-ic.pu { background:var(--purple-light);color:var(--purple); }
.ph-ic.te { background:var(--teal-light);color:#0e9cc0; }
.ph-ic.am { background:var(--amber-light);color:var(--amber); }
.ph-ic.re { background:var(--red-light);color:var(--red); }
.ph-ic.pk { background:var(--pink-light);color:var(--pink); }
.ph h1 { color:var(--text-dark) !important;font-size:1.25rem;font-weight:900;margin:0 0 3px; }
.ph p  { color:var(--text-mid);font-size:0.82rem;margin:0; }

/* ═══ NAV CARDS (Home Page) ═══ */
.nav-grid {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:14px;
    margin-bottom:24px;
}
.nav-card {
    background:var(--surface);
    border:1.5px solid var(--border);
    border-radius:18px;
    padding:22px 18px 20px;
    display:flex;flex-direction:column;align-items:center;gap:10px;
    cursor:pointer;
    transition:all 0.2s cubic-bezier(0.34,1.56,0.64,1);
    box-shadow:var(--sh-sm);
    position:relative;overflow:hidden;
    text-align:center;
}
.nav-card::before {
    content:'';
    position:absolute;top:0;left:0;right:0;height:3px;
    border-radius:18px 18px 0 0;
    transition:height 0.2s;
}
.nav-card:hover {
    transform:translateY(-4px) scale(1.02);
    box-shadow:var(--sh-lg);
    border-color:transparent;
}
.nav-card:hover::before { height:4px; }
.nc-bl::before { background:linear-gradient(90deg,#4361EE,#7209B7); }
.nc-bl:hover { box-shadow:0 16px 48px rgba(67,97,238,0.2); }
.nc-gr::before { background:linear-gradient(90deg,#06D6A0,#4CC9F0); }
.nc-gr:hover { box-shadow:0 16px 48px rgba(6,214,160,0.2); }
.nc-pu::before { background:linear-gradient(90deg,#7209B7,#F72585); }
.nc-pu:hover { box-shadow:0 16px 48px rgba(114,9,183,0.2); }
.nc-am::before { background:linear-gradient(90deg,#F8961E,#F72585); }
.nc-am:hover { box-shadow:0 16px 48px rgba(248,150,30,0.2); }
.nc-te::before { background:linear-gradient(90deg,#4CC9F0,#06D6A0); }
.nc-te:hover { box-shadow:0 16px 48px rgba(76,201,240,0.2); }
.nc-pk::before { background:linear-gradient(90deg,#F72585,#7209B7); }
.nc-pk:hover { box-shadow:0 16px 48px rgba(247,37,133,0.2); }

.nav-card-ic {
    width:56px;height:56px;border-radius:16px;
    display:flex;align-items:center;justify-content:center;
    font-size:1.5rem;
    margin-bottom:2px;
}
.nc-bl .nav-card-ic { background:var(--blue-light); }
.nc-gr .nav-card-ic { background:var(--green-light); }
.nc-pu .nav-card-ic { background:var(--purple-light); }
.nc-am .nav-card-ic { background:var(--amber-light); }
.nc-te .nav-card-ic { background:var(--teal-light); }
.nc-pk .nav-card-ic { background:var(--pink-light); }

.nav-card-title { font-size:0.92rem;font-weight:800;color:var(--text-dark); }
.nav-card-sub   { font-size:0.72rem;color:var(--text-light);font-weight:600; }

/* ═══ KPI CARDS ═══ */
.kpi {
    background:var(--surface);border:1px solid var(--border);
    border-radius:var(--radius);padding:18px 20px;
    box-shadow:var(--sh-sm);transition:all .18s;
    position:relative;overflow:hidden;
}
.kpi:hover { transform:translateY(-2px);box-shadow:var(--sh-md); }
.kpi-iw {
    width:44px;height:44px;border-radius:12px;
    display:flex;align-items:center;justify-content:center;
    font-size:1.1rem;margin-bottom:12px;
}
.kpi.bl .kpi-iw { background:var(--blue-light); }
.kpi.gr .kpi-iw { background:var(--green-light); }
.kpi.re .kpi-iw { background:var(--red-light); }
.kpi.pu .kpi-iw { background:var(--purple-light); }
.kpi.am .kpi-iw { background:var(--amber-light); }
.kpi.te .kpi-iw { background:var(--teal-light); }
.kpi.pk .kpi-iw { background:var(--pink-light); }
.kpi-v { font-size:2rem;font-weight:900;line-height:1;margin-bottom:3px; }
.kpi.bl .kpi-v { color:var(--blue); }
.kpi.gr .kpi-v { color:var(--green-dark); }
.kpi.re .kpi-v { color:var(--red); }
.kpi.pu .kpi-v { color:var(--purple); }
.kpi.am .kpi-v { color:var(--amber); }
.kpi.te .kpi-v { color:#0e9cc0; }
.kpi.pk .kpi-v { color:var(--pink); }
.kpi-l { font-size:0.8rem;color:var(--text-mid);font-weight:600; }
.kpi-bar { position:absolute;bottom:0;left:0;right:0;height:3px;border-radius:0 0 var(--radius) var(--radius); }
.kpi.bl .kpi-bar { background:linear-gradient(90deg,var(--blue),var(--purple)); }
.kpi.gr .kpi-bar { background:linear-gradient(90deg,var(--green),var(--teal)); }
.kpi.re .kpi-bar { background:var(--red); }
.kpi.pu .kpi-bar { background:linear-gradient(90deg,var(--purple),var(--pink)); }
.kpi.am .kpi-bar { background:var(--amber); }
.kpi.te .kpi-bar { background:var(--teal); }
.kpi.pk .kpi-bar { background:linear-gradient(90deg,var(--pink),var(--purple)); }

/* ═══ CARD ═══ */
.card {
    background:var(--surface);border:1px solid var(--border);
    border-radius:var(--radius);padding:20px 22px;
    box-shadow:var(--sh-sm);margin-bottom:18px;
}
.card-t {
    font-size:0.9rem;font-weight:800;color:var(--text-dark);
    margin-bottom:16px;padding-bottom:12px;
    border-bottom:1px solid var(--border);
    display:flex;align-items:center;gap:8px;
}
.card-t span { color:var(--blue); }

/* ═══ GROUP BADGES ═══ */
.gb { display:inline-flex;align-items:center;padding:3px 10px;border-radius:20px;font-size:0.72rem;font-weight:700; }
.gb0 { background:var(--blue-light);color:var(--blue); }
.gb1 { background:var(--green-light);color:var(--green-dark); }
.gb2 { background:var(--purple-light);color:var(--purple); }
.gb3 { background:var(--amber-light);color:#b45309; }
.gb4 { background:var(--teal-light);color:#0e9cc0; }
.gb5 { background:var(--pink-light);color:var(--pink); }

/* ═══ STUDENT CARD ═══ */
.sc {
    background:var(--surface);border:1px solid var(--border);
    border-radius:12px;padding:14px 16px;margin-bottom:8px;
    display:flex;align-items:center;gap:12px;
    box-shadow:var(--sh-sm);transition:all .18s;
}
.sc:hover { border-color:var(--blue);box-shadow:0 0 0 3px rgba(67,97,238,.08),var(--sh-md); }
.av {
    width:42px;height:42px;border-radius:12px;
    display:flex;align-items:center;justify-content:center;
    font-size:1rem;font-weight:900;color:white;flex-shrink:0;
}
.av0 { background:linear-gradient(135deg,#4361EE,#7209B7); }
.av1 { background:linear-gradient(135deg,#06D6A0,#4CC9F0); }
.av2 { background:linear-gradient(135deg,#F8961E,#EF233C); }
.av3 { background:linear-gradient(135deg,#7209B7,#F72585); }
.av4 { background:linear-gradient(135deg,#4CC9F0,#06D6A0); }
.sc-name { font-size:0.93rem;font-weight:700;color:var(--text-dark); }
.sc-meta { font-size:0.76rem;color:var(--text-mid);margin-top:2px; }

/* status pills */
.sp { padding:3px 10px;border-radius:20px;font-size:0.73rem;font-weight:700;white-space:nowrap; }
.sp-p { background:var(--green-light);color:var(--green-dark); }
.sp-a { background:var(--red-light);color:var(--red); }
.sp-l { background:var(--amber-light);color:#b45309; }
.sp-n { background:var(--bg);color:var(--text-light);border:1px solid var(--border); }

/* ═══ FORMS ═══ */
.stTextInput input,
.stTextArea textarea,
.stDateInput input {
    background:var(--bg) !important;border:1.5px solid var(--border) !important;
    border-radius:var(--radius-sm) !important;color:var(--text-dark) !important;
    font-family:'Tajawal',sans-serif !important;font-size:0.9rem !important;
    direction:rtl !important;padding:10px 14px !important;
    transition:border-color .18s,box-shadow .18s !important;
}
.stTextInput input:focus,.stTextArea textarea:focus {
    border-color:var(--blue) !important;
    box-shadow:0 0 0 3px rgba(67,97,238,.12) !important;
}
.stSelectbox > div > div,
.stSelectbox [data-baseweb="select"] > div,
.stSelectbox [data-baseweb="select"] > div > div {
    background:var(--bg) !important;
    border:1.5px solid var(--border) !important;
    border-radius:var(--radius-sm) !important;
}
.stSelectbox [data-baseweb="select"] span,
.stSelectbox [data-baseweb="select"] div[class*="singleValue"],
.stSelectbox [data-baseweb="select"] [data-testid="stSelectboxValue"],
div[data-baseweb="select"] span {
    color:var(--text-dark) !important;
    font-family:'Tajawal',sans-serif !important;
    font-size:0.9rem !important;font-weight:600 !important;direction:rtl !important;
}
ul[data-baseweb="menu"] li,
[data-baseweb="menu"] [role="option"] {
    font-family:'Tajawal',sans-serif !important;
    font-size:0.88rem !important;color:var(--text-dark) !important;direction:rtl !important;
}
[data-baseweb="menu"] [role="option"]:hover,
[data-baseweb="menu"] [aria-selected="true"] {
    background:var(--blue-light) !important;color:var(--blue) !important;
}
label { color:var(--text-mid) !important;font-size:0.82rem !important;font-weight:700 !important; }

/* ═══ TABS ═══ */
.stTabs [data-baseweb="tab-list"] {
    background:var(--bg) !important;border-radius:12px !important;
    padding:4px !important;border:1px solid var(--border) !important;gap:4px !important;
}
.stTabs [data-baseweb="tab"] {
    background:transparent !important;color:var(--text-mid) !important;
    border-radius:9px !important;font-weight:600 !important;
    font-size:0.86rem !important;padding:8px 16px !important;
}
.stTabs [data-baseweb="tab"]:hover { background:var(--surface) !important;color:var(--blue) !important; }
.stTabs [aria-selected="true"] {
    background:var(--surface) !important;color:var(--blue) !important;
    font-weight:800 !important;box-shadow:var(--sh-sm) !important;
}

/* ═══ WHATSAPP ═══ */
.wa-sm {
    display:inline-flex;align-items:center;gap:5px;
    background:#25D366;color:white !important;
    padding:6px 14px;border-radius:20px;
    font-size:0.8rem;font-weight:700;
    text-decoration:none !important;
    box-shadow:0 2px 8px rgba(37,211,102,.3);transition:all .18s;
}
.wa-sm:hover { background:#128C7E;transform:translateY(-1px); }
.wa-lg {
    display:block;text-align:center;
    background:linear-gradient(135deg,#25D366,#128C7E);
    color:white !important;padding:15px 24px;
    border-radius:var(--radius);font-size:0.97rem;font-weight:700;
    text-decoration:none !important;
    box-shadow:0 4px 14px rgba(37,211,102,.3);transition:all .2s;margin-top:12px;
}
.wa-lg:hover { transform:translateY(-2px);box-shadow:0 8px 22px rgba(37,211,102,.35); }

/* ═══ BUTTONS ═══ */
.block-container .stButton > button {
    background:linear-gradient(135deg,var(--blue),var(--blue-dark)) !important;
    color:white !important;border:none !important;
    border-radius:var(--radius-sm) !important;
    font-family:'Tajawal',sans-serif !important;
    font-weight:700 !important;font-size:0.88rem !important;
    padding:10px 20px !important;transition:all .18s !important;
    box-shadow:0 2px 8px rgba(67,97,238,.25) !important;
}
.block-container .stButton > button:hover {
    background:linear-gradient(135deg,var(--blue-dark),#1a2a9e) !important;
    transform:translateY(-1px) !important;
    box-shadow:0 6px 18px rgba(67,97,238,.35) !important;
}
.block-container button[data-testid="baseButton-primary"] {
    background:linear-gradient(135deg,var(--blue),var(--blue-dark)) !important;
    color:white !important;border-radius:var(--radius-sm) !important;
    box-shadow:0 2px 8px rgba(67,97,238,.3) !important;border:none !important;
}
.block-container button[data-testid="baseButton-primary"]:hover {
    transform:translateY(-1px) !important;
    box-shadow:0 6px 18px rgba(67,97,238,.35) !important;
}

/* ═══ BOTTOM NAV ═══ */
.bnav {
    position:fixed;bottom:0;left:0;right:0;z-index:999;
    background:var(--surface);border-top:1px solid var(--border);
    display:flex;align-items:center;
    padding:6px 0 env(safe-area-inset-bottom,6px);
    box-shadow:0 -4px 20px rgba(67,97,238,.10);
}
.bn-item {
    flex:1;display:flex;flex-direction:column;align-items:center;
    gap:3px;padding:6px 4px;cursor:pointer;
    color:var(--text-light);font-size:0.62rem;font-weight:700;
    text-transform:uppercase;letter-spacing:.5px;transition:all .15s;
    border-radius:8px;margin:0 2px;
}
.bn-item:hover,.bn-item.active { color:var(--blue); }
.bn-item .bn-ic { font-size:1.25rem;line-height:1; }

/* ═══ MISC ═══ */
hr { border-color:var(--border) !important;margin:16px 0 !important; }
.empty {
    text-align:center;padding:42px 20px;color:var(--text-light);
}
.empty .ei { font-size:2.5rem;display:block;margin-bottom:10px; }
.empty strong { color:var(--text-mid);display:block;font-size:0.95rem;margin-bottom:4px; }
.empty span { font-size:0.82rem; }
::-webkit-scrollbar { width:5px; }
::-webkit-scrollbar-track { background:var(--bg); }
::-webkit-scrollbar-thumb { background:var(--border);border-radius:3px; }
::-webkit-scrollbar-thumb:hover { background:var(--blue); }

/* ═══ BACK BUTTON IN HEADER ═══ */
.top-bar-right { display:flex; align-items:center; }
/* ═══ FLOATING BACK BUTTON ═══ */
.floating-back-btn-wrap {
    position: fixed;
    bottom: 85px;
    left: 16px;
    z-index: 9999;
    display: flex;
    flex-direction: column;
    align-items: center;
}
.floating-back-btn {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(135deg, #4361EE, #7209B7);
    color: white;
    border: none;
    font-size: 1.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    box-shadow: 0 6px 20px rgba(67,97,238,0.5), 0 2px 8px rgba(10,15,44,0.2);
    transition: all 0.2s cubic-bezier(0.34,1.56,0.64,1);
    -webkit-tap-highlight-color: transparent;
    touch-action: manipulation;
}
.floating-back-btn:hover { transform: scale(1.1); box-shadow: 0 10px 28px rgba(67,97,238,0.6); }
.floating-back-btn:active { transform: scale(0.92); }
.floating-back-label {
    color: #4361EE;
    font-size: 0.65rem;
    font-weight: 800;
    margin-top: 5px;
    letter-spacing: 0.5px;
    font-family: 'Tajawal', sans-serif;
}
.del-btn .stButton > button {
    background:var(--red-light) !important;color:var(--red) !important;
    border:1px solid rgba(239,35,60,.2) !important;
    border-radius:9px !important;padding:7px 12px !important;
    font-size:0.82rem !important;font-weight:700 !important;
    box-shadow:none !important;transform:none !important;
}
.del-btn .stButton > button:hover {
    background:var(--red) !important;color:white !important;
    transform:none !important;box-shadow:none !important;
}
/* ═══ GROUP FILTER PILLS ═══ */
.group-filter-wrap {
    display:flex;flex-wrap:wrap;gap:8px;margin-bottom:16px;
}
.gf-pill {
    padding:6px 16px;border-radius:20px;font-size:0.78rem;font-weight:700;
    cursor:pointer;border:1.5px solid var(--border);
    background:var(--surface);color:var(--text-mid);
    transition:all .15s;
}
.gf-pill.active { background:var(--blue);color:white;border-color:var(--blue); box-shadow:0 2px 8px rgba(67,97,238,.3); }

@media (max-width:768px) {
    .block-container { padding:0 0.5rem 5rem !important; }
    .nav-grid { grid-template-columns:repeat(2,1fr); }
    .top-bar { border-radius:0 0 20px 20px;padding:16px; }
    .top-bar-stats { display:none; }
}
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# DATA HELPERS
# ══════════════════════════════════════════════════════════════
DATA_FILE       = "students.json"
ATTENDANCE_FILE = "attendance.json"
GROUPS_FILE     = "groups.json"

GC = ["gb0","gb1","gb2","gb3","gb4","gb5"]
AC = ["av0","av1","av2","av3","av4"]

def get_gsheet_client():
    try:
        import gspread
        from google.oauth2.service_account import Credentials
        scopes = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=scopes)
        return gspread.authorize(creds)
    except Exception:
        return None

def get_sheet(client, name):
    try:
        sh = client.open(st.secrets["sheet_name"])
        try:    return sh.worksheet(name)
        except: return sh.add_worksheet(title=name, rows=1000, cols=10)
    except Exception:
        return None

def load_from_sheets(ws, default):
    try:
        val = ws.cell(1,1).value
        return json.loads(val) if val else default
    except Exception:
        return default

def save_to_sheets(ws, data):
    try:
        ws.update("A1", [[json.dumps(data, ensure_ascii=False)]])
    except Exception:
        pass

_gsheet_client = None
def _get_client():
    global _gsheet_client
    if _gsheet_client is None:
        _gsheet_client = get_gsheet_client()
    return _gsheet_client

def load_json(f, d):
    client = _get_client()
    if client:
        ws = get_sheet(client, f.replace(".json",""))
        if ws: return load_from_sheets(ws, d)
    return json.load(open(f,"r",encoding="utf-8")) if os.path.exists(f) else d

def save_json(f, data):
    json.dump(data, open(f,"w",encoding="utf-8"), ensure_ascii=False, indent=2)
    client = _get_client()
    if client:
        ws = get_sheet(client, f.replace(".json",""))
        if ws: save_to_sheets(ws, data)

def wa(phone, msg):
    p = phone.replace(" ","").replace("-","").replace("+","")
    if p.startswith("0"): p = "20"+p[1:]
    return f"https://wa.me/{p}?text={urllib.parse.quote(msg)}"

def gc(name):
    g = st.session_state.get("groups",[])
    try: return GC[g.index(name) % len(GC)]
    except: return GC[0]

def ac(name):
    return AC[sum(ord(c) for c in name) % len(AC)]

# ══ Session init ══
for k,v in [("students",load_json(DATA_FILE,[])),
            ("attendance",load_json(ATTENDANCE_FILE,{})),
            ("groups",load_json(GROUPS_FILE,[])),
            ("page","home"),
            ("page_history",[]),
            ("edit_id",None),
            ("confirm_del",None),
            ("msg_group_filter","الكل")]:
    if k not in st.session_state: st.session_state[k] = v

def go_to(new_page):
    """الانتقال لصفحة مع حفظ الصفحة الحالية في الـ history"""
    if st.session_state.page != new_page:
        st.session_state.page_history.append(st.session_state.page)
        st.session_state.page = new_page
        st.session_state.edit_id = None
    st.rerun()

def go_back():
    """الرجوع للصفحة السابقة"""
    if st.session_state.page_history:
        st.session_state.page = st.session_state.page_history.pop()
    else:
        st.session_state.page = "home"
    st.rerun()

# ══ فحص query_params — الزرار الـ floating بيبعت ?back=1 ══
if st.query_params.get("back") == "1":
    st.query_params.clear()
    go_back()

TODAY = datetime.now().strftime("%Y-%m-%d")
NOW   = datetime.now()



# ══════════════════════════════════════════════════════════════
# TOP HEADER BAR
# ══════════════════════════════════════════════════════════════
total_st = len(st.session_state.students)
total_gr = len(st.session_state.groups)

_cur_page = st.session_state.page

if _cur_page == "home":
    st.markdown(f"""
<div class="top-bar">
    <div class="top-bar-inner">
        <div class="top-bar-logo">
            <div class="top-logo-ic">🎓</div>
            <div class="top-bar-title">
                <h1>منصة الأستاذة إسلام البرماوي</h1>
                <p>Educational Monitoring Platform</p>
            </div>
        </div>
        <div class="top-bar-stats">
            <div class="tbs"><div class="tbs-v">{total_st}</div><div class="tbs-l">طالب</div></div>
            <div class="tbs"><div class="tbs-v">{total_gr}</div><div class="tbs-l">مجموعة</div></div>
            <div class="tbs"><div class="tbs-v">{NOW.strftime('%d/%m')}</div><div class="tbs-l">اليوم</div></div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
else:
    st.markdown("""
<div class="top-bar">
    <div class="top-bar-inner">
        <div class="top-bar-logo">
            <div class="top-logo-ic">🎓</div>
            <div class="top-bar-title">
                <h1>منصة الأستاذة إسلام البرماوي</h1>
                <p>Educational Monitoring Platform</p>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)
    # الزرار الـ floating الدائري — يشتغل عن طريق query_params (أضمن طريقة في Streamlit)
    st.markdown("""
<div class="floating-back-btn-wrap">
    <a href="?back=1" target="_self" style="text-decoration:none;display:block;">
        <button class="floating-back-btn" type="button">◀</button>
    </a>
    <div class="floating-back-label">رجوع</div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# BOTTOM NAV
# ══════════════════════════════════════════════════════════════
page = st.session_state.page

nav_pages = [
    ("home","🏠","الرئيسية"),
    ("students","👤","الطلاب"),
    ("attendance","📋","الحضور"),
    ("reports","📊","التقارير"),
    ("messages","💬","الرسائل"),
]
items_html = ""
for pid,ic,lbl in nav_pages:
    act = "active" if page==pid else ""
    items_html += f'<div class="bn-item {act}">{ic}<span>{lbl}</span></div>'
st.markdown(f'<div class="bnav">{items_html}</div>', unsafe_allow_html=True)

page = st.session_state.page



# ══════════════════════════════════════════════════════════════
# UI HELPERS
# ══════════════════════════════════════════════════════════════
def ph(icon, color, title, sub):
    st.markdown(f"""
    <div class="ph">
        <div class="ph-ic {color}">{icon}</div>
        <div><h1>{title}</h1><p>{sub}</p></div>
    </div>""", unsafe_allow_html=True)

def kpi_card(col, cls, icon, val, lbl):
    display_val = int(val) if isinstance(val,(int,float)) and str(val).replace('.','',1).isdigit() and float(val)==int(float(val)) else val
    col.markdown(f"""
    <div class="kpi {cls}">
        <div class="kpi-iw">{icon}</div>
        <div class="kpi-v">{display_val}</div>
        <div class="kpi-l">{lbl}</div>
        <div class="kpi-bar"></div>
    </div>""", unsafe_allow_html=True)

def srow(s, status="غير مسجل"):
    sp = {"حاضر":"sp-p","غائب":"sp-a","متأخر":"sp-l"}.get(status,"sp-n")
    return f"""
    <div class="sc">
        <div class="av {ac(s['name'])}">{s['name'][0]}</div>
        <div style="flex:1;min-width:0">
            <div class="sc-name">{s['name']}</div>
            <div class="sc-meta"><span class="gb {gc(s.get('group',''))}">{s.get('group','—')}</span>&ensp;📞 {s.get('parent_phone','—')}</div>
        </div>
        <span class="sp {sp}">{status}</span>
    </div>"""

# ══════════════════════════════════════════════════════════════
# PAGE: HOME
# ══════════════════════════════════════════════════════════════
if page == "home":
    att_t  = st.session_state.attendance.get(TODAY,{})
    total_s = len(st.session_state.students)
    total_g = len(st.session_state.groups)

    # Hero banner
    present_today = sum(1 for s in st.session_state.students if att_t.get(s["id"])=="حاضر")
    st.markdown(f"""
    <div style="background:linear-gradient(135deg,#0A0F2C 0%,#1a1f4e 50%,#2d3680 100%);
                border-radius:22px;padding:28px;margin-bottom:22px;
                position:relative;overflow:hidden;box-shadow:0 12px 40px rgba(10,15,44,.3)">
        <div style="position:absolute;top:-50px;left:-50px;width:200px;height:200px;
                    background:radial-gradient(circle,rgba(67,97,238,0.35) 0%,transparent 70%);border-radius:50%"></div>
        <div style="position:absolute;bottom:-40px;right:80px;width:140px;height:140px;
                    background:radial-gradient(circle,rgba(114,9,183,0.25) 0%,transparent 70%);border-radius:50%"></div>
        <div style="position:relative;z-index:1">
            <div style="color:rgba(255,255,255,0.6);font-size:0.75rem;font-weight:700;
                        text-transform:uppercase;letter-spacing:2px;margin-bottom:8px">
                ✨ مرحباً بك
            </div>
            <div style="color:white;font-size:1.6rem;font-weight:900;line-height:1.2;margin-bottom:12px">
                منصة الأستاذة<br>
                <span style="background:linear-gradient(90deg,#4CC9F0,#7209B7);-webkit-background-clip:text;-webkit-text-fill-color:transparent">
                    إسلام البرماوي 🎓
                </span>
            </div>
            <div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:16px">
                <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);
                            border-radius:12px;padding:10px 18px;backdrop-filter:blur(8px)">
                    <span style="color:white;font-size:1.3rem;font-weight:900">{total_s}</span>
                    <span style="color:rgba(255,255,255,0.6);font-size:0.78rem;margin-right:6px">طالب مسجل</span>
                </div>
                <div style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);
                            border-radius:12px;padding:10px 18px;backdrop-filter:blur(8px)">
                    <span style="color:white;font-size:1.3rem;font-weight:900">{total_g}</span>
                    <span style="color:rgba(255,255,255,0.6);font-size:0.78rem;margin-right:6px">مجموعة</span>
                </div>
                <div style="background:rgba(6,214,160,0.15);border:1px solid rgba(6,214,160,0.25);
                            border-radius:12px;padding:10px 18px;backdrop-filter:blur(8px)">
                    <span style="color:#06D6A0;font-size:1.3rem;font-weight:900">{present_today}</span>
                    <span style="color:rgba(255,255,255,0.6);font-size:0.78rem;margin-right:6px">حاضر اليوم</span>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Nav cards grid
    st.markdown('<div style="font-size:0.75rem;font-weight:800;color:var(--text-light);text-transform:uppercase;letter-spacing:2px;margin-bottom:12px">⚡ الأقسام الرئيسية</div>', unsafe_allow_html=True)

    nav_items = [
        ("students","nc-bl","👤","إدارة الطلاب","عرض وتعديل وحذف"),
        ("groups",  "nc-pu","👥","المجموعات",   "تنظيم الفصول"),
        ("add",     "nc-gr","➕","إضافة طالب",  "تسجيل طالب جديد"),
        ("attendance","nc-te","📋","سجل الحضور", "تسجيل يومي"),
        ("reports", "nc-am","📊","التقارير",    "إحصائيات وتصدير"),
        ("messages","nc-pk","💬","الرسائل",     "تواصل واتساب"),
    ]

    # Render nav cards as 3-column grid with real buttons
    rows = [nav_items[i:i+3] for i in range(0,len(nav_items),3)]
    for row in rows:
        cols = st.columns(len(row))
        for ci, (pid,nc,icon,label,hint) in enumerate(row):
            with cols[ci]:
                st.markdown(f"""
                <div class="nav-card {nc}">
                    <div class="nav-card-ic">{icon}</div>
                    <div class="nav-card-title">{label}</div>
                    <div class="nav-card-sub">{hint}</div>
                </div>""", unsafe_allow_html=True)
                if st.button(label, key=f"nav_{pid}", use_container_width=True):
                    go_to(pid)

    # Group summary
    if st.session_state.groups:
        st.markdown('<hr>', unsafe_allow_html=True)
        st.markdown('<div class="card-t">👥 <span>ملخص المجموعات اليوم</span></div>', unsafe_allow_html=True)
        gcols = st.columns(min(len(st.session_state.groups),4))
        for i,g in enumerate(st.session_state.groups):
            gs = [s for s in st.session_state.students if s.get("group")==g]
            gp = sum(1 for s in gs if att_t.get(s["id"])=="حاضر")
            ga = sum(1 for s in gs if att_t.get(s["id"])=="غائب")
            gcols[i%4].markdown(f"""
            <div class="kpi bl" style="margin-bottom:10px">
                <span class="gb {gc(g)}" style="font-size:0.78rem;margin-bottom:10px;display:inline-block">{g}</span>
                <div class="kpi-v" style="color:var(--text-dark);font-size:1.6rem">{len(gs)}</div>
                <div class="kpi-l" style="display:flex;gap:8px">
                    <span style="color:var(--green-dark)">✅ {gp}</span>
                    <span style="color:var(--red)">❌ {ga}</span>
                </div>
                <div class="kpi-bar"></div>
            </div>""", unsafe_allow_html=True)

    # Recent students
    st.markdown('<hr>', unsafe_allow_html=True)
    st.markdown('<div class="card-t">👤 <span>آخر الطلاب المضافين</span></div>', unsafe_allow_html=True)
    recent = sorted(st.session_state.students, key=lambda x: x.get("added_date",""), reverse=True)[:5]
    if not recent:
        st.markdown('<div class="empty"><span class="ei">📭</span><strong>لا يوجد طلاب</strong><span>أضف طلاباً من الأقسام أعلاه</span></div>', unsafe_allow_html=True)
    for s in recent:
        status = att_t.get(s["id"],"غير مسجل")
        st.markdown(srow(s,status), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: STUDENTS
# ══════════════════════════════════════════════════════════════
elif page == "students":
    ph("👤","pu","إدارة الطلاب","عرض وتعديل وحذف بيانات الطلاب")

    if st.session_state.edit_id:
        eid = st.session_state.edit_id
        s   = next((x for x in st.session_state.students if x["id"]==eid), None)
        if s:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            st.markdown(f'<div class="card-t">✏️ <span>تعديل بيانات: {s["name"]}</span></div>', unsafe_allow_html=True)
            with st.form("edit_form"):
                c1,c2 = st.columns(2)
                new_name  = c1.text_input("اسم الطالب", value=s["name"])
                new_group = c1.selectbox("المجموعة", st.session_state.groups,
                    index=st.session_state.groups.index(s["group"]) if s.get("group") in st.session_state.groups else 0)
                new_pname = c2.text_input("اسم ولي الأمر", value=s.get("parent_name",""))
                new_phone = c2.text_input("رقم الموبايل",  value=s.get("parent_phone",""))
                new_notes = st.text_area("ملاحظات", value=s.get("notes",""))
                sc1,sc2 = st.columns(2)
                if sc1.form_submit_button("💾  حفظ التعديلات", use_container_width=True, type="primary"):
                    for i,x in enumerate(st.session_state.students):
                        if x["id"]==eid:
                            st.session_state.students[i].update({
                                "name":new_name,"group":new_group,
                                "parent_name":new_pname,"parent_phone":new_phone,"notes":new_notes
                            })
                    save_json(DATA_FILE, st.session_state.students)
                    st.session_state.edit_id = None
                    st.success("✅ تم حفظ التعديلات"); st.rerun()
                if sc2.form_submit_button("❌  إلغاء", use_container_width=True):
                    st.session_state.edit_id = None; st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown('<hr>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    c1,c2 = st.columns([2,1])
    search = c1.text_input("بحث",placeholder="🔍  ابحث باسم الطالب...", label_visibility="collapsed")
    fg     = c2.selectbox("فلتر", ["الكل"]+st.session_state.groups, label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

    filtered = [s for s in st.session_state.students
                if (not search or search in s["name"]) and (fg=="الكل" or s.get("group")==fg)]

    if not filtered:
        st.markdown('<div class="empty"><span class="ei">📭</span><strong>لا يوجد طلاب</strong><span>جرب بحثاً مختلفاً أو أضف طلاباً</span></div>', unsafe_allow_html=True)

    att_t = st.session_state.attendance.get(TODAY, {})
    for s in filtered:
        status = att_t.get(s["id"], "غير مسجل")
        sp_cls = {"حاضر":"sp-p","غائب":"sp-a","متأخر":"sp-l"}.get(status,"sp-n")
        notes_html = f'<br><span style="font-size:0.72rem;color:var(--text-light)">📝 {s["notes"]}</span>' if s.get("notes") else ""

        st.markdown(f"""
        <div style="background:white;border:1px solid var(--border);border-radius:12px 12px 0 0;
                    padding:12px 16px;margin-bottom:0;display:flex;align-items:center;gap:12px;
                    box-shadow:0 1px 3px rgba(67,97,238,0.06)">
            <div class="av {ac(s['name'])}" style="flex-shrink:0">{s['name'][0]}</div>
            <div style="flex:1;min-width:0">
                <div style="font-size:0.93rem;font-weight:700;color:var(--text-dark)">{s['name']}</div>
                <div style="font-size:0.78rem;color:var(--text-mid);margin-top:2px">
                    <span class="gb {gc(s.get('group',''))}">{s.get('group','—')}</span>
                    &ensp;📞 {s.get('parent_phone','—')}{notes_html}
                </div>
            </div>
            <span class="sp {sp_cls}" style="flex-shrink:0">{status}</span>
        </div>
        <div style="display:flex;gap:6px;background:white;border:1px solid var(--border);
                    border-top:none;border-radius:0 0 12px 12px;padding:8px 16px;
                    margin-bottom:10px;box-shadow:0 1px 3px rgba(67,97,238,0.06)">
            <form method="get" style="margin:0">
                <button name="ed_{s['id']}" style="background:var(--blue-light);color:var(--blue);
                    border:1px solid rgba(67,97,238,0.2);border-radius:8px;padding:5px 16px;
                    font-family:Tajawal,sans-serif;font-size:0.8rem;font-weight:700;cursor:pointer">
                    ✏️ تعديل
                </button>
            </form>
            <form method="get" style="margin:0">
                <button name="dl_{s['id']}" style="background:var(--red-light);color:var(--red);
                    border:1px solid rgba(239,35,60,0.2);border-radius:8px;padding:5px 16px;
                    font-family:Tajawal,sans-serif;font-size:0.8rem;font-weight:700;cursor:pointer">
                    🗑️ حذف
                </button>
            </form>
        </div>""", unsafe_allow_html=True)

        bc1, bc2, bc3 = st.columns([1, 1, 4])
        with bc1:
            if st.button("✏️ تعديل", key=f"ed_{s['id']}", use_container_width=True):
                st.session_state.edit_id = s["id"]; st.rerun()
        with bc2:
            if st.button("🗑️ حذف", key=f"dl_{s['id']}", use_container_width=True):
                st.session_state.confirm_del = s["id"]

        if st.session_state.confirm_del == s["id"]:
            st.warning(f"⚠️ هل تريد حذف **{s['name']}** نهائياً؟")
            yc,nc2 = st.columns(2)
            if yc.button("✅ نعم، احذف", key=f"cy_{s['id']}", use_container_width=True, type="primary"):
                st.session_state.students = [x for x in st.session_state.students if x["id"]!=s["id"]]
                save_json(DATA_FILE, st.session_state.students)
                st.session_state.confirm_del = None
                st.success(f"🗑️ تم حذف {s['name']}"); st.rerun()
            if nc2.button("❌ إلغاء", key=f"cn_{s['id']}", use_container_width=True):
                st.session_state.confirm_del = None; st.rerun()

# ══════════════════════════════════════════════════════════════
# PAGE: GROUPS
# ══════════════════════════════════════════════════════════════
elif page == "groups":
    ph("👥","pu","إدارة المجموعات","أنشئ مجموعات الطلاب وتابع توزيعهم")

    c_add, c_list = st.columns([1,1], gap="large")
    with c_add:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-t">➕ <span>إضافة مجموعة جديدة</span></div>', unsafe_allow_html=True)
        ng = st.text_input("اسم المجموعة", placeholder="مثال: أولى ثانوي أ")
        if st.button("➕ إضافة", use_container_width=True, type="primary"):
            if ng and ng not in st.session_state.groups:
                st.session_state.groups.append(ng)
                save_json(GROUPS_FILE, st.session_state.groups)
                st.success(f"✅ تمت إضافة {ng}"); st.rerun()
            elif ng: st.warning("هذه المجموعة موجودة بالفعل")
        st.markdown("""
        <div style="background:var(--blue-light);border-radius:10px;padding:12px 14px;font-size:0.8rem;color:var(--blue);margin-top:14px">
            <strong>💡 أمثلة على أسماء المجموعات:</strong><br>
            • أولى ثانوي — ثانية إعدادي<br>
            • المجموعة الصباحية — المسائية<br>
            • أ — ب — ج
        </div>""", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with c_list:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<div class="card-t">📋 <span>المجموعات الحالية</span></div>', unsafe_allow_html=True)
        if not st.session_state.groups:
            st.markdown('<div class="empty"><span class="ei">👥</span><strong>لا توجد مجموعات بعد</strong><span>أضف مجموعة من اليسار</span></div>', unsafe_allow_html=True)
        for g in st.session_state.groups:
            cnt = len([s for s in st.session_state.students if s.get("group")==g])
            c1,c2 = st.columns([5,1])
            c1.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-bottom:1px solid var(--border)">
                <span class="gb {gc(g)}">{g}</span>
                <span style="color:var(--text-mid);font-size:0.81rem;font-weight:600">{cnt} طالب</span>
            </div>""", unsafe_allow_html=True)
            st.markdown('<div class="del-btn">', unsafe_allow_html=True)
            if c2.button("🗑", key=f"dg_{g}"):
                st.session_state.groups.remove(g)
                save_json(GROUPS_FILE, st.session_state.groups); st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if st.session_state.groups:
        st.markdown('<div class="card-t" style="margin-top:8px">📊 <span>طلاب كل مجموعة</span></div>', unsafe_allow_html=True)
        tabs = st.tabs(st.session_state.groups)
        for tab,g in zip(tabs,st.session_state.groups):
            with tab:
                gs = [s for s in st.session_state.students if s.get("group")==g]
                if not gs:
                    st.markdown(f'<div class="empty"><span class="ei">👤</span><strong>لا يوجد طلاب في {g}</strong></div>', unsafe_allow_html=True)
                for s in gs: st.markdown(srow(s), unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: ADD STUDENT
# ══════════════════════════════════════════════════════════════
elif page == "add":
    ph("➕","gr","إضافة طالب جديد","سجّل بيانات الطالب وولي الأمر")

    if not st.session_state.groups:
        st.markdown("""
        <div style="background:var(--amber-light);border:1px solid var(--amber);border-radius:14px;
                    padding:20px 24px;text-align:center;">
            <div style="font-size:2rem;margin-bottom:10px">⚠️</div>
            <div style="font-size:0.95rem;font-weight:700;color:#92400e;margin-bottom:6px">لا توجد مجموعات</div>
            <div style="font-size:0.82rem;color:#b45309">يجب إنشاء مجموعة أولاً قبل إضافة طلاب</div>
        </div>""", unsafe_allow_html=True)
        if st.button("👥 اذهب لإدارة المجموعات", use_container_width=True, type="primary"):
            go_to("groups")
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        with st.form("add_form", clear_on_submit=True):
            c1,c2 = st.columns(2)
            name  = c1.text_input("اسم الطالب *", placeholder="أحمد محمد علي")
            group = c1.selectbox("المجموعة *", st.session_state.groups)
            pname = c2.text_input("اسم ولي الأمر", placeholder="محمد علي")
            phone = c2.text_input("رقم الموبايل *", placeholder="01012345678")
            notes = st.text_area("ملاحظات", placeholder="أي ملاحظات إضافية عن الطالب...")
            if st.form_submit_button("✅  إضافة الطالب", use_container_width=True, type="primary"):
                if not name.strip() or not phone.strip():
                    st.error("⚠️ الاسم ورقم الموبايل مطلوبان")
                else:
                    st.session_state.students.append({
                        "id":f"{len(st.session_state.students)+1}_{NOW.strftime('%H%M%S')}",
                        "name":name.strip(),"group":group,
                        "parent_name":pname.strip(),"parent_phone":phone.strip(),
                        "notes":notes.strip(),"added_date":TODAY
                    })
                    save_json(DATA_FILE, st.session_state.students)
                    st.success(f"✅ تمت إضافة {name} إلى {group} بنجاح! 🎉")
                    st.balloons()
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: ATTENDANCE
# ══════════════════════════════════════════════════════════════
elif page == "attendance":
    ph("📋","te","سجل الحضور والغياب","سجّل الحضور يومياً لكل مجموعة")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    c1,c2 = st.columns([1,2])
    sel_date  = c1.date_input("التاريخ", value=NOW)
    sel_group = c2.selectbox("المجموعة", ["الكل"]+st.session_state.groups)
    date_key  = sel_date.strftime("%Y-%m-%d")
    st.markdown('</div>', unsafe_allow_html=True)

    if date_key not in st.session_state.attendance:
        st.session_state.attendance[date_key] = {}

    filt = [s for s in st.session_state.students
            if sel_group=="الكل" or s.get("group")==sel_group]

    if not filt:
        st.markdown('<div class="empty"><span class="ei">📋</span><strong>لا يوجد طلاب</strong><span>أضف طلاباً أولاً</span></div>', unsafe_allow_html=True)
    else:
        # Quick action buttons
        st.markdown('<div class="card">', unsafe_allow_html=True)
        q1,q2,q3 = st.columns(3)
        if q1.button("✅ الكل حاضر", use_container_width=True):
            for s in filt: st.session_state.attendance[date_key][s["id"]]="حاضر"
            save_json(ATTENDANCE_FILE, st.session_state.attendance); st.rerun()
        if q2.button("❌ الكل غائب", use_container_width=True):
            for s in filt: st.session_state.attendance[date_key][s["id"]]="غائب"
            save_json(ATTENDANCE_FILE, st.session_state.attendance); st.rerun()
        if q3.button("🔄 مسح الكل", use_container_width=True):
            for s in filt: st.session_state.attendance[date_key].pop(s["id"],None)
            save_json(ATTENDANCE_FILE, st.session_state.attendance); st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

        if st.button("💾  حفظ الحضور الآن", use_container_width=True, type="primary"):
            save_json(ATTENDANCE_FILE, st.session_state.attendance)
            st.success("✅ تم حفظ الحضور بنجاح!")

        # Stats strip
        p_count = sum(1 for s in filt if st.session_state.attendance[date_key].get(s["id"])=="حاضر")
        a_count = sum(1 for s in filt if st.session_state.attendance[date_key].get(s["id"])=="غائب")
        l_count = sum(1 for s in filt if st.session_state.attendance[date_key].get(s["id"])=="متأخر")
        n_count = len(filt) - p_count - a_count - l_count
        sc1,sc2,sc3,sc4 = st.columns(4)
        kpi_card(sc1,"gr","✅",p_count,"حاضر")
        kpi_card(sc2,"re","❌",a_count,"غائب")
        kpi_card(sc3,"am","⏰",l_count,"متأخر")
        kpi_card(sc4,"te","❓",n_count,"غير مسجل")

        st.markdown('<hr>', unsafe_allow_html=True)
        for s in filt:
            cur = st.session_state.attendance[date_key].get(s["id"],"غير مسجل")
            ci,cs,cw,csave = st.columns([3,2,1,1])
            ci.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;padding:8px 0">
                <div class="av {ac(s['name'])}" style="width:38px;height:38px;font-size:0.85rem">{s['name'][0]}</div>
                <div>
                    <div class="sc-name" style="font-size:0.88rem">{s['name']}</div>
                    <span class="gb {gc(s.get('group',''))}" style="font-size:0.68rem">{s.get('group','')}</span>
                </div>
            </div>""", unsafe_allow_html=True)
            ns = cs.selectbox("الحالة",["حاضر","غائب","متأخر","غير مسجل"],
                index=["حاضر","غائب","متأخر","غير مسجل"].index(cur),
                key=f"at_{s['id']}_{date_key}", label_visibility="collapsed")
            st.session_state.attendance[date_key][s["id"]] = ns
            if ns=="غائب" and s.get("parent_phone"):
                msg = f"السلام عليكم، نود إبلاغكم بغياب نجلكم/كريمتكم *{s['name']}* اليوم {sel_date.strftime('%d/%m/%Y')} 📌"
                cw.markdown(f'<a href="{wa(s["parent_phone"],msg)}" target="_blank" class="wa-sm" style="margin-top:10px;display:block">💬</a>', unsafe_allow_html=True)
            if csave.button("💾", key=f"save_{s['id']}_{date_key}", help="حفظ"):
                save_json(ATTENDANCE_FILE, st.session_state.attendance)
                st.toast(f"✅ تم حفظ {s['name']}")
            st.markdown('<hr style="margin:2px 0">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: REPORTS
# ══════════════════════════════════════════════════════════════
elif page == "reports":
    ph("📊","am","التقارير والإحصائيات","تحليل شامل لحضور وغياب الطلاب")

    if not st.session_state.students:
        st.markdown('<div class="empty"><span class="ei">📊</span><strong>لا توجد بيانات</strong><span>أضف طلاباً وسجّل الحضور أولاً</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        fg = st.selectbox("فلتر بالمجموعة", ["الكل"]+st.session_state.groups)
        st.markdown('</div>', unsafe_allow_html=True)

        sf = st.session_state.students if fg=="الكل" else [s for s in st.session_state.students if s.get("group")==fg]
        rows=[]
        for s in sf:
            total   = len(st.session_state.attendance)
            present = sum(1 for d in st.session_state.attendance.values() if d.get(s["id"])=="حاضر")
            absent  = sum(1 for d in st.session_state.attendance.values() if d.get(s["id"])=="غائب")
            rows.append({"الاسم":s["name"],"المجموعة":s.get("group",""),
                         "ولي الأمر":s.get("parent_name",""),"الموبايل":s.get("parent_phone",""),
                         "أيام الحضور":present,"أيام الغياب":absent,
                         "نسبة الحضور %":round((present/total*100) if total>0 else 0,1)})
        df = pd.DataFrame(rows)
        if len(df)>0:
            c1,c2,c3 = st.columns(3)
            avg_att = df['نسبة الحضور %'].mean()
            kpi_card(c1,"bl","📈",f"{avg_att:.1f}%","متوسط الحضور")
            kpi_card(c2,"gr","🏆",df.loc[df['أيام الحضور'].idxmax(),"الاسم"],"الأكثر حضوراً")
            kpi_card(c3,"am","⚠️",df.loc[df['أيام الغياب'].idxmax(),"الاسم"],"الأكثر غياباً")

        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True, hide_index=True)
        if st.button("📥  تحميل Excel", use_container_width=True):
            buf = io.BytesIO()
            with pd.ExcelWriter(buf, engine="openpyxl") as w:
                df.to_excel(w, index=False, sheet_name="التقرير")
            st.session_state["excel_buf"] = buf.getvalue()
        if "excel_buf" in st.session_state:
            st.download_button(
                "💾  اضغط هنا للتنزيل",
                data=st.session_state["excel_buf"],
                file_name=f"تقرير_{NOW.strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                use_container_width=True
            )
        st.markdown('</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════
# PAGE: MESSAGES
# ══════════════════════════════════════════════════════════════
elif page == "messages":
    ph("💬","gr","إرسال رسائل واتساب","تواصل مع أولياء الأمور بضغطة واحدة")

    if not st.session_state.students:
        st.markdown('<div class="empty"><span class="ei">💬</span><strong>لا يوجد طلاب</strong><span>أضف طلاباً أولاً</span></div>', unsafe_allow_html=True)
    else:
        t1,t2 = st.tabs(["📨  رسالة لطالب","📢  رسالة لمجموعة"])

        with t1:
            st.markdown('<div class="card">', unsafe_allow_html=True)

            # ── Group filter pills for fast access ──
            all_groups = ["الكل"] + st.session_state.groups
            if "t1_group_filter" not in st.session_state:
                st.session_state.t1_group_filter = "الكل"

            st.markdown('<div style="font-size:0.78rem;font-weight:700;color:var(--text-mid);margin-bottom:8px">🗂️ تصفية حسب المجموعة</div>', unsafe_allow_html=True)
            pill_cols = st.columns(len(all_groups))
            for pi, grp in enumerate(all_groups):
                is_active = st.session_state.t1_group_filter == grp
                btn_style = "primary" if is_active else "secondary"
                if pill_cols[pi].button(grp, key=f"t1_pill_{grp}", type=btn_style if is_active else "secondary",
                                         use_container_width=True):
                    st.session_state.t1_group_filter = grp
                    st.rerun()

            st.markdown('<hr style="margin:12px 0">', unsafe_allow_html=True)

            # Filtered students list
            group_filter = st.session_state.t1_group_filter
            filtered_students = st.session_state.students if group_filter=="الكل" else \
                                [s for s in st.session_state.students if s.get("group")==group_filter]

            c1,c2 = st.columns([1,1], gap="large")
            with c1:
                student_names = [s["name"] for s in filtered_students]
                if not student_names:
                    st.info("لا يوجد طلاب في هذه المجموعة")
                    sel = None
                else:
                    sn  = st.selectbox("اختر الطالب", student_names)
                    sel = next((s for s in filtered_students if s["name"]==sn), None)

                if sel:
                    tmap = {
                        "إشعار غياب":   f"السلام عليكم، نود إبلاغكم بغياب نجلكم/كريمتكم *{sel['name']}* اليوم. يرجى التواصل 🙏",
                        "تذكير بواجب":  f"السلام عليكم، تذكير بتسليم واجب *{sel['name']}* غداً 📚",
                        "تهنئة بتفوق":  f"السلام عليكم، مبروك! *{sel['name']}* حقق نتيجة ممتازة اليوم 🌟",
                        "طلب اجتماع":   f"السلام عليكم، نرجو ترتيب موعد للحديث عن مستوى *{sel['name']}* 🤝",
                        "رسالة مخصصة": ""
                    }
                    mt  = st.selectbox("نوع الرسالة", list(tmap.keys()))
                    msg = st.text_area("نص الرسالة", value=tmap[mt], height=120)

            with c2:
                if sel:
                    st.markdown(f"""
                    <div style="background:var(--bg);border:1px solid var(--border);border-radius:14px;padding:18px;margin-top:26px">
                        <div style="font-size:0.7rem;color:var(--text-light);font-weight:800;
                                    text-transform:uppercase;letter-spacing:1px;margin-bottom:12px">بيانات ولي الأمر</div>
                        <div style="display:flex;align-items:center;gap:10px;margin-bottom:14px">
                            <div class="av {ac(sel['name'])}" style="width:44px;height:44px">{sel['name'][0]}</div>
                            <div>
                                <div style="font-weight:800;font-size:0.93rem">{sel['name']}</div>
                                <span class="gb {gc(sel.get('group',''))}">{sel.get('group','—')}</span>
                            </div>
                        </div>
                        <div style="background:var(--surface);border-radius:10px;padding:12px 14px;border:1px solid var(--border)">
                            <div style="font-size:0.83rem;color:var(--text-mid);margin-bottom:6px">
                                👤 <strong>{sel.get('parent_name','—')}</strong>
                            </div>
                            <div style="font-size:0.83rem;color:var(--text-mid)">
                                📞 <strong>{sel.get('parent_phone','—')}</strong>
                            </div>
                        </div>
                    </div>""", unsafe_allow_html=True)
                    if sel.get("parent_phone") and msg:
                        st.markdown(f'<a href="{wa(sel["parent_phone"],msg)}" target="_blank" class="wa-lg">📱  إرسال عبر واتساب  →</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with t2:
            st.markdown('<div class="card">', unsafe_allow_html=True)
            if not st.session_state.groups:
                st.warning("أضف مجموعات أولاً")
            else:
                # Group filter pills for tab2
                st.markdown('<div style="font-size:0.78rem;font-weight:700;color:var(--text-mid);margin-bottom:8px">🗂️ اختر المجموعة</div>', unsafe_allow_html=True)
                sg = st.selectbox("اختر المجموعة", st.session_state.groups, key="msg_g", label_visibility="collapsed")

                bc = st.text_area("نص الرسالة",
                    placeholder="اكتب الرسالة...\nاستخدم {اسم_الطالب} لإضافة اسم الطالب تلقائياً", height=120)

                if bc:
                    gstu = [s for s in st.session_state.students if s.get("group")==sg and s.get("parent_phone")]
                    st.markdown(f"""
                    <div style="background:linear-gradient(135deg,var(--blue-light),var(--purple-light));
                                border-radius:12px;padding:12px 16px;font-size:0.85rem;margin:12px 0;
                                border:1px solid rgba(67,97,238,0.15)">
                        📢 سيتم الإرسال لـ <strong style="color:var(--blue)">{len(gstu)} ولي أمر</strong>
                        من مجموعة <strong style="color:var(--purple)">{sg}</strong>
                    </div>""", unsafe_allow_html=True)

                    for s in gstu:
                        m = bc.replace("{اسم_الطالب}",s["name"])
                        c1,c2 = st.columns([5,1])
                        c1.markdown(f"""
                        <div style="display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid var(--border)">
                            <div class="av {ac(s['name'])}" style="width:32px;height:32px;font-size:0.78rem">{s['name'][0]}</div>
                            <div>
                                <div style="font-weight:700;font-size:0.85rem">{s['name']}</div>
                                <div style="font-size:0.74rem;color:var(--text-mid)">{s.get('parent_name','')} · {s['parent_phone']}</div>
                            </div>
                        </div>""", unsafe_allow_html=True)
                        c2.markdown(f'<a href="{wa(s["parent_phone"],m)}" target="_blank" class="wa-sm" style="margin-top:12px">💬</a>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)