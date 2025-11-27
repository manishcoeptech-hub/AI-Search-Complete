import streamlit as st

st.set_page_config(
    page_title="AI Search Lab",
    page_icon="🧩",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---- Dark Mode Toggle ----
theme = st.sidebar.radio("Theme", ["Light", "Dark"])

if theme == "Dark":
    st.markdown("""
    <style>
        body { background: #111 !important; color: white; }
        .stButton button { background: #444 !important; color: white !important; }
        .tile { background: #333 !important; color: #eee !important; }
        .blank { background: #555 !important; }
    </style>
    """, unsafe_allow_html=True)

# ---- Title ----
st.title("🧩 AI Search Laboratory")

st.markdown("""
### Welcome to the Interactive Search Algorithms Lab

Use the left sidebar to explore:

- **Interactive Solver**  
- **Compare Algorithms**  
- **Self Solve Game**  
- **Frontier Visualization**  
- **Search Tree Animation**  
- **Theory Page**  
- **Download PDF Report**

This platform is designed for university-level AI teaching.
""")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/1/1a/8-puzzle.png",
    width=200
)

st.info("Choose a page from the sidebar to begin.")
