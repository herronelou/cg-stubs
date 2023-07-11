# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
from _typeshed import Incomplete

class ExpandingLabel(PyQt5.QtWidgets.QTextEdit):
    def __init__(self, *args): ...
    def _rightAlign(self): ...
    def minimumSizeHint(self): ...
    def resizeEvent(self, resizeEvent): ...
    def setText(self, qstring, color: Incomplete | None = ...): ...
    def sizeHint(self): ...
    def sizePolicy(self): ...