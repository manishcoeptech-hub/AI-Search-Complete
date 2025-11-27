import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from utils.puzzle import parse_state
from utils.algorithms import astar

st.title("📄 Download PDF Report")

start = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

if st.button("Generate PDF"):

    start = parse_state(start)
    goal = parse_state(goal)

    path, expanded = astar(start, goal, "manhattan")

    filename = "report.pdf"
    c = canvas.Canvas(filename, pagesize=letter)

    c.drawString(40, 750, "AI Search Report")
    c.drawString(40, 730, f"Start: {start}")
    c.drawString(40, 710, f"Goal: {goal}")
    c.drawString(40, 690, f"Moves: {len(path)-1}")
    c.drawString(40, 670, f"Expanded Nodes: {expanded}")

    y = 640
    for i, step in enumerate(path):
        c.drawString(40, y, f"Step {i}: {step}")
        y -= 20
        if y < 50:
            c.showPage()
            y = 750

    c.save()

    with open(filename, "rb") as f:
        st.download_button("Download PDF", f, "ai_search_report.pdf")
