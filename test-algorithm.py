import unittest
from algorithm import solve_n_queens

class TestNQueens(unittest.TestCase):
    def test_n_4(self):
        solutions = solve_n_queens(4)
        self.assertEqual(len(solutions), 2)

    def test_n_1(self):
        solutions = solve_n_queens(1)
        self.assertEqual(len(solutions), 1)

    def test_n_2(self):
        solutions = solve_n_queens(2)
        self.assertEqual(len(solutions), 0)

    def test_n_3(self):
        solutions = solve_n_queens(3)
        self.assertEqual(len(solutions), 0)

if __name__ == "__main__":
    unittest.main()  
