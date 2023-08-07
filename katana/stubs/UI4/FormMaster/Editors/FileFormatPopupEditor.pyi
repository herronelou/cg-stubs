# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes2DAPI as Nodes2DAPI
import QT4FormWidgets as QT4FormWidgets
import PyQt5.QtCore as QtCore
from QT4FormWidgets.PopupFormWidget import PopupFormWidget
from typing import Set, Tuple

class FileFormatPopupBase(PopupFormWidget):
    def __init__(self, formats, parent, valuePolicy, widgetFactory) -> None: ...
    def _FileFormatPopupBase__externalSetValueCallback(self, event): ...
    def _FileFormatPopupBase__updateFormat(self): ...
    def getWidgetHints(self): ...
    def setFilename(self, name): ...
    def validFormats(self): ...

class InputFileFormatPopup(FileFormatPopupBase):
    def __init__(self, *args) -> None: ...
    def formatFromFilename(self, filename): ...
    def isOutput(self): ...

class OutputFileFormatPopup(FileFormatPopupBase):
    def __init__(self, *args) -> None: ...
    def formatFromFilename(self, filename): ...
    def isOutput(self): ...