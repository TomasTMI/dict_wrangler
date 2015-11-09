# Module Object: file.py
import dict_wrangler as dw
pattern = 'file'
patternNameFile = 'file'

# Objeto de tipo Fichero - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class FileObj(dw.SuperObj):
    def __init__(self):
        # Definimos los atributos de padre e hijos
        self.name = None                    # Valor vacio

    def setName(self, name):
        self.name = name                    # File name


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        data = dictionary[patternNameFile]
        File_O = FileObj()
        File_O.setName(data)

#        if objecte == None:
#            objecte = File_O
#        else:
#            File_O.setParent(objecte)

        results.append(File_O)

        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, objecte)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, objecte)
    return
