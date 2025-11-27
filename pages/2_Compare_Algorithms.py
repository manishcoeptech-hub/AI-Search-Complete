import streamlit as st
import time
from utils.puzzle import parse_state, is_solvable
from utils.algorithms import bfs, dfs, greedy_best_first, astar

st.title("⚡ Compare Algorithms (Race Mode)")

start_text = st.text_input("Start", "1 8 7 0 3 5 2 4 6")
goal_text  = st.text_input("Goal", "1 2 3 4 5 6 7 8 0")

methods = st.multiselect(
    "Select algorithms to compare:",
    [
        "BFS",
        "DFS",
        "Greedy (Misplaced)",
        "Greedy (Manhattan)",
        "A* (Misplaced)",
        "A* (Manhattan)",
        "A* (Linear Conflict)",
    ],
    default=["A* (Manhattan)", "BFS"]
)

if st.button("Compare"):
    start = parse_state(start_text)
    goal = parse_state(goal_text)

    if not is_solvable(start):
        st.error("Not solvable.")
        st.stop()

    results = {}

    def run(algo):
        if algo == "BFS":
            return bfs(start, goal)
        if algo == "DFS":
            return dfs(start, goal)
        if algo == "Greedy (Misplaced)":
            return greedy_best_first(start, goal, "misplaced")
        if algo == "Greedy (Manhattan)":
            return greedy_best_first(start, goal, "manhattan")
        if algo == "A* (Manhattan)":
            return astar(start, goal, "manhattan")
        if algo == "A* (Linear Conflict)":
            return astar(start, goal, "linear")
        return astar(start, goal, "misplaced")

    st.subheader("📊 Results")
    for m in methods:
        t0 = time.time()
        path, expanded = run(m)
        t1 = time.time()

        results[m] = {
            "Moves": len(path) - 1,
            "Expanded": expanded,
            "Time (s)": round(t1 - t0, 4),
        }

    st.table(results)
