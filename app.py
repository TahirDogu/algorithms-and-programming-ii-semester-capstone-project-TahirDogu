import streamlit as st
from algorithm import solve_n_queens, step_by_step_solution
from utils import visualize_board

st.set_page_config(page_title="Chess Queen Solver", layout="centered")

st.title("Chess Queen Solver")

n = st.slider("Select the value of N (number of queens and board size):", min_value=4, max_value=12, value=8)

if st.button("Solve N-Queens"):
    solutions = solve_n_queens(n)
    st.success(f"Found {len(solutions)} solutions for N={n}.")
    for idx, solution in enumerate(solutions):
        st.write(f"Solution {idx+1}:")
        visualize_board(solution)

st.header("Step-by-Step Explanation")
if st.button("Show Step-by-Step Solution"):
    steps = step_by_step_solution(n)
    for step in steps:
        visualize_board(step)
        st.write("---") 
