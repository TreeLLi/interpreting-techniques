'''
Explanation: a simpler model approximating the underlying complicated model as the explanation

'''

import numpy as np

class Explanation:

    def __init__(self, w_num):
        self.w = np.zeros(w_num)

    # l: locality weight i.e. the distance between the input and other perturbed samples
    def fit(self, x, y, l):
        
