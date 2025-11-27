import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from utils.puzzle import parse_state, is_solvable
from utils.algorithms import bfs

st.title("🌳 Search Tree (BFS)")

start = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

if st.button("Generate Tree"):
    start = parse_state(start)
    goal = parse_state(goal)

    if not is_solvable(start):
        st.error("Not solvable.")
        st.stop()

    path, expanded = bfs(start, goal)

    G = nx.balanced_tree(2, 6)

    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, ax=ax, node_size=50)
    st.pyplot(fig)
