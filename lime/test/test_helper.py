'''
Unitest for functions from helper.py

'''

from test.test_base import TestBase

from helper import *

class TestDistance(TestBase):
    
    def test_distance(self):
        p = [1, 1]
        ps = [p, [3, 3]]
        dist = distance(p, ps)
        self.assertEqual(dist[0], 1)
        self.assertEqual(dist[1], np.exp(-np.sqrt(8)))

class TestConvertor(TestBase):

    def __init__(self, *args, **kwargs):
        super(TestConvertor, self).__init__(*args, *kwargs)
        self.img = [[[1, 0, 0], [3, 0, 0], [4, 0, 0]],
                    [[5, 0, 0], [2, 0, 0], [6, 0, 0]],
                    [[7, 0, 0], [8, 0, 0], [9, 0, 0]]]
        self.conv = Convertor(self.img)
    
    def test_segmentation(self):
        seg = self.conv.seg
        print(seg)
        self.assertListEqual(seg, [[0, 0, 1],
                                   [0, 0, 1],
                                   [2, 2, 3]])
        br = self.conv.br
        self.assertListEqual(br, [1, 1, 1, 1])

    def test_retrieve_img(self):
        br_0 = [1, 1, 1, 1]
        br_1 = [0, 1, 1, 1]
        imgs = self.conv.retrieve_imgs(np.asarray([br_0, br_1]))
        self.assertListEqual(imgs[0], self.img)
        self.assertListEqual(imgs[1], [[[0, 0, 0], [0, 0, 0], [4, 0, 0]],
                                       [[0, 0, 0], [0, 0, 0], [6, 0, 0]],
                                       [[7, 0, 0], [8, 0, 0], [9, 0, 0]]])
        
if __name__ == '__main__':
    unittest.main()
