'''
model wrapper defines a set of protocols for the behaviours of underlying model

'''

class Model:
    def __init__(self, model):
        self.model = model

    def predict(self, img, num=1, cls=-1):
        # return the prediction result of given inputs
        return img
