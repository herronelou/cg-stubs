# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
from QT4Widgets.PopdownLabel import PopdownLabel

class FCurveSnapSettingsMenu(PopdownLabel):
    def __init__(self, graphWidget, *args): ...
    def _FCurveSnapSettingsMenu__buildSettings(self, xInc, yInc): ...
    def buildMenu(self, menu): ...
    def updateState(self): ...

class SnapSettingsAction(PyQt5.QtWidgets.QAction):
    def __init__(self, settings, graphWidget, *args): ...
    def _SnapSettingsAction__activatedCB(self): ...