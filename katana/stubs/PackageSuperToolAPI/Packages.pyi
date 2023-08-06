# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import Callbacks as Callbacks
import PackageSuperToolAPI.NodeUtils as NU
import Naming as Naming
import NodegraphAPI as NodegraphAPI
import Utils as Utils
import typing
from Callbacks.Callbacks import _TypeEnum
from PyUtilModule.VirtualKatana import Decorators as Decorators
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

__AdoptableLocationTypes: dict
__DeprecatedPackageClasses: dict
__DisplayPackageClasses: dict
__GroupTypeRegistry: dict
__PackageClassRegistry: dict

class CallbackMixin(Mixin):
    _CallbackMixin__shaderSelectedCallbackRegistered: ClassVar[bool] = ...
    _OnGafferShaderSelectedCallbackType: ClassVar[str] = ...
    _OnPackageCreatedCallbackID: ClassVar[None] = ...
    _OnShaderSelectedCallbackID: ClassVar[_TypeEnum] = ...
    @classmethod
    def executeCreationCallback(cls, package: Package): ...
    @classmethod
    def onSceneGraphViewShaderSelected(cls, objectHash: Incomplete | None = ..., node: typing.Optional[NodegraphAPI.Node] = ..., parameterPolicy: Incomplete | None = ...): ...
    @classmethod
    def registerCallbacks(cls, packageClass: type): ...

class DisableableMixin(Mixin):
    def _DisableableMixin__createDisableNodes(self) -> NodegraphAPI.Node: ...
    def isDisabled(self) -> bool: ...
    def isDisabledByParents(self) -> bool: ...
    def setDisabled(self, disabled: bool): ...

class DummyGroupPackage(GroupPackage):
    DEFAULT_NAME: ClassVar[str] = ...
    DISPLAY_ICON: ClassVar[str] = ...
    def __init__(self, packageNode: NodegraphAPI.Node | None, locationPath: Incomplete | None = ..., mainNode: Incomplete | None = ...) -> None: ...
    def canAdoptPackage(self, package: Package) -> bool: ...
    @classmethod
    def canCreateChildPackage(cls, packageClassOrName: type | str, mainNode: NodegraphAPI.Node, locationPath: str) -> bool: ...
    def childRemoved(self): ...
    @classmethod
    def create(cls, enclosingNode, locationPath): ...
    def createChildPackage(self): ...
    @classmethod
    def createForLocation(cls, locationPath: str, mainNode: NodegraphAPI.Node): ...
    def createParentPackageHierarchy(self): ...
    def delete(self): ...
    def getChildPackageCreateNode(self) -> NodegraphAPI.Node: ...
    def getChildPackages(self) -> list[Package]: ...
    def getLocationPath(self) -> str: ...
    def getMainNode(self) -> NodegraphAPI.Node: ...
    def getParentPackage(self) -> Package | None: ...

class EditPackage(Package):
    def canBeAdoptedByPackage(self, package: Package) -> bool: ...
    @classmethod
    def canBeCreatedByPackageClass(cls, packageClass: type) -> bool: ...
    def canBeRenamed(self) -> bool: ...
    @classmethod
    def canCreatePackageClass(cls, packageClass: type) -> bool: ...
    @classmethod
    def create(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> Package: ...
    @classmethod
    def createPackage(cls, packageNode: NodegraphAPI.Node) -> Package: ...
    @classmethod
    def createPackageEditStackNode(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> NodegraphAPI.Node: ...
    def delete(self): ...

class GroupEditPackage(GroupMixin, EditPackage):
    def _GroupEditPackage__getCreateStackPackage(self, create: bool = ...) -> Package | None: ...
    def childRemoved(self): ...
    @classmethod
    def create(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> Package: ...
    def getChildPackageCreateNode(self) -> NodegraphAPI.Node: ...
    def getChildPackages(self) -> list[Package]: ...

class GroupMixin(Mixin):
    def adoptPackage(self, childPackage: Package, peerNames: Incomplete | None = ...): ...
    def canAdoptPackage(self, package: Package) -> bool: ...
    @classmethod
    def canCreateChildPackage(cls, packageClassOrName: type | str, mainNode: NodegraphAPI.Node, locationPath: str) -> bool: ...
    def canReorderChildPackage(self, oldIndex: int, newIndex: int) -> bool: ...
    def childRemoved(self): ...
    def createChildPackage(self, packageClassOrName: type | str, name: Incomplete | None = ..., peerNames: Incomplete | None = ...) -> Package | None: ...
    def getChildPackage(self, name: str, includeDummies: bool = ...) -> Package | None: ...
    def getChildPackageCreateNode(self) -> NodegraphAPI.Node: ...
    def getChildPackages(self) -> list[Package]: ...
    @classmethod
    def getLocationTypes(cls) -> list[str]: ...
    def reorderChildPackage(self, oldIndex: int, newIndex: int): ...

class GroupPackage(GroupMixin, Package):
    DEFAULT_NAME: ClassVar[str] = ...
    DISPLAY_ICON: ClassVar[str] = ...
    @classmethod
    def create(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> Package: ...
    @classmethod
    def createStandardPackageNodes(cls, packageNode: NodegraphAPI.Node) -> list[NodegraphAPI.Node]: ...
    def getChildPackages(self) -> list[Package]: ...
    def getExtraNodeDependencies(self) -> list[NodegraphAPI.Node]: ...
    def initializeExtraNodeDependencies(self): ...

class LinkingMixin(Mixin):
    LINKING_ILLUMINATION_EFFECT: ClassVar[str] = ...
    LINKING_ILLUMINATION_NODE_NAME: ClassVar[str] = ...
    LINKING_ILLUMINATION_NODE_REF: ClassVar[str] = ...
    LINKING_SHADOW_EFFECT: ClassVar[str] = ...
    LINKING_SHADOW_NODE_NAME: ClassVar[str] = ...
    LINKING_SHADOW_NODE_REF: ClassVar[str] = ...
    @classmethod
    def _createLinkingNode(cls, packageNode: NodegraphAPI.Node, nodeName: str, nodeRef: str, effect: str) -> NodegraphAPI.Node: ...
    @classmethod
    def getIlluminationLinkingNode(cls, packageNode: NodegraphAPI.Node, create: bool = ...) -> NodegraphAPI.Node | None: ...
    @classmethod
    def getLinkingNodes(cls, packageNode: NodegraphAPI.Node, create: bool = ...) -> Tuple[NodegraphAPI.Node, NodegraphAPI.Node] | Tuple[None, None]: ...
    @classmethod
    def getShadowLinkingNode(cls, packageNode: NodegraphAPI.Node, create: bool = ...) -> NodegraphAPI.Node | None: ...

class LockingMixin(Mixin):
    def isLocked(self) -> bool: ...
    def setLocked(self, state: bool): ...

class LookFileReferenceEditMixin(Mixin):
    def _getLookFileReferenceNode(self) -> NodegraphAPI.Node | None: ...
    def _getLookFileReferenceNodeTypeName(self) -> str | None: ...
    def _getOrCreateLookFileReferenceNode(self, forceCreate: bool) -> Tuple[NodegraphAPI.Node, NodegraphAPI.Node] | Tuple[None, None]: ...
    def getLookFileMaterial(self) -> None | None: ...
    def isLookFileMaterialActive(self) -> bool: ...
    def setLookFileMaterial(self, asset: str | None, materialPath: str | None, assetAsExpression: bool = ..., materialPathAsExpression: bool = ...): ...
    def setLookFileMaterialActive(self, lookFileMaterialActive: bool): ...

class MaterialMixin(Mixin):
    _OnLookFileMaterialActiveSetCallbackID: ClassVar[_TypeEnum] = ...
    _OnLookFileMaterialSetCallbackID: ClassVar[_TypeEnum] = ...
    def getLookFileMaterial(self) -> tuple[str, str] | Tuple[None, None]: ...
    def getShader(self, shaderType: str) -> str | None: ...
    def isLookFileMaterialActive(self) -> bool: ...
    def isUsingLookFileMaterial(self): ...
    def setIsUsingLookFileMaterial(self, newValue): ...
    def setLookFileMaterial(self, asset: str | None, materialPath: str, assetAsExpression: bool = ..., materialPathAsExpression: bool = ...): ...
    def setLookFileMaterialActive(self, lookFileMaterialActive: bool): ...
    def setShader(self, shaderType: str, shaderName: str | None, asExpression: bool = ...): ...

class Mixin(Upgradable): ...

class MuteAndSoloEditMixin(MuteAndSoloMixin):
    def delete(self): ...
    def setMuted(self, muted: bool): ...
    def setSoloed(self, soloed: bool): ...

class MuteAndSoloMixin(Mixin):
    MUTEANDSOLO_NODE_REFERENCE: ClassVar[str] = ...
    NODE_NAME: ClassVar[str] = ...
    SOLOLISTEDIT_NODE_REFERENCE: ClassVar[str] = ...
    @classmethod
    def _createMuteAndSolo(cls, packageNode: NodegraphAPI.Node): ...
    @classmethod
    def _createSoloListEdit(cls, packageNode: NodegraphAPI.Node) -> NodegraphAPI.Node: ...
    def _destroyMuteSoloNodeIfUnused(self, muteAndSoloNode: NodegraphAPI.Node, soloListEditNode: NodegraphAPI.Node): ...
    def _getState(self, node: NodegraphAPI.Node, name: str, default: bool = ...) -> bool: ...
    def _setState(self, node: NodegraphAPI.Node, name: str, state: bool): ...
    def delete(self, edit: bool = ...): ...
    def getExtraNodeDependencies(self) -> list[NodegraphAPI.Node]: ...
    def getMuteSoloAndSoloListEditNode(self, create: bool = ...): ...
    def getOverrideNodeAndParameter(self, attributeName: str) -> Tuple[NodegraphAPI.Node, NodegraphAPI.Parameter] | Tuple[None, None]: ...
    def initializeExtraNodeDependencies(self): ...
    def isMuteOverrideEnabled(self) -> bool: ...
    def isMuted(self) -> bool: ...
    def isSoloOverrideEnabled(self) -> bool: ...
    def isSoloed(self) -> bool: ...
    def setMuted(self, muted: bool, edit: bool = ...): ...
    def setSoloed(self, soloed: bool, edit: bool = ...): ...

class Package(Upgradable):
    _Package__editPackageClasses: ClassVar[dict] = ...
    def __init__(self, packageNode: NodegraphAPI.Node) -> None: ...
    def _setPackageNode(self, packageNode: NodegraphAPI.Node): ...
    def adoptPackage(self, childPackage: Package, peerNames: Incomplete | None = ...): ...
    def canAdoptPackage(self, package: Package) -> bool: ...
    def canBeAdoptedByPackage(self, package: Package) -> bool: ...
    @classmethod
    def canBeCreatedByPackageClass(cls, packageClass: type) -> bool: ...
    def canBeDeleted(self) -> bool: ...
    def canBeDuplicated(self, parentPackage: Incomplete | None = ...) -> bool: ...
    def canBeRenamed(self) -> bool: ...
    @classmethod
    def canCreateChildPackage(cls, packageClassOrName: type | str, mainNode: NodegraphAPI.Node, locationPath: str) -> bool: ...
    @classmethod
    def canCreatePackageClass(cls, packageClass: type) -> bool: ...
    def canDuplicate(self): ...
    def canReorderChildPackage(self, oldIndex: int, newIndex: int) -> bool: ...
    @classmethod
    def create(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> Package: ...
    def createChildPackage(self, packageClassOrName: type | str, name: Incomplete | None = ..., peerNames: Incomplete | None = ...) -> Package | None: ...
    @classmethod
    def createPackage(cls, packageNode: NodegraphAPI.Node) -> Package: ...
    @classmethod
    def createPackageGroupNode(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> NodegraphAPI.GroupNode: ...
    def createPostMergeStackNode(self) -> NodegraphAPI.GroupStack: ...
    @classmethod
    def createStandardPackageNodes(cls, packageNode: NodegraphAPI.Node) -> list[NodegraphAPI.Node]: ...
    def delete(self): ...
    def duplicate(self, peerNames: Incomplete | None = ..., parentPackage: Incomplete | None = ...) -> Package: ...
    @classmethod
    def getAdoptableLocationTypes(cls) -> set[str]: ...
    def getChildPackage(self, name: str, includeDummies: bool = ...) -> Package | None: ...
    def getChildPackages(self) -> list[Package]: ...
    def getCreateNode(self) -> NodegraphAPI.Node: ...
    @classmethod
    def getEditPackageClass(cls) -> type: ...
    def getExtraNodeDependencies(self) -> list[NodegraphAPI.Node]: ...
    def getLocationPath(self) -> str: ...
    def getMainNode(self) -> NodegraphAPI.Node: ...
    @classmethod
    def getMainNodeFromNode(cls, node: NodegraphAPI.Node) -> NodegraphAPI.Node | None: ...
    def getName(self) -> str: ...
    def getOrCreateNodeByType(self, nodeType: str, forceCreate: bool = ...) -> NodegraphAPI.Node | None: ...
    def getOverrideNodeAndParameter(self, attrName: str) -> Tuple[NodegraphAPI.Node, NodegraphAPI.Parameter]: ...
    @classmethod
    def getPackageClassFromNode(cls, node: NodegraphAPI.Node) -> Package | None: ...
    @classmethod
    def getPackageFromNode(cls, node: NodegraphAPI.Node) -> Package: ...
    def getPackageNode(self) -> NodegraphAPI.Node: ...
    def getParentPackage(self) -> Package | None: ...
    def getPostMergePackageStack(self, create: bool = ...) -> NodegraphAPI.GroupStack | None: ...
    def initializeExtraNodeDependencies(self): ...
    def isNodeOfType(self, node: NodegraphAPI.Node | None, nodeType: str) -> bool: ...
    def reorderChildPackage(self, oldIndex: int, newIndex: int): ...
    @classmethod
    def setEditPackageClass(cls, editPackageClass: type): ...
    def setName(self, name: str, queueEvent: bool = ..., selectLocation: bool = ..., makeUnique: bool = ..., replaceSelection: bool = ..., **kwargs) -> str: ...
    def supportsLocking(self) -> bool: ...
    @classmethod
    def walkUpPackageHierarchy(cls, leafPackage: Package, includeLeaf: bool = ...) -> typing.Iterator: ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __ne__(self, other) -> bool: ...

class RootPackage(GroupPackage):
    def __init__(self, packageNode: NodegraphAPI.Node) -> None: ...
    def canBeDeleted(self) -> bool: ...
    def canBeRenamed(self) -> bool: ...
    @classmethod
    def canCreatePackageClass(cls, packageClass: type) -> bool: ...
    @classmethod
    def create(cls, enclosingNode: NodegraphAPI.Node, locationPath: str) -> Package: ...
    def delete(self): ...
    def setName(self, name: str, peerNames: Incomplete | None = ..., queueEvent: bool = ..., selectLocation: bool = ..., replaceSelection: bool = ...): ...

class Upgradable:
    def upgradeToVersion(self, version: int): ...

def GetPackageClass(superToolName: str | None, packageClassName: str) -> Package | None: ...
def GetPackageClassAndPackageName(superToolName: str, packageClassOrName: type | str) -> Tuple[type, str] | Tuple[None, None]: ...
def GetPackageClassForGroupLocationType(superToolName: str | None, groupLocationType: str) -> Package | None: ...
def GetRegisteredDisplayPackageClasses(superToolName: str | None) -> list[Package]: ...
def GetRegisteredPackageClasses(superToolName: str | None) -> list[str, type]: ...
def IsLocationTypeAdoptable(superToolName: str | None, locationType: str) -> bool: ...
def RegisterDeprecatedPackageClass(superToolName: str | None, deprecatedPackageClassName: str, packageClass: type): ...
def RegisterPackage(superToolName, packageClass): ...
def RegisterPackageClass(superToolName: str | None, packageClass: type): ...
