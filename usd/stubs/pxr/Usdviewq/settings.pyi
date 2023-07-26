# mypy: disable-error-code="misc, override, no-redef"

from _typeshed import Incomplete
from typing import Callable, ClassVar

class ConfigManager:
    EXTENSION: ClassVar[str] = ...
    defaultConfig: ClassVar[str] = ...
    def __init__(self, configDirPath) -> None: ...
    def _loadConfigPaths(self): ...
    def close(self): ...
    def getConfigs(self): ...
    def loadSettings(self, config, version, isEphemeral: bool = ...): ...
    def save(self, newName: Incomplete | None = ...): ...

class ExclusiveFile:
    def __init__(self, *args, **kwargs) -> None: ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class Settings(StateSource):
    def __init__(self, version, stateFilePath: Incomplete | None = ...) -> None: ...
    def _getState(self): ...
    def _loadState(self): ...
    def onSaveState(self, state): ...
    def save(self): ...

class StateSource:
    def __init__(self, parent, name) -> None: ...
    def GetChildStateSource(self, childName): ...
    def _getChildState(self, childName): ...
    def _getState(self): ...
    def _registerChildStateSource(self, child): ...
    def _saveState(self): ...
    def _typeCheck(self, value, prop): ...
    def onSaveState(self, state): ...
    def stateProperty(self, name, default, propType: Incomplete | None = ..., validator: Callable = ...): ...

class _StateProp:
    def __init__(self, name, default, propType, validator) -> None: ...
