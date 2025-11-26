import streamlit as st

st.title("📘 Theory and Notes")

st.markdown("""
This page explains:

## 🔹 Breadth-First Search  
- Completeness  
- Optimality  
- Time/space complexity  
- How frontier grows  
- Perfect for short paths

---

## 🔹 Depth-First Search  
- Not optimal  
- Low memory  
- Deep but blind search  
- Risks infinite loops

---

## 🔹 Greedy Best First  
- Very fast  
- Uses heuristic only  
- Not optimal  
- Prone to local minima

---

## 🔹 A* Search  
### f(n) = g(n) + h(n)  
- **g(n)** = cost so far  
- **h(n)** = heuristic  
- **f(n)** = priority  
- Optimal if heuristic is admissible  

### Heuristics:
- Misplaced tile  
- Manhattan distance  
- Linear conflict (strongest)

---

## 🔹 Solvability  
8-puzzle is solvable iff the inversion count is even.

---

## 🔹 Trees vs Graph Search  
- Frontier  
- Closed set  
- Expansion pattern  
""")

st.info("Use the left sidebar to try algorithms interactively.")
