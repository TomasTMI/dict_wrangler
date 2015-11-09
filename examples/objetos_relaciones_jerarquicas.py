# Objeto principal de la que van a derivar otros objectos (Basicamente para no
# tener que definir la funcionalidad de padre e hijo una y otra vez).
# Posiblemente quieras definir este en otro fichero para poder llamarlo desde
# todos los modulos a la hora de crear los diferentes objetos.

class SuperObj():
    def __init__(self):
        # Definimos los atributos de padre e hijos

        self.parent = None                      # Valor vacio
        self.children = list()                  # Lista vacia

    def setParent(self, parent):
        # Funcion a la que llamaremos para definir el padre de un elemento

        self.parent = parent                # Da valor para parent
        parent.children.append(self)        # Se anhade a la lista de hijos


# Objeto de tipo Obj - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class Obj(SuperObj):
    pass

# Objeto de tipo Fichero - (Hereda de SuperObj)
# Cada modulo sera capaz de crear su propio tipo de obj
class Fichero(SuperObj):
    pass

# Ejemplo de funcionalidad
# -----------------------------------------------------------------------------

fichero01 = Fichero()           # Generamos objeto de tipo Fichero
obj01 = Obj()                   # Generamos objeto de tipo Obj

obj01.setParent(fichero01)      # Se establece relacion entre ellos

# Verificando que la relacion esta establecida correctamente
# -----------------------------------------------------------------------------
print obj01.parent              # Se imprime fichero a traves del hijo
print fichero01                 # Se imprime fichero directamente

print obj01                     # Se imprime objeto directamente
print fichero01.children[0]     # Se imprime objeto a traves del fichero
