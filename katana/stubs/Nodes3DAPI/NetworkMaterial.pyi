# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConditionalStateGrammar as ConditionalStateGrammar
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import RenderingAPI as RenderingAPI
from ConditionalStateGrammar.Parser import ParseCSG as ParseCSG
from Nodes3DAPI.CreateUtil import BuildChild as BuildChild
from Nodes3DAPI.InputGraphBasedCacheManager import InputGraphBasedCacheManager as InputGraphBasedCacheManager
from Nodes3DAPI.Node3D import Node3D as Node3D
from Nodes3DAPI.ShadingNodeUtil import GetConnectionNames as GetConnectionNames, ReportError as ReportError
from _typeshed import Incomplete
from typing import ClassVar

_ExtraHints: dict
_Parameter_XML: str

class NetworkMaterialNode(Node3D):
    inputsCacheManager: ClassVar[InputGraphBasedCacheManager] = ...
    kNodeGraphViewLayoutVersion: ClassVar[int] = ...
    def __init__(self): ...
    def _NetworkMaterialNode__buildLayoutAttrsOpArgsIfRequired(self, argsBuilder): ...
    def _NetworkMaterialNode__buildOpArgs(self, graphState, inputNames): ...
    def _NetworkMaterialNode__checkStructuredPortConnection(self, sPort, graphState, connectionsAttr, nodeDict, interfaceDict, interfaceOrder, visitedNodes): ...
    def _NetworkMaterialNode__getAllShadingConnectionNodes(self, node: NodegraphAPI.Node) -> list[NodegraphAPI.Node]: ...
    def _addArrayConnectionOverrides(self, node, frameTime, nodeDict, visitedNodes): ...
    def _addNodeOverrides(self, node, graphState, nodeDict, interfaceDict, interfaceOrder, visitedNodes, error: Incomplete | None = ...): ...
    def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
    def _getOp(self, port, graphState, visitedState, transaction): ...
    def addParameterHints(self, attrName, inputDict): ...
    def addShaderInputPort(self, rendererName: str, shaderType: str) -> NodegraphAPI.Port: ...
    def generateShaderInputPortName(self, rendererName: str, shaderType: str) -> str: ...
    def getScenegraphLocation(self, frameTime: Incomplete | None = ...) -> str | None: ...
    def invalidateLayout(self): ...
    def isResetPossible(self): ...
    def validateConnection(self, otherOutPort, myInPort, errorMessages: Incomplete | None = ...): ...