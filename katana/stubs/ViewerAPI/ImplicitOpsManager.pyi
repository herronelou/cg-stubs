# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnAttribute as FnAttribute
import PyFnGeolib as FnGeolib
import PyFnGeolibServices as FnGeolibServices
import Nodes3DAPI as Nodes3DAPI
import PyFnGeolib

class ImplicitOpsManager:
    def __init__(self): ...
    def _ImplicitOpsManager__createOpChainFromOpInfo(self, txn: PyFnGeolib.GeolibRuntimeTransaction, opsInfo: list[str, Attribute, bool]) -> list[PyFnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initAfterImplicitOps(self, txn: PyFnGeolib.GeolibRuntimeTransaction) -> list[PyFnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initBeforeImplicitOps(self, txn: PyFnGeolib.GeolibRuntimeTransaction) -> list[PyFnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initImplicitOps(self, txn: PyFnGeolib.GeolibRuntimeTransaction) -> list[PyFnGeolib.GeolibRuntimeOp]: ...
    def _ImplicitOpsManager__initOps(self): ...
    def applyAfterImplicitOps(self, txn, op): ...
    def applyBeforeImplicitOps(self, txn, op): ...
    def applyImplicitOps(self, txn, op): ...