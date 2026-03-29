import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility

import ep04

class Test(unittest.TestCase):

    @weight(1)
    @visibility('visible')
    def test_on_simple_example(self):
        """Works on a simple example."""

        #Test 1
        msg = """
        
            A = [3, 2, 6, 5]
            B = [1, 8, 2, 9]

        Swapping 8 and 6 would do it (but it's not the only possibility).

        """
        A = [3, 2, 6, 5]
        B = [1, 8, 2, 9]
        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)


        #Test 2

        msg = """
        
            A = [-4, -8, -1, 5, 4, -3, -5, 3, -8, -7, 2, -9, 9, -3, 3]
        	B = [-1, 8, 3, -4, 1, 5, 1, -2, 2, 2, -8, 5, 0, -9, 9, -4, -5, -7, -2, -8]

        Swapping 5 and 9 would do it (but it's not the only possibility).

        """

        A = [-4, -8, -1, 5, 4, -3, -5, 3, -8, -7, 2, -9, 9, -3, 3]
        B = [-1, 8, 3, -4, 1, 5, 1, -2, 2, 2, -8, 5, 0, -9, 9, -4, -5, -7, -2, -8]

        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)

        #Test 3

        msg = """
        
            A = [3, -5, 5, -6, -4, -1, 0, -6, 9, 2]
            B = [-6, -9, 9, 0, 7, -9, -2, 0, 9, 6]

        Swapping 5 and 9 would do it (but it's not the only possibility).

        """

        A = [3, -5, 5, -6, -4, -1, 0, -6, 9, 2]
        B = [-6, -9, 9, 0, 7, -9, -2, 0, 9, 6]

        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)

        #Test 4

        msg = """
        
            A = [-6, 1, 0, -5, 3]
        	B = [4, 9, 7, 6, -9, -8, -4, 9, 6, -3, 3, 3, -9, -10, 4, -4, 7, -10, 6, 2]

        Swapping 1 and 9 would do it (but it's not the only possibility).

        """

        A = [-6, 1, 0, -5, 3]
        B = [4, 9, 7, 6, -9, -8, -4, 9, 6, -3, 3, 3, -9, -10, 4, -4, 7, -10, 6, 2]

        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)

        #Test 5

        msg = """
        
            A = [2, 5, -5, -9, 2, -2, 6, 4, -5, -3]
        	B = [-3, 8, 7, -5, -10, 9, 4, 2, 4, 8, -9, 8, -1, 1, -6, -3, 1, -9, -3, 6]

        Swapping 6 and 9 would do it (but it's not the only possibility).

        """

        A = [2, 5, -5, -9, 2, -2, 6, 4, -5, -3]
        B = [7, 9, -8, 5, 0, -4, 0, -5, -1, -2]

        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)


