# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import UI4.Tabs.DopeSheet.DopeSheetTree as DopeSheetTree
import NodegraphAPI as NodegraphAPI
import UI4.KatanaPrefs.PrefNames as PrefNames
import PyQt5.QtCore
import QT4GLLayerStack as QT4GLLayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import UI4 as UI4
import UI4.Util.Events
import Utils as Utils
from PyUtilModule.VirtualKatana import ParameterKeyMimeData as ParameterKeyMimeData
from UI4.KatanaPrefs.KatanaPrefsObject import KatanaPrefs as KatanaPrefs
from UI4.Util.Events import EventProcessor as EventProcessor, EventProcessorHandler as EventProcessorHandler, LayerWorldDragEventProcessor as LayerWorldDragEventProcessor
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class BandSelectionEventProcessor(UI4.Util.Events.LayerWorldDragEventProcessor):
    def __init__(self, layerStack) -> None: ...
    def _BandSelectionEventProcessor__scrollLayerStack(self, dx, dy): ...
    def _BandSelectionEventProcessor__updateSelection(self, modifiers): ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...
    def finish(self, cancelled: bool = ...): ...

class BandSelectionLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs) -> None: ...
    def _BandSelectionLayer__updateRect(self): ...
    def getEnd(self): ...
    def getRectangle(self): ...
    def getStart(self): ...
    def paintGL(self): ...
    def setEnd(self, x1, y1): ...
    def setStart(self, x0, y0): ...

class CurrentTimeEventProcessor(UI4.Util.Events.LayerWorldDragEventProcessor):
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...
    def finish(self, cancelled: bool = ...): ...

class KeyInteractionLayer(QT4GLLayerStack.LayerStack.Layer, UI4.Util.Events.EventProcessorHandler):
    def __init__(self, treeWidget, *args, **kwargs) -> None: ...
    def _KeyInteractionLayer__copySelectedKeys(self): ...
    def _KeyInteractionLayer__deleteSelectedKeys(self): ...
    def _KeyInteractionLayer__getSelection(self, rootItem: Incomplete | None = ..., paramRoot: Incomplete | None = ...): ...
    def _KeyInteractionLayer__getSelectionHierarchy(self): ...
    def _KeyInteractionLayer__getSelectionHierarchyR(self, rootItem, paramRoot): ...
    def _KeyInteractionLayer__getToolTipText(self, layerStack, event): ...
    def _KeyInteractionLayer__pasteKeys(self): ...
    def _KeyInteractionLayer__setKey(self): ...
    def _KeyInteractionLayer__setKeyOnAll(self): ...
    def _KeyInteractionLayer__setKeyR(self, entry, t, paramRoot): ...
    def _KeyInteractionLayer__toggleToolTips(self): ...
    def _KeyInteractionLayer__updateActions(self, layerStack): ...
    def _KeyInteractionLayer__updateGhostTime(self, layerStack, pos: Incomplete | None = ..., updateGL: bool = ...): ...
    def _processEvent(self, event): ...
    def _processEventUnconditional(self, event): ...
    def buildContextMenu(self, menu, contextMenuEvent): ...
    def contextMenuFinished(self): ...
    def processEvent(self, event): ...
    def setLayerStack(self, *args): ...

class KeyMoveEventProcessor(UI4.Util.Events.LayerWorldDragEventProcessor):
    _KeyMoveEventProcessor__COPY_KEY: ClassVar[PyQt5.QtCore.Qt.Key] = ...
    _KeyMoveEventProcessor__COPY_MODIFIER: ClassVar[PyQt5.QtCore.Qt.KeyboardModifier] = ...
    _KeyMoveEventProcessor__OVERWRITE_KEY: ClassVar[PyQt5.QtCore.Qt.Key] = ...
    _KeyMoveEventProcessor__OVERWRITE_MODIFIER: ClassVar[PyQt5.QtCore.Qt.KeyboardModifier] = ...
    def __init__(self, layerStack, treeWidget) -> None: ...
    def _KeyMoveEventProcessor__checkAllowed(self): ...
    def _KeyMoveEventProcessor__scrollLayerStack(self, dx, dy): ...
    def _KeyMoveEventProcessor__showCopyCursor(self, showAsCopy): ...
    def _KeyMoveEventProcessor__showMove(self): ...
    def _update(self, worldStart, worldEnd, modifiers, initial: bool = ..., endChanged: bool = ..., modifiersChanged: bool = ..., final: bool = ...): ...
    def finish(self, cancelled: bool = ...): ...

class PasteTarget:
    def __init__(self, treeWidget) -> None: ...
    def _PasteTarget__getMimeData(self): ...
    def _PasteTarget__getParametersFromEntry(self, entry): ...
    def _PasteTarget__getTargetParameters(self, mimeData): ...
    def _PasteTarget__unwrapPotentials(self, potentialsHierarchy): ...
    def clear(self): ...
    def getPasteDescription(self): ...
    def getPotentials(self): ...
    def getTargetEntry(self): ...
    def getTargetRootEntry(self): ...
    def getTargetTime(self): ...
    def isTargetTimeSet(self): ...
    def isValid(self): ...
    def paste(self): ...
    def setTargetEntry(self, entry): ...
    def setTargetTime(self, time): ...