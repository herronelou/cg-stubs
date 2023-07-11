# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import NodegraphAPI.Constants.ApplyWhenOptions as ApplyWhenOptions
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

class Updater2_0_1_5(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade_AttributeFile_In(self, node): ...
    def upgrade_AttributeModifierDefine(self, node): ...
    def upgrade_AttributeScript(self, node): ...
    def upgrade_GenericOp(self, node): ...
    def upgrade_OpScript(self, node): ...

def renameApplyWhenValues(node): ...
