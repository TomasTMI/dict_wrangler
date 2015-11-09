# Module Object: file.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'file'
patternNameFile = 'file'


# Objeto de tipo Fichero - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class FileObj(obj.SuperObj):
    def __init__(self):
        super(FileObj, self).__init__()
        # Definimos los atributos de padre e hijos
        self.name = None                    # Valor vacio

    def setName(self, name):
        self.name = name                    # File name

    def __repr__(self):
        return "file"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        data = dictionary[patternNameFile]
        File_O = FileObj()
        File_O.setName(data)

        File_O.setParent(objecte)

        results.append(File_O)

        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, File_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, File_O)
    return
