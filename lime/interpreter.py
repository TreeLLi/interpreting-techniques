'''
interpret a prediction of given model

'''

class Interpreter:
    def __init__(self, model):
        self.model = model

    def _convert_to_br(self, img):

    def interpret(self, inp_img):
        # return the prediction and the explanations
        inp_br = _convert_to_br(inp_img)
        i_pc, i_pp = self.model.predict(inp_img)

        samp_brs = sample(inp_br)
        samp_imgs = self.convertor.retrieve_img(samp_brs)
        s_pcs, s_pps = self.model.predict(samp_imgs, cls=i_pc)

        e = Explanation(inp_br.shape[0])
        # add input point into the samples
        e_brs = [inp_br] + samp_brs
        e_pps = [i_pp] + s_pps
        ds = distance(inp_img, [inp_img] + samp_imgs)
        e.fit(e_brs, e_pps, ds)
