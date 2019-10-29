'''
utility functions like sampling, converting representations, and 

'''

import numpy as np
from scipy.spatial.distance import euclidean as dist

'''
Sample: sample perturbed instances around the reference

'''

def sample(ref, rule, num=0, seed=0):
    return ref


'''
Converter: transform images to binary representations

'''

class Convertor:
    def __init__(self, img):
        set_img(img)

    def set_img(self, img):
        self.origin = img
        self.seg = np.zeros(img.shape[:-1])
        # TODO - segment image for binary representaton
        # each digit represents a segmentation id
        
    def get_binary_rep(self):
        return self.origin
        
    def retrieve_img(self, br):
        return self.origin
        
    
'''
Distance: compute the distance between two points

'''

def distance(ref, points):
    dists = [-dist(ref, p) for p in points]
    return np.exp(dists)
