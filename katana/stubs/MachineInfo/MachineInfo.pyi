# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

from typing import Set, Tuple

def GetFreeSpaceB(dirName): ...
def GetNumberOfProcessors(quiet: bool = ..., raiseExc: bool = ...): ...
def GetTotalMemoryKB(quiet: bool = ..., raiseExc: bool = ...): ...
def GetUsedSpaceB(dirName): ...
