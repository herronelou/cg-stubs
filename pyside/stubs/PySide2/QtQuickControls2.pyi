import collections.abc
import shiboken2
import typing
T = typing.TypeVar('T')

class QQuickStyle(shiboken2.Object):
    def __init__(self) -> None: ...
    @classmethod
    def addStylePath(cls, path: str) -> None: ...
    @classmethod
    def availableStyles(cls) -> typing.List[str]: ...
    @classmethod
    def name(cls) -> str: ...
    @classmethod
    def path(cls) -> str: ...
    @classmethod
    def setFallbackStyle(cls, style: str) -> None: ...
    @classmethod
    def setStyle(cls, style: str) -> None: ...
    @classmethod
    def stylePathList(cls) -> typing.List[str]: ...