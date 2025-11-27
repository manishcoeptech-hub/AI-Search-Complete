import streamlit as st

st.title("📘 Theory and Notes")

st.markdown("""
## 🔹 BFS
- Optimal
- Complete
- Large memory use

## 🔹 DFS
- Low memory
- Not optimal
- Can loop

## 🔹 Greedy Best First
- Uses only h(n)
- Fast but not optimal

## 🔹 A* Search
### f(n) = g(n) + h(n)
- Optimal if h is admissible
- Misplaced Tile
- Manhattan Distance
- Linear Conflict

## 🔹 Solvability
Even inversion count ⇒ solvable.
""")
