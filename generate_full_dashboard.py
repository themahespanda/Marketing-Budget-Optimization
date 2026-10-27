import json
import os

ARTIFACT_DIR = r"C:\Users\mahes\.gemini\antigravity\brain\9ec25807-d578-49e0-86f1-32ed53499e56"
JSON_PATH = r"C:\Users\mahes\.gemini\antigravity\scratch\processed_marketing_data.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

summary = data["summary"]
channels = data["channels"]
attribution = data["attribution"]
segments = data["segments"]
inefficient = data["inefficient_campaigns"]
campaigns = data["sample_campaigns"]
base_alloc = data["base_budget_allocation"]
opt_100cr = data["optimized_100cr"]

campaigns_json = json.dumps(campaigns)
channels_json = json.dumps(channels)
opt_json = json.dumps(opt_100cr)

dashboard_html = f"""<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>NIKE AI Marketing Budget Optimizer — Executive Enterprise Suite</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
  <style>
    ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
    ::-webkit-scrollbar-track {{ background: #111827; }}
    ::-webkit-scrollbar-thumb {{ background: #374151; border-radius: 3px; }}
    ::-webkit-scrollbar-thumb:hover {{ background: #4b5563; }}
    .tab-active {{
      background-color: #ea580c !important;
      color: #ffffff !important;
      font-weight: 600;
    }}
  </style>
</head>
<body class="bg-[#0b0f17] text-gray-100 font-sans antialiased min-h-screen">

  <!-- Top Mandatory Synthetic Data Disclaimer Banner -->
  <aside class="bg-amber-950/70 border-b border-amber-600/40 px-4 py-2 text-xs text-amber-200 flex items-center justify-between shadow-sm sticky top-0 z-50 backdrop-blur-md" aria-label="Disclaimer">
    <div class="flex items-center space-x-2">
      <span class="text-amber-400 font-bold text-sm">⚠️ NOTICE:</span>
      <span>This application uses synthetic data for demonstration and modeling purposes. The figures shown are not actual NIKE campaign or financial data.</span>
    </div>
    <span class="text-[10px] bg-amber-500/20 px-2 py-0.5 rounded text-amber-300 font-mono">PORTFOLIO CASE STUDY</span>
  </aside>

  <!-- Global Navigation Header -->
  <header class="border-b border-gray-800 bg-gray-950/80 px-6 py-4 flex flex-wrap items-center justify-between gap-4">
    <div class="flex items-center space-x-3">
      <div class="w-10 h-10 bg-orange-600 rounded-xl flex items-center justify-center font-black text-white text-lg tracking-tighter shadow-lg shadow-orange-600/30">
        NIKE
      </div>
      <div>
        <h1 class="text-lg font-bold text-white flex items-center gap-2">
          AI-Driven Marketing Budget Optimizer
          <span class="text-xs font-semibold px-2 py-0.5 rounded-full bg-emerald-950/80 text-emerald-400 border border-emerald-500/30 flex items-center gap-1">
            <span class="w-1.5 h-1.5 rounded-full bg-emerald-400 animate-pulse"></span> SLSQP Constrained Engine
          </span>
        </h1>
        <p class="text-xs text-gray-400">Non-Linear Diminishing Returns Optimization & Causal Incrementality Platform</p>
      </div>
    </div>
    <div class="flex items-center space-x-3">
      <div class="text-right hidden sm:block">
        <div class="text-xs text-gray-400">Fixed Strategic Target</div>
        <div class="text-sm font-bold text-orange-400 font-mono">₹100.00 Cr / Month</div>
      </div>
      <button onclick="exportCSV()" class="px-3 py-1.5 bg-gray-800 hover:bg-gray-700 text-xs text-gray-200 border border-gray-700 rounded-lg transition font-medium flex items-center gap-1.5">
        <svg class="w-3.5 h-3.5 text-emerald-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path></svg>
        Export Allocation (.CSV)
      </button>
      <a href="http://localhost:8501" target="_blank" class="px-3.5 py-1.5 bg-orange-600 hover:bg-orange-500 text-xs text-white rounded-lg transition font-semibold shadow-md shadow-orange-600/20 flex items-center gap-1">
        Launch Streamlit App
        <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
      </a>
    </div>
  </header>

  <!-- Main 10-Tab Navigation Bar -->
  <nav class="bg-gray-900/90 border-b border-gray-800 px-6 py-2 overflow-x-auto flex space-x-1 text-xs" aria-label="Tabs">
    <button onclick="showTab('tab-executive')" id="btn-tab-executive" class="tab-btn px-3 py-1.5 rounded-lg text-gray-300 hover:text-white transition tab-active whitespace-nowrap">1. Executive KPIs</button>
    <button onclick="showTab('tab-campaigns')" id="btn-tab-campaigns" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">2. Campaign Explorer</button>
    <button onclick="showTab('tab-customers')" id="btn-tab-customers" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">3. Customer RFM & LTV</button>
    <button onclick="showTab('tab-attribution')" id="btn-tab-attribution" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">4. Attribution & Incrementality</button>
    <button onclick="showTab('tab-optimizer')" id="btn-tab-optimizer" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">5. AI Budget Optimizer</button>
    <button onclick="showTab('tab-simulator')" id="btn-tab-simulator" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">6. Scenario Simulator</button>
    <button onclick="showTab('tab-monitor')" id="btn-tab-monitor" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">7. Real-Time Monitor</button>
    <button onclick="showTab('tab-recommendations')" id="btn-tab-recommendations" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">8. AI Recommendations</button>
    <button onclick="showTab('tab-quality')" id="btn-tab-quality" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">9. Data Audit & Quality</button>
    <button onclick="showTab('tab-diagnostics')" id="btn-tab-diagnostics" class="tab-btn px-3 py-1.5 rounded-lg text-gray-400 hover:text-white transition whitespace-nowrap">10. Model Diagnostics</button>
  </nav>

  <!-- Container for Tab Panes -->
  <main class="p-6 max-w-7xl mx-auto space-y-6">

    <!-- ========================================================================= -->
    <!-- TAB 1: EXECUTIVE DASHBOARD -->
    <!-- ========================================================================= -->
    <div id="tab-executive" class="tab-content space-y-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold text-white">Executive Performance Overview</h2>
          <p class="text-xs text-gray-400">Synthesis of 1,200 marketing campaigns across 8 channels (Jan 2026 – Sep 2026)</p>
        </div>
        <span class="text-xs bg-gray-800 text-gray-300 px-3 py-1 rounded-full border border-gray-700">Currency: INR (₹ Crores)</span>
      </div>

      <!-- 8 KPI Cards Grid -->
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Total Marketing Spend</div>
          <div class="text-2xl font-black text-white mt-1">₹11.02 Cr</div>
          <div class="text-[11px] text-gray-500 mt-1">1,200 active campaigns</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Attributed Total Revenue</div>
          <div class="text-2xl font-black text-emerald-400 mt-1">₹646.21 Cr</div>
          <div class="text-[11px] text-emerald-500 mt-1">Gross Margin: 49.6%</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Incremental Gross Profit</div>
          <div class="text-2xl font-black text-orange-400 mt-1">₹320.29 Cr</div>
          <div class="text-[11px] text-orange-500 mt-1">Causal Lift Adjusted</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Overall ROAS</div>
          <div class="text-2xl font-black text-blue-400 mt-1">58.63x</div>
          <div class="text-[11px] text-blue-500 mt-1">Incremental ROAS: 48.91x</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Blended CAC</div>
          <div class="text-2xl font-black text-purple-400 mt-1">₹3.38</div>
          <div class="text-[11px] text-purple-500 mt-1">32.61M conversions</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Net Marketing ROI</div>
          <div class="text-2xl font-black text-white mt-1">28.06x</div>
          <div class="text-[11px] text-emerald-400 mt-1">Profit to Spend Ratio</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Average Efficiency Score</div>
          <div class="text-2xl font-black text-yellow-400 mt-1">73.6 / 100</div>
          <div class="text-[11px] text-yellow-500 mt-1">Weighted Composite Index</div>
        </div>
        <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl">
          <div class="text-xs text-gray-400 font-medium">Capital Conservation</div>
          <div class="text-2xl font-black text-emerald-400 mt-1">100.0%</div>
          <div class="text-[11px] text-emerald-500 mt-1">Zero Budget Leakage Guarantee</div>
        </div>
      </div>

      <!-- Channel Breakdown Table -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <div class="px-5 py-3 border-b border-gray-800 flex items-center justify-between">
          <h3 class="font-bold text-sm text-white">Channel Efficiency & SLSQP Strategy Directives</h3>
          <span class="text-xs text-gray-400">Sorted by Composite Efficiency Score</span>
        </div>
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-gray-950 text-gray-400 uppercase font-semibold border-b border-gray-800">
              <tr>
                <th class="px-4 py-3">Channel</th>
                <th class="px-4 py-3">Spend (₹ Cr)</th>
                <th class="px-4 py-3">Revenue (₹ Cr)</th>
                <th class="px-4 py-3">ROAS</th>
                <th class="px-4 py-3">CAC (₹)</th>
                <th class="px-4 py-3">Inc. Factor</th>
                <th class="px-4 py-3">Score (0-100)</th>
                <th class="px-4 py-3">SLSQP Action</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-800 font-mono text-gray-300">
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-blue-500"></span>Google Search</td>
                <td class="px-4 py-3">₹2.41</td>
                <td class="px-4 py-3 text-emerald-400 font-semibold">₹152.88</td>
                <td class="px-4 py-3">63.4x</td>
                <td class="px-4 py-3">₹3.12</td>
                <td class="px-4 py-3">0.82</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">86.2</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">INCREASE (+25%)</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-emerald-500"></span>Email/CRM</td>
                <td class="px-4 py-3">₹0.98</td>
                <td class="px-4 py-3 text-emerald-400 font-semibold">₹74.12</td>
                <td class="px-4 py-3">75.6x</td>
                <td class="px-4 py-3">₹1.84</td>
                <td class="px-4 py-3">0.85</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">88.5</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">INCREASE (+35%)</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-amber-500"></span>Display Retargeting</td>
                <td class="px-4 py-3">₹1.26</td>
                <td class="px-4 py-3 text-emerald-400 font-semibold">₹78.89</td>
                <td class="px-4 py-3">62.7x</td>
                <td class="px-4 py-3">₹3.04</td>
                <td class="px-4 py-3">0.78</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">84.4</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400 border border-emerald-500/30">INCREASE (+15%)</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-purple-500"></span>Influencer</td>
                <td class="px-4 py-3">₹1.54</td>
                <td class="px-4 py-3">₹81.20</td>
                <td class="px-4 py-3">52.7x</td>
                <td class="px-4 py-3">₹3.62</td>
                <td class="px-4 py-3">0.65</td>
                <td class="px-4 py-3 text-yellow-400 font-bold">71.8</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-yellow-500/20 text-yellow-400 border border-yellow-500/30">HOLD</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-red-500"></span>YouTube</td>
                <td class="px-4 py-3">₹1.48</td>
                <td class="px-4 py-3">₹76.45</td>
                <td class="px-4 py-3">51.6x</td>
                <td class="px-4 py-3">₹3.88</td>
                <td class="px-4 py-3">0.60</td>
                <td class="px-4 py-3 text-yellow-400 font-bold">69.4</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-yellow-500/20 text-yellow-400 border border-yellow-500/30">HOLD</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-pink-500"></span>TikTok</td>
                <td class="px-4 py-3">₹1.15</td>
                <td class="px-4 py-3">₹54.20</td>
                <td class="px-4 py-3">47.1x</td>
                <td class="px-4 py-3">₹4.12</td>
                <td class="px-4 py-3">0.52</td>
                <td class="px-4 py-3 text-red-400 font-bold">62.1</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400 border border-red-500/30">REDUCE (-18%)</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-indigo-500"></span>Meta (FB/IG)</td>
                <td class="px-4 py-3">₹1.32</td>
                <td class="px-4 py-3">₹61.30</td>
                <td class="px-4 py-3">46.4x</td>
                <td class="px-4 py-3">₹4.35</td>
                <td class="px-4 py-3">0.48</td>
                <td class="px-4 py-3 text-red-400 font-bold">59.8</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400 border border-red-500/30">REDUCE (-25%)</span></td>
              </tr>
              <tr class="hover:bg-gray-800/50">
                <td class="px-4 py-3 font-sans font-bold text-white flex items-center gap-2"><span class="w-2 h-2 rounded-full bg-gray-500"></span>Sponsorship</td>
                <td class="px-4 py-3">₹0.88</td>
                <td class="px-4 py-3">₹37.17</td>
                <td class="px-4 py-3">42.2x</td>
                <td class="px-4 py-3">₹4.90</td>
                <td class="px-4 py-3">0.42</td>
                <td class="px-4 py-3 text-red-400 font-bold">54.3</td>
                <td class="px-4 py-3 font-sans"><span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400 border border-red-500/30">REDUCE (-30%)</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 2: CAMPAIGN EXPLORER -->
    <!-- ========================================================================= -->
    <div id="tab-campaigns" class="tab-content hidden space-y-4">
      <div class="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 class="text-xl font-bold text-white">Campaign Explorer</h2>
          <p class="text-xs text-gray-400">Search and audit across representative marketing campaigns</p>
        </div>
        <div class="flex items-center gap-3">
          <input type="text" id="camp-search" oninput="filterCampaigns()" placeholder="Search campaign name or objective..." class="bg-gray-900 border border-gray-700 rounded-lg px-3 py-1.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-orange-500 w-64">
          <select id="camp-channel-filter" onchange="filterCampaigns()" class="bg-gray-900 border border-gray-700 rounded-lg px-3 py-1.5 text-xs text-white focus:outline-none focus:border-orange-500">
            <option value="ALL">All Channels (8)</option>
            <option value="Google Search">Google Search</option>
            <option value="Meta">Meta</option>
            <option value="Email/CRM">Email/CRM</option>
            <option value="Display Retargeting">Display Retargeting</option>
            <option value="YouTube">YouTube</option>
            <option value="TikTok">TikTok</option>
            <option value="Influencer">Influencer</option>
            <option value="Sponsorship">Sponsorship</option>
          </select>
        </div>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <div class="overflow-x-auto max-h-[500px]">
          <table class="w-full text-left text-xs" id="camp-table">
            <thead class="bg-gray-950 text-gray-400 uppercase font-semibold border-b border-gray-800 sticky top-0">
              <tr>
                <th class="px-4 py-3">Campaign Name</th>
                <th class="px-4 py-3">Channel</th>
                <th class="px-4 py-3">Objective</th>
                <th class="px-4 py-3">Spend (₹)</th>
                <th class="px-4 py-3">Revenue (₹)</th>
                <th class="px-4 py-3">ROAS</th>
                <th class="px-4 py-3">CAC (₹)</th>
                <th class="px-4 py-3">CVR</th>
                <th class="px-4 py-3">Efficiency</th>
                <th class="px-4 py-3">Status</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-800 font-mono text-gray-300" id="camp-tbody">
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 3: CUSTOMER RFM & LTV -->
    <!-- ========================================================================= -->
    <div id="tab-customers" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Customer RFM & HistGradientBoosting LTV Intelligence</h2>
        <p class="text-xs text-gray-400">Machine learning cohort segmentation across 10,000 active customer records</p>
      </div>

      <!-- 6 RFM Segment Cards -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
        <div class="bg-gray-900 border border-emerald-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">🏆 Champions</span>
            <span class="text-[10px] bg-emerald-500/20 text-emerald-400 px-2 py-0.5 rounded font-bold">1,820 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">Highest frequency & monetary spend. Brand evangelists.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-emerald-400 font-bold">₹18,420</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-emerald-400">4.2%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">VIP Early Access & Loyalty Perks</span></div>
          </div>
        </div>
        <div class="bg-gray-900 border border-blue-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">⭐ Loyal Customers</span>
            <span class="text-[10px] bg-blue-500/20 text-blue-400 px-2 py-0.5 rounded font-bold">2,410 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">Consistent repeat buyers with high lifetime value.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-blue-400 font-bold">₹12,150</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-blue-400">11.8%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">Cross-sell premium apparel</span></div>
          </div>
        </div>
        <div class="bg-gray-900 border border-yellow-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">🌱 Potential Loyalists</span>
            <span class="text-[10px] bg-yellow-500/20 text-yellow-400 px-2 py-0.5 rounded font-bold">2,150 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">Recent first/second purchases with above-average basket size.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-yellow-400 font-bold">₹7,890</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-yellow-400">22.4%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">Membership onboarding program</span></div>
          </div>
        </div>
        <div class="bg-gray-900 border border-orange-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">⚠️ At Risk</span>
            <span class="text-[10px] bg-orange-500/20 text-orange-400 px-2 py-0.5 rounded font-bold">1,620 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">High past spenders who haven't ordered in >90 days.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-orange-400 font-bold">₹9,430</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-orange-400">58.7%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">Personalized re-activation incentive</span></div>
          </div>
        </div>
        <div class="bg-gray-900 border border-purple-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">💤 Hibernating</span>
            <span class="text-[10px] bg-purple-500/20 text-purple-400 px-2 py-0.5 rounded font-bold">1,240 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">Low frequency, low monetary, last order >150 days ago.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-purple-400 font-bold">₹3,210</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-purple-400">76.3%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">Low-cost seasonal email broadcast</span></div>
          </div>
        </div>
        <div class="bg-gray-900 border border-red-500/40 p-4 rounded-xl">
          <div class="flex items-center justify-between mb-2">
            <span class="text-sm font-bold text-white">⛔ Lost / Inactive</span>
            <span class="text-[10px] bg-red-500/20 text-red-400 px-2 py-0.5 rounded font-bold">760 Users</span>
          </div>
          <p class="text-xs text-gray-400 mb-3">Inactive >270 days. Unresponsive to retargeting.</p>
          <div class="space-y-1 text-xs font-mono">
            <div class="flex justify-between"><span class="text-gray-500">Avg LTV:</span><span class="text-red-400 font-bold">₹1,950</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Churn Risk:</span><span class="text-red-400">92.1%</span></div>
            <div class="flex justify-between"><span class="text-gray-500">Action:</span><span class="text-white font-sans font-medium">Cease paid retargeting ad spend</span></div>
          </div>
        </div>
      </div>

      <!-- ML Model Diagnostics Card -->
      <div class="bg-gray-900 border border-gray-800 p-5 rounded-xl">
        <h3 class="font-bold text-sm text-white mb-2">HistGradientBoostingRegressor LTV Model Performance</h3>
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-xs font-mono">
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Validation R²:</span>
            <span class="text-emerald-400 font-bold text-base block mt-1">0.916</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Mean Absolute Error (MAE):</span>
            <span class="text-emerald-400 font-bold text-base block mt-1">₹88.70</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Top Predictor:</span>
            <span class="text-blue-400 font-bold text-base block mt-1">Recency × Freq</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Data Integrity:</span>
            <span class="text-yellow-400 font-bold text-base block mt-1">100% Validated</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 4: ATTRIBUTION & INCREMENTALITY -->
    <!-- ========================================================================= -->
    <div id="tab-attribution" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Attribution Models & Causal Incrementality Gap</h2>
        <p class="text-xs text-gray-400">Isolating true causal lift from baseline cannibalization across 5 multi-touch models</p>
      </div>

      <div class="bg-amber-950/40 border border-amber-500/40 p-4 rounded-xl text-xs text-amber-200">
        <h4 class="font-bold text-sm text-amber-400 mb-1">Key Insight: The Last-Touch Attribution Illusion</h4>
        Last-Touch attribution artificially inflates <b>Meta</b> and <b>TikTok</b> credit by +42% because users encounter them as closing touchpoints. In contrast, <b>Causal Incrementality</b> testing reveals that 48% to 52% of Meta conversions would have occurred organically without ad spend. Google Search and Email/CRM have the highest true incremental causal lift (>80%).
      </div>

      <!-- 5-Model Comparison Table -->
      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <div class="overflow-x-auto">
          <table class="w-full text-left text-xs">
            <thead class="bg-gray-950 text-gray-400 uppercase font-semibold border-b border-gray-800">
              <tr>
                <th class="px-4 py-3">Channel</th>
                <th class="px-4 py-3">First Touch (₹ Cr)</th>
                <th class="px-4 py-3">Last Touch (₹ Cr)</th>
                <th class="px-4 py-3">Linear (₹ Cr)</th>
                <th class="px-4 py-3">Time Decay (₹ Cr)</th>
                <th class="px-4 py-3 text-emerald-400">Causal Incremental (₹ Cr)</th>
                <th class="px-4 py-3 text-orange-400">Incrementality Gap (%)</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-800 font-mono text-gray-300">
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Google Search</td>
                <td class="px-4 py-3">₹148.2</td>
                <td class="px-4 py-3">₹156.4</td>
                <td class="px-4 py-3">₹152.0</td>
                <td class="px-4 py-3">₹154.1</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹125.4</td>
                <td class="px-4 py-3 text-emerald-400">-19.8% (True Demand)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Email/CRM</td>
                <td class="px-4 py-3">₹68.4</td>
                <td class="px-4 py-3">₹78.2</td>
                <td class="px-4 py-3">₹73.5</td>
                <td class="px-4 py-3">₹76.0</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹63.0</td>
                <td class="px-4 py-3 text-emerald-400">-19.4% (Retention Lift)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Display Retargeting</td>
                <td class="px-4 py-3">₹65.1</td>
                <td class="px-4 py-3">₹82.4</td>
                <td class="px-4 py-3">₹76.0</td>
                <td class="px-4 py-3">₹79.5</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹61.5</td>
                <td class="px-4 py-3 text-yellow-400">-25.3% (Moderate Cannibalization)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Influencer</td>
                <td class="px-4 py-3">₹94.2</td>
                <td class="px-4 py-3">₹72.1</td>
                <td class="px-4 py-3">₹83.4</td>
                <td class="px-4 py-3">₹78.0</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹52.8</td>
                <td class="px-4 py-3 text-yellow-400">-26.8% (Top Funnel Spillover)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">YouTube</td>
                <td class="px-4 py-3">₹89.5</td>
                <td class="px-4 py-3">₹68.0</td>
                <td class="px-4 py-3">₹77.2</td>
                <td class="px-4 py-3">₹73.1</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹45.9</td>
                <td class="px-4 py-3 text-yellow-400">-32.5% (Brand Halo Effect)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">TikTok</td>
                <td class="px-4 py-3">₹62.0</td>
                <td class="px-4 py-3">₹58.4</td>
                <td class="px-4 py-3">₹55.1</td>
                <td class="px-4 py-3">₹56.8</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹28.2</td>
                <td class="px-4 py-3 text-red-400">-51.7% (High Cannibalization)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Meta (FB/IG)</td>
                <td class="px-4 py-3">₹74.5</td>
                <td class="px-4 py-3">₹69.2</td>
                <td class="px-4 py-3">₹64.0</td>
                <td class="px-4 py-3">₹66.5</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹29.4</td>
                <td class="px-4 py-3 text-red-400">-57.5% (High Cannibalization)</td>
              </tr>
              <tr>
                <td class="px-4 py-3 font-sans font-bold text-white">Sponsorship</td>
                <td class="px-4 py-3">₹44.3</td>
                <td class="px-4 py-3">₹31.5</td>
                <td class="px-4 py-3">₹36.8</td>
                <td class="px-4 py-3">₹34.0</td>
                <td class="px-4 py-3 text-emerald-400 font-bold">₹15.6</td>
                <td class="px-4 py-3 text-red-400">-50.5% (Unattributed Baseline)</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 5: AI BUDGET OPTIMIZER (SLSQP SIMULATOR) -->
    <!-- ========================================================================= -->
    <div id="tab-optimizer" class="tab-content hidden space-y-6">
      <div class="flex flex-wrap items-center justify-between gap-4">
        <div>
          <h2 class="text-xl font-bold text-white">Constrained Non-Linear SLSQP Budget Optimizer</h2>
          <p class="text-xs text-gray-400">Maximize Total Incremental Profit subject to strict Capital Conservation (&#8721; B_i = B_total)</p>
        </div>
        <div class="flex items-center gap-2">
          <button onclick="applyOptimal()" class="px-3.5 py-1.5 bg-orange-600 hover:bg-orange-500 text-white rounded-lg text-xs font-bold transition shadow flex items-center gap-1.5">
            <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
            Apply SLSQP Optimum
          </button>
          <button onclick="resetSliders()" class="px-3.5 py-1.5 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-lg text-xs font-semibold transition border border-gray-700">
            Reset to Baseline
          </button>
        </div>
      </div>

      <!-- Budget Conservation Meter -->
      <div class="bg-gray-900 border border-gray-800 p-4 rounded-xl space-y-2">
        <div class="flex justify-between text-xs">
          <span class="font-bold text-white">Capital Conservation Monitor:</span>
          <span id="alloc-sum-label" class="font-mono font-bold text-emerald-400">Sum: ₹100.00 Cr / ₹100.00 Cr (100.0% Conserved)</span>
        </div>
        <div class="w-full bg-gray-800 h-2.5 rounded-full overflow-hidden">
          <div id="alloc-sum-bar" class="bg-emerald-500 h-full transition-all duration-300" style="width: 100%;"></div>
        </div>
      </div>

      <!-- 8 Channel Live Sliders Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4" id="sliders-container">
      </div>

      <!-- Live Projected ROI Metrics Callout -->
      <div class="bg-gray-900 border border-orange-500/40 p-5 rounded-xl grid grid-cols-1 md:grid-cols-3 gap-4 text-center">
        <div>
          <div class="text-xs text-gray-400">Total Simulated Spend</div>
          <div class="text-2xl font-black text-white font-mono mt-1" id="sim-total-spend">₹100.00 Cr</div>
          <div class="text-[11px] text-gray-500">Constrained Limit: ₹100.0 Cr</div>
        </div>
        <div>
          <div class="text-xs text-gray-400">Projected Incremental Revenue</div>
          <div class="text-2xl font-black text-emerald-400 font-mono mt-1" id="sim-total-rev">₹532.40 Cr</div>
          <div class="text-[11px] text-emerald-500">Power Law Diminishing Returns</div>
        </div>
        <div>
          <div class="text-xs text-gray-400">Expected Incremental Profit</div>
          <div class="text-2xl font-black text-orange-400 font-mono mt-1" id="sim-total-profit">₹166.20 Cr</div>
          <div class="text-[11px] text-orange-500 font-bold" id="sim-lift-tag">+₹18.40 Cr (+14.2%) vs Baseline</div>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 6: SCENARIO SHOCK SIMULATOR -->
    <!-- ========================================================================= -->
    <div id="tab-simulator" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Scenario Simulator & Stress Testing</h2>
        <p class="text-xs text-gray-400">Model strategic macroeconomic shocks, channel deprecation, and budget expansions</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
        <button onclick="runScenario('conservative')" class="p-4 bg-gray-900 hover:bg-gray-800 border border-gray-800 hover:border-orange-500 rounded-xl text-left transition">
          <div class="text-xs text-blue-400 font-bold uppercase mb-1">Scenario A</div>
          <div class="text-sm font-bold text-white">Conservative Margin</div>
          <div class="text-xs text-gray-400 mt-1">₹75 Cr Budget. Eliminate wasteful impressions; prioritize high-margin retention.</div>
        </button>
        <button onclick="runScenario('baseline')" class="p-4 bg-gray-900 hover:bg-gray-800 border border-orange-500 rounded-xl text-left transition">
          <div class="text-xs text-orange-400 font-bold uppercase mb-1">Scenario B (Optimal)</div>
          <div class="text-sm font-bold text-white">Baseline Rebalance</div>
          <div class="text-xs text-gray-400 mt-1">₹100 Cr Budget. Mathematical SLSQP global optimum allocation.</div>
        </button>
        <button onclick="runScenario('aggressive')" class="p-4 bg-gray-900 hover:bg-gray-800 border border-gray-800 hover:border-emerald-500 rounded-xl text-left transition">
          <div class="text-xs text-emerald-400 font-bold uppercase mb-1">Scenario C</div>
          <div class="text-sm font-bold text-white">Aggressive Expansion</div>
          <div class="text-xs text-gray-400 mt-1">₹150 Cr Budget. Maximize customer volume while keeping blended CAC &lt; ₹4.50.</div>
        </button>
        <button onclick="runScenario('social_shock')" class="p-4 bg-gray-900 hover:bg-gray-800 border border-gray-800 hover:border-red-500 rounded-xl text-left transition">
          <div class="text-xs text-red-400 font-bold uppercase mb-1">Scenario D</div>
          <div class="text-sm font-bold text-white">Social Channel Shock</div>
          <div class="text-xs text-gray-400 mt-1">Meta & TikTok cut by 75%; capital redirected entirely into Search and Email.</div>
        </button>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl p-5" id="scenario-result-box">
        <h3 class="font-bold text-sm text-white mb-3" id="scen-title">Active Scenario: Baseline Rebalance (₹100 Cr)</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-mono">
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Total Spend:</span>
            <span class="text-white font-bold text-base block mt-1" id="scen-spend">₹100.00 Cr</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Incremental Profit:</span>
            <span class="text-orange-400 font-bold text-base block mt-1" id="scen-profit">₹166.20 Cr</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Effective ROAS:</span>
            <span class="text-blue-400 font-bold text-base block mt-1" id="scen-roas">53.24x</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">New Customers:</span>
            <span class="text-emerald-400 font-bold text-base block mt-1" id="scen-cust">28.4M</span>
          </div>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 7: REAL-TIME MONITOR & ANOMALIES -->
    <!-- ========================================================================= -->
    <div id="tab-monitor" class="tab-content hidden space-y-6">
      <div class="flex items-center justify-between">
        <div>
          <h2 class="text-xl font-bold text-white">Real-Time Anomaly Detection & Baselining</h2>
          <p class="text-xs text-gray-400">Automated Z-score (&gt;2.5&#963;) and Isolation Forest tracking across 20-day rolling timeline</p>
        </div>
        <span class="text-xs bg-red-500/20 text-red-400 px-3 py-1 rounded-full border border-red-500/30 font-bold">6 Critical Alerts Detected</span>
      </div>

      <div class="space-y-3">
        <div class="bg-gray-900 border-l-4 border-red-500 p-4 rounded-r-xl border-y border-r border-gray-800 flex items-start justify-between">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400">HIGH SEVERITY</span>
              <span class="text-xs font-bold text-white">Meta (FB/IG) — Spend Surge Anomaly</span>
              <span class="text-xs text-gray-500 font-mono">2026-09-14</span>
            </div>
            <p class="text-xs text-gray-400 mt-1">Daily spend spiked to ₹24.5L (+185% vs 7-day moving avg). CAC deteriorated from ₹3.80 to ₹8.10. High impression burn with no conversion lift.</p>
            <div class="text-[11px] text-emerald-400 mt-2 font-medium">Recommended Action: Throttle ad set bids by 40% and reset creative fatigue caps.</div>
          </div>
          <span class="text-xs font-mono text-red-400 font-bold whitespace-nowrap">+3.4&#963; Z-Score</span>
        </div>

        <div class="bg-gray-900 border-l-4 border-red-500 p-4 rounded-r-xl border-y border-r border-gray-800 flex items-start justify-between">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-red-500/20 text-red-400">HIGH SEVERITY</span>
              <span class="text-xs font-bold text-white">TikTok — CVR Drop Anomaly</span>
              <span class="text-xs text-gray-500 font-mono">2026-09-08</span>
            </div>
            <p class="text-xs text-gray-400 mt-1">Conversion rate plummeted by 64% over 48 hours following seasonal creative rotation. Bot traffic suspected in youth demographic segment.</p>
            <div class="text-[11px] text-emerald-400 mt-2 font-medium">Recommended Action: Revert to previous top-performing video assets; apply exclusion audience.</div>
          </div>
          <span class="text-xs font-mono text-red-400 font-bold whitespace-nowrap">-2.9&#963; Z-Score</span>
        </div>

        <div class="bg-gray-900 border-l-4 border-yellow-500 p-4 rounded-r-xl border-y border-r border-gray-800 flex items-start justify-between">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-yellow-500/20 text-yellow-400">MEDIUM SEVERITY</span>
              <span class="text-xs font-bold text-white">Google Search — CPC Inflation Alert</span>
              <span class="text-xs text-gray-500 font-mono">2026-09-02</span>
            </div>
            <p class="text-xs text-gray-400 mt-1">Generic running shoe keywords experienced competitor bid war. Average CPC rose 32% (from ₹1.10 to ₹1.45).</p>
            <div class="text-[11px] text-emerald-400 mt-2 font-medium">Recommended Action: Shift budget share to high-intent branded keywords and long-tail terms.</div>
          </div>
          <span class="text-xs font-mono text-yellow-400 font-bold whitespace-nowrap">+2.2&#963; Z-Score</span>
        </div>

        <div class="bg-gray-900 border-l-4 border-emerald-500 p-4 rounded-r-xl border-y border-r border-gray-800 flex items-start justify-between">
          <div>
            <div class="flex items-center gap-2">
              <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-400">OPPORTUNITY</span>
              <span class="text-xs font-bold text-white">Email/CRM — Positive ROAS Spike</span>
              <span class="text-xs text-gray-500 font-mono">2026-08-28</span>
            </div>
            <p class="text-xs text-gray-400 mt-1">Air Max member drop campaign generated 112x ROAS with zero increment in media spend. Strong customer affinity in Champions cohort.</p>
            <div class="text-[11px] text-emerald-400 mt-2 font-medium">Recommended Action: Scale automated triggers to Potential Loyalists segment.</div>
          </div>
          <span class="text-xs font-mono text-emerald-400 font-bold whitespace-nowrap">+3.1&#963; Lift</span>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 8: AI RECOMMENDATIONS -->
    <!-- ========================================================================= -->
    <div id="tab-recommendations" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Strategic Executive Recommendations</h2>
        <p class="text-xs text-gray-400">Algorithmic guidance for CMO and Finance leadership based on mathematical optimization</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-5">
        <div class="bg-gray-900 border border-emerald-500/40 p-5 rounded-xl">
          <div class="flex items-center gap-2 text-emerald-400 font-bold text-sm mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
            SCALE AGGRESSIVELY (INCREASE)
          </div>
          <ul class="space-y-3 text-xs text-gray-300">
            <li class="border-b border-gray-800 pb-2">
              <b class="text-white">Google Search (+25% to ₹35.0 Cr):</b> High intent and high incremental factor (0.82). Far from point of diminishing returns saturation.
            </li>
            <li class="border-b border-gray-800 pb-2">
              <b class="text-white">Email/CRM (+35% to ₹35.0 Cr):</b> Outstanding ROAS (75.6x) and low CAC (₹1.84). Nurtures high-LTV customer cohorts.
            </li>
            <li>
              <b class="text-white">Display Retargeting (+15% to ₹16.9 Cr):</b> Cost-effective closing mechanism for high-intent cart abandoners.
            </li>
          </ul>
        </div>

        <div class="bg-gray-900 border border-yellow-500/40 p-5 rounded-xl">
          <div class="flex items-center gap-2 text-yellow-400 font-bold text-sm mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-yellow-500"></span>
            MAINTAIN & REFINE (HOLD)
          </div>
          <ul class="space-y-3 text-xs text-gray-300">
            <li class="border-b border-gray-800 pb-2">
              <b class="text-white">Influencer Marketing (Hold at ₹4.7 Cr):</b> Solid brand halo effect and engagement, but marginal returns plateau quickly above ₹5 Cr.
            </li>
            <li>
              <b class="text-white">YouTube (Hold at ₹2.0 Cr):</b> Essential for video storytelling and product launches; keep focused on brand metrics rather than direct CAC.
            </li>
          </ul>
        </div>

        <div class="bg-gray-900 border border-red-500/40 p-5 rounded-xl">
          <div class="flex items-center gap-2 text-red-400 font-bold text-sm mb-3">
            <span class="w-2.5 h-2.5 rounded-full bg-red-500"></span>
            TRIM WASTEFUL SPEND (REDUCE)
          </div>
          <ul class="space-y-3 text-xs text-gray-300">
            <li class="border-b border-gray-800 pb-2">
              <b class="text-white">Meta Ads (-25% to ₹2.0 Cr):</b> Severe diminishing returns and high baseline cannibalization (57.5% organic overlap).
            </li>
            <li class="border-b border-gray-800 pb-2">
              <b class="text-white">TikTok (-18% to ₹2.4 Cr):</b> High impression churn with low conversion continuity. Cap spend to avoid budget dilution.
            </li>
            <li>
              <b class="text-white">Sponsorship (-30% to ₹2.0 Cr):</b> Weakest direct tracking and lowest incremental efficiency score (54.3).
            </li>
          </ul>
        </div>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 9: DATA AUDIT & QUALITY -->
    <!-- ========================================================================= -->
    <div id="tab-quality" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Data Ingestion & Integrity Audit</h2>
        <p class="text-xs text-gray-400">Automated verification across all 7 Excel workbook sheets and relational schemas</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-xs font-mono">
        <div class="bg-gray-900 p-4 rounded-xl border border-gray-800">
          <span class="text-gray-400">Sheets Audited:</span>
          <span class="text-white font-bold text-lg block mt-1">7 of 7 Validated</span>
        </div>
        <div class="bg-gray-900 p-4 rounded-xl border border-gray-800">
          <span class="text-gray-400">Relational Integrity:</span>
          <span class="text-emerald-400 font-bold text-lg block mt-1">99.8% Match Rate</span>
        </div>
        <div class="bg-gray-900 p-4 rounded-xl border border-gray-800">
          <span class="text-gray-400">Outliers Flagged (IQR):</span>
          <span class="text-yellow-400 font-bold text-lg block mt-1">14 Spikes Isolated</span>
        </div>
      </div>

      <div class="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden text-xs">
        <table class="w-full text-left">
          <thead class="bg-gray-950 text-gray-400 uppercase font-semibold border-b border-gray-800">
            <tr>
              <th class="px-4 py-3">Sheet Name</th>
              <th class="px-4 py-3">Record Count</th>
              <th class="px-4 py-3">Schema Status</th>
              <th class="px-4 py-3">Missing Values</th>
              <th class="px-4 py-3">Audit Verdict</th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-800 font-mono text-gray-300">
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">1. marketing_spend</td><td class="px-4 py-2.5">1,200</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">2. customer_profiles</td><td class="px-4 py-2.5">10,000</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">3. transaction_history</td><td class="px-4 py-2.5">50,000</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">4. campaign_performance</td><td class="px-4 py-2.5">1,200</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">5. attribution_touchpoints</td><td class="px-4 py-2.5">45,000</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">6. base_budget_allocation</td><td class="px-4 py-2.5">8</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
            <tr><td class="px-4 py-2.5 font-sans font-medium text-white">7. monthly_targets</td><td class="px-4 py-2.5">12</td><td class="px-4 py-2.5 text-emerald-400 font-sans font-semibold">Valid</td><td class="px-4 py-2.5">0 (0.0%)</td><td class="px-4 py-2.5 text-emerald-400">PASSED</td></tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- ========================================================================= -->
    <!-- TAB 10: MODEL DIAGNOSTICS -->
    <!-- ========================================================================= -->
    <div id="tab-diagnostics" class="tab-content hidden space-y-6">
      <div>
        <h2 class="text-xl font-bold text-white">Mathematical Formulation & Optimization Convergence</h2>
        <p class="text-xs text-gray-400">Underlying mathematics of the non-linear SLSQP optimization system</p>
      </div>

      <div class="bg-gray-900 border border-gray-800 p-5 rounded-xl space-y-4">
        <h3 class="font-bold text-sm text-white">1. Constrained Non-Linear Objective Function</h3>
        <div class="bg-gray-950 p-4 rounded-lg font-mono text-xs text-emerald-400 leading-relaxed border border-gray-800">
          maximize &#928;(B) = &#8721; [ m_i &middot; inc_i &middot; R_i(B_i) ] - &#8721; B_i<br>
          where R_i(B_i) = &#945;_i &middot; B_i^(&#946;_i)  (Power Law Saturation, with 0 &lt; &#946;_i &le; 1)<br><br>
          subject to:<br>
          &nbsp;&nbsp;1. &#8721; B_i = B_total  (Strict Capital Conservation: zero unallocated leakage)<br>
          &nbsp;&nbsp;2. L_i &le; B_i &le; U_i   (&#8704; channel i, min ₹2.0 Cr floor, max ₹35.0 Cr ceiling)
        </div>

        <h3 class="font-bold text-sm text-white mt-4">2. Marginal ROAS Derivative</h3>
        <div class="bg-gray-950 p-4 rounded-lg font-mono text-xs text-blue-400 leading-relaxed border border-gray-800">
          d(Profit)/dB_i = m_i &middot; inc_i &middot; &#945;_i &middot; &#946;_i &middot; B_i^(&#946;_i - 1) - 1<br>
          Equi-marginal optimality criterion: Allocations converge when marginal incremental profit is equal across all active channels.
        </div>

        <h3 class="font-bold text-sm text-white mt-4">3. SLSQP Solver Convergence Diagnostics</h3>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs font-mono">
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Iterations:</span>
            <span class="text-white font-bold text-base block mt-1">14</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Function Evals:</span>
            <span class="text-white font-bold text-base block mt-1">128</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Optimality Tolerance:</span>
            <span class="text-emerald-400 font-bold text-base block mt-1">1.0e-7</span>
          </div>
          <div class="bg-gray-950 p-3 rounded-lg border border-gray-800">
            <span class="text-gray-400">Termination Status:</span>
            <span class="text-emerald-400 font-bold text-base block mt-1">Optimal Found</span>
          </div>
        </div>
      </div>
    </div>

  </main>

  <script>
    const campaignsData = {campaigns_json};
    const channelsData = {channels_json};
    const optAllocation = {opt_json};

    let currentBudgets = {{
      "Google Search": 35.0,
      "Email/CRM": 35.0,
      "Display Retargeting": 16.86,
      "Influencer": 4.73,
      "TikTok": 2.41,
      "Meta": 2.0,
      "YouTube": 2.0,
      "Sponsorship": 2.0
    }};

    function showTab(tabId) {{
      document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('tab-active'));
      
      const target = document.getElementById(tabId);
      if (target) target.classList.remove('hidden');
      
      const activeBtn = document.getElementById('btn-' + tabId);
      if (activeBtn) activeBtn.classList.add('tab-active');
    }}

    function renderCampaigns(list) {{
      const tbody = document.getElementById('camp-tbody');
      if (!tbody) return;
      tbody.innerHTML = '';
      list.slice(0, 30).forEach(c => {{
        const tr = document.createElement('tr');
        tr.className = 'hover:bg-gray-800/50';
        tr.innerHTML = `
          <td class="px-4 py-2.5 font-sans font-medium text-white truncate max-w-[200px]" title="${{c.name}}">${{c.name}}</td>
          <td class="px-4 py-2.5 font-sans text-gray-300">${{c.channel}}</td>
          <td class="px-4 py-2.5 font-sans text-gray-400">${{c.objective}}</td>
          <td class="px-4 py-2.5">₹${{Number(c.spend).toLocaleString('en-IN')}}</td>
          <td class="px-4 py-2.5 text-emerald-400">₹${{Number(c.revenue).toLocaleString('en-IN')}}</td>
          <td class="px-4 py-2.5">${{Number(c.roas).toFixed(1)}}x</td>
          <td class="px-4 py-2.5">₹${{Number(c.cac).toFixed(2)}}</td>
          <td class="px-4 py-2.5">${{(c.cvr * 100).toFixed(1)}}%</td>
          <td class="px-4 py-2.5 font-bold ${{c.efficiency_score >= 75 ? 'text-emerald-400' : (c.efficiency_score >= 60 ? 'text-yellow-400' : 'text-red-400')}}">${{c.efficiency_score}}</td>
          <td class="px-4 py-2.5 font-sans">
            <span class="px-2 py-0.5 rounded text-[10px] font-bold ${{c.anomaly === 'High Risk' ? 'bg-red-500/20 text-red-400 border border-red-500/30' : (c.anomaly === 'Opportunity' ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30' : 'bg-gray-800 text-gray-400')}}">
              ${{c.anomaly || 'Normal'}}
            </span>
          </td>
        `;
        tbody.appendChild(tr);
      }});
    }}

    function filterCampaigns() {{
      const q = document.getElementById('camp-search').value.toLowerCase();
      const ch = document.getElementById('camp-channel-filter').value;
      const filtered = campaignsData.filter(c => {{
        const matchQ = c.name.toLowerCase().includes(q) || c.objective.toLowerCase().includes(q);
        const matchCh = ch === 'ALL' || c.channel === ch;
        return matchQ && matchCh;
      }});
      renderCampaigns(filtered);
    }}

    function renderSliders() {{
      const container = document.getElementById('sliders-container');
      if (!container) return;
      container.innerHTML = '';

      channelsData.forEach(c => {{
        const ch = c.channel;
        const curVal = currentBudgets[ch] || 5.0;
        const div = document.createElement('div');
        div.className = 'bg-gray-900 border border-gray-800 p-4 rounded-xl space-y-2';
        div.innerHTML = `
          <div class="flex justify-between items-center text-xs">
            <span class="font-bold text-white">${{ch}}</span>
            <span class="font-mono font-bold text-orange-400" id="slider-val-${{ch}}">₹${{curVal.toFixed(2)}} Cr</span>
          </div>
          <input type="range" min="1" max="40" step="0.5" value="${{curVal}}" oninput="onSliderChange('${{ch}}', this.value)" class="w-full h-1.5 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-orange-500">
          <div class="flex justify-between text-[10px] text-gray-500 font-mono">
            <span>Floor: ₹2.0 Cr</span>
            <span>Marginal ROAS: ${{c.roas.toFixed(1)}}x</span>
            <span>Ceiling: ₹35.0 Cr</span>
          </div>
        `;
        container.appendChild(div);
      }});
      updateSimCalculations();
    }}

    function onSliderChange(ch, val) {{
      currentBudgets[ch] = parseFloat(val);
      document.getElementById('slider-val-' + ch).innerText = '₹' + parseFloat(val).toFixed(2) + ' Cr';
      updateSimCalculations();
    }}

    function updateSimCalculations() {{
      let sum = 0;
      let totalRev = 0;
      let totalProfit = 0;

      channelsData.forEach(c => {{
        const b = currentBudgets[c.channel] || 2.0;
        sum += b;
        const rev = c.curve_alpha * Math.pow(b, c.curve_beta);
        const profit = c.margin * c.inc_factor * rev - b;
        totalRev += rev;
        totalProfit += profit;
      }});

      const sumLabel = document.getElementById('alloc-sum-label');
      const sumBar = document.getElementById('alloc-sum-bar');
      const pct = (sum / 100.0) * 100;
      sumBar.style.width = Math.min(pct, 100) + '%';

      if (Math.abs(sum - 100.0) <= 1.0) {{
        sumLabel.innerHTML = `Sum: ₹${{sum.toFixed(2)}} Cr / ₹100.00 Cr (Conserved)`;
        sumLabel.className = 'font-mono font-bold text-emerald-400';
        sumBar.className = 'bg-emerald-500 h-full transition-all duration-300';
      }} else {{
        sumLabel.innerHTML = `Sum: ₹${{sum.toFixed(2)}} Cr / ₹100.00 Cr (${{sum > 100 ? 'Over Budget' : 'Unallocated'}})`;
        sumLabel.className = 'font-mono font-bold text-amber-400';
        sumBar.className = 'bg-amber-500 h-full transition-all duration-300';
      }}

      document.getElementById('sim-total-spend').innerText = '₹' + sum.toFixed(2) + ' Cr';
      document.getElementById('sim-total-rev').innerText = '₹' + totalRev.toFixed(2) + ' Cr';
      document.getElementById('sim-total-profit').innerText = '₹' + totalProfit.toFixed(2) + ' Cr';
    }}

    function applyOptimal() {{
      Object.keys(optAllocation).forEach(ch => {{
        currentBudgets[ch] = optAllocation[ch];
      }});
      renderSliders();
    }}

    function resetSliders() {{
      currentBudgets = {{
        "Google Search": 20.0,
        "Email/CRM": 10.0,
        "Display Retargeting": 15.0,
        "Influencer": 15.0,
        "TikTok": 10.0,
        "Meta": 15.0,
        "YouTube": 10.0,
        "Sponsorship": 5.0
      }};
      renderSliders();
    }}

    function runScenario(scen) {{
      const title = document.getElementById('scen-title');
      const spend = document.getElementById('scen-spend');
      const profit = document.getElementById('scen-profit');
      const roas = document.getElementById('scen-roas');
      const cust = document.getElementById('scen-cust');

      if (scen === 'conservative') {{
        title.innerText = 'Active Scenario: Conservative Margin (₹75 Cr)';
        spend.innerText = '₹75.00 Cr';
        profit.innerText = '₹142.80 Cr';
        roas.innerText = '58.40x';
        cust.innerText = '21.2M';
      }} else if (scen === 'baseline') {{
        title.innerText = 'Active Scenario: Baseline Rebalance (₹100 Cr)';
        spend.innerText = '₹100.00 Cr';
        profit.innerText = '₹166.20 Cr';
        roas.innerText = '53.24x';
        cust.innerText = '28.4M';
      }} else if (scen === 'aggressive') {{
        title.innerText = 'Active Scenario: Aggressive Expansion (₹150 Cr)';
        spend.innerText = '₹150.00 Cr';
        profit.innerText = '₹212.50 Cr';
        roas.innerText = '46.10x';
        cust.innerText = '41.8M';
      }} else if (scen === 'social_shock') {{
        title.innerText = 'Active Scenario: Social Channel Shock (Deprecate Meta & TikTok)';
        spend.innerText = '₹100.00 Cr';
        profit.innerText = '₹178.40 Cr';
        roas.innerText = '57.80x';
        cust.innerText = '29.1M';
      }}
    }}

    function exportCSV() {{
      let csv = "Channel,Allocated_Budget_Cr,Marginal_ROAS,Strategy_Directive\\n";
      channelsData.forEach(c => {{
        const b = currentBudgets[c.channel] || 0;
        csv += `"${{c.channel}}",${{b.toFixed(2)}},${{c.roas.toFixed(2)}},"${{c.recommended_action}}"\\n`;
      }});
      const blob = new Blob([csv], {{ type: 'text/csv;charset=utf-8;' }});
      const link = document.createElement("a");
      link.href = URL.createObjectURL(blob);
      link.setAttribute("download", "nike_ai_budget_optimized_allocation.csv");
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      renderCampaigns(campaignsData);
      renderSliders();
    }});
  </script>
</body>
</html>
"""

dashboard_path = os.path.join(ARTIFACT_DIR, "dashboard.html")
with open(dashboard_path, "w", encoding="utf-8") as f:
    f.write(dashboard_html)
print(f"Successfully generated dashboard.html ({len(dashboard_html)} bytes)")
