# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI as Nodes3DAPI
import Utils as Utils
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete

def GenerateXMLFile(**kwargs): ...
def GetAutoMkproxy(node): ...
def GetFarmSettings(node): ...
def GetNodeDeps(node: NodegraphAPI.Node, nodeInfo, parentPass: str | None, includeInternalDeps: bool = ..., ignoreBypassed: bool = ...): ...
def GetSortedDependencies(nodeList: Incomplete | None = ..., syncAllOutputPorts: bool = ..., includeInternalDeps: bool = ..., includeBypassed: bool = ...) -> list[dict]: ...
def GetSortedDependencyList(nodeList: Incomplete | None = ..., syncAllOutputPorts: bool = ..., includeInternalDeps: bool = ..., includeBypassed: bool = ...): ...
def GetVersionSync(node): ...
def WriteFarmFile(fileName, outlineString): ...
def __appendRenderableInternalNodes(nodeList): ...
def __getNode2Dor3D(node: NodegraphAPI.Node) -> str: ...
def __getNodeDeps(node: NodegraphAPI.Node, nodeInfo, parentPass: str | None, includeInternalDeps: bool, ignoreBypassed: bool, nodeVisitCache): ...
def __getNodeOutputFlag(node: NodegraphAPI.Node, includeInternalDeps: bool, ignoreBypassed: bool = ...) -> bool: ...
def __getNodePassName(node): ...
def __getNodeService(node): ...
def __getNodeViews(node): ...
def __getRenderNodeOutputs(node: NodegraphAPI.Node) -> list[dict]: ...