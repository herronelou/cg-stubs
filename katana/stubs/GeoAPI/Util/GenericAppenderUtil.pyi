# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import KatanaResources as KatanaResources
import NodegraphAPI as NodegraphAPI
import PyXmlIO
import Utils as Utils
import PyXmlIO as XmlIO
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete

GlobalAppenderDict: dict
GlobalAppenderList: list
__attrTypes: dict
g_nodeTypeCache: dict

def BuildAttrFromParsedEntry(element, refDict: Incomplete | None = ...): ...
def EscapeValue(v): ...
def GetGenericAppenderFileList(): ...
def GetGenericAppenderLocations(): ...
def InitGenericAppenders(path: Incomplete | None = ...): ...
def ParseArgsFile(filename): ...
def ParseArgsString(xmlString): ...
def RegisterAppenderNodeTypes(searchPath: Incomplete | None = ...): ...
def SearchForAppenders(searchPath): ...
def __CreateAppenderNodeCallback(nodeTypeName): ...
def __GetAppenderArgs(name): ...
def __GetExpandedHintsFromElement(element, refDict): ...
def __ParseContainerContents(rootElement, pagename: str = ..., containerPath: str = ..., containerHintDict: Incomplete | None = ..., refDict: Incomplete | None = ..., filepath: Incomplete | None = ...): ...
def __ParseOutputs(rootElement): ...
def __ParseRefDictElement(element, refDict, filepath): ...
def __ParseTags(element): ...
def __ProcessAttrType(e): ...
def __ProcessHintDict(e): ...
def __ProcessHintList(e): ...
def _buildArgsDictFromXmlElement(xmlElement: PyXmlIO.Element | None, filename: Incomplete | None = ...) -> dict: ...