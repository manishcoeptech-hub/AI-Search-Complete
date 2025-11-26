import streamlit as st
import time

from utils.puzzle import parse_state, is_solvable, count_inversions
from utils.algorithms import bfs, dfs, greedy_best_first, astar
from utils.visualization import render_state_html

# ---------- PAGE SETUP ----------
st.title("🔍 Interactive 8-Puzzle Solver")

st.markdown("""
Enter a **start state** and a **goal state**, then select an algorithm.
Scroll down to watch the puzzle solve step-by-step.
""")

# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    start_text = st.text_input(
        "Start State (9 numbers, 0 = blank):",
        "1 8 7 0 3 5 2 4 6"
    )

with col2:
    goal_text = st.text_input(
        "Goal State:",
        "1 2 3 4 5 6 7 8 0"
    )

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

speed = st.slider("Animation Speed (seconds per step)", 0.05, 2.0, 0.4)

go = st.button("Solve")

st.markdown("---")


# =====================================================================
#   PROCESSING + ANIMATION SECTION
# =====================================================================
if go:

    # ---- PARSE INPUT ----
    try:
        start = parse_state(start_text)
        goal = parse_state(goal_text)
    except Exception as e:
        st.error(str(e))
        st.stop()

    # ---- SOLVABILITY CHECK ----
    if not is_solvable(start):
        st.error(
            f"❌ This puzzle is NOT solvable.\n"
            f"Inversions: {count_inversions(start)}"
        )
        st.stop()

    st.success("✔ Puzzle is solvable — running algorithm...")
    st.markdown("---")

    # ---- RUN SELECTED ALGORITHM ----
    if algo == "BFS":
        path, expanded = bfs(start, goal)

    elif algo == "DFS":
        path, expanded = dfs(start, goal)

    elif algo == "Greedy Best First (Misplaced)":
        path, expanded = greedy_best_first(start, goal, heuristic="misplaced")

    elif algo == "Greedy Best First (Manhattan)":
        path, expanded = greedy_best_first(start, goal, heuristic="manhattan")

    elif algo == "A* (Manhattan Distance)":
        path, expanded = astar(start, goal, heuristic="manhattan")

    elif algo == "A* (Linear Conflict)":
        path, expanded = astar(start, goal, heuristic="linear")

    else:  # A* Misplaced
        path, expanded = astar(start, goal, heuristic="misplaced")

    if path is None:
        st.error("No solution found (unexpected).")
        st.stop()

    # ---------- RESULTS ----------
    st.subheader("📊 Results")
    c1, c2 = st.columns(2)
    c1.metric("Moves", len(path) - 1)
    c2.metric("Nodes Expanded", expanded)

    st.markdown("---")

    # =====================================================================
    #   ANIMATION CONTROLS
    # =====================================================================

    st.subheader("▶️ Step-by-Step Visualization")

    # Checkboxes & buttons
    play = st.checkbox("Play Automatically", value=True)
    step_button = st.button("Next Step")

    # Placeholder for animation frame
    ph = st.empty()

    # Session state for manual mode
    if "manual_step" not in st.session_state:
        st.session_state.manual_step = 0

    # ---------- AUTO-PLAY MODE ----------
    if play:
        for step, state in enumerate(path):
            with ph.container():
                st.markdown(f"### Step {step}")
                st.markdown(
                    render_state_html(state, tile_size=80),
                    unsafe_allow_html=True
                )
            time.sleep(speed)

        st.success("🎉 Completed!")

    # ---------- MANUAL STEP MODE ----------
    else:
        if step_button:
            if st.session_state.manual_step < len(path) - 1:
                st.session_state.manual_step += 1

        step = st.session_state.manual_step

        st.markdown(f"### Step {step}")
        st.markdown(
            render_state_html(path[step], tile_size=80),
            unsafe_allow_html=True
        )

        if step == len(path) - 1:
            st.success("🎉 Completed!")
