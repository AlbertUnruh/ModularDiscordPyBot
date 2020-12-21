from typing import *

try:
    from NewClass import AttrDict
except ImportError:
    import AttrDict


Branch = AttrDict({
    "on_ready":     1,
    "on_message":   2,
})


class Help(object):
    def __init__(self, _help: Optional[str] = None):
        self.help = _help

    def __str__(self):
        return self.help if self.supports() else "There is no help set!"

    def supports(self):
        return False if self.help is None else True
