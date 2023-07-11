# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from _typeshed import Incomplete
from typing import Set, Tuple

__ArrayPrefix: str

def GetConnectionNames(sourceNodeName: str, sourcePortName: str, isArray: bool) -> tuple[str, str]: ...
def IsArrayConnection(connectedNodeName: str) -> bool: ...
def ReportError(errorMessage: str, errorMessages: Incomplete | None = ..., loggingFunction: Incomplete | None = ...): ...
