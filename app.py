"""
AI MARKETING BUDGET OPTIMIZER
Synthetic NIKE Marketing Budget Optimization Case Study
Main Application Dashboard orchestrating 10 Enterprise Views
"""
import streamlit as st
import pandas as pd
import numpy as np
import os, sys

# Set Streamlit Page Configuration
st.set_page_config(
    page_title="AI Marketing Budget Optimizer — Synthetic NIKE Case Study",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Enterprise Nike-inspired Dark CSS
st.markdown("""
<style>
  .stApp {
    background-color: #0b0f17;
    color: #f1f5f9;
  }
  .disclaimer-banner {
    background: rgba(245, 158, 11, 0.1);
    border: 1px solid rgba(245, 158, 11, 0.3);
    border-radius: 8px;
    padding: 10px 14px;
    font-size: 13px;
    color: #fcd34d;
    margin-bottom: 20px;
  }
  .sidebar .sidebar-content {
    background-color: #080c14;
  }
</style>
""", unsafe_allow_html=True)

from core.data_ingestion import MarketingDataLoader
from core.currency_formatter import format_inr, format_inr_cr
from core.export_manager import export_df_to_csv, export_workbook_to_excel, generate_executive_html_report
from core.metrics_calculator import calculate_executive_kpis
from models.diminishing_returns import SaturationModel
from models.budget_optimizer import MarketingBudgetOptimizer
from models.customer_ltv import CustomerLTVEngine
from models.attribution_engine import AttributionEngine
from models.inefficiency_detector import InefficiencyDetector

# Import 10 Component Views
from components.executive_view import render_executive_view
from components.campaign_view import render_campaign_view
from components.customer_view import render_customer_view
from components.attribution_view import render_attribution_view
from components.optimizer_view import render_optimizer_view
from components.simulator_view import render_simulator_view
from components.monitor_view import render_monitor_view
from components.recommendations_view import render_recommendations_view
from components.data_quality_view import render_data_quality_view
from components.model_performance_view import render_model_performance_view

# Header & Case Study Branding
st.title("⚡ AI MARKETING BUDGET OPTIMIZER")
st.caption("Synthetic NIKE Marketing Budget Optimization Case Study &bull; Enterprise Decision-Support System")

# Mandatory Real Company Case Study Disclaimer
st.markdown("""
<div class="disclaimer-banner">
  ⚠️ <strong>Synthetic Data Disclaimer:</strong> This application uses synthetic data for demonstration and modeling purposes. The figures shown are not actual NIKE campaign or financial data.
</div>
""", unsafe_allow_html=True)

# Data Loader with caching and upload buffer support
DEFAULT_DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "nike_marketing_budget_optimizer_synthetic_data.xlsx")

@st.cache_data
def load_app_data(custom_file_bytes=None):
    source = custom_file_bytes if custom_file_bytes is not None else DEFAULT_DATA_PATH
    loader = MarketingDataLoader(source)
    sheets, report = loader.load_and_validate()
    
    # 1. Train Saturation Curves
    sat_model = SaturationModel()
    sat_model.fit_from_campaigns(sheets['Campaign_Data'])
    
    # 2. Fit Constrained Budget Optimizer
    opt_engine = MarketingBudgetOptimizer(sat_model, sheets['Channel_Summary'])
    default_opt_res = opt_engine.optimize(total_budget_cr=100.0)
    
    # 3. Fit RFM & Customer LTV Regressor
    ltv_engine = CustomerLTVEngine()
    cust_full, seg_summary = ltv_engine.segment_rfm(sheets.get('Transactions', pd.DataFrame()), sheets['Customer_Data'])
    cust_pred, ltv_metrics = ltv_engine.train_ltv_model(cust_full)
    
    # 4. Fit Attribution Engine
    attr_engine = AttributionEngine(sheets['Channel_Summary'])
    attr_models = attr_engine.compute_models()
    
    return sheets, report, sat_model, opt_engine, default_opt_res, cust_pred, seg_summary, ltv_metrics, attr_models

try:
    custom_bytes = st.session_state.get('custom_file', None)
    sheets, report, sat_model, opt_engine, default_opt_res, cust_pred, seg_summary, ltv_metrics, attr_models = load_app_data(custom_bytes)
except Exception as e:
    st.error(f"Error loading marketing dataset: {e}")
    st.info("Please upload a valid Excel workbook in the Data Quality section.")
    st.stop()

# Sidebar Navigation with Icons
st.sidebar.markdown("### ⚡ NIKE AI OPTIMIZER")
st.sidebar.caption(f"Health Score: **{report['health_score']:.1f}/100** &bull; {report['campaign_count']} Campaigns")

pages = [
    "1. Executive Dashboard",
    "2. Campaign Analytics",
    "3. Customer Intelligence",
    "4. Attribution & Incrementality",
    "5. Budget Optimizer ★",
    "6. Scenario Simulator",
    "7. Real-Time Monitor",
    "8. AI Recommendations",
    "9. Data Quality",
    "10. Model Performance"
]

page = st.sidebar.radio("Navigation Menu", pages, index=0)

# Sidebar Export Center
st.sidebar.write("---")
st.sidebar.markdown("#### 📥 Export Advisory Reports")

alloc_export_df = pd.DataFrame.from_dict(default_opt_res['details'], orient='index')

# CSV Export
st.sidebar.download_button(
    "📄 Export Optimal Budget (CSV)",
    data=export_df_to_csv(alloc_export_df),
    file_name="optimal_marketing_budget_allocation.csv",
    mime="text/csv",
    use_container_width=True
)

# Multi-sheet Excel Export
excel_bundle = {
    'Budget_Optimal': alloc_export_df,
    'Campaign_Matrix': sheets['Campaign_Data'].head(200),
    'RFM_Segments': seg_summary,
    'Attribution_Models': pd.DataFrame(attr_models)
}
st.sidebar.download_button(
    "📊 Export Full Audit (Excel .xlsx)",
    data=export_workbook_to_excel(excel_bundle),
    file_name="nike_marketing_budget_audit_export.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    use_container_width=True
)

# Executive Briefing HTML Report (Printable PDF)
ineff_obj = InefficiencyDetector(sheets['Campaign_Data'], sheets['Channel_Summary'], cust_pred)
dyn_insights = ineff_obj.generate_dynamic_insights()
exec_kpis = calculate_executive_kpis(sheets['Campaign_Data'], cust_pred, default_opt_res)

rec_export_list = [
    {
        'channel': ch,
        'action': d['Action'],
        'why': f"Marginal ROAS {d['Marginal_ROAS']:.1f}x with {d['Confidence']} causal confidence.",
        'expected_impact': f"Recommended spend ₹{d['Recommended_Budget_Cr']:.2f} Cr generating ₹{d['Expected_Revenue_Cr']:.1f} Cr revenue.",
        'confidence': d['Confidence']
    }
    for ch, d in default_opt_res['details'].items()
]

html_report_str = generate_executive_html_report(exec_kpis, alloc_export_df, dyn_insights, rec_export_list)

st.sidebar.download_button(
    "📑 Executive Report (HTML / PDF)",
    data=html_report_str.encode('utf-8'),
    file_name="executive_marketing_budget_briefing.html",
    mime="text/html",
    use_container_width=True,
    help="Open in any web browser and select Print -> Save as PDF."
)

# Page Routing
if page == "1. Executive Dashboard":
    render_executive_view(sheets, sat_model, default_opt_res, cust_pred)
    
elif page == "2. Campaign Analytics":
    render_campaign_view(sheets, cust_pred)
    
elif page == "3. Customer Intelligence":
    render_customer_view(cust_pred, seg_summary, ltv_metrics)
    
elif page == "4. Attribution & Incrementality":
    render_attribution_view(attr_models)
    
elif page == "5. Budget Optimizer ★":
    render_optimizer_view(opt_engine, sat_model)
    
elif page == "6. Scenario Simulator":
    render_simulator_view(opt_engine, sat_model, sheets)
    
elif page == "7. Real-Time Monitor":
    render_monitor_view(sheets)
    
elif page == "8. AI Recommendations":
    render_recommendations_view(sheets, default_opt_res, cust_pred)
    
elif page == "9. Data Quality":
    render_data_quality_view(report, load_app_data)
    
elif page == "10. Model Performance":
    render_model_performance_view(ltv_metrics, sat_model, default_opt_res)

