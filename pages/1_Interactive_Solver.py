import streamlit as st
import time

from utils.puzzle import parse_state, is_solvable, count_inversions
from utils.algorithms import bfs, dfs, greedy_best_first, astar
from utils.visualization import render_state_html

st.title("🔍 Interactive 8-Puzzle Solver")

st.markdown("Enter a start and goal state, choose an algorithm, then watch the solution.")

col1, col2 = st.columns(2)

with col1:
    start_text = st.text_input("Start State:", "1 8 7 0 3 5 2 4 6")

with col2:
    goal_text = st.text_input("Goal State:", "1 2 3 4 5 6 7 8 0")

algo = st.selectbox(
    "Algorithm",
    [
        "A* (Misplaced Tile)",
        "A* (Manhattan Distance)",
        "A* (Linear Conflict)",
        "Greedy Best First (Misplaced)",
        "Greedy Best First (Manhattan)",
        "BFS",
        "DFS",
    ]
)

speed = st.slider("Animation Speed (seconds)", 0.05, 2.0, 0.4)

go = st.button("Solve")

st.markdown("---")

if go:
    try:
        start = parse_state(start_text)
        goal = parse_state(goal_text)
    except Exception as e:
        st.error(e)
        st.stop()

    if not is_solvable(start):
        st.error(f"This puzzle is NOT solvable. Inversions: {count_inversions(start)}")
        st.stop()

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

    st.subheader("📊 Results")
    c1, c2 = st.columns(2)
    c1.metric("Moves", len(path) - 1)
    c2.metric("Nodes Expanded", expanded)

    st.markdown("---")
    st.subheader("▶️ Step-by-Step Visualization")

    play = st.checkbox("Play Automatically", value=True)
    step_button = st.button("Next Step (Manual Mode)")

    ph = st.empty()

    if "manual_step" not in st.session_state:
        st.session_state.manual_step = 0

    if play:
        for i, state in enumerate(path):
            with ph.container():
                st.markdown(f"### Step {i}")
                st.markdown(render_state_html(state, 80), unsafe_allow_html=True)
            time.sleep(speed)
    else:
        if step_button:
            st.session_state.manual_step = min(st.session_state.manual_step + 1, len(path) - 1)

        i = st.session_state.manual_step

        st.markdown(f"### Step {i}")
        st.markdown(render_state_html(path[i], 80), unsafe_allow_html=True)