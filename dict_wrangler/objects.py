class SuperObj(object):
    def __init__(self):
        # Definimos los atributos de padre e hijos
        self.parent = None                      # Valor vacio
        self.children = list()                  # Lista vacia

    def setParent(self, parent):
        # Funcion a la que llamaremos para definir el padre de un elemento
        self.parent = parent                # Da valor para parent
        parent.children.append(self)        # Se anhade a la lista de hijos


class RootObj(SuperObj):
    def __init__(self):
        super(RootObj, self).__init__()
        self.name = None

    def __repr__(self):
        return "ROOT"
