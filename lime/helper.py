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
        if not isinstance(img, np.ndarray):
            img = np.asarray(img)
        self.img = img

    @property
    def seg(self):
        return self.__seg

    @property
    def br(self):
        return self.__br

    @property
    def img(self):
        return self.__img
    
    @img.setter
    def img(self, img):
        self.__img = img
        seg = np.zeros(img.shape[:-1], dtype=np.int8)
        # each digit represents a segmentation id
        it = np.nditer(seg, flags=["multi_index"])
        column_size = seg.shape[0] // 2 + 1
        while not it.finished:
            i = it.multi_index
            seg[i] = (i[0]//2)*column_size + i[1]//2
            it.iternext()
        self.__seg = seg
        self.__br = np.ones(int(seg[-1, -1])+1, dtype=np.int8)
        
    def retrieve_img(self, br):
        img = self.img
        r = np.zeros_like(img)
        it = np.nditer(self.seg, flags=["multi_index"])
        for seg_id in it:
            idx = it.multi_index
            r[idx] = img[idx] if br[seg_id]==1 else [0, 0, 0]
        return r
        
    def retrieve_imgs(self, brs):
        return [self.retrieve_img(br) for br in brs]
    
    
'''
Distance: compute the distance between two points

'''

def distance(ref, points):
    dists = [-dist(ref, p) for p in points]
    return np.exp(dists)
