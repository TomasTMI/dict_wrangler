# Object module: author.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'author'


# Author Object - (Inherited from SuperObj)
class AuthorObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(AuthorObj, self).__init__()
        self.value = None

    def setValue(self, value):
        self.value = value

    def __repr__(self):
        return "author"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        data = dictionary['value']
        Author_O = AuthorObj()
        Author_O.setValue(data)
        Author_O.setParent(objecte)
        results.append(Author_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Author_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Author_O)
    return
