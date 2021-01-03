
class AttrDict:
    def __init__(self, data: dict):
        for key in list(data.keys()):
            if type(data[key]) == dict:
                self.__dict__[key.replace(" ", "_")] = self.__class__(data[key])
            else:
                self.__dict__[key.replace(" ", "_")] = data[key]

    def __str__(self):
        def recursive(data: AttrDict):
            __ = ""
            for key in list(data.__dict__.keys()):
                if type(data[key]) == self.__class__:
                    __ += f"{key!r}: " "{" + recursive(data[key]) + "}, "
                else:
                    __ += f"{key!r}: {data[key]!r}, "
            return __[:-2]
        return "{" + recursive(self) + "}"

    def __getitem__(self, item):
        return self.__dict__[item]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __getattr__(self, item):
        if item in list(self.__dict__.keys()):
            return self.__dict__[item]
        else:
            raise AttributeError(f"{item!r} is not a valid Attribute!")
