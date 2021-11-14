from json import JSONDecoder, JSONEncoder, JSONDecodeError, loads, dump
class Order:
    loaded_orders=[]
    def __init__(self,address,orders):
        self.address=address
        self.orders=orders

    def __repr__(self):
        return "[ Address:"+str(self.address)+", Orders"+str(self.orders)+" ]"

    @classmethod
    def load_orders(cls):
        decoder = Decoder_Order()
        try:
            with open("orders.txt") as f:
                for line in f:
                    data = loads(line)
                    decoded_order = decoder.decode(data)
                    if decoded_order not in cls.loaded_orders:
                        cls.loaded_orders.append(decoded_order)
        except (JSONDecodeError, FileNotFoundError) as e:
            cls.loaded_orders = []
        return cls.loaded_orders


    @classmethod
    def add_order(cls, cat):
        cls.load_orders()
        if cat not in cls.loaded_orders:
            with open("orders.txt", 'a') as f:
                e = Encoder_Order()
                encoded_cat = e.encode(cat)
                dump(encoded_cat, f)
                f.write("\n")

class Encoder_Order(JSONEncoder):
    def default(self, o):
        return o.__dict__

class Decoder_Order(JSONDecoder):
    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Order(*vals)
        return cat

