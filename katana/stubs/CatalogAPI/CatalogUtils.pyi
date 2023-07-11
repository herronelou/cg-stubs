# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import AssetAPI as AssetAPI
import ConfigurationAPI_cmodule as Configuration
import NodegraphAPI as NodegraphAPI
import PyUtilModule as PyUtilModule
import PyResolutionTableFn as ResolutionTable
from _typeshed import Incomplete

def ExportCatalogToDisk(items, filePath, imageFormat, imageOptions): ...
def GetCommonResolutionNameFromItems(items): ...
def GetFirstFrame(resolvedLocation): ...
def GetMemoryUsageMB(): ...
def GetNearestTimeInSequence(sequence, time): ...
def GetSequenceCreationTime(resolvedLocation): ...
def GetSequenceObj(resolvedLocation: str) -> FileSequence | None: ...
def GetUniqueImageNumberInDirectory(directory): ...
def ImportImageSequence(assetId, nodeName: str = ..., setPersistant: bool = ..., sampleRate: Incomplete | None = ...): ...
def IsPersistantCatalogAllowed(): ...
def ValidatePersistantDirectory(onlyTestExistance: bool = ...): ...