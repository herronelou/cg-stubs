# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import DrawingModule as DrawingModule
import KatanaResources as KatanaResources
import UI4.FormMaster.NodeMimeData as NodeMimeData
import NodegraphAPI as NodegraphAPI
import PyQt5.QtGui
import PyQt5.QtWidgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import Utils as Utils
import typing
from NodegraphAPI.LiveGroup import LiveGroupMixin as LiveGroupMixin
from PyUtilModule.VirtualKatana import Widgets as Widgets
from QT4Widgets.FilterablePopupButton import FilterablePopupButton
from UI4.Tabs.NodeGraphTab.NodeGoRootButton import NodeGoRootButton as NodeGoRootButton
from UI4.Widgets.NodeButton import NodeButton as NodeButton
from UI4.Widgets.NodePopupMenu import NodePopupMenu as NodePopupMenu
from _typeshed import Incomplete
from typing import Set, Tuple

__liveGroupPixmapNames: dict
__nodePixmaps: dict

class NodeBreadcrumbsFrame(PyQt5.QtWidgets.QFrame):
    def __init__(self, enterGroupNodeCallback: typing.Optional[typing.Callable] = ..., goToNodeCallback: typing.Optional[typing.Callable] = ..., parent: Incomplete | None = ...) -> None: ...
    def _NodeBreadcrumbsFrame__addFrameWidgets(self, frameWidgets: list, groupNodes: list[NodegraphAPI.GroupNode]) -> list[NodegraphAPI.GroupNode]: ...
    def _NodeBreadcrumbsFrame__enterOrRevealNode(self, node: NodegraphAPI.Node): ...
    def _NodeBreadcrumbsFrame__insertFrameWidgets(self, frameWidgets: list, insertionIndex: int, groupNode: Incomplete | None = ..., lastNode: bool = ...) -> bool: ...
    def _NodeBreadcrumbsFrame__on_nodeButton_clicked(self): ...
    def _NodeBreadcrumbsFrame__on_node_updated(self, args: list[tuple[str, object, dict]]): ...
    def _NodeBreadcrumbsFrame__removeFrameWidgets(self): ...
    def _NodeBreadcrumbsFrame__updateNodeButtons(self): ...
    def dragEnterEvent(self, event): ...
    def dropEvent(self, event): ...
    def fontChange(self, oldFont): ...
    def getDeepestNotDeletedNode(self) -> list[NodegraphAPI.Node]: ...
    def resizeEvent(self, event): ...
    def setCurrentNodeView(self, groupNode: NodegraphAPI.GroupNode | None): ...
    def showEvent(self, event: PyQt5.QtGui.QShowEvent): ...

class _EllipsisPopupButton(FilterablePopupButton):
    def __init__(self, enterGroupNodeCallback: callback, parent: Incomplete | None = ...) -> None: ...
    def _EllipsisPopupButton__on_itemChosen(self, name, meta: Incomplete | None = ...): ...
    def _EllipsisPopupButton__on_node_setColor(self, eventType, eventID, **kwargs): ...
    def _EllipsisPopupButton__on_popupAboutToShow(self): ...
    def _EllipsisPopupButton__on_popupWindowTreeWidget_mousePressEvent(self, event: PyQt5.QtGui.QMouseEvent): ...
    def _EllipsisPopupButton__on_popupWindowTreeWidget_rightClick(self, event: PyQt5.QtGui.QMouseEvent): ...
    def setGroupNodes(self, groupNodes): ...

class _SeparatorLabel(PyQt5.QtWidgets.QLabel):
    def __init__(self, parent: Incomplete | None = ...) -> None: ...

def _GetNodePixmap(node: NodegraphAPI.Node) -> PyQt5.QtGui.QPixmap: ...
def _InitNodePixmaps(): ...