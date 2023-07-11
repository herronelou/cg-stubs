# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import QT4GLLayerStack.LayerStack as LayerStack
import QT4GLLayerStack.LayerStack
import QT4Widgets as QT4Widgets
import PyQt5.QtCore as QtCore
import PyQt5.QtGui as QtGui
import PyQt5.QtWidgets as QtWidgets
import QT4GLLayerStack.Util as Util
from _typeshed import Incomplete
from typing import Set, Tuple

ARRAY_TYPE_TO_CONSTANT: list
GL_VOID_P: object
GLvoid: None
_defaultAnimSeconds: float
ctypes_version: list
integer_types: tuple
void: None

class FrameAllLayer(QT4GLLayerStack.LayerStack.Layer):
    def __init__(self, *args, **kwargs): ...
    def _FrameAllLayer__start(self): ...
    def _FrameAllLayer__update(self, x): ...
    def frameAll(self, no_animation: bool = ..., viewBounds: Incomplete | None = ...): ...
    def isAlreadyFramed(self, viewBounds: Incomplete | None = ...): ...
    def paintGL(self): ...
    def processEvent(self, event): ...
    def setAnimSeconds(self, animSeconds): ...
    def setKeepAspectRatio(self, keepAspectRatio): ...
    def stop(self): ...
