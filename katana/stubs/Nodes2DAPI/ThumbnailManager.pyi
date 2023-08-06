# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI as NodegraphAPI
import Nodes2DAPI_cmodule as Nodes2DAPI_cmodule
import Utils as Utils
from typing import Set, Tuple

THUMBNAIL_UPDATE_CONTINUOUS: int
THUMBNAIL_UPDATE_NEVER: int
THUMBNAIL_UPDATE_ONCE: int

def GetThumbnailMode(): ...
def RegenerateAllThumbnails(): ...
def RenderThumbnail(node: NodegraphAPI.Node, priorCacheID: str = ..., size: tuple = ...): ...
def SetThumbnailMode(mode): ...
def SetThumbnailSampleRate(sampleRate): ...
