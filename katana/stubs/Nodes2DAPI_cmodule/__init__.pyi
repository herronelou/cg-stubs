# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI_cmodule
import PyFnAttribute
import PyXmlIO
import Nodes2DAPI_cmodule.Views as Views
import types
import typing
from typing import Any, overload

RENDER_TYPE_IDLE: int
RENDER_TYPE_PRIMARY: int
TILE_PRIORITIZER_NONE: int
TILE_PRIORITIZER_SCANLINE: int
TILE_PRIORITIZER_SPIRAL: int
__cleanup: PyCapsule

class FrameBuffer:
    def __init__(self, filename: str, sampleRateX: float, sampleRateY: float, nodeName: str, renderTime: float, isRender3D: bool) -> None: ...
    def copyImageData(self, data: Any, rect: list[tuple[int, int, int, int]], rowBytes: int, numChannels: int) -> None: ...
    def dirtyBufferRects(self, updateRects: typing.Sequence, texturePool: dict) -> bool: ...
    def duplicate(self) -> FrameBuffer: ...
    def getBackgroundColor(self) -> tuple: ...
    def getBackgroundRegion(self) -> list: ...
    def getChannels(self) -> str: ...
    def getDataRegion(self) -> list: ...
    def getDataRegionOutline(self) -> list[Tuple[int, int, int, int]]: ...
    def getDataWindow(self) -> tuple: ...
    def getDisplayWindow(self) -> tuple: ...
    def getFrameTime(self) -> float: ...
    def getNativeDataWindow(self) -> tuple: ...
    def getNodeName(self) -> str: ...
    def getSampleRate(self) -> tuple: ...
    def getSequenceID(self) -> int: ...
    def getSize(self) -> int: ...
    def getThumbnailData(self, width: int = ..., forceRegenerate: bool = ...) -> bytes: ...
    def getThumbnailHeight(self) -> int: ...
    def getThumbnailWidth(self) -> int: ...
    def getTiles(self, clipWindow: list[tuple[int, int, int, int]], adjustClipWindowForProxyScale: bool = ...) -> list: ...
    def getView(self) -> str: ...
    def glTexSubImage2D(self, target: int, level: int, xoffset: int, yoffset: int, width: int, height: int) -> None: ...
    def isFirstInConnection(self) -> bool: ...
    def isRender3D(self) -> bool: ...
    def queryHistogram(self, rect: list[tuple[int, int, int, int]], binMin: list[tuple[float, float, float, float]], binMax: list[tuple[float, float, float, float]], size: int, colorspace: str) -> dict: ...
    def queryRegionStats(self, rect: list[tuple[int, int, int, int]], ignoreNanInfValues: bool = ..., minInfValue: Any = ..., maxInfValue: Any = ...) -> dict: ...
    def queryScanline(self, scanline: int, isHorizontal: bool, colorspace: str = ..., lutForward: int = ...) -> dict: ...
    def setSequenceID(self, id: int) -> None: ...
    def setView(self, view: str) -> None: ...
    def writeToDisk(self, filename: str, args: dict, width: int, height: int, writeID: bool) -> None: ...
    def __hash__(self) -> int: ...

class IntImage:
    def __init__(self) -> None: ...
    def channels(self) -> int: ...
    def height(self) -> int: ...
    def imageData(self) -> Any: ...
    def width(self) -> int: ...
    def __hash__(self) -> int: ...

class Node2D(NodegraphAPI_cmodule.Node):
    def __init__(self) -> None: ...

def CancelRender(renderType: int, stallOnCompletion: bool) -> None: ...
def CheckExternalRender() -> None: ...
def CheckFileIns(nodeNames: list[str], renderTime: float) -> list: ...
def ClearDisplayWindowCache() -> None: ...
def ClearImageHeaderCache() -> None: ...
def ClearSpeculativeCacheContents() -> None: ...
def ConvertUpdateRectsToFnAttribute(arg0: list[list[tuple[int, int, int, int]]]) -> PyFnAttribute.IntAttribute: ...
def CreateExternalRenderListener(port: int) -> None: ...
def EnumerateReadableImageFormats() -> list: ...
def EnumerateWriteableImageFormats() -> list: ...
def FinishRender(arg0) -> None: ...
def GetAllRenderTypes() -> tuple: ...
@overload
def GetDisplayWindow(port: NodegraphAPI_cmodule.Port, graphState: NodegraphAPI_cmodule.GraphState) -> tuple: ...
@overload
def GetDisplayWindow(port: NodegraphAPI_cmodule.Port, time: float) -> tuple: ...
def GetErrorMessages() -> tuple: ...
def GetExternalRenderListenerInfo() -> Any: ...
def GetFileOutAssetId(node: Node2D, inputIndex: int, graphState: NodegraphAPI_cmodule.GraphState, includeRep: bool) -> str: ...
def GetFileOutColorspace(node: Node2D, inputIndex: int) -> str: ...
def GetFileOutEnabled(node: Node2D, inputIndex: int) -> bool: ...
def GetFileOutFilename(node: Node2D, inputIndex: int, graphState: NodegraphAPI_cmodule.GraphState, resolveFrame: bool = ...) -> str: ...
def GetFileOutFormat(node: Node2D, inputIndex: int) -> str: ...
def GetFileOutOutputParams() -> str: ...
def GetFileOutPassName(node: Node2D, graphState: NodegraphAPI_cmodule.GraphState) -> str: ...
def GetFileOutPostScriptInfo(node: Node2D, scriptIndex: int, graphState: NodegraphAPI_cmodule.GraphState) -> dict: ...
def GetFileOutPostScriptParams() -> str: ...
def GetFileOutProxyOnCue(node: Node2D, inputIndex: int) -> bool: ...
def GetFileOutRepPrefix(node: Node2D, inputIndex: int) -> str: ...
def GetFileOutRepresentation(node: Node2D, inputIndex: int, graphState: NodegraphAPI_cmodule.GraphState, includeExtension: bool) -> str: ...
def GetFileOutResolutionName(node: Node2D, inputIndex: int, graphState: NodegraphAPI_cmodule.GraphState) -> str: ...
def GetFilmWidthFromString(filmBack: str) -> float: ...
def GetFrameBufferCancelledMessages() -> tuple: ...
def GetFrameBufferCompletedMessages() -> tuple: ...
def GetFrameBufferRectUpdateMessages() -> dict: ...
def GetImageDescription(filename: str) -> dict: ...
def GetImageDiskUsage() -> int: ...
def GetImageMemoryUsage() -> int: ...
def GetImageReadPath(node: Node2D, renderTime: float) -> str: ...
def GetIncrementedRenderSequenceID() -> int: ...
def GetMaxDiskUsage() -> int: ...
def GetMaxImageMemory() -> int: ...
def GetNewFrameBuffers() -> list: ...
@overload
def GetOutputDisplayWindow(port: NodegraphAPI_cmodule.Port, graphState: NodegraphAPI_cmodule.GraphState) -> tuple: ...
@overload
def GetOutputDisplayWindow(port: NodegraphAPI_cmodule.Port, time: float) -> tuple: ...
def GetRenderMessages() -> list: ...
def GetRenderProgressMessages() -> list: ...
def GetRenderTerminationSignal(rendererName: str) -> int: ...
def GetRenderThreads() -> int: ...
def GetSpeculativeCacheContents() -> PyXmlIO.Element: ...
def GetSpeculativeCacheEnabled() -> bool: ...
def GetTileRenderOrderMessages() -> dict: ...
def GetTileSize() -> tuple: ...
def GetTransformBetweenNodes(src: NodegraphAPI_cmodule.Node, dst: NodegraphAPI_cmodule.Node, time: float) -> tuple: ...
def GetTransformForInputPort(inputPort: NodegraphAPI_cmodule.Port, time: float) -> tuple: ...
def IsExternalRenderInProgress(sequenceID: int) -> bool: ...
def IsRenderInProgress() -> bool: ...
def IsThumbnailRendering() -> bool: ...
def KillExternalRender(sequenceID: int, waitOnCompletion: bool) -> None: ...
def NotifyBufferChanged(buffer: FrameBuffer) -> None: ...
def PrintImageMemoryUsage() -> None: ...
def QueueErrorMessage(sequenceID: int, errorCode: int, nodeName: str, message: str) -> None: ...
def QueueRenderMessage(sequenceID: int, message: str) -> None: ...
def ReadImage(filename: str, scale: float) -> Any: ...
def ReadImageThreaded(filename: str, mipSizeX: int, mipSizeY: int, callback: typing.Callable = ..., tileLocation: Any = ...) -> bool: ...
def RegisterNukeSession(serviceHost: str, servicePort: int, catalogRegistryHost: str, catalogRegistryPort: int, mainSequenceID: int, previewComp: bool, mappings: list[Tuple[str, int, str, int, FrameBuffer]]) -> None: ...
def Render(ports: list[NodegraphAPI_cmodule.Port], buffers: list[FrameBuffer], rois: list[typing.Sequence], names: list[str], renderTaskIDs: list[int], views: list[str], outputTime: float, sampleRateX: float, sampleRateY: float, hotRender: bool, interactive: bool, emitRenderTileOrdering: bool, diskCachingAllowed: bool, tilePrioritizerType: int, tilePrioritizerCenter: Any, tilePrioritizerRect: Any, interactiveOverscanPadding: Any, renderType: int, renderMethodName: str) -> tuple: ...
def RenderThumbnail(port: NodegraphAPI_cmodule.Port, renderTime: float, proxyScaleX: float, proxyScaleY: float, nodeName: str, maxWidth: int, maxHeight: int, ignoreCacheID: str) -> str: ...
def RestartExternalRender(sequenceID: int) -> None: ...
def SetCatalogEventReceiver(callable: typing.Callable) -> None: ...
def SetMaxDiskUsage(sizeInMegabytes: int) -> None: ...
def SetMaxImageMemory(sizeInMegabytes: int) -> None: ...
def SetNukeSessionMappings(mainSequenceID: int, mappings: list[Tuple[str, int, str, int, FrameBuffer]]) -> None: ...
def SetNukeSessionOutputNodeName(mainSequenceID: int, outputNodeName: str) -> None: ...
def SetRenderDebug(enabled: bool) -> None: ...
def SetRenderLogFile(filename: str) -> None: ...
def SetRenderThreads(numThreads: int) -> None: ...
def SetSpeculativeCacheEnabled(enabled: bool) -> None: ...
def SetTileSize(width: int, height: int) -> None: ...
def SignalExternalRender(sequenceID: int, signal: int) -> None: ...
def StartExternalRender(rendererName: str, sequenceID: int, nodeName: str, preCommands: list[str], renderCommand: str, postCommands: list[str], isRemoteRender: bool, renderFarm: str) -> tuple: ...
def TerminateCancelledRenders() -> None: ...
def TileStitch(xTiles: int, yTiles: int, inputFilenames: list[str], outputImageOptions: str, outputFilename: dict, outputDataRect: list[tuple[int, int, int, int]], outputDisplayRect: list[tuple[int, int, int, int]], clampOutput: bool, colorConvert: bool, computeStats: str) -> None: ...
def UnregisterNukeSession(mainSequenceID: int) -> None: ...
def _Register2DFactories() -> None: ...
def _Set_GetRenderProducer_Fn(callable: typing.Callable) -> None: ...
def _internalRegisterCommandLineNode(nodeType: str, paramXML: str, ctor: typing.Callable) -> None: ...
def _internalSetFarmPluginManager(farmManagerModule: types.ModuleType) -> None: ...
def fbo_bind(arg0: int) -> None: ...
def fbo_create(arg0: int, arg1: int) -> tuple: ...
def fbo_delete(arg0: int) -> None: ...
def fbo_init() -> None: ...
def fbo_unbind() -> None: ...
def glBatchVertex(vertexSequence: typing.Sequence) -> None: ...
def glDrawProjectedLatLongLine(startPt: list[tuple[float, float, float]], endPt: list[tuple[float, float, float]], latLngWidthHeight: list[tuple[float, float]], subdivisions: int) -> None: ...
def gl_disableFragmentProgram() -> None: ...
def gl_enableFilmlookFragmentProgram(displayRequest: dict[str, Any], textureID: int) -> None: ...
def gl_enableFragmentProgram(fragmentProgram: str, textureID: int) -> None: ...