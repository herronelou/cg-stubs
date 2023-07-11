# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.InputWidgets as InputWidgets
import QT4FormWidgets.PaintingUtils as PaintingUtils
import PyQt5.QtCore
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.BaseValueFormWidget import BaseValueFormWidget as BaseValueFormWidget
from QT4FormWidgets.FormWidget import AlignChildLabelWidths as AlignChildLabelWidths, AlignLeftControlWidths as AlignLeftControlWidths, FormWidget as FormWidget, ScrubbingStates as ScrubbingStates
from QT4FormWidgets.MultiStateBadge import MultiStateBadge as MultiStateBadge, ToggleStateBadge as ToggleStateBadge, ToggleValuePolicyState as ToggleValuePolicyState
from typing import ClassVar, Set, Tuple

class TextFormWidget(BaseValueFormWidget):
    backtabPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    tabPressed: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def _TextFormWidget__indentText(self): ...
    def _TextFormWidget__unindentText(self): ...
    def _buildControlWidget(self, layout): ...
    def _checkControlWidget(self): ...
    def _controlTextChanged(self): ...
    def _getControlWidget(self): ...
    def _lockChanged(self, state): ...
    def _updateControlWidget(self): ...
    def eventFilter(self, watched, event): ...
