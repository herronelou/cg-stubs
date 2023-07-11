# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyXmlIO
import NodegraphAPI.Xio as Xio
from NodegraphAPI.Version.Updater import Updater as Updater
from typing import ClassVar, Set, Tuple

_Version: tuple

class Updater2_2_3_1(Updater):
    VERSION: ClassVar[tuple] = ...
    def upgrade__LightFilterReferencePackageInternal(self, node: PyXmlIO.Element, document: PyXmlIO.Element): ...
