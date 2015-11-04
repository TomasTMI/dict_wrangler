import module_mgr as mm
import dict_wrangler as dw

module_manager = mm.Manager()
modules_folders = None


def load_modules():
    module_manager.register_paths([modules_folders])
    registered_paths = module_manager.registered_paths()
    module_manager.add_folders_to_pythonpath(registered_paths)
    modules_discovered = module_manager.discover_modules()
    modules_loaded = module_manager.load_modules(modules_discovered)
    return modules_loaded


def read_dict(dictionary=None):
    assert isinstance(dictionary, dict), "Not a dictionary"

    results = list()

    modules = dw.load_modules()
    for module in modules:
        try:
            module.main(dictionary, results)

        except Exception, e:
            print "An exception has ocurred:", e

    return results
