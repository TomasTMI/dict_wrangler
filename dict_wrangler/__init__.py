import module_mgr as mm
import dict_wrangler as dw

module_manager = mm.Manager()
modules_folders = None


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


def load_modules():
    module_manager.register_paths([modules_folders])
    registered_paths = module_manager.registered_paths()
    module_manager.add_folders_to_pythonpath(registered_paths)
    modules_discovered = module_manager.discover_modules()
    modules_loaded = module_manager.load_modules(modules_discovered)
    return modules_loaded


def read_dict(dictionary=None, results=list(), objecte=None):
    assert isinstance(dictionary, dict), "Not a dictionary"

    modules = dw.load_modules()
    for module in modules:
        try:
            module.main(dictionary, results, objecte)

        except Exception, e:
            print "An exception has ocurred:", e

    return results
