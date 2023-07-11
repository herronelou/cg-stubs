# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import ConfigurationAPI_cmodule as Configuration
import KatanaResources as KatanaResources
import Shelves
import Utils as Utils
from Utils.Decorators import deprecated as deprecated
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

SHELF_TYPE_BUILTIN: int
SHELF_TYPE_CUSTOM: int
SHELF_TYPE_UNKNOWN: int
SHELF_TYPE_USER: int
_ConsoleHandler: None
_ShelfTypeCallback: None

class Shelf:
    def __init__(self, name, path, shelfType, shelfTypeStr: Incomplete | None = ...): ...
    def _Shelf__triggerChange(self): ...
    def append(self, item): ...
    def createItem(self, name: str, description: str, keyboardShortcut: str = ..., icon: Incomplete | None = ...) -> Shelves.ShelfItem: ...
    def createNewItem(self, name, desc, dropTypes, icon): ...
    def find(self, name): ...
    def getEditable(self): ...
    def getItems(self): ...
    def getName(self): ...
    def getPath(self): ...
    def getType(self): ...
    def getTypeStr(self): ...
    def load(self): ...
    def remove(self, item): ...
    def replace(self, oldItem, newItem): ...

class ShelfItem:
    _defaultPixmap: ClassVar[None] = ...
    def __init__(self, name: str, icon: str, keyboardShortcut: str, description, sourceFile: str, scope: tuple = ...): ...
    def _ShelfItem__isScopeValid(self, nodeTypes: list) -> bool: ...
    def deleteSourceFile(self): ...
    def getCode(self): ...
    def getDescription(self): ...
    def getDropTypes(self): ...
    def getIconName(self): ...
    def getKeyboardShortcut(self) -> str: ...
    def getName(self): ...
    def getScope(self): ...
    def getSourceFile(self): ...
    def getSourceFilename(self): ...
    def run(self, additionalEnvironment: Incomplete | None = ..., checkScope: bool = ...): ...
    def setKeyboardShortcut(self, shortcut: str): ...
    def setScope(self, scope: list): ...
    def sourceFileExists(self): ...

def ClearConsole(raiseTab: bool = ...): ...
def CreateShelfItem(shelfItemFilename): ...
def CreateUserShelf(shelfName, suffix: str = ...): ...
def GetBuiltinShelves(): ...
def GetShelves2(forceReload: bool = ...): ...
def GetShelvesWithSuffix(suffix, forceReload: bool = ...): ...
def GetUserShelves(suffix: str = ...): ...
def ParseFile(filename: str) -> dict: ...
def PrintToConsole(message: str, raiseTab: bool = ...): ...
def RegisterPrintHandler(callback): ...
def RegisterShelfTypeCallback(callback): ...
def ShelfPrint(message, important: bool = ...): ...
def _GetDocstring_Description(docstring): ...
def _GetDocstring_DropTypes(docstring): ...
def _GetDocstring_Icon(docstring): ...
def _GetDocstring_KeyboardShortcut(docstring): ...
def _GetDocstring_Name(docstring): ...
def _GetDocstring_Scope(docstring): ...
def _GetItemList(shelfPath): ...
def _GetScriptFile(name: str, desc: str, keyboardShortcut: str, icon, code: str) -> str: ...
def _GetShelfList(rootPath): ...
def _GetUniqueFile(dirName, prefix, suffix, maxInt: int = ...): ...
def _UpgradeOldShelf(filename, targetDirectory): ...
def _ValidateUserShelf(suffix: str = ...): ...
