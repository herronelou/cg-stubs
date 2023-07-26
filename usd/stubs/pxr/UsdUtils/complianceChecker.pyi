# mypy: disable-error-code="misc, override, no-redef"

import pxr.Ar as Ar
import pxr.UsdUtils.constantsGroup
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from typing import ClassVar

class ARKitFileExtensionChecker(BaseRuleChecker):
    _allowedFileExtensions: ClassVar[tuple] = ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckZipFile(self, zipFile, packagePath): ...
    @staticmethod
    def GetDescription(): ...

class ARKitLayerChecker(BaseRuleChecker):
    _allowedLayerFormatIds: ClassVar[tuple] = ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckLayer(self, layer): ...
    @staticmethod
    def GetDescription(): ...

class ARKitMaterialBindingChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...

class ARKitPackageEncapsulationChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckDependencies(self, usdStage, layerDeps, assetDeps): ...
    @staticmethod
    def GetDescription(): ...

class ARKitPrimTypeChecker(BaseRuleChecker):
    _allowedPrimTypeNames: ClassVar[tuple] = ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...

class ARKitRootLayerChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckStage(self, usdStage): ...
    @staticmethod
    def GetDescription(): ...

class ARKitShaderChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...

class BaseRuleChecker:
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckDependencies(self, usdStage, layerDeps, assetDeps): ...
    def CheckDiagnostics(self, diagnostics): ...
    def CheckLayer(self, layer): ...
    def CheckPrim(self, prim): ...
    def CheckStage(self, usdStage): ...
    def CheckUnresolvedPaths(self, unresolvedPaths): ...
    def CheckZipFile(self, zipFile, packagePath): ...
    def GetErrors(self): ...
    def GetFailedChecks(self): ...
    def GetWarnings(self): ...
    def ResetCaches(self): ...
    def _AddError(self, msg): ...
    def _AddFailedCheck(self, msg): ...
    def _AddWarning(self, msg): ...
    def _Msg(self, msg): ...

class ByteAlignmentChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckZipFile(self, zipFile, packagePath): ...
    @staticmethod
    def GetDescription(): ...

class ComplianceChecker:
    def __init__(self, arkit: bool = ..., skipARKitRootLayerCheck: bool = ..., rootPackageOnly: bool = ..., skipVariants: bool = ..., verbose: bool = ..., assetLevelChecks: bool = ...) -> None: ...
    def CheckCompliance(self, inputFile): ...
    @staticmethod
    def DumpAllRules(): ...
    def DumpRules(self): ...
    @staticmethod
    def GetARKitRules(skipARKitRootLayerCheck: bool = ...): ...
    @staticmethod
    def GetBaseRules(): ...
    def GetErrors(self): ...
    def GetFailedChecks(self): ...
    @staticmethod
    def GetRules(arkit: bool = ..., skipARKitRootLayerCheck: bool = ...): ...
    def GetWarnings(self): ...
    def _AddError(self, errMsg): ...
    def _AddWarning(self, errMsg): ...
    def _CheckLayer(self, layer): ...
    def _CheckPackage(self, packagePath): ...
    def _CheckPrim(self, prim): ...
    def _Msg(self, msg): ...
    def _TraverseRange(self, primRangeIt, isStageRoot): ...
    def _TraverseVariants(self, prim): ...

class CompressionChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckZipFile(self, zipFile, packagePath): ...
    @staticmethod
    def GetDescription(): ...

class MaterialBindingAPIAppliedChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...

class MissingReferenceChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckDiagnostics(self, diagnostics): ...
    def CheckUnresolvedPaths(self, unresolvedPaths): ...
    @staticmethod
    def GetDescription(): ...

class NodeTypes(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    UsdPreviewSurface: ClassVar[str] = ...
    UsdPrimvarReader: ClassVar[str] = ...
    UsdTransform2d: ClassVar[str] = ...
    UsdUVTexture: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class NormalMapTextureChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...
    def _GetInputValue(self, shader, inputName): ...
    def _GetShaderId(self, shader): ...
    def _TextureIs8Bit(self, asset): ...

class PrimEncapsulationChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...
    def ResetCaches(self): ...
    def _FindConnectableAncestor(self, prim): ...
    def _HasGprimAncestor(self, prim): ...

class ShaderProps(pxr.UsdUtils.constantsGroup.ConstantsGroup):
    Bias: ClassVar[str] = ...
    File: ClassVar[str] = ...
    Normal: ClassVar[str] = ...
    Scale: ClassVar[str] = ...
    SourceColorSpace: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class SkelBindingAPIAppliedChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    @staticmethod
    def GetDescription(): ...

class StageMetadataChecker(BaseRuleChecker):
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckStage(self, usdStage): ...
    @staticmethod
    def GetDescription(): ...

class TextureChecker(BaseRuleChecker):
    _basicUSDZImageFormats: ClassVar[tuple] = ...
    _extraUSDZ_OIIOImageFormats: ClassVar[str] = ...
    _unsupportedImageFormats: ClassVar[list] = ...
    def __init__(self, verbose, consumerLevelChecks, assetLevelChecks) -> None: ...
    def CheckPrim(self, prim): ...
    def CheckStage(self, usdStage): ...
    @staticmethod
    def GetDescription(): ...
    def _CheckTexture(self, texAssetPath, inputPath): ...

def _IsPackageOrPackagedLayer(layer): ...
