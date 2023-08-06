# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_18(Updater):
    VERSION: ClassVar[tuple] = ...
    @classmethod
    def _Updater2_0_1_18__getOpScript_MarkNotInInput(cls): ...
    @classmethod
    def _Updater2_0_1_18__getOpScript_StripNotAdopted(cls): ...
    @classmethod
    def _Updater2_0_1_18__getOpScript_StripNotInInput(cls): ...
    @classmethod
    def _Updater2_0_1_18__iterChildrenRecursive(cls, node: NodegraphAPI.Node): ...
    @classmethod
    def _Updater2_0_1_18__setOpScriptForNode(cls, node, script): ...
    def upgrade_GafferThree(self, node, document): ...
