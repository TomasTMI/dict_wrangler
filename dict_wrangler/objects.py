# Global structure of OBJECTS for Dict_Wrangler

class SuperObj(object):
    def __init__(self):
        # Attributes: father, children, ...
        self.parent = None                      # Valor vacio
        self.children = list()                  # Lista vacia

    def setParent(self, parent):
        # Funcion a la que llamaremos para definir el padre de un elemento
        self.parent = parent                # Da valor para parent
        parent.children.append(self)        # Se anhade a la lista de hijos


class RootObj(SuperObj):
    def __init__(self):
        super(RootObj, self).__init__()
        self.name = "ROOT"

    def __repr__(self):
        return "ROOT"
