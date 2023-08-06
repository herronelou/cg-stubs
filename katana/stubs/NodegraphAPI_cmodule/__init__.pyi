# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import typing
from typing import Any, ClassVar, Set, Tuple, overload

__cleanupNodeClass: PyCapsule
__cleanupNotify: PyCapsule
__cleanupPortClass: PyCapsule
__cleanupPythonNodeClasses: PyCapsule

class Context:
    Legacy: ClassVar[str] = ...
    NetworkMaterial: ClassVar[str] = ...
    NodeGraphContextParameter: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetNodeGraphContext(cls, node: NodegraphAPI.Node) -> str: ...

class Flavor:
    RendererAgnostic: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None: ...

class GraphState:
    def __init__(self) -> None: ...
    def edit(self) -> GraphStateBuilder: ...
    def getDynamicEntry(self, path: str) -> Any: ...
    def getDynamicHash(self) -> int: ...
    def getHash(self) -> int: ...
    def getMaxTimeSamples(self) -> int: ...
    def getOpSystemArgs(self) -> GroupAttribute: ...
    def getROI(self) -> tuple: ...
    def getRenderMethodName(self) -> str: ...
    def getSampleRateX(self) -> float: ...
    def getSampleRateY(self) -> float: ...
    def getShutterClose(self) -> float: ...
    def getShutterOpen(self) -> float: ...
    def getStaticEntry(self, path: str) -> Any: ...
    def getStaticHash(self) -> int: ...
    def getTime(self) -> float: ...
    def getView(self) -> str: ...
    def isDiskCachingAllowed(self) -> bool: ...
    def isExternalRenderAllowed(self) -> bool: ...
    def isHotRender(self) -> bool: ...
    def isROIAbsolute(self) -> bool: ...
    def isTaskCachingIgnored(self) -> bool: ...
    def matchVariableWithCEL(self, variableName: str, celStatement: str) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __lt__(self, other: object) -> bool: ...

class GraphStateBuilder:
    def __init__(self) -> None: ...
    @overload
    def build(self) -> GraphState: ...
    @overload
    def build(self) -> Any: ...
    def deleteDynamicEntry(self, path: str) -> GraphStateBuilder: ...
    def deleteStaticEntry(self, path: str) -> GraphStateBuilder: ...
    def setDiskCachingAllowed(self, allowCaching: bool) -> GraphStateBuilder: ...
    @overload
    def setDynamicEntry(self, path: str, attr) -> GraphStateBuilder: ...
    @overload
    def setDynamicEntry(self, path: str, value: int) -> GraphStateBuilder: ...
    @overload
    def setDynamicEntry(self, path: str, value: float) -> GraphStateBuilder: ...
    @overload
    def setDynamicEntry(self, path: str, value: str) -> GraphStateBuilder: ...
    def setExternalRenderAllowed(self, allowExternal: bool) -> GraphStateBuilder: ...
    def setHotRender(self, isHot: bool) -> GraphStateBuilder: ...
    def setIgnoreTaskCaching(self, ignoreCaching: bool) -> GraphStateBuilder: ...
    def setMaxTimeSamples(self, maxSamples: int) -> GraphStateBuilder: ...
    def setROI(self, roi: list[tuple[float, float, float, float]]) -> GraphStateBuilder: ...
    def setRenderMethodName(self, name: str) -> GraphStateBuilder: ...
    def setSampleRateX(self, sampleRate: float) -> GraphStateBuilder: ...
    def setSampleRateY(self, sampleRate: float) -> GraphStateBuilder: ...
    def setShutterClose(self, time: float) -> GraphStateBuilder: ...
    def setShutterOpen(self, time: float) -> GraphStateBuilder: ...
    @overload
    def setStaticEntry(self, path: str, attr) -> GraphStateBuilder: ...
    @overload
    def setStaticEntry(self, path: str, value: int) -> GraphStateBuilder: ...
    @overload
    def setStaticEntry(self, path: str, value: float) -> GraphStateBuilder: ...
    @overload
    def setStaticEntry(self, path: str, value: str) -> GraphStateBuilder: ...
    def setTime(self, time: float) -> GraphStateBuilder: ...
    def setView(self, view: str) -> GraphStateBuilder: ...

class GroupNode(Node):
    def __init__(self, *args, **kwargs) -> None: ...
    def checkChildrenForCycles(self) -> bool: ...
    def getChild(self, name: str) -> Node: ...
    def getChildByIndex(self, index: int) -> Any: ...
    def getChildren(self) -> list[Node]: ...
    def getNumChildren(self) -> int: ...
    def getReturnPort(self, name: str) -> Port: ...
    def getSendPort(self, name: str) -> Port: ...
    def isContentLocked(self) -> bool: ...
    def setContentLocked(self, value: bool) -> None: ...
    def setLocked(self, value: bool) -> None: ...

class Node:
    def __init__(self, *args, **kwargs) -> None: ...
    def addInputPort(self, name: str) -> NodegraphAPI.Port: ...
    def addInputPortAtIndex(self, name: str, index: int) -> NodegraphAPI.Port: ...
    def addOutputPort(self, name: str) -> NodegraphAPI.Port: ...
    def addOutputPortAtIndex(self, name: str, index: int) -> NodegraphAPI.Port: ...
    def customReset(self) -> bool: ...
    def delete(self) -> bool: ...
    def getAttributes(self) -> dict: ...
    def getBaseType(self) -> str: ...
    def getBoolValue(self, name: str, time: float) -> bool: ...
    def getBypassRouting(self) -> dict: ...
    def getDefaultParameter(self, *args, **kwargs): ...
    def getGraphState(self, *args, **kwargs): ...
    def getInfoString(self) -> str: ...
    def getInputPort(self, *args, **kwargs): ...
    def getInputPortAndGraphState(self, outputPort: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState) -> tuple: ...
    def getInputPortByIndex(self, index: int) -> NodegraphAPI.Port: ...
    def getInputPorts(self) -> list: ...
    def getInputSource(self, name: str, graphState: NodegraphAPI.GraphState) -> tuple: ...
    def getName(self) -> str: ...
    def getNumInputPorts(self) -> int: ...
    def getNumOutputPorts(self) -> int: ...
    def getOutputPort(self, *args, **kwargs): ...
    def getOutputPortByIndex(self, index: int) -> NodegraphAPI.Port: ...
    def getOutputPorts(self) -> list: ...
    def getParameter(self, name: str) -> Parameter: ...
    def getParameterValue(self, name: str, time: float) -> Any: ...
    def getParameters(self) -> GroupParameter: ...
    def getParent(self, *args, **kwargs): ...
    def getSourcePort(self, port: NodegraphAPI.Port, graphState: NodegraphAPI.GraphState) -> tuple: ...
    def getType(self) -> str: ...
    def isAutoRenameAllowed(self) -> bool: ...
    def isBypassed(self) -> bool: ...
    def isLocked(self, considerParents: bool = ...) -> bool: ...
    def isMarkedForDeletion(self) -> bool: ...
    def isRenameAllowed(self) -> bool: ...
    def isResetPossible(self) -> bool: ...
    def loadEnd(self) -> Any: ...
    def parseParameters(self, parameterString: str) -> Any: ...
    def removeInputPort(self, name: str) -> bool: ...
    def removeOutputPort(self, name: str) -> bool: ...
    def renameInputPort(self, *args, **kwargs): ...
    def renameOutputPort(self, *args, **kwargs): ...
    def setAttributes(self, attributes: dict) -> Any: ...
    def setAutoRenameAllowed(self, autoRenameAllowed: bool) -> Any: ...
    def setBypassRouting(self, portRouting: dict) -> Any: ...
    def setBypassed(self, bypassed: bool) -> Any: ...
    def setLocked(self, locked: bool) -> Any: ...
    def setName(self, name: str, updateExpressions: bool = ...) -> str: ...
    def setParent(self, parentNode, notify: bool = ...) -> bool: ...
    def setRenameAllowed(self, renameAllowed: bool) -> Any: ...
    def setType(self, typeName: str) -> Any: ...
    def __hash__(self) -> int: ...

class Parameter:
    INTERPOLATION_CONSTANT: ClassVar[int] = ...
    INTERPOLATION_LINEAR: ClassVar[int] = ...
    REFERENCECOLLECTIONTARGETS_NODES: ClassVar[int] = ...
    REFERENCECOLLECTIONTARGETS_OMIT_DIRECT: ClassVar[int] = ...
    REFERENCECOLLECTIONTARGETS_OMIT_GRAPHSTATE: ClassVar[int] = ...
    REFERENCECOLLECTIONTARGETS_PARAMS: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def buildXmlIO(self, *args, **kwargs): ...
    def createChildGroup(self, name: str, index: int = ...) -> Parameter: ...
    def createChildNumber(self, name: str, value: float, index: int = ...) -> Parameter: ...
    def createChildNumberArray(self, name: str, size: int, index: int = ...) -> Parameter: ...
    def createChildString(self, name: str, value: str, index: int = ...) -> Parameter: ...
    def createChildStringArray(self, name: str, size: int, index: int = ...) -> Parameter: ...
    def createChildXmlIO(self, element, index: int = ...) -> Parameter: ...
    def deleteChild(self, child: Parameter) -> None: ...
    def finalizeValue(self) -> None: ...
    def getAutoKey(self) -> bool: ...
    def getChild(self, name: str) -> Parameter: ...
    def getChildByIndex(self, index: int) -> Parameter: ...
    def getChildren(self) -> list[Parameter]: ...
    def getCurve(self) -> Any: ...
    def getExpression(self) -> str: ...
    def getExpressionError(self) -> str: ...
    def getFileSequenceValue(self, time: float) -> str: ...
    def getFullName(self, includeNodeName: bool = ...) -> str: ...
    def getHintString(self) -> str: ...
    def getIndex(self) -> int: ...
    def getInterpolation(self) -> int: ...
    def getKeys(self) -> list[float]: ...
    def getName(self) -> str: ...
    def getNode(self) -> Node: ...
    def getNumChildren(self) -> int: ...
    def getOpaqueDataInfo(self) -> dict: ...
    def getParent(self) -> Parameter: ...
    def getReferences(self, time: float) -> list[str]: ...
    def getSamples(self) -> Any: ...
    def getTupleSize(self) -> int: ...
    def getType(self) -> str: ...
    def getValue(self, time: float) -> Any: ...
    def getValueXmlIO(self, element, time: float) -> None: ...
    def getXML(self, forcePersistant: bool = ...) -> str: ...
    def hasFloatingCurve(self) -> bool: ...
    def hasKey(self, time: float) -> bool: ...
    def hasUseNodeDefault(self) -> bool: ...
    def insertArrayElement(self, index: int) -> Parameter: ...
    def isAnimated(self) -> bool: ...
    def isExpression(self) -> bool: ...
    def isPersistant(self) -> bool: ...
    def makeConstant(self, time: float) -> None: ...
    @overload
    def moveKeys(self, times: list[float], dt: float) -> None: ...
    @overload
    def moveKeys(self, times: Set[float], dt: float) -> None: ...
    def parseXML(self, xml: str) -> None: ...
    def parseXmlIO(self, element) -> bool: ...
    @classmethod
    def popReferenceCollectionStack(cls) -> tuple: ...
    @classmethod
    def pushReferenceCollectionStack(cls, targets: int = ...) -> None: ...
    def readOpaqueDataFromFile(self, filenames: list[str]) -> None: ...
    def readOpaqueDataFromXmlIO(self, element) -> None: ...
    def removeArrayElement(self, index: int) -> None: ...
    def removeArrayElements(self, index: int, count: int) -> None: ...
    def removeKey(self, time: float) -> None: ...
    @overload
    def removeKeys(self, times: list[float]) -> None: ...
    @overload
    def removeKeys(self, times: Set[float]) -> None: ...
    def renameExpression(self, oldNodeName: str, newNodeName: str) -> None: ...
    def reorderChild(self, child: Parameter, index: int) -> None: ...
    def reorderChildren(self, oldIndex: int, newIndex: int, count: int) -> None: ...
    def reparentAtomic(self, parent: Parameter) -> str: ...
    def reparentExpression(self, oldPath: str, newPath: str) -> None: ...
    def replaceXML(self, xml: str, removeChildren: bool = ...) -> None: ...
    def replaceXmlIO(self, element, removeChildren: bool = ...) -> None: ...
    def resetFloatingCurve(self) -> None: ...
    def resizeArray(self, length: int) -> None: ...
    def sendSignal_finalize(self, **kwargs) -> None: ...
    def sendSignal_setKey(self, keyTime: float) -> None: ...
    def sendSignal_setValue(self, **kwargs) -> None: ...
    def setAutoKey(self, value: bool) -> None: ...
    def setCurve(self, curve, final: bool = ...) -> None: ...
    def setExpression(self, expression: str, enable: bool = ...) -> None: ...
    def setExpressionFlag(self, value: bool) -> None: ...
    def setHintString(self, hint: str) -> None: ...
    def setInterpolation(self, interpolation: int, final: bool = ...) -> None: ...
    def setKey(self, time: float, sendNotifyMessage: bool = ...) -> None: ...
    def setName(self, newName: str) -> str: ...
    def setPersistant(self, arg0: bool) -> None: ...
    def setSamples(self, samples: dict[float, list[float]], final: bool = ...) -> None: ...
    def setTupleSize(self, size: int) -> None: ...
    def setUseNodeDefault(self, value: bool) -> None: ...
    def setValue(self, value: object, time: float, final: bool = ..., sendNotifyMessage: bool = ...) -> None: ...
    def setValueAutoKey(self, value: object, time: float, final: bool = ...) -> None: ...
    def setValueXmlIO(self, element, time: float, final: bool = ..., sendNotifyMessage: bool = ...) -> None: ...
    def useNodeDefault(self) -> bool: ...
    def writeOpaqueDataToFile(self, filenames: list[str]) -> None: ...
    def writeOpaqueDataToXmlIO(self, *args, **kwargs): ...
    def __hash__(self) -> int: ...

class Port:
    FLAVOR_DEPENDENCY: ClassVar[int] = ...
    FLAVOR_MASK: ClassVar[int] = ...
    FLAVOR_STANDARD: ClassVar[int] = ...
    TYPE_CONSUMER: ClassVar[int] = ...
    TYPE_PRODUCER: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def addOrUpdateMetadata(self, key: str, value: str) -> None: ...
    def connect(self, other: Port, doCycleCheck: bool = ...) -> bool: ...
    def deleteMetadata(self, key: str) -> None: ...
    def disconnect(self, other: Port) -> bool: ...
    def getAttributes(self) -> dict: ...
    def getColor(self) -> tuple: ...
    def getConnectedPort(self, index: int) -> Port: ...
    def getConnectedPorts(self) -> list[Port]: ...
    def getDisplayName(self, prefixWithPageNames: bool = ...) -> str: ...
    def getFlavor(self) -> int: ...
    def getIndex(self) -> int: ...
    def getMetadata(self, key: str) -> Any: ...
    def getMetadataDict(self) -> dict[str, str]: ...
    def getName(self) -> str: ...
    def getNode(self) -> Node: ...
    def getNumConnectedPorts(self) -> int: ...
    def getTags(self) -> list: ...
    def getType(self) -> int: ...
    def hasCustomColor(self) -> bool: ...
    def isConnected(self, other: Port) -> bool: ...
    def setAttributes(self, attrs: dict) -> None: ...
    def setColor(self, r: float, g: float, b: float, isCustom: bool = ...) -> None: ...
    def setTags(self, tags: list[str]) -> None: ...
    def __hash__(self) -> int: ...

class PythonGroupNode(GroupNode):
    def __init__(self) -> None: ...

class PythonNode(Node):
    def __init__(self) -> None: ...
    @overload
    def getInputPortAndGraphState(self, port: Port, graphState: GraphState) -> tuple: ...
    @overload
    def getInputPortAndGraphState(self, port: Port, time: float) -> tuple: ...

def BuildAttrFromGroupParameter(param: Parameter, graphState: GraphState = ..., multisampleDefault: bool = ..., numberAttrTypeDefault: object = ..., includeEmptyGroups: bool = ..., groupInherit: bool = ...) -> Any: ...
def BuildAttrFromStringParameter(param: Parameter, graphState: GraphState = ..., multisample: bool = ...) -> Any: ...
def BuildDoubleAttrFromNumberParameter(param: Parameter, graphState: GraphState = ..., multisample: bool = ...) -> Any: ...
def BuildFloatAttrFromNumberParameter(param: Parameter, graphState: GraphState = ..., multisample: bool = ...) -> Any: ...
def BuildIntAttrFromNumberParameter(param: Parameter, graphState: GraphState = ..., multisample: bool = ...) -> Any: ...
def GetGraphStateAtPort(searchPort: Port, startPort: Port, startGraphState: GraphState) -> Any: ...
def GetLocalGraphState() -> Any: ...
def GetSampleTimes(shutterOpen: float, shutterClose: float, maxTimeSamples: int, useSinglePrecision: bool = ...) -> tuple: ...
def GetSampleTimesFromGraphState(graphState: GraphState, useSinglePrecision: bool = ...) -> tuple: ...
def GetSingleSampleTimeFromGraphState(graphState: GraphState) -> float: ...
def IsParameterConstant(parameter: Parameter) -> bool: ...
def PopLocalGraphState() -> None: ...
def PushLocalGraphState(graphState: GraphState) -> None: ...
def curve_writeCurveXML(curve) -> str: ...
def node_addNodeFlavor(nodeType: str, flavor: str) -> None: ...
def node_clearFlavorNodes(flavor: str) -> None: ...
def node_createNode(nodeType: str, parent: Node = ...) -> Any: ...
def node_getAllConnectedInputs(sourceNodes: typing.Iterable) -> set: ...
def node_getAllFlavors() -> list[str]: ...
def node_getAllNodes(includeDeleted: bool = ..., sortByName: bool = ...) -> list: ...
def node_getAllNodesByType(nodeType: str, includeDeleted: bool = ..., sortByName: bool = ...) -> list: ...
def node_getCurrentGraphState() -> GraphState: ...
def node_getCurrentTime() -> float: ...
def node_getFlavorNodes(flavor: str, existsFlag: bool) -> list[str]: ...
def node_getGraphState(time: float) -> GraphState: ...
def node_getNode(nodeName: str) -> Any: ...
def node_getNodeFlavors(nodeType: str) -> list[str]: ...
def node_getOriginalProjectAssetID() -> str: ...
def node_getProjectAssetID() -> str: ...
def node_getTypeList() -> str: ...
def node_isLoading() -> bool: ...
def node_needsRedraw() -> bool: ...
def node_registerExtension(extension: object) -> None: ...
def node_registerPythonGroupType(typeName: str, constructor: typing.Callable) -> None: ...
def node_registerPythonNodeFactory(nodeType: str, factory: typing.Callable) -> None: ...
def node_registerPythonNodeType(typeName: str, constructor: typing.Callable) -> None: ...
def node_registerQueryFlag(callbacK: typing.Callable) -> None: ...
def node_removeNodeFlavor(nodeType: str, flavor: str) -> None: ...
def node_setExpressionObject(arg0: object) -> None: ...
def node_setIsLoading(value: bool) -> None: ...
def node_setNeedsRedraw(arg0: bool) -> None: ...
def node_setOriginalProjectAssetID(assetId: str) -> None: ...
def node_setProjectAssetID(assetId: str) -> None: ...
def node_setRootNode(rootNode: Node) -> None: ...
def notify_areNotificationsEnabled() -> bool: ...
def notify_setNotificationFn(handler: typing.Callable) -> None: ...
def notify_setNotificationsEnabled(arg0: bool) -> None: ...
def parameter_getAllExpressionedParameters(errorsOnly: bool = ..., noErrorsOnly: bool = ...) -> Set[Parameter]: ...
def parameter_getAutoKeyAll() -> bool: ...
def parameter_getExpressionReferences(referents: object = ..., referers: object = ...) -> dict: ...
def parameter_popExpressionCache() -> None: ...
def parameter_pushExpressionCache() -> None: ...
def parameter_resetAllFloatingCurves() -> None: ...
def parameter_setAutoKeyAll(autoKeyAll: bool) -> None: ...
def parameter_setExpressionGlobals(globals: object) -> None: ...
def parameter_setExpressionLocalFn(locals: typing.Callable) -> None: ...
def parameter_setOpaqueParameterBuildXmlIOHandler(handler: object) -> None: ...
def port_registerComplexConnector(connector: typing.Callable) -> None: ...
def pyerror_occurred() -> bool: ...
def registerBuiltinFactories() -> None: ...
