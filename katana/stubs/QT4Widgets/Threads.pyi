# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from _typeshed import Incomplete
from typing import Set, Tuple

_GlobalThreadPool: None

class ThreadPool:
    def __init__(self): ...
    def _ThreadPool__threadFinishedCB(self): ...
    def start(self, thread, priority: Incomplete | None = ...): ...
    def __del__(self): ...

def GetGlobalThreadPool(): ...
