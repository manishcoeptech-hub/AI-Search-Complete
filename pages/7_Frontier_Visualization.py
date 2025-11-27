import streamlit as st
from utils.puzzle import parse_state, is_solvable
from utils.algorithms import astar_with_frontier
from utils.visualization import render_state_html

st.title("📦 Frontier Visualization (A*)")

start = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

if st.button("Visualize Frontier"):
    start = parse_state(start)
    goal = parse_state(goal)

    if not is_solvable(start):
        st.error("Not solvable")
        st.stop()

    steps = astar_with_frontier(start, goal)

    for idx, s in enumerate(steps):
        st.markdown(f"### Step {idx}")
        col1, col2 = st.columns(2)

        with col1:
            st.markdown("#### Open List")
            for node in s["open"][:5]:
                st.markdown(render_state_html(node, 50), unsafe_allow_html=True)

        with col2:
            st.markdown("#### Closed List")
            for node in s["closed"][:5]:
                st.markdown(render_state_html(node, 50), unsafe_allow_html=True)

        st.markdown("---")
