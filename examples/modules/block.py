# Module Object: block.py
import dict_wrangler as dw
pattern = 'block'

# Objeto de tipo Fichero - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class BlockObj(dw.SuperObj):
    pass


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        Block_O = BlockObj()

#        if objecte == None:
#            objecte = Block_O
#        else:
#            Block_O.setParent(objecte)

        results.append(Block_O)

        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, objecte)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, objecte)
    return
