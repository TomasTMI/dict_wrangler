# Module Object: block.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'block'


# Objeto de tipo Fichero - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class BlockObj(obj.SuperObj):
    def __init__(self):
        super(BlockObj, self).__init__()
        self.name = 'Bloque'

    def __repr__(self):
        return "block"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        Block_O = BlockObj()

        Block_O.setParent(objecte)

        results.append(Block_O)

        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, Block_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, Block_O)
    return
