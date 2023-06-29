# mypy: disable_error_code = misc
import PySide6.QtWidgets
from _typeshed import Incomplete
from typing import ClassVar

class ArrayAttributeView(PySide6.QtWidgets.QWidget):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...): ...
    def CanView(self, attr): ...
    def CopyAll(self): ...
    def CopySelected(self): ...
    def SelectAll(self): ...
    def SetAttribute(self, attr, frame): ...
    def _CopyValsToClipboard(self, vals): ...
    def _SetupContextMenu(self): ...
    def _ShowContextMenu(self, point): ...
    def keyPressEvent(self, e): ...

class _ArrayAttributeModel(PySide6.QtCore.QAbstractListModel):
    RawDataRole: ClassVar[int] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self): ...
    def GetArrayData(self): ...
    def GetScalarTypeName(self): ...
    def SetArrayDataAndTypeName(self, arrayData, scalarTypeName): ...
    def SetSlice(self, slice_): ...
    def TryToFetchMore(self): ...
    def _Reset(self): ...
    def canFetchMore(self, index): ...
    def columnCount(self, parent: PySide6.QtCore.QModelIndex = ...): ...
    def data(self, index, role: PySide6.QtCore.Qt.ItemDataRole = ...): ...
    def fetchMore(self, index): ...
    def index(self, row, col, parent: PySide6.QtCore.QModelIndex = ...): ...
    def parent(self, index): ...
    def rowCount(self, parent: PySide6.QtCore.QModelIndex = ...): ...

class _SliceLineEdit(PySide6.QtWidgets.QLineEdit):
    class Validator(PySide6.QtGui.QValidator):
        staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
        def validate(self, s, pos): ...
    SliceChanged: ClassVar[PySide6.QtCore.Signal] = ...
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parent: Incomplete | None = ...): ...
    def _OnEditingFinished(self): ...
    def setText(self, t): ...

def _GetLengthOfRange(start, stop, step): ...
def _GetSliceFromString(s): ...
def _IntOrNone(s): ...