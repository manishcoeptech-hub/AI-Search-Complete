import streamlit as st
import time

from utils.puzzle import parse_state, is_solvable
from utils.algorithms import bfs, astar, greedy_best_first
from utils.visualization import render_state_html

st.title("🏁 Algorithm Race (Side By Side)")

start = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

col1, col2 = st.columns(2)
algoA = col1.selectbox("Left Algorithm", ["A*", "BFS", "Greedy"])
algoB = col2.selectbox("Right Algorithm", ["A*", "BFS", "Greedy"])

speed = st.slider("Speed", 0.05, 1.0, 0.2)

if st.button("Start Race"):

    start = parse_state(start)
    goal  = parse_state(goal)

    if not is_solvable(start):
        st.error("Not solvable")
        st.stop()

    def run(algo):
        if algo == "A*": return astar(start, goal, "manhattan")
        if algo == "BFS": return bfs(start, goal)
        return greedy_best_first(start, goal, "manhattan")

    pathA, _ = run(algoA)
    pathB, _ = run(algoB)

    max_len = max(len(pathA), len(pathB))

    for i in range(max_len):
        c1, c2 = st.columns(2)

        with c1:
            st.markdown(f"### {algoA} Step {min(i, len(pathA)-1)}")
            st.markdown(render_state_html(pathA[min(i,len(pathA)-1)], 70),
                        unsafe_allow_html=True)

        with c2:
            st.markdown(f"### {algoB} Step {min(i, len(pathB)-1)}")
            st.markdown(render_state_html(pathB[min(i,len(pathB)-1)], 70),
                        unsafe_allow_html=True)

        time.sleep(speed)
        st.markdown("---")
