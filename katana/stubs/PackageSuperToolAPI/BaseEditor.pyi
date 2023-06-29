# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PackageSuperToolAPI.NodeUtils as NU
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import Packages as Packages
import PyFnAttribute
import PyQt5.QtWidgets
import QT4FormWidgets as QT4FormWidgets
import QtCore as QtCore
import QtWidgets as QtWidgets
import UI4 as UI4
import PackageSuperToolAPI.UIDelegate as UIDelegate
import Utils as Utils
import typing
from BaseNode import BaseNode
from PyUtilModule.VirtualKatana import Decorators as Decorators, FormMaster as FormMaster, NodeMaster as NodeMaster, ScenegraphManager as ScenegraphManager
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar

LAYOUT_HORIZONTAL: int
LAYOUT_VERTICAL: int
SYNC_SELECTION_IN_OUT: float
SYNC_SELECTION_OFF: float
SYNC_SELECTION_OUT: float

class BaseEditor(PyQt5.QtWidgets.QWidget):
    class _PackageValidityStatus:
        NOT_IN_INPUT: ClassVar[int] = ...
        NO_SUCH_PACKAGE: ClassVar[int] = ...
        OK: ClassVar[int] = ...
        TYPE_MISMATCH: ClassVar[int] = ...
        @classmethod
        def textForStatusCode(cls, code): ...
    class _TabAreaState:
        EDIT: ClassVar[int] = ...
        ERROR: ClassVar[int] = ...
        INACTIVE: ClassVar[int] = ...
        __hash__: ClassVar[None] = ...
        def __init__(self, locationPath, statusCode): ...
        @classmethod
        def Edit(cls, locationPath): ...
        @classmethod
        def Error(cls, locationPath): ...
        @classmethod
        def Inactive(cls): ...
        def getLocationPath(self): ...
        def getStatusCode(self): ...
        def __eq__(self, rhs): ...
        def __ne__(self, rhs): ...
    class _TabAreaUpdate:
        USE_CURRENT_SELECTION: ClassVar[object] = ...
        def __init__(self, locationPath): ...
        @classmethod
        def Location(cls, locationPath): ...
        @classmethod
        def Selection(cls): ...
        def getLocationPath(self) -> USE_CURRENT_SELECTION | str | None: ...
    AddPackageRegistry: ClassVar[dict] = ...
    PackageMenuActionsRegistry: ClassVar[dict] = ...
    SEPARATOR: ClassVar[str] = ...
    TAB_AREA_UPDATE_INTERVAL: ClassVar[int] = ...
    _BaseEditor__HasRegisteredKeyboardShortcuts: ClassVar[bool] = ...
    def __init__(self, parent: QtWidgets.QWidget | None, node: NodegraphAPI.Node): ...
    def _BaseEditor__aboutToDragCallback(self, items, dragObject): ...
    def _BaseEditor__actionMenuAboutToShow(self): ...
    def _BaseEditor__addPackage(self): ...
    def _BaseEditor__adoptLocationsForEditing(self, locationPaths: list[str], locationAttributes: list[PyFnAttribute.GroupAttribute | PyFnAttribute.GroupAttribute]): ...
    def _BaseEditor__buildToolbar(self): ...
    def _BaseEditor__canAnySelectedPackageBeDeleted(self) -> bool: ...
    def _BaseEditor__canAnySelectedPackageBeDuplicated(self) -> bool: ...
    def _BaseEditor__configureSceneGraphView(self): ...
    def _BaseEditor__configureTabWidget(self): ...
    def _BaseEditor__contextMenuEventHandler(self, contextMenuEvent, menu): ...
    def _BaseEditor__createChildPackage(self, children: list[str], parentPackage: Package, packageClass: type): ...
    def _BaseEditor__deletePackage(self): ...
    def _BaseEditor__dispatchPackageMenuAction(self): ...
    def _BaseEditor__dragMoveEventCallback(self, dragMoveEvent, draggedItems, parentItem, childItemIndex): ...
    def _BaseEditor__dropEventCallback(self, dropEvent, droppedItems, parentItem, childItemIndex): ...
    def _BaseEditor__duplicatePackage(self): ...
    def _BaseEditor__freeze(self): ...
    def _BaseEditor__getAndValidatePackageForPath(self, locationPath: str) -> Tuple[Packages.Package, _PackageValidityStatus]: ...
    def _BaseEditor__getGlobalOrdering(self, items: list[QTreeWidgetItem]) -> list[QTreeWidgetItem]: ...
    def _BaseEditor__getIncomingChildCount(self, parent: QTreeWidgetItem | None) -> int: ...
    def _BaseEditor__getInternalViewPort(self): ...
    def _BaseEditor__hideTabsLabel(self): ...
    def _BaseEditor__iterTabs(self) -> typing.Iterator[str, QtWidgets.QWidget]: ...
    def _BaseEditor__locationAddedOrUpdatedCallback(self, locationPath, topLevelLocationPath): ...
    def _BaseEditor__mainNodeParameterFinalizedHandler(self, args): ...
    def _BaseEditor__nodeSetLockedChanged(self, *args): ...
    def _BaseEditor__on_cachedWidgetDestroyed(self, cache: dict, cacheKey: str): ...
    def _BaseEditor__on_scenegraphManager_pinChanged(self, eventType, eventID, locations, sender): ...
    def _BaseEditor__on_scenegraphManager_selectionChanged(self, *args): ...
    def _BaseEditor__on_tabAreaUpdateTimer_timeout(self): ...
    def _BaseEditor__overrideParameterRequestCallback(self, overrideParameters): ...
    def _BaseEditor__populateAddMenu(self, menu: QtWidgets.QMenu, package: Package): ...
    def _BaseEditor__populateStandardContextMenuItems(self, menu): ...
    def _BaseEditor__potentialPortViewChangeHandler(self, args): ...
    def _BaseEditor__registerDestructionCallback(self, widget: QtCore.QObject, cache: dict, cacheKey: str): ...
    def _BaseEditor__registerHandlers(self, state: bool): ...
    def _BaseEditor__reparentPackages(self, children, droppedItems, childItemIndex, incomingChildCount, parentPackage, parentItem): ...
    def _BaseEditor__restoreExpansionStateFor(self, locationPath, topLevelLocation): ...
    def _BaseEditor__restoreSelectionStateFor(self, locationPath, topLevelLocation): ...
    def _BaseEditor__restoreTopLevelLocations(self, children, currentRootLocation): ...
    def _BaseEditor__rootChildrenChangedCallback(self, locationPath, children): ...
    def _BaseEditor__rootLocationPolicyEvent(self, *args, **kwds): ...
    def _BaseEditor__saveCurrentSelectionAndExpansionState(self, oldRootLocation: str): ...
    def _BaseEditor__selectionChangedHandler(self, syncSelection: bool = ...): ...
    def _BaseEditor__syncSelectionEvent(self, args: list): ...
    def _BaseEditor__syncSelectionValueChanged(self, event): ...
    def _BaseEditor__tabAreaClearWidgets(self): ...
    def _BaseEditor__tabAreaHandleChangesForLocation(self, locationPath: str): ...
    def _BaseEditor__tabAreaHandleChangesForLocationSync(self, locationPath: str): ...
    def _BaseEditor__tabAreaRepaintWithWidgetsForPackage(self, package: Package): ...
    def _BaseEditor__tabAreaScheduleUpdate(self): ...
    def _BaseEditor__tabAreaSetEditedLocation(self, locationPath: str | None): ...
    def _BaseEditor__tabAreaSetEditedLocationFromSelection(self): ...
    def _BaseEditor__tabAreaSetEditedLocationFromSelectionSync(self): ...
    def _BaseEditor__tabAreaSetEditedLocationSync(self, locationPath: str | None): ...
    def _BaseEditor__tabAreaSetLabelText(self, message: Incomplete | None = ...): ...
    def _BaseEditor__terminalOpCallback(self, portOpClient, op, graphState, txn): ...
    def _BaseEditor__thaw(self): ...
    def _BaseEditor__updateColumnItemDelegates(self): ...
    def _BaseEditor__updateCurrentItem(self): ...
    def _BaseEditor__updatePort(self, port): ...
    def _BaseEditor__updateRootLocation(self, currentRoot): ...
    def _BaseEditor__updateSyncSelection(self, syncSelection): ...
    def _BaseEditor__updateTerminalOps(self, graphState: Incomplete | None = ..., txn: Incomplete | None = ...): ...
    def _executeCallbackWhenChildrenReady(self, parentLocationPath: str, callback: typing.Callable, errorMessage: Incomplete | None = ..., **kwargs): ...
    def addTab(self, tabName: str) -> QtWidgets.QWidget: ...
    def canSelectionBeExported(self) -> bool: ...
    def getAddPackageMenuActions(self) -> list[tuple[str, str, bool]]: ...
    def getAttribute(self, locationPath: str, attributeName: str) -> PyFnAttribute | None: ...
    def getChildrenUnder(self, parentPath): ...
    def getDefaultAddMenuGroupName(self) -> str: ...
    @classmethod
    def getDefaultSceneGraphViewTerminalOpUpdates(cls, graphState: NodegraphAPI.GraphState): ...
    @classmethod
    def getDefaultSceneGraphViewTerminalOps(cls, graphState: NodegraphAPI.GraphState): ...
    @classmethod
    def getKeyboardShortcuts(cls): ...
    @classmethod
    def getLayoutOrientation(cls) -> int: ...
    def getMainNode(self) -> BaseNode: ...
    def getMainPanelWidget(self) -> QtWidgets.QWidget: ...
    def getMenuActions(self) -> list[tuple[str, str, bool]]: ...
    def getPackageForPath(self, locationPath: str, includeEditPackages: bool = ..., createDummyOnMissing: bool = ...) -> Package | None: ...
    def getSceneGraphView(self) -> UI4.Widgets.SceneGraphView: ...
    @classmethod
    def getSceneGraphViewTerminalOpUpdates(cls, graphState: NodegraphAPI.GraphState, rootLocations: tuple[str, ...]) -> list[tuple[str, PyFnAttribute.GroupAttribute, str]]: ...
    @classmethod
    def getSceneGraphViewTerminalOps(cls, graphState: NodegraphAPI.GraphState, rootLocations: tuple[str, ...]) -> list[tuple[str, PyFnAttribute.GroupAttribute] | Tuple[str, PyFnAttribute.GroupAttribute, str]]: ...
    def getSelectedItems(self) -> list[str]: ...
    def getSelectedPackages(self, includeEditPackages: bool = ..., createDummyOnMissing: bool = ...) -> list[tuple]: ...
    @classmethod
    def getSuperToolName(cls) -> str: ...
    @classmethod
    def getTabNames(cls) -> list[str]: ...
    def getTabWidget(self) -> QtWidgets.QTabWidget: ...
    def getTopLevelPackage(self, package: Package) -> Package: ...
    def hideEvent(self, event): ...
    def onSelectionChanged(self): ...
    def populateContextMenu(self, menu: QtWidgets.QMenu): ...
    @classmethod
    def registerAddPackageKeyboardShortcut(cls, packageClass: type): ...
    @classmethod
    def registerKeyboardShortcuts(cls): ...
    @classmethod
    def registerPackageKeyboardShortcuts(cls, packageClass: type): ...
    def removeTab(self, tabName: str): ...
    def setColumnToUpdateOnStateChange(self, columnName): ...
    def setupSceneGraphViewColumns(self): ...
    def setupTabWidget(self): ...
    def showEvent(self, event): ...

class GafferThreeInteractionDelegate(UI4.NodeMaster.NodeInteractionDelegateManager.Delegate):
    def addToNodeSpecificShelfEnvironment(self, targetNode, editor, envDict): ...