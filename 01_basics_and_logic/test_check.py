import unittest

from grade_checker import check

# Import your function here (assuming it's in a file called score.py)
# from score import check

class TestScoreFunction(unittest.TestCase):
    
    def test_distinction(self):
        # Testing boundary and regular distinction scores
        self.assertEqual(check(85), "distinction")
        self.assertEqual(check(70), "distinction") # Boundary
        
    def test_credit(self):
        self.assertEqual(check(60), "credit")
        self.assertEqual(check(50), "credit") # Boundary
        
    def test_invalid_scores(self):
        # Testing out-of-bounds numbers
        self.assertEqual(check(105), "Invalid Score (Must be 0-100)")
        self.assertEqual(check(-5), "Invalid Score (Must be 0-100)")
        
    def test_invalid_types(self):
        # Testing wrong data types
        self.assertEqual(check("ninety"), "invalid input")

if __name__ == '__main__':
    unittest.main()