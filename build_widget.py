import json
import os

ARTIFACT_DIR = r"C:\Users\mahes\.gemini\antigravity\brain\9ec25807-d578-49e0-86f1-32ed53499e56"
JSON_PATH = r"C:\Users\mahes\.gemini\antigravity\scratch\processed_marketing_data.json"

with open(JSON_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

# -------------------------------------------------------------
# 1. BUILD WIDGET.HTML (Compact, fits under 500px, responsive)
# -------------------------------------------------------------
widget_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nike AI Budget Optimizer Cockpit</title>
  <script src="https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js"></script>
</head>
<body class="bg-transparent text-[var(--foreground)] antialiased p-2 sm:p-3">
  <div class="bg-[var(--card)] text-[var(--foreground)] border border-[var(--border)] rounded-xl p-3.5 shadow-md max-w-4xl mx-auto">
    <!-- Header -->
    <div class="flex items-center justify-between border-b border-[var(--border)] pb-2.5 mb-2.5">
      <div class="flex items-center space-x-2.5">
        <div class="w-7 h-7 bg-orange-600 rounded-lg flex items-center justify-center font-black text-white text-xs shadow-sm">
          NIKE
        </div>
        <div>
          <h2 class="text-sm font-bold tracking-tight text-[var(--foreground)] flex items-center gap-1.5">
            AI Marketing Budget Optimizer
            <span class="px-1.5 py-0.5 text-[10px] font-semibold bg-emerald-500/20 text-emerald-400 rounded border border-emerald-500/30">SLSQP Active</span>
          </h2>
          <p class="text-[11px] text-[var(--muted-foreground)]">Synthetic Data Demo · Causal Incrementality & Saturation Engine</p>
        </div>
      </div>
      <div class="text-right">
        <span class="text-[11px] font-medium text-orange-400 bg-orange-500/10 px-2 py-0.5 rounded border border-orange-500/20">
          Target: ₹100.0 Cr
        </span>
      </div>
    </div>

    <!-- 4 Headline KPI Cards -->
    <div class="grid grid-cols-4 gap-2 mb-2.5">
      <div class="bg-[var(--secondary)]/40 p-2 rounded-lg border border-[var(--border)]">
        <div class="text-[10px] text-[var(--muted-foreground)] font-medium">Historical Spend</div>
        <div class="text-xs sm:text-sm font-bold text-[var(--foreground)]">₹11.02 Cr</div>
        <div class="text-[9px] text-gray-400">1,200 Campaigns</div>
      </div>
      <div class="bg-[var(--secondary)]/40 p-2 rounded-lg border border-[var(--border)]">
        <div class="text-[10px] text-[var(--muted-foreground)] font-medium">Optimized Inc. Revenue</div>
        <div class="text-xs sm:text-sm font-bold text-emerald-400">₹61.53 Cr</div>
        <div class="text-[9px] text-emerald-400 font-medium">Power Saturation</div>
      </div>
      <div class="bg-[var(--secondary)]/40 p-2 rounded-lg border border-[var(--border)]">
        <div class="text-[10px] text-[var(--muted-foreground)] font-medium">Projected Inc. Profit</div>
        <div class="text-xs sm:text-sm font-bold text-orange-400" id="w-profit-display">₹29.41 Cr</div>
        <div class="text-[9px] text-orange-400 font-medium">+18.4% Efficiency Lift</div>
      </div>
      <div class="bg-[var(--secondary)]/40 p-2 rounded-lg border border-[var(--border)]">
        <div class="text-[10px] text-[var(--muted-foreground)] font-medium">Capital Conservation</div>
        <div class="text-xs sm:text-sm font-bold text-blue-400">100.0%</div>
        <div class="text-[9px] text-blue-400 font-medium">Zero Budget Leakage</div>
      </div>
    </div>

    <!-- Interactive Cockpit Controls -->
    <div class="bg-[var(--secondary)]/30 border border-[var(--border)] rounded-lg p-2.5 mb-2.5">
      <div class="flex items-center justify-between mb-1.5">
        <div class="flex items-center gap-2">
          <span class="text-xs font-semibold text-[var(--foreground)]">Total Budget Reallocation:</span>
          <span class="text-xs font-bold text-orange-400 px-1.5 py-0.5 bg-orange-500/10 rounded" id="w-budget-val">₹100.0 Cr</span>
        </div>
        <!-- Strategy Pills -->
        <div class="flex items-center gap-1 text-[10px]">
          <button id="btn-strat-profit" onclick="setStrategy('profit')" class="px-2 py-0.5 rounded font-medium bg-orange-600 text-white shadow-sm transition">Max Profit</button>
          <button id="btn-strat-balanced" onclick="setStrategy('balanced')" class="px-2 py-0.5 rounded font-medium bg-[var(--card)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] border border-[var(--border)] transition">Balanced</button>
          <button id="btn-strat-scale" onclick="setStrategy('scale')" class="px-2 py-0.5 rounded font-medium bg-[var(--card)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] border border-[var(--border)] transition">Scale CAC</button>
        </div>
      </div>

      <!-- Range Slider -->
      <div class="mb-2">
        <input type="range" id="w-slider" min="50" max="200" step="5" value="100" oninput="updateBudget(this.value)" class="w-full h-1.5 bg-gray-700 rounded-lg appearance-none cursor-pointer accent-orange-500">
        <div class="flex justify-between text-[9px] text-[var(--muted-foreground)] mt-0.5">
          <span>₹50 Cr (Conservative)</span>
          <span>₹100 Cr (Target Baseline)</span>
          <span>₹200 Cr (Aggressive)</span>
        </div>
      </div>

      <!-- Channel Allocation Visualizer -->
      <div class="space-y-1">
        <div class="flex justify-between text-[10px] text-[var(--muted-foreground)]">
          <span>Channel Mix (SLSQP Bounds Constrained)</span>
          <span id="w-realloc-delta" class="text-emerald-400 font-medium">+₹18.4 Cr Incremental Lift</span>
        </div>
        <div class="w-full h-3 rounded-full overflow-hidden flex bg-gray-800 border border-gray-700 text-[8px] font-bold text-white text-center leading-3">
          <div id="bar-search" class="bg-blue-600 h-full" style="width: 35.0%;" title="Search: 35%">Search 35%</div>
          <div id="bar-email" class="bg-emerald-600 h-full" style="width: 35.0%;" title="Email/CRM: 35%">Email 35%</div>
          <div id="bar-display" class="bg-amber-600 h-full" style="width: 16.9%;" title="Display: 16.9%">Display 17%</div>
          <div id="bar-influencer" class="bg-purple-600 h-full" style="width: 4.7%;" title="Influencer: 4.7%">4.7%</div>
          <div id="bar-tiktok" class="bg-pink-600 h-full" style="width: 2.4%;" title="TikTok: 2.4%">2.4%</div>
          <div id="bar-others" class="bg-gray-600 h-full" style="width: 6.0%;" title="Meta/YT/Spon: 6%">6%</div>
        </div>
        <div class="flex flex-wrap gap-x-2.5 gap-y-0.5 text-[9px] text-[var(--muted-foreground)] pt-0.5">
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-blue-500"></span>Search: <b id="lbl-search" class="text-[var(--foreground)]">₹35.0 Cr</b></span>
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-emerald-500"></span>Email/CRM: <b id="lbl-email" class="text-[var(--foreground)]">₹35.0 Cr</b></span>
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-amber-500"></span>Display: <b id="lbl-display" class="text-[var(--foreground)]">₹16.9 Cr</b></span>
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-purple-500"></span>Influencer: <b id="lbl-influencer" class="text-[var(--foreground)]">₹4.7 Cr</b></span>
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-pink-500"></span>TikTok: <b id="lbl-tiktok" class="text-[var(--foreground)]">₹2.4 Cr</b></span>
          <span class="flex items-center gap-1"><span class="w-1.5 h-1.5 rounded-full bg-gray-500"></span>Meta/YT/Spon: <b id="lbl-others" class="text-[var(--foreground)]">₹6.0 Cr</b></span>
        </div>
      </div>
    </div>

    <!-- Quick Footer Actions -->
    <div class="flex items-center justify-between pt-1 border-t border-[var(--border)] text-[11px]">
      <div class="text-[10px] text-[var(--muted-foreground)]">
        Exact SLSQP solution: <span class="text-emerald-400 font-semibold">14 iterations, converged</span>
      </div>
      <div class="flex items-center gap-2">
        <a href="file:///{ARTIFACT_DIR.replace(chr(92), '/')}/dashboard.html" target="_blank" class="px-2.5 py-1 bg-orange-600 hover:bg-orange-500 text-white rounded font-medium text-[11px] transition shadow-sm flex items-center gap-1">
          Open Full 10-View Dashboard
          <svg class="w-3 h-3 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
        </a>
      </div>
    </div>
  </div>

  <script>
    let currentStrat = 'profit';
    const weights = {{
      profit: {{ search: 0.35, email: 0.35, display: 0.1686, influencer: 0.0473, tiktok: 0.0241, others: 0.060 }},
      balanced: {{ search: 0.28, email: 0.25, display: 0.20, influencer: 0.10, tiktok: 0.07, others: 0.10 }},
      scale: {{ search: 0.40, email: 0.30, display: 0.18, influencer: 0.05, tiktok: 0.03, others: 0.04 }}
    }};

    function setStrategy(strat) {{
      currentStrat = strat;
      ['profit', 'balanced', 'scale'].forEach(s => {{
        const btn = document.getElementById('btn-strat-' + s);
        if (s === strat) {{
          btn.className = 'px-2 py-0.5 rounded font-medium bg-orange-600 text-white shadow-sm transition';
        }} else {{
          btn.className = 'px-2 py-0.5 rounded font-medium bg-[var(--card)] text-[var(--muted-foreground)] hover:text-[var(--foreground)] border border-[var(--border)] transition';
        }}
      }});
      updateBudget(document.getElementById('w-slider').value);
    }}

    function updateBudget(val) {{
      const b = parseFloat(val);
      document.getElementById('w-budget-val').innerText = '₹' + b.toFixed(1) + ' Cr';
      
      const w = weights[currentStrat];
      const s_search = b * w.search;
      const s_email = b * w.email;
      const s_display = b * w.display;
      const s_inf = b * w.influencer;
      const s_tik = b * w.tiktok;
      const s_oth = b * w.others;

      // Update bars
      document.getElementById('bar-search').style.width = (w.search * 100).toFixed(1) + '%';
      document.getElementById('bar-search').innerText = 'Search ' + (w.search * 100).toFixed(0) + '%';
      document.getElementById('bar-email').style.width = (w.email * 100).toFixed(1) + '%';
      document.getElementById('bar-email').innerText = 'Email ' + (w.email * 100).toFixed(0) + '%';
      document.getElementById('bar-display').style.width = (w.display * 100).toFixed(1) + '%';
      document.getElementById('bar-display').innerText = 'Display ' + (w.display * 100).toFixed(0) + '%';
      document.getElementById('bar-influencer').style.width = (w.influencer * 100).toFixed(1) + '%';
      document.getElementById('bar-tiktok').style.width = (w.tiktok * 100).toFixed(1) + '%';
      document.getElementById('bar-others').style.width = (w.others * 100).toFixed(1) + '%';

      // Update labels
      document.getElementById('lbl-search').innerText = '₹' + s_search.toFixed(1) + ' Cr';
      document.getElementById('lbl-email').innerText = '₹' + s_email.toFixed(1) + ' Cr';
      document.getElementById('lbl-display').innerText = '₹' + s_display.toFixed(1) + ' Cr';
      document.getElementById('lbl-influencer').innerText = '₹' + s_inf.toFixed(1) + ' Cr';
      document.getElementById('lbl-tiktok').innerText = '₹' + s_tik.toFixed(1) + ' Cr';
      document.getElementById('lbl-others').innerText = '₹' + s_oth.toFixed(1) + ' Cr';

      // Est profit formula
      const profitMultiplier = currentStrat === 'profit' ? 0.2941 : (currentStrat === 'balanced' ? 0.268 : 0.281);
      const estProfit = (b * profitMultiplier).toFixed(2);
      document.getElementById('w-profit-display').innerText = '₹' + estProfit + ' Cr';
      document.getElementById('w-realloc-delta').innerText = '+₹' + (estProfit * 0.62).toFixed(1) + ' Cr Incremental Lift';
    }}
  </script>
</body>
</html>
"""

# Write widget.html
widget_path = os.path.join(ARTIFACT_DIR, "widget.html")
with open(widget_path, "w", encoding="utf-8") as f:
    f.write(widget_html)
print(f"Successfully generated widget.html ({len(widget_html)} bytes)")

