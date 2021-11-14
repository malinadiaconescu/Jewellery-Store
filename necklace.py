import product
from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
class Encoder_Necklace(JSONEncoder):
        def default(self, o):
            return o.__dict__

class Decoder_Necklace(JSONDecoder):
    def decode(self, o):
            data = loads(o)
            vals = []
            for key in data.keys():
                vals.append(data[key])
            cat = Necklace(*vals)
            return cat

class Necklace(product.Product):
    length=0
    def __init__(self,name,material,color,weight,length):
        self.length=length
        product.Product.__init__(self,name,material,color,weight)

    def __repr__(self):
        return "{Category:" + str(self.name) + ", Weight:" + str(self.weight) + ", Color:" + str(
            self.color) + ", Material:" + str(self.material) + "}\n"