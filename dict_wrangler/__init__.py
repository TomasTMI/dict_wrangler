import module_mgr as mm
import dict_wrangler as dw

modules_folder = None


def load_modules():
    mm.register_paths([modules_folder])
    registered_paths = mm.registered_paths()
    mm.add_folders_to_pythonpath(registered_paths)
    modules_discovered = mm.discover_modules()
    modules_loaded = mm.load_modules(modules_discovered)
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
