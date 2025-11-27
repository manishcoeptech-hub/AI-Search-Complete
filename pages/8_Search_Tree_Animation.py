import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from utils.puzzle import parse_state, is_solvable
from utils.algorithms import astar_with_frontier
from utils.visualization import render_state_html

st.title("🌲 A* Search Tree Animation")

start = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

if st.button("Animate Tree"):
    start = parse_state(start)
    goal = parse_state(goal)

    if not is_solvable(start):
        st.error("Not solvable.")
        st.stop()

    steps = astar_with_frontier(start, goal)

    for idx, step in enumerate(steps):
        st.markdown(f"### Step {idx}")
        st.markdown(render_state_html(step["current"], 70), unsafe_allow_html=True)

        G = nx.DiGraph()
        for n in step["closed"]:
            G.add_node(tuple(n))

        fig, ax = plt.subplots(figsize=(6, 5))
        nx.draw(G, ax=ax, node_size=30)
        st.pyplot(fig)

        st.markdown("---")
