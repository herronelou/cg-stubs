# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolibServices.ExpressionMath as ExpressionMath
import FnAttribute as FnAttribute
import PyFnGeolibServices as FnGeolibServices
import PackageSuperToolAPI.NodeUtils as NU
import NodegraphAPI as NodegraphAPI
import Nodes3DAPI as Nodes3DAPI
import PackageSuperToolAPI.Packages
import PackageSuperToolAPI.Packages as Packages
from NodegraphAPI.SuperTool import SuperTool
from PyUtilModule.VirtualKatana import Decorators as Decorators
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

API_VERSION: int
SYNC_SELECTION_IN_OUT: float
SYNC_SELECTION_OFF: float
SYNC_SELECTION_OUT: float

class BaseNode(SuperTool):
    VERSION: ClassVar[int] = ...
    def __init__(self, version: Incomplete | None = ...): ...
    @classmethod
    def _BaseNode__getEditPackageForLocationPath(cls, mainNode: NodegraphAPI.Node, locationPath: str) -> PackageSuperToolAPI.Packages.Package | None: ...
    def _BaseNode__getNotInInputMarkingOpScript(self): ...
    def _BaseNode__getNotInInputStrippingOpScript(self): ...
    def _BaseNode__getOpScriptForNonAdoptedStripping(self): ...
    def adoptLocationForEditing(self, locationPath: str, locationAttributes: Incomplete | None = ...): ...
    def adoptLocationsForEditing(self, locationPaths: list[str], locationAttributes: Incomplete | None = ...): ...
    def canAdoptLocationForEditing(self, location: str) -> bool: ...
    def canAdoptLocationsForEditing(self, locations: list[str]) -> bool: ...
    def getAPIVersion(self) -> int: ...
    @classmethod
    def getDefaultRootLocation(cls) -> str: ...
    @classmethod
    def getItemListAttributeName(cls) -> str | None: ...
    def getLocationAttributes(self, locationPath: str) -> FnAttribute.GroupAttribute | None: ...
    def getPackageForPath(self, locationPath: str, raiseOnMissing: bool = ..., locationAttributes: Incomplete | None = ..., includeEditPackages: bool = ..., createDummyOnMissing: bool = ...) -> PackageSuperToolAPI.Packages.Package | None: ...
    def getRegisteredDisplayPackageClasses(self) -> list[PackageSuperToolAPI.Packages.Package]: ...
    def getRegisteredPackageClasses(self) -> list[tuple[str, type]]: ...
    def getRootLocation(self) -> str: ...
    def getRootPackage(self) -> PackageSuperToolAPI.Packages.Package: ...
    def getShowIncomingScene(self) -> bool: ...
    @classmethod
    def getSuperToolName(cls) -> str: ...
    def getSyncSelection(self) -> int: ...
    def getVersion(self) -> int: ...
    def isLocationAdopted(self, locationPath: str) -> bool: ...
    def setRootLocation(self, locationPath: str): ...
    def setShowIncomingScene(self, state: bool): ...
    def setSyncSelection(self, syncSelection: int): ...
    def setVersion(self, version: int): ...
    @classmethod
    def superToolRegistered(cls): ...
    def upgrade(self, rootPackage: RootPackage): ...

def RegisterTagAdoptedNodeType(): ...
