# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from _typeshed import Incomplete
from typing import Any, ClassVar, Set, Tuple

_OutputFormats: list
_OutputFormatsByName: dict

class BaseLookFileBakeOutputFormat:
    DisplayName: ClassVar[None] = ...
    FileExtension: ClassVar[None] = ...
    Hidden: ClassVar[bool] = ...
    PassFileExtension: ClassVar[None] = ...
    def __init__(self, settings: LookFileBakeSettings): ...
    def postProcess(self, filePaths: list[str]) -> list[str]: ...
    def writeSinglePass(self, passData: LookFilePassData) -> list[str]: ...

class LookFileBakeSettings(_BaseSettings):
    def __init__(self, settings: Incomplete | None = ...): ...

class LookFilePassData(_BaseSettings):
    def __init__(self, settings: Incomplete | None = ...): ...

class _BaseSettings:
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: object): ...

def GetDefaultOutputFormat() -> BaseLookFileBakeOutputFormat | None: ...
def GetOutputFormatByName(outputFormatName: str) -> BaseLookFileBakeOutputFormat: ...
def GetOutputFormatFileExtensions(includeHidden: bool = ...) -> list[str]: ...
def GetOutputFormatNames(includeHidden: bool = ...) -> list[str]: ...
def GetOutputFormats(includeHidden: bool = ...) -> list[BaseLookFileBakeOutputFormat]: ...
def RegisterOutputFormat(outputFormat: BaseLookFileBakeOutputFormat): ...
def SetDefaultOutputFormat(outputFormat: BaseLookFileBakeOutputFormat): ...
def UnregisterOutputFormat(outputFormat: BaseLookFileBakeOutputFormat | str): ...
