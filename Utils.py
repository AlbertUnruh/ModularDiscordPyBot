from typing import *


class Help(object):
    def __init__(self, _help: Optional[str] = None):
        self.help = _help

    def __str__(self):
        return self.help if self.supports() else "There is no help set!"

    def supports(self):
        return False if self.help is None else True
