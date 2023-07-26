# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
from typing import ClassVar

class OverridableLineEdit(PySide6.QtWidgets.QLineEdit):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent) -> None: ...
    def _overrideSet(self, text): ...
    def _resetDefault(self): ...
    def resizeEvent(self, event): ...
    def setText(self, text): ...
