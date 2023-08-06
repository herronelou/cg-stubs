# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import NodegraphAPI_cmodule as NodegraphAPI_cmodule
import PyXmlIO as PyXmlIO
import Utils as Utils
import NodegraphAPI.Xio as Xio
from typing import Set, Tuple

class UserParameterError(RuntimeError): ...

def CreateButton(node: NodegraphAPI.Node, name, text: str = ..., script: str = ...): ...
def CreateColor(node: NodegraphAPI.Node, name): ...
def CreateGroup(node: NodegraphAPI.Node, name): ...
def CreateNumber(node: NodegraphAPI.Node, name): ...
def CreateNumberArray(node: NodegraphAPI.Node, name): ...
def CreateString(node: NodegraphAPI.Node, name): ...
def CreateStringArray(node: NodegraphAPI.Node, name): ...
def Delete(node: NodegraphAPI.Node, name): ...
def DeleteLiveUserParameter(node: NodegraphAPI.Node): ...
def DeleteUserParameter(node: NodegraphAPI.Node): ...
def ExecuteButton(node: NodegraphAPI.Node, name): ...
def GetLiveUserParameter(node: NodegraphAPI.Node, createIfMissing: bool = ...): ...
def GetUserParameter(node: NodegraphAPI.Node): ...
