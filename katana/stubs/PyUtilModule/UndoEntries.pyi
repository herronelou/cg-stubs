# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Utils.EventModule as EventModule
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Utils.UndoStack as UndoStack
import Utils as Utils
import Utils.UndoStack
from _typeshed import Incomplete
from typing import Set, Tuple

_parameter_changing_map: dict

class _FloatVectorStateAtTime:
    def __init__(self, parameter, time): ...

class node_addInputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, portName, portIndex): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_addOutputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, portName, portIndex): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_create_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, nodeType): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_delete_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, nodeParentName, xmlElement, locked): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_paste_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeNames, nodeParentName, xmlElement): ...
    def redo(self): ...
    def undo(self): ...

class node_removeInputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, portName, portIndex, portMetadata, portTags): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_removeOutputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, portName, portIndex, portMetadata, portTags): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_renameInputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldPortName, newPortName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_renameOutputPort_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldPortName, newPortName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setAutoRenameAllowed_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, value): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setBypassRouting_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldVal, newVal): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setBypassed_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, bypassValue): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setName_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, undoName, redoName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setParent_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, undoParentName, redoParentName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setPosition_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldPosition, newPosition): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setThumbnailEnabled_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, newValue, oldValue): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_setType_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldType, newType): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class node_shapeAttrsChanged_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, oldAttrs, newAttrs): ...
    def _node_shapeAttrsChanged_UndoEntry__setAttrs(self, attrs, otherAttrs): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_createChild_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, element, index): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_deleteChild_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, element, childName, index): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_floatVector_setValue_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, undoState, redoState): ...
    def _parameter_floatVector_setValue_UndoEntry__applyState(self, state): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_reorderChild_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, oldIndex, newIndex): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_reorderChildren_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, oldIndex, newIndex, count): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_reparentAtomic_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeName, paramName, newParamName, oldParentName, oldIndex, newParentName, newIndex): ...
    def doReparent(self, fromParentName, fromName, toParentName, toIndex, toName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_replaceXML_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, undoXML, redoXML): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_setName_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterParentFullName, undoName, redoName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class parameter_setValue_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, parameterFullName, undoXML, redoXML): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class port_connect_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeNameA: str, portNameA: str, nodeNameB: str, portNameB: str, portA: NodegraphAPI.Port, portB: NodegraphAPI.Port, oldSourceNode: str | None, oldSourcePort: str | None, portC: NodegraphAPI.Port | None): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class port_disconnect_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, nodeNameA, portNameA, nodeNameB, portNameB, portA, portB, isPortASendPort, isPortBReturnPort, nodeAShapeAttrs, nodeBShapeAttrs): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

class port_metadataUpdated_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, port, oldMetadata, newMetadata): ...
    def _port_metadataUpdated_UndoEntry__clearMetadata(self): ...
    def getName(self): ...
    def getNode(self): ...
    def getPort(self): ...
    def redo(self): ...
    def undo(self): ...

class port_setTags_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, port, newTags, oldTags): ...
    def getName(self): ...
    def getPort(self) -> NodegraphAPI.Port | None: ...
    def redo(self): ...
    def undo(self): ...

class roto_event_UndoEntry(Utils.UndoStack.UndoEntry):
    def __init__(self, rotoUE, nodeName): ...
    def getName(self): ...
    def redo(self): ...
    def undo(self): ...

def _Undo_Filter(eventType, eventID, **kwargs): ...
def __node_addInputPort_Undo(eventType, eventID, nodeName, portName, portIndex, **kwargs): ...
def __node_addOutputPort_Undo(eventType, eventID, nodeName, portName, portIndex, **kwargs): ...
def __node_beginRemoveInputPort_Undo(eventType, eventID, nodeName, portName, port, **kwargs): ...
def __node_create_Undo(eventType, eventID, node, nodeName, nodeType, **kwargs): ...
def __node_paste_Undo(eventType, eventID, nodeNames, nodeParentName, xmlElement, **kwargs): ...
def __node_removeInputPort_Undo(eventType, eventID, nodeName, portName, port, **kwargs): ...
def __node_removeOutputPort_Undo(eventType, eventID, nodeName, portName, port, **kwargs): ...
def __node_renameInputPort_Undo(eventType, eventID, nodeName, oldPortName, newPortName, **kwargs): ...
def __node_renameOutputPort_Undo(eventType, eventID, nodeName, oldPortName, newPortName, **kwargs): ...
def __node_setAutoRenameAllowed_Undo(eventType, eventID, node, nodeName, **kwargs): ...
def __node_setBypassRouting_Undo(eventType, eventID, node, nodeName, **kwargs): ...
def __node_setBypassed_Undo(eventType, eventID, node, nodeName, **kwargs): ...
def __node_setName_Undo(eventType, eventID, node, newName, oldName, **kwargs): ...
def __node_setParent_Undo(eventType, eventID, nodeName, oldParentName, newParentName, **kwargs): ...
def __node_setPosition_Undo(eventType, eventID, nodeName, oldPosition, newPosition, **kwargs): ...
def __node_setThumbnailEnabled_Undo(eventType, eventID, node, nodeName, thumbnailEnabled, oldThumbnailEnabled): ...
def __node_setType_Undo(eventType, eventID, node, nodeName, **kwargs): ...
def __node_shapeAttrsChanged_Undo(eventType, eventID, nodeName, oldAttrs, newAttrs, **kwargs): ...
def __parameter_createChild_Undo(eventType, eventID, param, paramName, childParam, element, index, **kwargs): ...
def __parameter_deleteChild_Undo(eventType, eventID, param, paramName, element, childName, index, **kwargs): ...
def __parameter_reorderChild_Undo(eventType, eventID, paramName, oldIndex, newIndex, **kwargs): ...
def __parameter_reorderChildren_Undo(eventType, eventID, paramName, oldIndex, newIndex, count, **kwargs): ...
def __parameter_reparentAtomic_Undo(eventType, eventID, param, paramName, newParamName, nodeName, oldParentName, oldIndex, newParentName, **kwargs): ...
def __parameter_replaceXML_Undo(eventType, eventID, param, oldXML, newXML, paramName, **kwargs): ...
def __parameter_setName_Undo(eventType, eventID, paramParentName, oldName, newName, **kwargs): ...
def __port_connect_Undo(eventType, eventID, portA, nodeNameA, portNameA, portB, nodeNameB, portNameB, **kwargs): ...
def __port_disconnect_Undo(eventType, eventID, portA, nodeNameA, portNameA, portB, nodeNameB, portNameB, isPortASendPort: bool = ..., isPortBReturnPort: bool = ..., nodeAShapeAttrs: Incomplete | None = ..., nodeBShapeAttrs: Incomplete | None = ..., **kwargs): ...
def __port_metadataUpdated_Undo(_eventType, _eventID, port, oldMetadata, newMetadata): ...
def __port_setTags_Undo(eventType, eventID, nodeName, port, portName, newTags, oldTags, **kwargs): ...
def __roto_event_Undo(eventType, eventID, rotoUE, nodeName, **kwargs): ...
