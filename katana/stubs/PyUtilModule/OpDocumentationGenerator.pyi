# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
from typing import ClassVar

class AttrTypes:
    kTypeAnyAttribute: ClassVar[int] = ...
    kTypeDoubleAttribute: ClassVar[int] = ...
    kTypeDynamic: ClassVar[int] = ...
    kTypeFloatAttribute: ClassVar[int] = ...
    kTypeGroupAttribute: ClassVar[int] = ...
    kTypeIntAttribute: ClassVar[int] = ...
    kTypeNumericAttribute: ClassVar[int] = ...
    kTypeStringAttribute: ClassVar[int] = ...
    @classmethod
    def toString(cls, value: int) -> str: ...

class OpDescription:
    def __init__(self, opType: str, descriptionAttr: FnAttribute.GroupAttribute): ...
    def _OpDescription__getAttrs(self, descriptionAttr, attrsAttrName): ...
    def _OpDescription__getChildValue(self, groupAttr, childName): ...
    def _OpDescription__getOpArgs(self, descriptionAttr): ...
    def _OpDescription__sort(self, items, descriptionAttr, orderingAttrName): ...

def GenerateRstDocument() -> str: ...
def GetAlignedText(text: str, indent: int = ...) -> str: ...
def GetCleanedText(text: str | None) -> str: ...
def OpDescriptionToRst(opDescription) -> list[str]: ...