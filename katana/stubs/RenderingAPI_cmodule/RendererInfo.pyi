# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
from RenderingAPI import FlushPluginCaches as FlushPluginCaches
from typing import Any, overload

kRenderMethodTypeDiskRender: str
kRenderMethodTypeLiveRender: str
kRenderMethodTypePreviewRender: str
kRenderPluginApiVersion: int
kRendererInfoApiVersion: int
kRendererObjectTypeDriver: str
kRendererObjectTypeFilter: str
kRendererObjectTypeOutputChannel: str
kRendererObjectTypeOutputChannelAttrHints: str
kRendererObjectTypeOutputChannelCustomParam: str
kRendererObjectTypeRenderOutput: str
kRendererObjectTypeShader: str
kRendererObjectValueTypeBoolean: int
kRendererObjectValueTypeByte: int
kRendererObjectValueTypeColor3: int
kRendererObjectValueTypeColor4: int
kRendererObjectValueTypeEnum: int
kRendererObjectValueTypeFloat: int
kRendererObjectValueTypeInt: int
kRendererObjectValueTypeLocation: int
kRendererObjectValueTypeMatrix: int
kRendererObjectValueTypeNormal: int
kRendererObjectValueTypePoint2: int
kRendererObjectValueTypePoint3: int
kRendererObjectValueTypePoint4: int
kRendererObjectValueTypePointer: int
kRendererObjectValueTypeShader: int
kRendererObjectValueTypeString: int
kRendererObjectValueTypeUint: int
kRendererObjectValueTypeUnknown: int
kRendererObjectValueTypeVector2: int
kRendererObjectValueTypeVector3: int
kRendererObjectValueTypeVector4: int
kRendererOutputTypeColor: str
kRendererOutputTypeDeep: str
kRendererOutputTypeForceNone: str
kRendererOutputTypeMerge: str
kRendererOutputTypePreScript: str
kRendererOutputTypeRaw: str
kRendererOutputTypeScript: str
kRendererOutputTypeShadow: str
kTerminalOpStateArgRenderMethodType: str
kTerminalOpStateArgSystem: str

class RendererInfoPlugin:
    def __init__(self, *args, **kwargs) -> None: ...
    def addObjectLocation(self, type: str, location: str) -> None: ...
    def clearObjectLocations(self, type: str = ...) -> None: ...
    def getBatchRenderMethod(self) -> PyFnAttribute.GroupAttribute: ...
    def getLiveRenderTerminalOps(self, stateArgs: PyFnAttribute.GroupAttribute) -> list: ...
    def getRegisteredRendererName(self) -> str: ...
    def getRegisteredRendererVersion(self) -> str: ...
    def getRenderMethods(self) -> PyFnAttribute.GroupAttribute: ...
    def getRenderTerminalOps(self, stateArgs: PyFnAttribute.GroupAttribute) -> list: ...
    def getRendererCoshaderType(self) -> str: ...
    def getRendererObjectDefaultType(self, type: str) -> str: ...
    def getRendererObjectInfo(self, *args, **kwargs) -> Any: ...
    @overload
    def getRendererObjectNames(self, type: str, typeTag: str) -> list[str]: ...
    @overload
    def getRendererObjectNames(self, type: str, typeTags: list[str] = ...) -> list[str]: ...
    def getRendererObjectTypes(self, type: str) -> list[str]: ...
    def getRendererShaderTypeTags(self, shaderType: str) -> list[str]: ...
    def getShaderInputNames(self, shader: str) -> list[str]: ...
    def getShaderInputTags(self, shader: str, inputName: str) -> list[str]: ...
    def getShaderOutputNames(self, shader: str) -> list[str]: ...
    def getShaderOutputTags(self, shader: str, outputName: str) -> list[str]: ...
    def isNodeTypeSupported(self, nodeType: str) -> bool: ...
    def isPolymeshFacesetSplittingEnabled(self) -> bool: ...
    def isPresetLocalFileNeeded(self, outputType: str) -> bool: ...
    def setKatanaPath(self, katanaPath: str) -> None: ...
    def setPluginPath(self, pluginPath: str) -> None: ...
    def setPluginRootPath(self, pluginPath: str) -> None: ...
    def setTmpPath(self, tmpPath: str) -> None: ...
    def setTypeTagNameFilter(self, filter: str, typeTag: str) -> None: ...

class RendererObjectInfo:
    def __init__(self, *args, **kwargs) -> None: ...
    def getContainerHints(self) -> PyFnAttribute.Attribute: ...
    def getFullPath(self) -> str: ...
    def getLocation(self) -> str: ...
    def getName(self) -> str: ...
    def getOutputType(self) -> int: ...
    def getParam(self, name: str) -> Any: ...
    def getParams(self) -> list: ...
    def getType(self) -> str: ...
    def getTypeTags(self) -> list[str]: ...

class RendererObjectParamInfo:
    def __init__(self, *args, **kwargs) -> None: ...
    def getArraySize(self) -> int: ...
    def getDefault(self) -> PyFnAttribute.Attribute: ...
    def getEnums(self) -> PyFnAttribute.Attribute: ...
    def getHints(self) -> PyFnAttribute.Attribute: ...
    def getName(self) -> str: ...
    def getType(self) -> int: ...

def GetPlugin(arg0: str) -> Any: ...
def ReleaseManager() -> None: ...
def _FlushPluginCaches() -> None: ...