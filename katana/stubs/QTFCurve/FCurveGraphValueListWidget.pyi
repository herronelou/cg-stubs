# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFCurve as PyFCurve
import PyQt5.QtWidgets
from QTFCurve.FCurveListView import FCurveListView as FCurveListView
from QTFCurve.FCurveValueEdit import FCurveValueEdit as FCurveValueEdit
from _typeshed import Incomplete

class FCurveGraphValueListWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self, parent: Incomplete | None = ...): ...
    def addCustomColumn(self, name, defaultValue, valueList: list = ...): ...
    def getCurves(self) -> Container: ...
    def getGraphView(self) -> GraphWidget: ...
    def getListView(self) -> FCurveListView: ...
    def getValueEdit(self) -> FCurveValueEdit: ...