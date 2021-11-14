from json import JSONEncoder, JSONDecoder, dump, loads
class Encoder(JSONEncoder):
    def default(self, o: str) -> str:
        return o.__dict__


class Decoder(JSONDecoder):
    def decode(self, o):
        data = loads(o)
        vals = []
        for key in data.keys():
            vals.append(data[key])
        cat = Category(*vals)
        return cat


class Category:
    """ define the Category class which holds the categories of products """

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        """ Overloaded in order to verify the membership inside a collection """
        return self.name == other.name

    def __repr__(self):
        return "[Name: "+str(self.name)+"]"