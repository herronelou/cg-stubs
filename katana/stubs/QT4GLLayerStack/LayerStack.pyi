# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyQt5.QtWidgets
import QT4Widgets as QT4Widgets
from _typeshed import Incomplete
from typing import ClassVar

EVENT_TYPES: dict

class Layer(PyQt5.QtCore.QObject):
    def __init__(self, name: Incomplete | None = ..., visible: bool = ..., interactive: bool = ..., enabled: bool = ...): ...
    def applyWindowSpace(self): ...
    def applyWindowSpaceWithDropShadow(self, *args): ...
    def applyWorldSpace(self): ...
    def applyWorldSpaceWithDropShadow(self, *args): ...
    def enabled(self) -> bool: ...
    def focused(self) -> bool: ...
    def getWindowSize(self): ...
    def initializeGL(self): ...
    def interactive(self) -> bool: ...
    def layerStack(self) -> LayerStack: ...
    def mapFromQTLocalToWindow(self, qtX, qtY): ...
    def mapFromQTLocalToWorld(self, qtX, qtY): ...
    def mapFromWindowToQTLocal(self, winX, winY): ...
    def mapFromWindowToWorld(self, winX, winY): ...
    def mapFromWorldToQTLocal(self, worldX, worldY): ...
    def mapFromWorldToWindow(self, worldX, worldY): ...
    def name(self) -> str | None: ...
    def paintGL(self): ...
    def paintGLLeft(self): ...
    def paintGLRight(self): ...
    def processEvent(self, e) -> bool: ...
    def resizeGL(self): ...
    def setEnabled(self, flag: bool): ...
    def setFocused(self, flag: bool): ...
    def setInteractive(self, interactive: bool): ...
    def setLayerStack(self, v: LayerStack): ...
    def setName(self, n: str): ...
    def setStereo(self, s): ...
    def setVisible(self, visible: bool): ...
    def startDrag(self): ...
    def stereo(self) -> bool: ...
    def update(self): ...
    def visible(self) -> bool: ...

class LayerStack(PyQt5.QtWidgets.QOpenGLWidget):
    SPACE_MODE_WINDOW: ClassVar[int] = ...
    SPACE_MODE_WORLD: ClassVar[int] = ...
    STEREO_MODE_ANAGLYPH: ClassVar[int] = ...
    STEREO_MODE_MONO: ClassVar[bool] = ...
    STEREO_MODE_QUAD: ClassVar[int] = ...
    layerStack_scaleChanged: ClassVar[PyQt5.QtCore.pyqtSignal] = ...
    def __init__(self, *args): ...
    def _LayerStack__delegateEvent(self, e): ...
    def _LayerStack__startDrag(self): ...
    def appendLayer(self, layer: Layer, stealFocus: bool = ...): ...
    def applyWindowSpace(self): ...
    def applyWindowSpaceWithDropShadow(self, screendx: float = ..., screendy: float = ...): ...
    def applyWorldSpace(self): ...
    def applyWorldSpaceWithDropShadow(self, screendx: float = ..., screendy: float = ...): ...
    def beginTextPainter(self): ...
    def contextMenuEvent(self, ev): ...
    def customEvent(self, event): ...
    def endTextPainter(self): ...
    def event(self, e): ...
    def firstPaintGL(self): ...
    def firstPaintGLLeft(self): ...
    def firstPaintGLRight(self): ...
    def focusLayer(self) -> Layer: ...
    def getClipPlanes(self) -> Tuple[float, float]: ...
    def getEyePoint(self): ...
    def getEyePointLeft(self): ...
    def getEyePointMain(self): ...
    def getEyePointRight(self): ...
    def getLayerByIndex(self, i: int) -> Layer: ...
    def getLayerByName(self, name: str) -> Layer: ...
    def getLayerCount(self) -> int: ...
    def getLayers(self) -> list[Layer]: ...
    def getMousePos(self) -> Tuple[int, int]: ...
    def getPseudoTopLevelWidget(self): ...
    def getTabletPressure(self): ...
    def getTabletTilt(self): ...
    def getViewScale(self) -> None: ...
    def getVisibleArea(self) -> Tuple[Tuple[float, float], Tuple[float, float]]: ...
    def getWindowSize(self) -> Tuple[int, int]: ...
    def getWorldBounds(self) -> Tuple[float, float, float, float] | None: ...
    def glDraw(self): ...
    def initializeGL(self): ...
    def insertLayer(self, layer: Layer, index: int): ...
    def isCapableOfNativeStereo(self): ...
    def isEraser(self): ...
    def isLayerFocused(self, layer): ...
    def mapFromQTLocalToWindow(self, qtX: float, qtY: float) -> Tuple[float, float]: ...
    def mapFromQTLocalToWorld(self, qtX: float, qtY: float) -> Tuple[float, float]: ...
    def mapFromWindowToQTLocal(self, winX: float, winY: float) -> Tuple[float, float]: ...
    def mapFromWindowToWorld(self, winX: float, winY: float) -> Tuple[float, float]: ...
    def mapFromWorldToQTLocal(self, worldX: float, worldY: float) -> Tuple[float, float]: ...
    def mapFromWorldToWindow(self, worldX: float, worldY: float) -> Tuple[float, float]: ...
    def paintGL(self): ...
    def removeLayer(self, layer: Layer): ...
    def renderText(self, *args): ...
    def reset(self): ...
    def resizeEvent(self, evt): ...
    def resizeGL(self, width, height): ...
    def setClipPlanes(self, nearClip: float, farClip: float): ...
    def setEyePoint(self, pt: None): ...
    def setEyePointLeft(self, pt): ...
    def setEyePointRight(self, pt): ...
    def setFocusLayer(self, layer: Layer, isFocused: bool = ...): ...
    def setStereoMode(self, stereoMode: int): ...
    def setTextColor(self, r, g, b, a: float = ...): ...
    def setViewLeft(self): ...
    def setViewMono(self): ...
    def setViewRight(self): ...
    def setViewScale(self, scale: None, final: bool = ...): ...
    def setVisibleArea(self, viewBounds): ...
    def stereoMode(self): ...
    def updateGL(self): ...

def ParititionMouseButtonState(buttons): ...