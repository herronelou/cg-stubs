# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.FWidget as FWidget
import QT4FormWidgets.FWidget
import ResourceFiles as ResourceFiles
from ResourceFiles.IconManager import ResourceManager as ResourceManager

DISABLED_OPACITY: float

class FormClose(QT4FormWidgets.FWidget.FPixmap):
    def __init__(self, parent): ...
    def _FormClose__on_fpixmap_clicked(self): ...
    def paint(self, painter, width, height): ...
    def setEnabled(self, yorn): ...