# Object module: block.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'block'


# Block Object - (Inherited from SuperObj)
class BlockObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(BlockObj, self).__init__()

    def __repr__(self):
        return "block"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        Block_O = BlockObj()
        Block_O.setParent(objecte)
        results.append(Block_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Block_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Block_O)
    return
