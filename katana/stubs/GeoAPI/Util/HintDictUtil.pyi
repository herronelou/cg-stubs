# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
from _typeshed import Incomplete

g_evalCache: dict

def ContainerHintDictFromAttr(attr, path: str = ..., output: Incomplete | None = ..., allowGroupAttrForm: bool = ...): ...
def FlushCache(): ...
def HintDictFromAttr(attr, allowGroupAttrForm: bool = ...): ...
def _AttrToObject(attr): ...