# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import FnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import PyFnGeolibServices as FnGeolibServices
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI_cmodule as Nodes3DAPI_cmodule
import Utils as Utils
import collections
from Nodes3DAPI.Node3D import Node3D as Node3D
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

_ExtraHints: dict
_Parameter_XML: str

class GenericAssign(Node3D):
    _GenericAssign__AttrTypeClasses: ClassVar[dict] = ...
    _HintTrueValues: ClassVar[list] = ...
    __pychecker__: ClassVar[str] = ...
    def __init__(self): ...
    def EscapeValue(self, value): ...
    def HintTrue(self, hintName: str, hints: dict, default: bool = ...) -> bool: ...
    def _GenericAssign__applyOverridesToInput(self, inputProducer, port, sourceTime, frameTime, applyLocalSettings: bool = ..., varNameSuffix: Incomplete | None = ...): ...
    def _decodeHints(self, text: str) -> dict: ...
    def _encodeHints(self, hints: collections.OrderedDict | dict) -> str: ...
    def _filterAttrList(self, graphState, attrList): ...
    def _getAttrRootForIncomingSceneQuery(self): ...
    def _getIncomingSceneOpAndLocation(self, port, graphState, transaction): ...
    def _getOpChain(self, interface): ...
    def _getStaticAttrHintsForIncomingSceneQuery(self, attrPath): ...
    def _getStaticDefaultAttrForIncomingSceneQuery(self, attrPath): ...
    def _processGroup(self, attrlist, currentpath): ...
    def addParameterHints(self, attrName, inputDict): ...
    def canOverride(self, attrName): ...
    def findOverrideParameter(self, path, attrName, time, index: Incomplete | None = ..., editable: bool = ...): ...
    def getArgsParamRoot(self): ...
    def getFixedCELStatement(self): ...
    def setOverride(self, path, attrName, time, attrData, index: Incomplete | None = ..., *args, **kwargs): ...
    def updateArgsParameterDict(self, argsinfo, changeNode: bool = ...): ...
    def updateArgsParameterFile(self, filename: str): ...

def GetArgsFileDict(filename: str) -> collections.OrderedDict: ...
def GetArgsFileXML(filename: str) -> str: ...
def __ConvertArgsAttributeToObject(attribute: FnAttribute | None, isDefaultAttribute: bool = ...) -> collections.OrderedDict | int | float | str | list | FnAttribute.DataAttribute: ...
def __ConvertOrderedDictToContainerHints(pageName: str, containerHints: dict, childContainerHints: collections.OrderedDict): ...
def __ConvertParamsToAttrsAndContainerHints(params: dict, containerHints: dict) -> list[None]: ...
