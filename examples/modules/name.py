# Object module: name.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'name'


# Name Object - (Inherited from SuperObj)
class NameObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(NameObj, self).__init__()
        self.value = None

    def setValue(self, value):
        self.value = value

    def __repr__(self):
        return "name"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        data = dictionary['value']
        Name_O = NameObj()
        Name_O.setValue(data)
        Name_O.setParent(objecte)
        results.append(Name_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Name_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Name_O)
    return
