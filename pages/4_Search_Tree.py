import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

from utils.puzzle import parse_state, is_solvable
from utils.algorithms import bfs
from utils.visualization import render_state_html

st.title("🌳 Search Tree Visualization")

st.markdown("""
Visualize how search expands nodes as a tree.

(Currently BFS is used for clarity.)
""")

start_text = st.text_input("Start State", "1 8 7 0 3 5 2 4 6")
goal_text  = st.text_input("Goal State",  "1 2 3 4 5 6 7 8 0")

go = st.button("Build Tree")

if go:
    try:
        start = parse_state(start_text)
        goal = parse_state(goal_text)
    except Exception as e:
        st.error(str(e))
        st.stop()

    if not is_solvable(start):
        st.error("Not solvable.")
        st.stop()

    st.info("Building tree with BFS (first 400 nodes)…")

    # Build BFS tree
    frontier = [tuple(start)]
    came = {tuple(start): None}
    nodes = []

    limit = 400

    while frontier and len(nodes) < limit:
        current = frontier.pop(0)
        nodes.append(current)

        blank = current.index(0)
        from utils.algorithms import MOVES

        for m in MOVES[blank]:
            nxt = list(current)
            nxt[blank], nxt[m] = nxt[m], nxt[blank]
            n_t = tuple(nxt)
            if n_t not in came:
                came[n_t] = current
                frontier.append(n_t)

    G = nx.DiGraph()
    for child, parent in came.items():
        if parent:
            G.add_edge(parent, child)

    st.subheader("Tree Graph (first 400 nodes)")

    fig, ax = plt.subplots(figsize=(10, 8))
    pos = nx.spring_layout(G, k=0.4)
    nx.draw(G, pos, node_size=10, arrows=False, ax=ax)
    st.pyplot(fig)
