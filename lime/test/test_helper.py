'''
Unitest for functions from helper.py

'''

import unittest
import numpy as np

from helper import *

class TestHelper(unittest.TestCase):
    
    def test_distance(self):
        p = [1, 1]
        ps = [p, [3, 3]]
        dist = distance(p, ps)
        self.assertEqual(dist[0], 1)
        self.assertEqual(dist[1], np.exp(-np.sqrt(8)))

if __name__ == '__main__':
    unittest.main()
