# mypy: disable-error-code="misc, override, no-redef"

import pxr.Ndr as Ndr
import pxr.Sdr as Sdr
import pxr.Tf as Tf
from pxr.Sdf import SdfTypes as SdfTypes

def GetType(property): ...
def IsNodeOSL(node): ...
def TestBasicNode(node, nodeSourceType, nodeDefinitionURI, nodeImplementationURI): ...
def TestBasicProperties(node): ...
def TestShaderPropertiesNode(node): ...
def TestShaderSpecificNode(node): ...
def TestShadingProperties(node): ...