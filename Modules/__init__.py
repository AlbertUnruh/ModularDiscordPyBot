from os import listdir
import importlib


required = ["__main__", "Branch", "HELP"]

Modules = [_.replace(".py", "") for _ in listdir("./Modules") if _.endswith(".py") and not _ == "__init__.py"]
libs = {}


for lib in Modules[:]:
    libs[lib] = importlib.import_module(f"Modules.{lib}", "Modules")

    for attr in required:
        if not hasattr(libs[lib], attr):
            del libs[lib]
            Modules.remove(lib)
            continue


del listdir, lib, importlib, attr
