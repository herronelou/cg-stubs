# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
from Nodes3DAPI.TerminalOpDelegates.TerminalOpDelegate import TerminalOpDelegate as TerminalOpDelegate
from typing import Set, Tuple

class ExampleTerminalOpDelegate(TerminalOpDelegate):
    def __init__(self): ...
    def appendOp(self, op, txn, port, graphState): ...
    def reset(self): ...
    def update(self): ...
