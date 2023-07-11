# mypy: disable-error-code="misc, override, no-redef"

import PySide6.QtCore
import PySide6.QtWidgets
import pxr.Usdviewq.usdviewContextMenuItem
from pxr.Usdviewq.usdviewContextMenuItem import UsdviewContextMenuItem as UsdviewContextMenuItem
from typing import Any, ClassVar

class HeaderContextMenu(PySide6.QtWidgets.QMenu):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent): ...
    def _prepForShow(self): ...

class HeaderContextMenuItem(pxr.Usdviewq.usdviewContextMenuItem.UsdviewContextMenuItem):
    action: Any
    def __init__(self, parent, column): ...
    def GetText(self): ...
    def IsChecked(self): ...
    def IsEnabled(self): ...
    def RunCommand(self): ...

def _GetContextMenuItems(parent): ...