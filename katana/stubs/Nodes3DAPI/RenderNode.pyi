# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import Nodes3DAPI.Node3D as Node3D
import NodegraphAPI as NodegraphAPI
import Nodes2DAPI as Nodes2DAPI
import Nodes3DAPI.RenderNodeUtil as RenderNodeUtil
import Nodes3DAPI.Rendering as Rendering
import RenderingAPI as RenderingAPI
import Nodes3DAPI.RenderingUtil as RenderingUtil
import Utils as Utils
from typing import Set, Tuple

class MergeOutputs:
    def __init__(self) -> None: ...

class RenderNode:
    def __init__(self, node: NodegraphAPI.Node, graphState: NodegraphAPI.GraphState) -> None: ...
    def _RenderNode__addRenderOutputEnabledStatesToRecipe(self, txn, op, enabledOutputNames): ...
    def _RenderNode__addRenderTargetLocationsToRecipe(self, txn, op, renderTargetLocations, finalRenderTargetLocations): ...
    def _RenderNode__addTempFileInformationToRecipe(self, txn, op): ...
    def _RenderNode__buildCommandLines(self): ...
    def _RenderNode__getAttrValueOrEmptyString(self, attr): ...
    def _RenderNode__processMergeOutputs(self, outputName, outputInfo, client, mergedOutputs): ...
    def _RenderNode__processOutputs(self, client, op): ...
    def _RenderNode__processPreScriptOutput(self, outputInfo): ...
    def _RenderNode__processScriptOutput(self, outputInfo): ...
    def finalizeSetup(self, rect): ...
    def getCacheID(self): ...
    def getCleanupFiles(self): ...
    def getCommandLines(self): ...
    def getConvertFiles(self): ...
    def getCopyFiles(self): ...
    def getDataWindow(self): ...
    def getDisplayWindow(self): ...
    def getImageFiles(self): ...
    def getPackageString(self): ...
    def getPostCommands(self): ...
    def getPreCommands(self): ...
    def getRenderFinishedFilename(self): ...
    def getRendererString(self): ...
    def loadOutputsInMonitor(self): ...
