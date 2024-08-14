# Sudoku-Solver
Solves the game Sudoku using the Backtracking Algorithm
  
  
  
  
  
**Overview:**

This project is a Sudoku solver implemented in Python, with a real-time visualization of the solving process using Pygame. The solver uses a backtracking algorithm to fill in the Sudoku grid, and the visualization highlights the process by coloring the cells green when a number is placed, red when backtracking occurs, and white when cells are reset.
  
 
   
  
**Features:**


&#8226; Backtracking Algorithm: Efficiently solves any valid Sudoku puzzle.

&#8226; Real-time Visualization: Watch the solving process in action with color-coded feedback:

&#8226; Green: A number is successfully placed in a cell.

&#8226; Red: The algorithm backtracks, removing a previously placed number.

&#8226; White: The cell is reset to its original state after backtracking.

&#8226; Interactive GUI: The Pygame window allows you to observe the solver in action. The window remains open after solving, allowing you to inspect the final solution.


**Start:**


![image](https://github.com/user-attachments/assets/ded435aa-9dd3-47a8-9414-8c9452cdf999)

**End Result:**


![image](https://github.com/user-attachments/assets/106d5360-8d51-484b-862f-27b4da64bf50)



**Installation:**

To run this project on your local machine, follow these steps:

**1.** Clone the Repository
git clone https://github.com/yourusername/sudoku-solver-pygame.git
cd sudoku-solver-pygame

**2.** Install Dependencies
Make sure you have Python installed. Then, install the required packages:
pip install pygame

**3.** Run the Project
python sudoku_visualization.py

   
  
  
**Usage:**

The Sudoku grid is hardcoded into the script. You can modify the grid variable in the main() function to solve different Sudoku puzzles.
The solving process is visualized in the Pygame window. The window will stay open after solving is complete, allowing you to close it manually.
 
 
   
**Project Structure:**

├── sudoku_solver.py           # Contains the Sudoku solver logic

├── sudoku_visualization.py    # Pygame visualization and integration with the solver

└── README.md                  # Project documentation











