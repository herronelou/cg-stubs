# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute
import typing
from typing import Set, Tuple

def CalcTransformMatrixAtExistingTimes(attr: PyFnAttribute.GroupAttribute) -> Tuple[PyFnAttribute.DoubleAttribute, bool]: ...
def CalcTransformMatrixAtTime(attr: object, time: float) -> Tuple[PyFnAttribute.DoubleAttribute, bool]: ...
def CalcTransformMatrixAtTimes(attr: PyFnAttribute.GroupAttribute, times: list[float]) -> Tuple[PyFnAttribute.DoubleAttribute, bool]: ...
def CalcTransformedBoundsAtExistingTimes(xform: PyFnAttribute.Attribute, bounds: PyFnAttribute.DoubleAttribute) -> PyFnAttribute.DoubleAttribute: ...
def CollapseBoundsTimeSamples(bounds: PyFnAttribute.DoubleAttribute) -> PyFnAttribute.DoubleAttribute: ...
def MergeBounds(bounds1: PyFnAttribute.DoubleAttribute, bounds2: PyFnAttribute.DoubleAttribute) -> PyFnAttribute.DoubleAttribute: ...
def PushMatrixAttr(xform: object, matrix: typing.Sequence) -> PyFnAttribute.Attribute: ...
def PushOriginAttr(xform: object) -> PyFnAttribute.Attribute: ...
def PushRotateAttr(xform: object, angle: float, x: float, y: float, z: float) -> PyFnAttribute.Attribute: ...
def PushScaleAttr(xform: object, x: float, y: float, z: float) -> PyFnAttribute.Attribute: ...
def PushTranslateAttr(xform: object, x: float, y: float, z: float) -> PyFnAttribute.Attribute: ...
