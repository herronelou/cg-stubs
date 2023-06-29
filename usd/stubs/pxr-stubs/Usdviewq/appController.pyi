# mypy: disable_error_code = misc
import pxr.Ar as Ar
import pxr.Glf as Glf
import PySide6.QtCore
import pxr.Sdf as Sdf
import pxr.Tf as Tf
import pxr.Usd as Usd
import pxr.UsdAppUtils as UsdAppUtils
import pxr.UsdGeom as UsdGeom
import pxr.UsdImagingGL as UsdImagingGL
import pxr.UsdShade as UsdShade
import pxr.UsdUtils as UsdUtils
import pxr.Usdviewq.adjustDefaultMaterial as adjustDefaultMaterial
import pxr.Usdviewq.adjustFreeCamera as adjustFreeCamera
import pxr.Usdviewq.plugin as plugin
import pxr.Usdviewq.preferences as preferences
import pxr.Usdviewq.prettyPrint as prettyPrint
from _typeshed import Incomplete
from pxr.UsdAppUtils.complexityArgs import RefinementComplexities as RefinementComplexities
from pxr.UsdUtils.constantsGroup import ConstantsGroup as ConstantsGroup
from pxr.Usdviewq import Utils as Utils
from pxr.Usdviewq.attributeViewContextMenu import AttributeViewContextMenu as AttributeViewContextMenu
from pxr.Usdviewq.common import BusyContext as BusyContext, CameraMaskModes as CameraMaskModes, ClearColors as ClearColors, ColorCorrectionModes as ColorCorrectionModes, Drange as Drange, DumpMallocTags as DumpMallocTags, GetAssetCreationTime as GetAssetCreationTime, GetEnclosingModelPrim as GetEnclosingModelPrim, GetPrimsLoadability as GetPrimsLoadability, GetPropertyColor as GetPropertyColor, GetPropertyTextFont as GetPropertyTextFont, GetRootLayerStackInfo as GetRootLayerStackInfo, GetValueAndDisplayString as GetValueAndDisplayString, HasSessionVis as HasSessionVis, HighlightColors as HighlightColors, InvisRootPrims as InvisRootPrims, KeyboardShortcuts as KeyboardShortcuts, LayerInfo as LayerInfo, PickModes as PickModes, PrimNotFoundException as PrimNotFoundException, PrintWarning as PrintWarning, PropTreeWidgetTypeIsRel as PropTreeWidgetTypeIsRel, PropertyViewDataRoles as PropertyViewDataRoles, PropertyViewIcons as PropertyViewIcons, PropertyViewIndex as PropertyViewIndex, RenderModes as RenderModes, ResetSessionVisibility as ResetSessionVisibility, SelectionHighlightModes as SelectionHighlightModes, ShadedRenderModes as ShadedRenderModes, Timer as Timer, UIBaseColors as UIBaseColors, UIFonts as UIFonts, UIPropertyValueSourceColors as UIPropertyValueSourceColors
from pxr.Usdviewq.configController import ConfigController as ConfigController
from pxr.Usdviewq.customAttributes import BoundingBoxAttribute as BoundingBoxAttribute, CustomAttribute as CustomAttribute, LocalToWorldXformAttribute as LocalToWorldXformAttribute, ResolvedBoundMaterial as ResolvedBoundMaterial, _GetCustomAttributes as _GetCustomAttributes
from pxr.Usdviewq.headerContextMenu import HeaderContextMenu as HeaderContextMenu
from pxr.Usdviewq.layerStackContextMenu import LayerStackContextMenu as LayerStackContextMenu
from pxr.Usdviewq.legendUtil import ToggleLegendWithBrowser as ToggleLegendWithBrowser
from pxr.Usdviewq.mainWindowUI import Ui_MainWindow as Ui_MainWindow
from pxr.Usdviewq.primContextMenu import PrimContextMenu as PrimContextMenu
from pxr.Usdviewq.primTreeWidget import PrimTreeWidget as PrimTreeWidget
from pxr.Usdviewq.primViewItem import PrimViewColumnIndex as PrimViewColumnIndex, PrimViewItem as PrimViewItem
from pxr.Usdviewq.pythonInterpreter import Myconsole as Myconsole
from pxr.Usdviewq.rootDataModel import ChangeNotice as ChangeNotice, RootDataModel as RootDataModel
from pxr.Usdviewq.selectionDataModel import SelectionDataModel as SelectionDataModel
from pxr.Usdviewq.settings import ConfigManager as ConfigManager, StateSource as StateSource
from pxr.Usdviewq.stageView import StageView as StageView
from pxr.Usdviewq.usdviewApi import UsdviewApi as UsdviewApi
from pxr.Usdviewq.variantComboBox import VariantComboBox as VariantComboBox
from pxr.Usdviewq.viewSettingsDataModel import ViewSettingsDataModel as ViewSettingsDataModel
from typing import Any, ClassVar

class AppController(PySide6.QtCore.QObject):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, parserData, resolverContextFn): ...
    def GrabViewportShot(self, cropToAspectRatio: bool = ...): ...
    def GrabWindowShot(self): ...
    def _HUDInfoChanged(self): ...
    def _UpdateTimeSamples(self, resetStageDataOnly: bool = ...): ...
    def _accountForFlattening(self, shape): ...
    def _addRichTextIndicators(self, s): ...
    def _adjustDefaultMaterial(self, checked): ...
    def _adjustFreeCamera(self, checked): ...
    def _advanceFrame(self): ...
    def _advanceFrameForPlayback(self): ...
    def _ambientOnlyClicked(self, checked: Incomplete | None = ...): ...
    def _applyMoreRendererSettings(self): ...
    def _applyStageOpenLayerMutes(self, stage, muteLayersRe): ...
    def _attrViewFindNext(self): ...
    def _cacheViewerModeEscapeSizes(self, pos: Incomplete | None = ..., index: Incomplete | None = ...): ...
    def _calculateGeomCounts(self, prim, frame): ...
    def _cameraSelectionChanged(self, camera): ...
    def _changeBgColor(self, mode): ...
    def _changeColorCorrection(self, mode): ...
    def _changeComplexity(self, action): ...
    def _changeHighlightColor(self, color): ...
    def _changeInterpolationType(self, interpolationType): ...
    def _changePickMode(self, mode): ...
    def _changePrimViewDepth(self, action): ...
    def _changeRenderMode(self, mode): ...
    def _changeSelHighlightMode(self, mode): ...
    def _cleanAndClose(self): ...
    def _cleanStr(self, s, repl): ...
    def _clearCaches(self, preserveCamera: bool = ...): ...
    def _clearGeomCountsForPrimPath(self, primPath): ...
    def _closeStage(self): ...
    def _comparePaths(self, path1, path2): ...
    def _compositionTreeContextMenu(self, point): ...
    def _computeDisplayPredicate(self): ...
    def _configureColorManagement(self): ...
    def _configurePauseAction(self): ...
    def _configurePlugins(self): ...
    def _configureRendererAovs(self): ...
    def _configureRendererCommands(self): ...
    def _configureRendererPlugins(self): ...
    def _configureRendererSettings(self): ...
    def _configureStopAction(self): ...
    def _copyViewerImage(self): ...
    def _currentPathChanged(self): ...
    def _decrementComplexity(self): ...
    def _disableOCIOAction(self): ...
    def _displayPurposeChanged(self): ...
    def _drawFirstImage(self): ...
    def _expandPrims(self, prims, expand: bool = ...): ...
    def _expandToDepth(self, depth, suppressTiming: bool = ...): ...
    def _findClosestFrameIndex(self, timeSample): ...
    def _findIndentPos(self, s): ...
    def _findPrims(self, pattern, useRegex: bool = ...): ...
    def _formatMetadataValueView(self, val): ...
    def _frameSelection(self): ...
    def _frameStringChanged(self): ...
    def _getCommonPrims(self, pathsList): ...
    def _getExpandedPrimViewPrims(self): ...
    def _getFilteredChildren(self, prim): ...
    def _getGeomCounts(self, prim, frame): ...
    def _getHUDStatKeys(self): ...
    def _getItemAtPath(self, path, ensureExpanded: bool = ...): ...
    def _getPathsFromItems(self, items, prune: bool = ...): ...
    def _getPrimFromPropString(self, p): ...
    def _getPrimsFromPaths(self, paths): ...
    def _getPropertiesDict(self): ...
    def _getSaveFileName(self, caption, recommendedFilename): ...
    def _getSelectedObject(self): ...
    def _incrementComplexity(self): ...
    def _invokeRendererCommand(self, cmd): ...
    def _isHUDVisible(self): ...
    def _isMatch(self, pattern, isRegex, prim, useDisplayName): ...
    def _itemClicked(self, item, col): ...
    def _itemPressed(self, item, col): ...
    def _layerStackContextMenu(self, point): ...
    def _limitToolTipSize(self, s, isList: bool = ...): ...
    def _limitValueDisplaySize(self, s): ...
    def _makeTimer(self, label, printTiming: bool = ...): ...
    def _maxToolTipHeight(self): ...
    def _maxToolTipWidth(self): ...
    def _moreRendererSettings(self): ...
    def _onCompositionSelectionChanged(self, curr: Incomplete | None = ..., prev: Incomplete | None = ...): ...
    def _onDomeLightClicked(self, checked: Incomplete | None = ...): ...
    def _onDomeLightTexturesVisibleClicked(self, checked: Incomplete | None = ...): ...
    def _onPrimsChanged(self, primsChange, propertiesChange): ...
    def _openFile(self): ...
    def _openSettings(self, defaultSettings, config): ...
    def _openStage(self, usdFilePath, sessionFilePath, populationMaskPaths, muteLayersRe): ...
    def _otherAov(self): ...
    @classmethod
    def _outputBaseDirectory(cls): ...
    def _pickCameraMaskColor(self): ...
    def _pickCameraReticlesColor(self): ...
    def _playClicked(self): ...
    def _populateChildren(self, item, depth: int = ..., maxDepth: int = ..., childrenToAdd: Incomplete | None = ...): ...
    def _populateItem(self, prim, depth: int = ..., maxDepth: int = ...): ...
    def _populatePropertyInspector(self): ...
    def _populateRoots(self): ...
    def _primLegendToggleCollapse(self): ...
    def _primSelectionChanged(self, added, removed): ...
    def _primViewContextMenu(self, point): ...
    def _primViewExpanded(self, index): ...
    def _primViewFindNext(self): ...
    def _primViewHeaderContextMenu(self, point): ...
    def _primsFromSelectionRanges(self, ranges): ...
    def _propSelectionChanged(self): ...
    def _propertyLegendToggleCollapse(self): ...
    def _propertyViewContextMenu(self, point): ...
    def _propertyViewCurrentItemChanged(self, currentItem, lastItem): ...
    def _propertyViewDeselectItem(self, item): ...
    def _propertyViewHeaderContextMenu(self, point): ...
    def _propertyViewSelectionChanged(self): ...
    def _rangeBeginChanged(self): ...
    def _rangeEndChanged(self): ...
    def _redrawOptionToggled(self, checked): ...
    def _refreshAttributeValue(self): ...
    def _refreshBBox(self): ...
    def _refreshBBoxMenu(self): ...
    def _refreshCameraGuidesMenu(self): ...
    def _refreshCameraListAndMenu(self, preserveCurrCamera): ...
    def _refreshCameraMaskMenu(self): ...
    def _refreshCameraMenu(self): ...
    def _refreshCameraReticlesMenu(self): ...
    def _refreshClearColorsMenu(self): ...
    def _refreshColorCorrectionModeMenu(self): ...
    def _refreshComplexityMenu(self): ...
    def _refreshDisplayPurposesMenu(self): ...
    def _refreshHUDMenu(self): ...
    def _refreshLightsMenu(self): ...
    def _refreshPickModeMenu(self): ...
    def _refreshPrimViewSelection(self, expandedPrims): ...
    def _refreshRedrawOnScrub(self): ...
    def _refreshRenderModeMenu(self): ...
    def _refreshRolloverPrimInfoMenu(self): ...
    def _refreshSelectionHighlightColorMenu(self): ...
    def _refreshSelectionHighlightingMenu(self): ...
    def _refreshShowPrimMenu(self): ...
    def _refreshViewMenu(self): ...
    def _refreshViewMenubar(self): ...
    def _reloadFixedUI(self, resetStageDataOnly: bool = ...): ...
    def _reloadStage(self): ...
    def _reloadVaryingUI(self): ...
    def _rendererAovChanged(self, aov): ...
    def _rendererPluginChanged(self, plugin): ...
    def _rendererSettingsFlagChanged(self, action): ...
    def _reopenStage(self): ...
    def _resetGUI(self): ...
    def _resetMoreRendererSettings(self): ...
    def _resetPrimView(self, restoreSelection: bool = ...): ...
    def _resetPrimViewVis(self, selItemsOnly: bool = ..., authoredVisHasChanged: bool = ...): ...
    def _resetSettings(self): ...
    def _resetView(self, selectPrim: Incomplete | None = ...): ...
    def _resizePrimView(self): ...
    def _retreatFrame(self): ...
    def _saveFlattenedAs(self): ...
    def _saveOverridesAs(self): ...
    def _saveViewerImage(self): ...
    def _scheduleResizePrimView(self): ...
    def _selectionChanged(self, added, removed): ...
    def _setComplexity(self, complexity): ...
    def _setFrameIndex(self, frameIndex): ...
    def _setPlayShortcut(self): ...
    def _setPlaybackAvailability(self, enabled: bool = ...): ...
    def _setSelectedPrimsActivation(self, active): ...
    def _setStyleSheetUsingState(self): ...
    def _setUseExtentsHint(self): ...
    def _setupCustomFont(self): ...
    def _showDebugFlags(self): ...
    def _showHUDChanged(self): ...
    def _showHUD_ComplexityChanged(self): ...
    def _showHUD_GPUstatsChanged(self): ...
    def _showHUD_InfoChanged(self): ...
    def _showHUD_PerformanceChanged(self): ...
    def _showHydraSceneBrowser(self): ...
    def _showInterpreter(self): ...
    def _showPrimContextMenu(self, item): ...
    def _sliderMoved(self, frameIndex): ...
    def _startQtShutdownTimer(self): ...
    def _stepSizeChanged(self): ...
    def _stopQtShutdownTimer(self): ...
    def _storeAndReturnViewState(self): ...
    def _tallyPrimStats(self, prim): ...
    def _toggleAutoComputeClippingPlanes(self): ...
    def _toggleCullBackfaces(self): ...
    def _toggleDisplayCameraOracles(self): ...
    def _toggleDisplayGuide(self): ...
    def _toggleDisplayPrimId(self): ...
    def _toggleDisplayProxy(self): ...
    def _toggleDisplayRender(self): ...
    def _toggleEnableSceneLights(self): ...
    def _toggleEnableSceneMaterials(self): ...
    def _toggleFramedView(self): ...
    def _togglePause(self): ...
    def _togglePreferences(self, checked): ...
    def _toggleRolloverPrimInfo(self): ...
    def _toggleShowAABBox(self): ...
    def _toggleShowAbstractPrims(self): ...
    def _toggleShowBBoxPlayback(self): ...
    def _toggleShowBBoxes(self): ...
    def _toggleShowInactivePrims(self): ...
    def _toggleShowOBBox(self): ...
    def _toggleShowPrimDisplayName(self): ...
    def _toggleShowPrototypePrims(self): ...
    def _toggleShowUndefinedPrims(self): ...
    def _toggleStop(self): ...
    def _toggleViewerMode(self): ...
    def _trimWidth(self, s, isList: bool = ...): ...
    def _updateCameraMaskMenu(self): ...
    def _updateCameraMaskOutlineMenu(self): ...
    def _updateCameraReticlesInsideMenu(self): ...
    def _updateCameraReticlesOutsideMenu(self): ...
    def _updateCompositionView(self, obj: Incomplete | None = ...): ...
    def _updateEditMenu(self): ...
    def _updateForStageChanges(self, hasPrimResync: bool = ...): ...
    def _updateGUIForFrameChange(self): ...
    def _updateHUDGeomCounts(self): ...
    def _updateHUDPrimStats(self): ...
    def _updateLayerStackView(self, obj: Incomplete | None = ...): ...
    def _updateMetadataView(self, obj: Incomplete | None = ...): ...
    def _updateNavigationMenu(self): ...
    def _updateOnFrameChange(self): ...
    def _updatePrimPathText(self): ...
    def _updatePrimView(self): ...
    def _updatePrimViewSelection(self, added, removed): ...
    def _updatePropertiesFromPropertyView(self): ...
    def _updatePropertyInspector(self, index: Incomplete | None = ..., obj: Incomplete | None = ...): ...
    def _updatePropertyView(self): ...
    def _updatePropertyViewInternal(self): ...
    def _updatePropertyViewSelection(self): ...
    def _viewSettingChanged(self): ...
    def activateSelectedPrims(self): ...
    @classmethod
    def clearSettings(cls): ...
    def deactivateSelectedPrims(self): ...
    def editComplete(self, msg): ...
    def getActiveCamera(self): ...
    def getSelectedItems(self): ...
    def invisSelectedPrims(self): ...
    def isViewerMode(self): ...
    def loadSelectedPrims(self): ...
    def onPrimSelected(self, path, instanceIndex, topLevelPath, topLevelInstanceIndex, point, button, modifiers): ...
    def onRollover(self, path, instanceIndex, topLevelPath, topLevelInstanceIndex, modifiers): ...
    def onStageViewMouseDrag(self): ...
    def processNavKeyEvent(self, kpEvent): ...
    def removeVisSelectedPrims(self): ...
    def resetSessionVisibility(self): ...
    def saveFrame(self, fileName): ...
    def selectBindingRelForPurpose(self, materialPurpose): ...
    def selectBoundFullMaterial(self): ...
    def selectBoundMaterialForPurpose(self, materialPurpose): ...
    def selectBoundPreviewMaterial(self): ...
    def selectEnclosingModel(self): ...
    def selectFullBindingRel(self): ...
    def selectPreviewBindingRel(self): ...
    def selectPseudoroot(self): ...
    def setFrame(self, frame): ...
    def setFrameField(self, frame): ...
    def setViewerMode(self, viewerMode): ...
    def statusMessage(self, msg, timeout: int = ...): ...
    def unloadSelectedPrims(self): ...
    def updateGUI(self): ...
    def visOnlySelectedPrims(self): ...
    def visSelectedPrims(self): ...
    def __del__(self): ...

class Blocker:
    def __init__(self): ...
    def blocked(self): ...
    def __enter__(self): ...
    def __exit__(self, *args): ...

class HUDEntries(ConstantsGroup):
    CV: ClassVar[str] = ...
    FACE: ClassVar[str] = ...
    GETBOUNDS: ClassVar[str] = ...
    NOTYPE: ClassVar[str] = ...
    PLAYBACK: ClassVar[str] = ...
    PRIM: ClassVar[str] = ...
    RENDER: ClassVar[str] = ...
    VERT: ClassVar[str] = ...
    _all: ClassVar[tuple] = ...

class LayerStackViewColumnIndex(ConstantsGroup):
    LAYER: ClassVar[int] = ...
    OFFSET: ClassVar[int] = ...
    PATH: ClassVar[int] = ...
    VALUE: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class MainWindow(PySide6.QtWidgets.QMainWindow):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, closeFunc): ...
    def closeEvent(self, event): ...

class PropertyIndex(ConstantsGroup):
    COMPOSITION: ClassVar[int] = ...
    LAYERSTACK: ClassVar[int] = ...
    METADATA: ClassVar[int] = ...
    VALUE: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class UIDefaults(ConstantsGroup):
    ATTRIBUTE_INSPECTOR_WIDTH: ClassVar[int] = ...
    ATTRIBUTE_VIEW_WIDTH: ClassVar[int] = ...
    BOTTOM_HEIGHT: ClassVar[int] = ...
    PRIM_VIEW_WIDTH: ClassVar[int] = ...
    STAGE_VIEW_WIDTH: ClassVar[int] = ...
    TOP_HEIGHT: ClassVar[int] = ...
    _all: ClassVar[tuple] = ...

class UIStateProxySource(StateSource):
    def __init__(self, mainWindow, parent, name): ...
    def onSaveState(self, state): ...

class UsdviewDataModel(RootDataModel):
    staticMetaObject: ClassVar[PySide6.QtCore.QMetaObject] = ...
    def __init__(self, makeTimer, settings): ...
    def _emitPrimsChanged(self, primChange, propertyChange): ...
    @property
    def selection(self) -> Any: ...
    @property
    def viewSettings(self) -> Any: ...