import unittest
import pandas as pd
import pathlib
from gradescope_utils.autograder_utils.decorators import weight, visibility, leaderboard

import ep02


class Test(unittest.TestCase):

    @weight(0)
    @visibility('visible')
    def test_part_a_on_simple_example(self):
        """Part a) Works on a simple example."""

        msg = """
        
        data = [5, 3, 6, 7, 1]
        colors = ['red', 'blue', 'red', 'red', 'blue']

        """
        data = [5, 3, 6, 7, 1]
        colors = ['red', 'blue', 'red', 'red', 'blue']

        actual = ep02.learn_theta(data, colors)
        self.assertLess(actual, 5, msg)
        self.assertGreaterEqual(actual, 3, msg)

    @weight(0)
    @visibility('visible')
    def test_part_b_on_simple_example(self):
        """Part b) Works on a simple example."""
        
        msg = """

        data = [5, 3, 6, 7, 1, 0]
        colors = ['red', 'blue', 'red', 'red', 'blue', 'red']
        theta = 3.5

        """
        data = [5, 3, 6, 7, 1, 0]
        colors = ['red', 'blue', 'red', 'red', 'blue', 'red']
        actual = ep02.compute_ell(data, colors, 3.5)
        self.assertEqual(actual, 1, msg)

    @weight(0)
    @visibility('visible')
    def test_part_c_on_simple_example(self):
        """Part c) Works on a simple example."""

        msg = """
        
        data = [5, 3, 6, 7, 1]
        colors = ['red', 'blue', 'red', 'red', 'blue']

        """
        data = [5, 3, 6, 7, 1]
        colors = ['red', 'blue', 'red', 'red', 'blue']

        actual = ep02.minimize_ell(data, colors)
        self.assertLess(actual, 5, msg)
        self.assertGreaterEqual(actual, 3, msg)

