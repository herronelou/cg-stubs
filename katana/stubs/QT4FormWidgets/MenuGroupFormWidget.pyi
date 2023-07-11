# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
from QT4FormWidgets.FWidget import FBoxLayout as FBoxLayout, FButton as FButton, FDisclosureTriangle as FDisclosureTriangle, FLabel as FLabel, FLockIcon as FLockIcon, FMenu as FMenu, FPixmap as FPixmap, FSpacer as FSpacer, FStateBadge as FStateBadge, FSvgIcon as FSvgIcon, FToggleStateBadge as FToggleStateBadge, FWidget as FWidget
from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates
from QT4FormWidgets.ValuePolicy import ValuePolicyEvent as ValuePolicyEvent
from typing import Set, Tuple

class MenuGroupFormWidget(FormWidget):
    def __init__(self, parent, policy, factory): ...
    def _MenuGroupFormWidget__doTriangleClicked(self): ...
    def _MenuGroupFormWidget__updateTriangleColor(self): ...
    def _buildControlWidget(self, layout): ...
    def _buildLabel(self, labelText, pos: int = ...): ...
    def _createChildWidget(self, policy, parentWidget, factory, index): ...
    def _firstChildFormWidgetIndex(self): ...
    def _freeze(self): ...
    def _lockChanged(self, state): ...
    def _participatesInLabelAlignment(self): ...
    def _thaw(self): ...
    def buildMenu(self, menu): ...
    def valueChangedEvent(self, event): ...
