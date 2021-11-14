from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
class Encoder_Product(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Decoder_Product(JSONDecoder):
    def decode(self, o):
        data = loads(o)
        vals = []
        cat=Product("Demo","Demo","demo",0)
        for key in data.keys():
            vals.append(data[key])
        if data["name"]=="Necklace":
            import necklace
            cat = necklace.Necklace(*vals)
        elif data["name"]=="Bracelet":
            import bracelet
            cat = bracelet.Bracelet(*vals)
        elif data["name"]=="Earring":
            import Earring
            cat = Earring.Earring(*vals)
        return cat

class Product:
    loaded_products=[]
    def __init__(self, name,material,color,weight):
        self.name = name
        self.material=material
        self.color=color
        self.weight=weight

    def __repr__(self):
        #return "{Category:"+str(self.name)+", Weight:"+str(self.weight)+", Color:"+str(self.color)+", Material:"+str(self.material)+"}\n"
        return str(self)

    def __eq__(self, other):
        """ Overloaded in order to verify the membership inside a collection """
        return self.name == other.name

    @classmethod
    def load_products(cls):
        decoder = Decoder_Product()
        try:
            with open("products.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_product = decoder.decode(data)
                    if decoded_product not in cls.loaded_products:
                        cls.loaded_products.append(decoded_product)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.loaded_products = []
        return cls.loaded_products


    @classmethod
    def remove_product(cls, cat):
        cls.load_products()
        if cat in cls.loaded_products:
            cls.load_products().remove(cat)
            with open("products.txt", 'w') as f:
                for cat in cls.loaded_products:
                    e = Encoder_Product()
                    encoded_cat = e.encode(cat)
                    dump(encoded_cat, f)
                    f.write("\n")

    @classmethod
    def add_product(cls, cat):
        cls.load_products()
        if cat not in cls.loaded_products:
            with open("products.txt", 'a') as f:
                e = Encoder_Product()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")