# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Nodes3DAPI.DynamicParameterUtil as DynamicParameterUtil
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import Utils as Utils
from Nodes3DAPI.Node3D import Node3D as Node3D
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class NetworkMaterialParameterEdit(Node3D):
    _NetworkMaterialParameterEdit__staticHints: ClassVar[dict] = ...
    def __init__(self) -> None: ...
    def _NetworkMaterialParameterEdit___checkDynamicParametersInternal(self, universalAttr: Incomplete | None = ..., forceUpdate: bool = ...): ...
    def _getIncomingSceneOpAndLocation(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath): ...
    def _updateParameters(self, groupAttr, force: bool = ..., defaultAttr: Incomplete | None = ...): ...
    def addParameterHints(self, attrName, inputDict): ...
    def checkDynamicParameters(self, *args, **kwds): ...
    def getScenegraphLocation(self, sourceTime: int = ...): ...
