'''
Test base: define the global behaviours for other test

'''

import unittest
import numpy as np

class TestBase(unittest.TestCase):

    def assertListEqual(self, x, y, msg=None):
        x = x.tolist() if isinstance(x, np.ndarray) else x
        y = y.tolist() if isinstance(y, np.ndarray) else y
        super(TestBase, self).assertListEqual(x, y, msg)
