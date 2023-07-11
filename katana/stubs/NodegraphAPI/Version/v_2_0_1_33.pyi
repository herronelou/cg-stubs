# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar

class Updater2_0_1_33(Updater):
    VERSION: ClassVar[tuple] = ...
    _NewScriptSource: ClassVar[str] = ...
    _OldScriptSource: ClassVar[str] = ...
    @classmethod
    def _Updater2_0_1_33__iterChildrenRecursive(cls, node): ...
    def upgrade_GafferThree(self, node, document): ...