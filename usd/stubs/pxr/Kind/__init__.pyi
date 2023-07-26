# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
from typing import ClassVar

__MFB_FULL_PACKAGE_NAME: str

class Registry(Boost.Python.instance):
    def __init__(self) -> None: ...
    @classmethod
    def GetAllKinds(cls) -> list[str]: ...
    @classmethod
    def GetBaseKind(cls, arg1: str | pxr.Ar.ResolvedPath) -> str: ...
    @classmethod
    def HasKind(cls, arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def IsA(cls, arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath) -> bool: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class Tokens(Boost.Python.instance):
    assembly: ClassVar[str] = ...  # read-only
    component: ClassVar[str] = ...  # read-only
    group: ClassVar[str] = ...  # read-only
    model: ClassVar[str] = ...  # read-only
    subcomponent: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...
