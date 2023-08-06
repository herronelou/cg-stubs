# mypy: disable-error-code="misc, override, attr-defined, no-redef, assignment"

import PyFnGeolib as FnGeolib
import PyFnGeolibProducers as FnGeolibProducers
import PyFnGeolib
import PyFnGeolibProducers
import PyUtilModule.WorkingSet
from PyUtilModule.WorkingSet import LocationStateMap as LocationStateMap, WorkingSet as WorkingSet
from _typeshed import Incomplete
from typing import ClassVar, Set, Tuple

class WorkingSetClient:
    _WorkingSetClient__DELEGATE_TO_CLIENT: ClassVar[list] = ...
    _WorkingSetClient__DISALLOWED_WHEN_WORKINGSET_SET: ClassVar[list] = ...
    def __init__(self, txn: PyFnGeolib.GeolibRuntimeTransaction, op: PyFnGeolib.GeolibRuntimeOp) -> None: ...
    def _WorkingSetClient__applyWorkingSetToClient(self): ...
    def _WorkingSetClient__locationStateChangedCallback(self, stateChanges: list[tuple], workingSet: WorkingSet, sender: object | None): ...
    def _WorkingSetClient__openIncludedWithChildrenLocations(self, locationPaths: Incomplete | None = ...): ...
    def eventsFiltered(self) -> bool: ...
    def forceAsyncCookLocation(self, locationPath: str): ...
    def getLocationEvents(self, maxEvents: Incomplete | None = ...) -> list[PyFnGeolib.LocationDataChange]: ...
    def getProducerAtLocation(self, locationPath: str, producerType: str = ...) -> PyFnGeolibProducers.GeometryProducer: ...
    def getWorkingSet(self) -> PyUtilModule.WorkingSet.WorkingSet | None: ...
    def removeWorkingSet(self, openLocations: Incomplete | None = ..., activeLocations: Incomplete | None = ...): ...
    def setEventsFiltered(self, eventsFiltered: bool): ...
    def setOp(self, transaction: PyFnGeolib.GeolibRuntimeTransaction, op: PyFnGeolib.GeolibRuntimeOp): ...
    def setWorkingSet(self, workingSet: WorkingSet): ...
    def updateFollowingPotentialOpChange(self): ...
    def __dir__(self) -> list[str]: ...
    def __getattr__(self, name): ...
