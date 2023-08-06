# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import LookFileBakeAPI as LookFileBakeAPI
import Nodes3DAPI.LookFileBaking as LookFileBaking
import NodegraphAPI as NodegraphAPI
import Utils as Utils
import typing
from LookFileBakeAPI.Constants import OutputFormat as OutputFormat
from LookFileBakeAPI.Exceptions import LookFileBakeException as LookFileBakeException
from Nodes3DAPI.Node3D import Node3D as Node3D
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import Set, Tuple

class LookFileBake(Node3D):
    def __init__(self) -> None: ...
    def AddPassInput(self, passName: str): ...
    def CheckRootLocations(self, rootLocations, origProducer, asmbCmptDict: Incomplete | None = ...): ...
    def DeletePassInput(self, index: int): ...
    def PostLookFileBake(self, assetId, asmbCmptDict, progressCallback: typing.Optional[typing.Callable] = ..., abortCallback: typing.Optional[typing.Callable] = ...): ...
    def PreLookFileBake(self, assetId, asmbCmptDict, progressCallback: typing.Optional[typing.Callable] = ..., abortCallback: typing.Optional[typing.Callable] = ...): ...
    def RenamePassInput(self, index: int, newName: str): ...
    def ReorderInput(self, index: int, newIndex: int): ...
    def WriteLookFileBakeScriptFiles(self, sessionPath: str, graphState: NodegraphAPI.GraphState, versionup: bool, publish: bool): ...
    def WriteLookFileToDirectory(self, outputFormatName, graphState: NodegraphAPI.GraphState, dirPath, includeGlobalAttributes: bool = ..., includeLodInfo: bool = ..., progressCallback: typing.Optional[typing.Callable] = ..., passName: Incomplete | None = ...): ...
    def WriteToAsset(self, graphState: NodegraphAPI.GraphState, assetId, args: Incomplete | None = ..., progressCallback: typing.Optional[typing.Callable] = ...): ...
    def WriteToCompoundFile(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], dirPath: str, includeGlobalAttributes: bool = ..., includeLodInfo: bool = ..., progressCallback: typing.Optional[typing.Callable] = ..., passName: Incomplete | None = ...) -> list[str]: ...
    def WriteToDirectory(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], dirPath: str, includeGlobalAttributes: bool = ..., includeLodInfo: bool = ..., progressCallback: typing.Optional[typing.Callable] = ..., passName: Incomplete | None = ...) -> list[str]: ...
    def WriteToLookFile(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], filePath: str, includeGlobalAttributes: bool = ..., includeLodInfo: bool = ..., progressCallback: typing.Optional[typing.Callable] = ..., passName: Incomplete | None = ...): ...
    def _LookFileBake__getBakerOps(self, passInputPortNames, graphState: NodegraphAPI.GraphState): ...
    def _LookFileBake__getIncludeGlobalAttributes(self, frameTime): ...
    def _LookFileBake__getIncludeLodInfo(self, frameTime): ...
    def _LookFileBake__getMaterialTreeRootLocations(self, frameTime): ...
    def _LookFileBake__getOutputFormatName(self, frameTime): ...
    def _LookFileBake__getRootLocations(self, frameTime): ...
    @staticmethod
    def _LookFileBake__getSourceFile(): ...
    def _getOpChain(self, interface): ...
    def _getPassInputPortNames(self): ...
    def _getPassInputPorts(self): ...
    def _getReferenceInputPort(self): ...
    def _getReferenceInputPortName(self): ...
    def addParameterHints(self, attrName, inputDict): ...
    def getOrigProducer(self, graphState: NodegraphAPI.GraphState, portName: Incomplete | None = ..., addCELMatchOp: bool = ...): ...
    def getReferenceProducer(self, graphState: NodegraphAPI.GraphState): ...
