# Object module: file.py
import dict_wrangler as dw
import dict_wrangler.objects as obj
pattern = 'file'
patternNameFile = 'file'


# File Object - (Inherited from SuperObj)
class FileObj(obj.SuperObj):
    def __init__(self):
        # Attributes: father, children, ...
        super(FileObj, self).__init__()
        self.name = None

    def setName(self, name):
        self.name = name

    def __repr__(self):
        return "file"


def main(dictionary, results, objecte):
    if dictionary['type'] == pattern:
        # Object
        data = dictionary[patternNameFile]
        File_O = FileObj()
        File_O.setName(data)
        File_O.setParent(objecte)
        results.append(File_O)

        # Next element
        value = dictionary['value']
        if isinstance(value, dict):
            dw.read_dict(value, results, File_O)
        elif isinstance(value, list):
            for dictionary in value:
                dw.read_dict(dictionary, results, File_O)
    return
