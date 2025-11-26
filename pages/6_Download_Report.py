import streamlit as st
import pandas as pd
from io import StringIO

st.title("📄 Download Your Report")

st.markdown("""
Export your algorithm comparison, path details, heuristics, and notes.
""")

txt = st.text_area("Notes (optional)", "My observations:")

report = f"""
AI Search Lab Report
=====================

{txt}

Generated using the AI Search Teaching Tool.
"""

# Markdown file download
st.download_button(
    "Download Markdown Report",
    data=report,
    file_name="ai_search_report.md",
    mime="text/markdown"
)

