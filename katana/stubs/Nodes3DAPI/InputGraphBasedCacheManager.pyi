# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import CacheManager as CacheManager
import NodegraphAPI as NodegraphAPI
import Utils as Utils
import typing
from Nodes3DAPI.Node3D_geolib3 import _GetPushDependencies as _GetPushDependencies
from typing import Any, Set, Tuple

NodegraphEventTypes: dict
kNodePortChangeEventsKey: int
kParamChangedEventsKey: int
kPortConnectionEventsKey: int

class InputGraphBasedCacheManager:
    def __init__(self) -> None: ...
    def _InputGraphBasedCacheManager__on_node_delete(self, eventType, eventID, node: NodegraphAPI.Node, oldName): ...
    def _InputGraphBasedCacheManager__on_nodegraphChangedEvent(self, eventName, eventId, **kwargs): ...
    def _InputGraphBasedCacheManager__resolveInvalidations(self): ...
    def cacheValue(self, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, portIndex: int, value: object, getInputNodesFnc: typing.Callable): ...
    def clear(self): ...
    def discard(self, node: NodegraphAPI.Node): ...
    def getCachedValue(self, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState, portIndex: int) -> Any: ...

class _NodeRecord:
    def __init__(self) -> None: ...
    def getValue(self, graphState: NodegraphAPI.GraphState, portIndex): ...
    def invalidate(self): ...
    def invalidateCache(self): ...
    def setValue(self, graphState: NodegraphAPI.GraphState, portIndex, value): ...
