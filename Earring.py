import product
from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
class Encoder_Earring(JSONEncoder):
        def default(self, o):
            return o.__dict__

class Decoder_Earring(JSONDecoder):
    def decode(self, o):
            data = loads(o)
            vals = []
            for key in data.keys():
                vals.append(data[key])
            cat = Earring(*vals)
            return cat

class Earring(product.Product):
    diameter=0
    def __init__(self,name,material,color,weight,diameter):
        self.diameter=diameter
        product.Product.__init__(self,name,material,color,weight)

    def __repr__(self):
        return "{Category:" + str(self.name) + ", Weight:" + str(self.weight) + ", Color:" + str(
            self.color) + ", Material:" + str(self.material) + "}\n"