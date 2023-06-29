# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import ConfigurationAPI_cmodule as Configuration
import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import LookFileBakeAPI as LookFileBakeAPI
import LookFileBakeAPI.LookFileUtil as LookFileUtil
import NodegraphAPI as NodegraphAPI
from LookFileBakeAPI.Constants import OutputFormat as OutputFormat
from LookFileBakeAPI.Exceptions import LookFileBakeException as LookFileBakeException
from Nodes3DAPI.Node3D import Node3D as Node3D
from _typeshed import Incomplete

_ExtraHints: dict
_Parameter_XML: str

class LookFileMaterialsOut(Node3D):
    def __init__(self): ...
    def WriteLookFileToDirectory(self, outputFormatName: str, graphState: Tuple[NodegraphAPI.GraphState, float | None], outputPath: str, progressCallback: Incomplete | None = ...) -> list[str]: ...
    def WriteToAsset(self, graphState, assetId, args: Incomplete | None = ..., progressCallback: Incomplete | None = ...): ...
    def WriteToCompoundFile(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], filePath: str, progressCallback: Incomplete | None = ...): ...
    def WriteToDirectory(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], dirPath: str, progressCallback: Incomplete | None = ...) -> list[str]: ...
    def WriteToLookFile(self, graphState: Tuple[NodegraphAPI.GraphState, float | None], outputPath: str, *args, **kw) -> list[str]: ...
    def _LookFileMaterialsOut__getProducer(self, graphState: Incomplete | None = ...): ...
    def _getOpChain(self, interface): ...
    def addParameterHints(self, attrName, inputDict): ...
    def test(self): ...