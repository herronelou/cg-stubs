# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
import pxr.Usd as Usd
from pxr.Usdviewq.attributeValueEditorUI import Ui_AttributeValueEditor as Ui_AttributeValueEditor
from pxr.Usdviewq.common import GetPropertyColor as GetPropertyColor, UIPropertyValueSourceColors as UIPropertyValueSourceColors
from pxr.Usdviewq.scalarTypes import ToString as ToString
from typing import ClassVar

class AttributeValueEditor(PySide6.QtWidgets.QWidget):
    editComplete: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent): ...
    def _FindView(self, attr): ...
    def clear(self): ...
    def populate(self, primPath, propName): ...
    def refresh(self): ...
    def setAppController(self, appController): ...