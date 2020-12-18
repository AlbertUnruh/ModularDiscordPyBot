from os import listdir
import importlib


Modules = [_.replace(".py", "") for _ in listdir("./Modules") if _.endswith(".py") and not _ == "__init__.py"]
libs = {}


for lib in Modules:
    libs[lib] = importlib.import_module(f"Modules.{lib}", "Modules")

del listdir, lib, importlib
