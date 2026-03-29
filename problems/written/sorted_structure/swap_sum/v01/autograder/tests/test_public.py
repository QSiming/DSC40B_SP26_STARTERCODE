import unittest
import pandas as pd
import pathlib
from gradescope_utils.autograder_utils.decorators import weight, visibility, leaderboard

import ep04


class Test(unittest.TestCase):

    @weight(0)
    @visibility('visible')
    def test_on_simple_example(self):
        """Works on a simple example."""
        msg = """
        
            A = [3, 2, 6, 5]
            B = [1, 8, 2, 9]

        Swapping 8 and 6 would do it (but it's not the only possibility).

        """
        A = [3, 2, 6, 5]
        B = [1, 8, 2, 9]
        a, b = ep04.swap_sum(list(A), list(B))
        self.assertEqual(sum(A) - a  + b, sum(B) - b + a, msg)


