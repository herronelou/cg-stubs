# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4FormWidgets.MenuUtils as MenuUtils
import QT4FormWidgets.PaintingUtils as PaintingUtils
import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
from QT4FormWidgets.FWidget import FDisclosureTriangle as FDisclosureTriangle
from QT4FormWidgets.FixableBoxLayout import FixableBoxLayout as FixableBoxLayout
from QT4FormWidgets.InputWidgets import InputLineEdit as InputLineEdit, InputTextEdit as InputTextEdit
from QT4FormWidgets.NumberFormWidget import EvalLocalMath as EvalLocalMath
from typing import Set, Tuple

class ArrayItemEntry(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent): ...
    def _ArrayItemEntry__on_entry_dragStarted(self): ...
    def _ArrayItemEntry__on_entry_lostFocus(self): ...
    def _ArrayItemEntry__on_exprTriangle_expanded(self, item, state): ...
    def _ArrayItemEntry__on_expr_lostFocus(self): ...
    def contextMenuEvent(self, event): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def isLocked(self): ...
    def mousePressEvent(self, event): ...
    def policyChanged(self, event): ...
    def setLocked(self, state): ...
    def setPolicy(self, policy): ...

def DarkPalette(palette): ...
