# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI_cmodule as NodegraphAPI_cmodule
import PyXmlIO as PyXmlIO
import Utils as Utils
import NodegraphAPI.Xio as Xio
from typing import Set, Tuple

class UserParameterError(RuntimeError): ...

def CreateButton(node, name, text: str = ..., script: str = ...): ...
def CreateColor(node, name): ...
def CreateGroup(node, name): ...
def CreateNumber(node, name): ...
def CreateNumberArray(node, name): ...
def CreateString(node, name): ...
def CreateStringArray(node, name): ...
def Delete(node, name): ...
def DeleteLiveUserParameter(node): ...
def DeleteUserParameter(node): ...
def EnableUserEditor(node, state): ...
def ExecuteButton(node, name): ...
def GetLiveUserParameter(node, createIfMissing: bool = ...): ...
def GetUserParameter(node): ...
def _BuildUserPath(node, path): ...
def _CheckForExistingParamParent(node, paramName): ...
def _CheckNode(node): ...
def _PrecreateCheck(node, paramName): ...
