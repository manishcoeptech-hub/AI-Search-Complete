import streamlit as st
import time
from utils.puzzle import parse_state, generate_solvable_puzzle
from utils.visualization import render_state_html

st.title("🎮 Self-Solve Game (Play the 8-Puzzle)")

st.markdown("""
Try solving the 8-puzzle yourself!  
Click tiles to move them and reach the goal.
""")

# Session state for interactive game
if "current_state" not in st.session_state:
    st.session_state.current_state = [1,2,3,4,5,6,7,8,0]

if "move_count" not in st.session_state:
    st.session_state.move_count = 0

# Show puzzle board
st.markdown("### Current State")
st.markdown(render_state_html(st.session_state.current_state, 80), unsafe_allow_html=True)

# Move tile (UI Buttons Grid)
idx = st.session_state.current_state.index(0)

moves = {
    0: [1,3], 1: [0,2,4], 2: [1,5],
    3: [0,4,6], 4: [1,3,5,7], 5: [2,4,8],
    6: [3,7], 7: [4,6,8], 8: [5,7],
}

st.markdown("### Click a Neighbour Tile to Slide It")

cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(str(st.session_state.current_state[i]) if st.session_state.current_state[i] != 0 else " ", key=f"b{i}"):
            if i in moves[idx]:
                # swap
                cs = st.session_state.current_state
                cs[idx], cs[i] = cs[i], cs[idx]
                st.session_state.current_state = cs
                st.session_state.move_count += 1
                st.experimental_rerun()

# Move Counter
st.metric("Moves Taken", st.session_state.move_count)

# Random Puzzle Button
if st.button("🔀 Generate Random Puzzle"):
    st.session_state.current_state = generate_solvable_puzzle()
    st.session_state.move_count = 0
    st.experimental_rerun()

# Reset Button
if st.button("♻ Reset to Goal"):
    st.session_state.current_state = [1,2,3,4,5,6,7,8,0]
    st.session_state.move_count = 0
    st.experimental_rerun()
