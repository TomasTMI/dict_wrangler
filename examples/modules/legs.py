# Object module: legs.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'legs'


# Legs Object - (Inherited from SuperObj)
class LegsObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(LegsObj, self).__init__()
        self.value = None

    def setValue(self, value):
        self.value = value

    def __repr__(self):
        return "legs"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        data = dictionary['value']
        Legs_O = LegsObj()
        Legs_O.setValue(data)
        Legs_O.setParent(objecte)
        results.append(Legs_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Legs_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Legs_O)
    return
