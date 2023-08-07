# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4.Widgets.SortablePanel as SortablePanel
import UI4.Widgets.SortablePanel
import Utils as Utils
from typing import Set, Tuple

class GroupPanel(UI4.Widgets.SortablePanel.ParameterSortablePanel):
    def __init__(self, parent, name, policy, factory, reorderable: bool = ..., deletable: bool = ..., onlyLastDeletable: bool = ...) -> None: ...
    def getValuePolicy(self): ...
    def getWidget(self): ...
    def setIndex(self, index): ...
    def setLocked(self, value): ...
    def updateWidgetState(self): ...

class SortableGroupsFormWidget(UI4.Widgets.SortablePanel.ParameterSortablePanelFormWidget):
    def __init__(self, parent, policy, factory) -> None: ...
    def _SortableGroupsFormWidget__getNode(self): ...
    def _getPanelForPolicy(self, vp): ...
    def addEntry(self): ...
    def buildAddMenu(self, menu): ...
    def panelDeleted(self, index): ...
    def panelReordered(self, oldPos, newPos): ...
    def updatePanelWidgets(self): ...
    def updatePanels(self): ...