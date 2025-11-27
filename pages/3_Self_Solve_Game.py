import streamlit as st
from utils.puzzle import generate_solvable_puzzle
from utils.visualization import render_state_html

st.title("🎮 Self Solve Puzzle")

st.markdown("Click tiles next to the blank to move them.")

if "current_state" not in st.session_state:
    st.session_state.current_state = generate_solvable_puzzle()

if "move_count" not in st.session_state:
    st.session_state.move_count = 0

state = st.session_state.current_state
idx = state.index(0)

MOVES = {
    0: [1,3], 1: [0,2,4], 2: [1,5],
    3: [0,4,6], 4: [1,3,5,7], 5: [2,4,8],
    6: [3,7], 7: [4,6,8], 8: [5,7]
}

st.markdown(render_state_html(state, 80), unsafe_allow_html=True)

cols = st.columns(3)
for i in range(9):
    with cols[i % 3]:
        if st.button(str(state[i]) if state[i] != 0 else " ", key=f"b{i}"):
            if i in MOVES[idx]:
                state[idx], state[i] = state[i], state[idx]
                st.session_state.move_count += 1
                st.experimental_rerun()

st.metric("Moves", st.session_state.move_count)

if st.button("🔀 Random Puzzle"):
    st.session_state.current_state = generate_solvable_puzzle()
    st.session_state.move_count = 0
    st.experimental_rerun()

if st.button("♻ Reset"):
    st.session_state.current_state = [1,2,3,4,5,6,7,8,0]
    st.session_state.move_count = 0
    st.experimental_rerun()
