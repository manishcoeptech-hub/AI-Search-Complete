import streamlit as st

st.set_page_config(
    page_title="AI Search Lab",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("🧩 AI Search Laboratory")
st.markdown("""
### Welcome to the Interactive Search Algorithms Lab

Use the left sidebar to navigate:

- **Interactive Solver** → Solve 8-puzzle with A*, BFS, DFS, Greedy, etc  
- **Compare Algorithms** → Race A* vs BFS vs DFS  
- **Self-Solve Game** → Drag-and-drop puzzle and try to solve it  
- **Search Tree Visualization** → Explore frontier & tree growth  
- **Theory & Notes** → Learn algorithm concepts  
- **Download Report** → Save your run as PDF  

This lab is designed for teaching AI search clearly and visually.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/1/1a/8-puzzle.png", width=200)

st.markdown("---")

st.info("Start by selecting **Interactive Solver** from the sidebar!")
