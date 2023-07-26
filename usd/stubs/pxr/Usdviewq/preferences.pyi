# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
from pxr.Usdviewq.common import FixableDoubleValidator as FixableDoubleValidator
from pxr.Usdviewq.preferencesUI import Ui_Preferences as Ui_Preferences
from typing import ClassVar

class Preferences(PySide6.QtWidgets.QDialog):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent, dataModel) -> None: ...
    def _apply(self): ...
    def _buttonBoxButtonClicked(self, button): ...
    def _updateEditorsFromDataModel(self): ...
