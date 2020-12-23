from os import listdir
import importlib
import Utils


required = ["__main__", "EVENTS", "HELP"]

MODULES = [module.replace(".py", "") for module in listdir("./Modules") if module.endswith(".py") and not module == "__init__.py"]
libs = {}


for lib in MODULES.copy():

    libs[lib] = importlib.import_module(f"Modules.{lib}", "Modules")

    for attr in required:
        if not hasattr(libs[lib], attr):
            if attr == "HELP":
                if Utils.EVENT.on_message in libs[lib].__getattribute__("EVENTS"):
                    del libs[lib]
                    MODULES.remove(lib)
                    break


del listdir, lib, importlib, attr, required
