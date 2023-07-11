# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import NodegraphAPI_cmodule
from _typeshed import Incomplete

_DefaultShapeAttrs: tuple
_ExtraHints: dict
_Parameter_XML: str

class GroupMergeNode(NodegraphAPI_cmodule.PythonGroupNode):
    def __init__(self): ...
    def _GroupMergeNode__buildMergeNode(self): ...
    def _GroupMergeNode__getMergeNode(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def allowChildReparentingViaDrag(self, childNode): ...
    def buildChildNode(self, adoptNode: Incomplete | None = ...): ...
    def canAdoptNodes(self, nodes): ...
    def deleteChildNode(self, childNode): ...
    def getChildNodeType(self): ...
    def getChildNodes(self): ...
    def getDefaultNodeShapeAttrs(self): ...
    def getDisplayNameExpression(self): ...
    def getDisplayNameForChildNode(self, childNode): ...
    def getInfoString(self): ...
    def positionChildNodes(self): ...
    def preprocessChildReparentingViaDrag(self, childNode): ...
    def reorderChildNode(self, fromIndex, toIndex): ...
    def setChildNodeType(self, nodeType): ...
    def setDisplayNameExpression(self, exprText): ...