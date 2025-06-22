import streamlit as st

def visualize_board(solution):
    n = len(solution)
    
    # Create CSS for chess board styling
    css = """
    <style>
    .chess-board {
        display: inline-block;
        border: 2px solid #333;
        margin: 10px 0;
    }
    .chess-row {
        display: flex;
    }
    .chess-cell {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
        font-weight: bold;
    }
    .white-cell {
        background-color: #f0d9b5;
    }
    .black-cell {
        background-color: #b58863;
    }
    .queen {
        color: #d63031;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    }
    </style>
    """
    
    # Create HTML for the chess board
    html = css + '<div class="chess-board">'
    
    for row in range(n):
        html += '<div class="chess-row">'
        for col in range(n):
            # Determine cell color (alternating pattern)
            is_white = (row + col) % 2 == 0
            cell_class = "white-cell" if is_white else "black-cell"
            
            # Check if queen is placed here
            if solution[row] == col:
                html += f'<div class="chess-cell {cell_class}"><span class="queen">♛</span></div>'
            else:
                html += f'<div class="chess-cell {cell_class}"></div>'
        
        html += '</div>'
    
    html += '</div>'
    
    # Display the chess board
    st.markdown(html, unsafe_allow_html=True)

# You can add more utilities as needed for visualization or data processing. 
