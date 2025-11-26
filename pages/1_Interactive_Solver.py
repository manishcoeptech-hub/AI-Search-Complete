import streamlit as st
import time
from utils.puzzle import parse_state, is_solvable, count_inversions
from utils.algorithms import bfs, dfs, greedy_best_first, astar
from utils.visualization import render_state_html

st.title("🔍 Interactive Solver")

start_text = st.text_input("Start state", "1 8 7 0 3 5 2 4 6")
goal_text  = st.text_input("Goal state",  "1 2 3 4 5 6 7 8 0")

algo = st.selectbox(
    "Select Algorithm",
    [
        "A* (Misplaced Tile)",
        "A* (Manhattan Distance)",
        "A* (Linear Conflict)",
        "Greedy Best First (Misplaced)",
        "Greedy Best First (Manhattan)",
        "BFS",
        "DFS",
    ],
)

speed = st.slider("Animation Speed (seconds per step)", 0.05, 1.0, 0.4)

go = st.button("Solve")

if go:
    try:
        start = parse_state(start_text)
        goal = parse_state(goal_text)
    except Exception as e:
        st.error(str(e))
        st.stop()

    if not is_solvable(start):
        st.error(
            f"❌ This puzzle has {count_inversions(start)} inversions and is NOT solvable."
        )
        st.stop()

    st.success("Puzzle is solvable — running algorithm...")

    # Select algorithm
    if algo == "BFS":
        path, expanded = bfs(start, goal)
    elif algo == "DFS":
        path, expanded = dfs(start, goal)
    elif algo == "Greedy Best First (Misplaced)":
        path, expanded = greedy_best_first(start, goal, "misplaced")
    elif algo == "Greedy Best First (Manhattan)":
        path, expanded = greedy_best_first(start, goal, "manhattan")
    elif algo == "A* (Manhattan Distance)":
        path, expanded = astar(start, goal, "manhattan")
    elif algo == "A* (Linear Conflict)":
        path, expanded = astar(start, goal, "linear")
    else:
        path, expanded = astar(start, goal, "misplaced")

    if path is None:
        st.error("No solution found.")
        st.stop()

    st.subheader("Results")
    c1, c2 = st.columns(2)
    c1.metric("Moves", len(path)-1)
    c2.metric("Nodes Expanded", expanded)

    st.subheader("Visualization")
    ph = st.empty()

    for step, state in enumerate(path):
        with ph.container():
            st.markdown(f"### Step {step}")
            st.markdown(render_state_html(state, 80), unsafe_allow_html=True)
        time.sleep(speed)

    st.success("Done!")
