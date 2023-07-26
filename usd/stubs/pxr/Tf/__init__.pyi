# mypy: disable-error-code="misc, override, no-redef"

import Boost.Python
import pxr.Ar
import types
import typing
from typing import Any, Callable, ClassVar, overload

Fatal: Callable
GetCodeLocation: Callable
PrepareModule: Callable
PreparePythonModule: Callable
RaiseCodingError: Callable
RaiseRuntimeError: Callable
Status: Callable
TF_APPLICATION_EXIT_TYPE: DiagnosticType
TF_DIAGNOSTIC_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_CODING_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_FATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_NONFATAL_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_RUNTIME_ERROR_TYPE: DiagnosticType
TF_DIAGNOSTIC_STATUS_TYPE: DiagnosticType
TF_DIAGNOSTIC_WARNING_TYPE: DiagnosticType
Warn: Callable
_Alpha: _TestEnum
_Bravo: _TestEnum
_Charlie: _TestEnum
_Delta: _TestEnum
__MFB_FULL_PACKAGE_NAME: str

class CallContext(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def file(self) -> str: ...
    @property
    def function(self) -> str: ...
    @property
    def line(self) -> int: ...
    @property
    def prettyFunction(self) -> str: ...

class CppException(Exception): ...

class Debug(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetDebugSymbolDescription(cls, arg1: str | pxr.Ar.ResolvedPath) -> str: ...
    @classmethod
    def GetDebugSymbolDescriptions(cls) -> str: ...
    @classmethod
    def GetDebugSymbolNames(cls) -> list[str]: ...
    @classmethod
    def IsDebugSymbolNameEnabled(cls, arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def SetDebugSymbolsByName(cls, pattern: str | pxr.Ar.ResolvedPath, value: bool) -> list[str]: ...
    @classmethod
    def SetOutputFile(cls, arg1: FILE) -> None: ...

class DiagnosticType(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...

class Enum(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @classmethod
    def GetValueFromFullName(cls, arg1: str | pxr.Ar.ResolvedPath) -> tuple[Enum, bool]: ...

class Error(_DiagnosticBase):
    class Mark(Boost.Python.instance):
        __instance_size__: ClassVar[int] = ...
        def __init__(self) -> None: ...
        def Clear(self) -> bool: ...
        def GetErrors(self) -> list: ...
        def IsClean(self) -> bool: ...
        def SetMark(self) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def errorCode(self) -> Enum: ...
    @property
    def errorCodeString(self): ...

class ErrorException(RuntimeError):
    __init__: ClassVar[Callable] = ...

class MallocTag(Boost.Python.instance):
    class CallTree(Boost.Python.instance):
        class CallSite(Boost.Python.instance):
            def __init__(self, *args, **kwargs) -> None: ...
            @property
            def nBytes(self): ...
            @property
            def name(self): ...

        class PathNode(Boost.Python.instance):
            def __init__(self, *args, **kwargs) -> None: ...
            def GetChildren(self) -> list: ...
            @property
            def nAllocations(self): ...
            @property
            def nBytes(self): ...
            @property
            def nBytesDirect(self): ...
            @property
            def siteName(self): ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetCallSites(self) -> list: ...
        def GetPrettyPrintString(self) -> str: ...
        def GetRoot(self) -> MallocTag.CallTree.PathNode: ...
        def LogReport(self, rootName: str | pxr.Ar.ResolvedPath = ...) -> str: ...
        @overload
        def Report(self, fileName: str | pxr.Ar.ResolvedPath, rootName: str | pxr.Ar.ResolvedPath = ...) -> None: ...
        @overload
        def Report(self, rootName: str | pxr.Ar.ResolvedPath = ...) -> None: ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetCallStacks(self) -> list: ...
    @classmethod
    def GetCallTree(cls) -> MallocTag.CallTree: ...
    @classmethod
    def GetMaxTotalBytes(cls) -> int: ...
    @classmethod
    def GetTotalBytes(cls) -> int: ...
    @classmethod
    def Initialize(cls, arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
    @classmethod
    def IsInitialized(cls) -> bool: ...
    @classmethod
    def SetCapturedMallocStacksMatchList(cls, arg1: str | pxr.Ar.ResolvedPath) -> None: ...
    @classmethod
    def SetDebugMatchList(cls, arg1: str | pxr.Ar.ResolvedPath) -> None: ...

class NamedTemporaryFile:
    __init__: ClassVar[Callable] = ...
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...
    @property
    def name(self): ...

class Notice(Boost.Python.instance):
    class Listener(Boost.Python.instance):
        def __init__(self, *args, **kwargs) -> None: ...
        @overload
        def Revoke(self) -> None: ...
        @overload
        def Revoke(self) -> typing.Any: ...
    def __init__(self) -> None: ...
    @overload
    @classmethod
    def Register(cls, noticeType, callback, sender) -> Listener: ...
    @overload
    @classmethod
    def Register(cls, arg1: Type, arg2: object, arg3: object) -> Listener: ...
    @overload
    @classmethod
    def Register(cls, arg1: Type, arg2: Method, arg3: Sender) -> Listener: ...
    @overload
    def RegisterGlobally(self, noticeType, callback) -> Listener: ...
    @overload
    def RegisterGlobally(self, arg1: Type, arg2: object) -> Listener: ...
    @overload
    def Send(self, sender) -> typing.Any: ...
    @overload
    def Send(self, arg2: object) -> int: ...
    @overload
    def SendGlobally(self) -> int: ...
    @overload
    def SendGlobally(self) -> typing.Any: ...

class PyModuleWasLoaded(Notice):
    def __init__(self, *args, **kwargs) -> None: ...
    def name(self) -> str: ...

class RefPtrTracker(Boost.Python.instance):
    def __init__(self) -> None: ...
    def GetAllTracesReport(self) -> str: ...
    def GetAllWatchedCountsReport(self) -> str: ...
    def GetTracesReportForWatched(self, arg2: int) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class ScopeDescription(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def SetDescription(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def __enter__(self) -> ScopeDescription: ...
    def __exit__(self, type: type[BaseException] | None, value: BaseException | None, traceback: types.TracebackType | None) -> None: ...

class ScriptModuleLoader(Boost.Python.instance):
    def __init__(self) -> None: ...
    def GetModuleNames(self) -> list[str]: ...
    def GetModulesDict(self) -> dict: ...
    def WriteDotFile(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def _LoadModulesForLibrary(self, arg2: object) -> None: ...
    def _RegisterLibrary(self, arg2: object, arg3: object, arg4: object) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class Singleton(Boost.Python.instance):
    def __init__(self) -> None: ...

class StatusObject(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None: ...

class Stopwatch(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def AddFrom(self, arg2: Stopwatch) -> None: ...
    def Reset(self) -> None: ...
    def Start(self) -> None: ...
    def Stop(self) -> None: ...
    @property
    def microseconds(self) -> int: ...
    @property
    def milliseconds(self) -> int: ...
    @property
    def nanoseconds(self) -> int: ...
    @property
    def sampleCount(self) -> int: ...
    @property
    def seconds(self) -> float: ...

class TemplateString(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def GetEmptyMapping(self) -> dict: ...
    def GetParseErrors(self) -> list[str]: ...
    def SafeSubstitute(self, arg2: dict) -> str: ...
    def Substitute(self, arg2: dict) -> str: ...
    @property
    def template(self) -> str: ...
    @property
    def valid(self): ...

class Tf_PyEnumWrapper(Enum):
    def __init__(self, *args, **kwargs) -> None: ...
    @overload
    def __and__(self, arg2: int) -> Any: ...
    @overload
    def __and__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __invert__(self) -> Any: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    @overload
    def __or__(self, arg2: int) -> Any: ...
    @overload
    def __or__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    def __rand__(self, arg2: int) -> Any: ...
    def __ror__(self, arg2: int) -> Any: ...
    def __rxor__(self, arg2: int) -> Any: ...
    @overload
    def __xor__(self, arg2: int) -> Any: ...
    @overload
    def __xor__(self, arg2: Tf_PyEnumWrapper) -> Any: ...
    @property
    def displayName(self): ...
    @property
    def fullName(self): ...
    @property
    def name(self): ...
    @property
    def value(self): ...

class Tf_TestAnnotatedBoolResult(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self, arg2: bool, arg3: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __getitem__(self, arg2: int) -> Any: ...
    def __iter__(self) -> typing.Iterator[Any]: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def annotation(self): ...

class Tf_TestPyContainerConversions(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def GetPairTimesTwo(self) -> Any: ...
    def GetTokens(self) -> Any: ...
    def GetVectorTimesTwo(self) -> Any: ...

class Tf_TestPyOptional(Boost.Python.instance):
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...
    def TakesOptional(self, optString: object = ..., optStrvec: object = ...) -> tuple: ...
    def TestOptionalChar(self) -> Any: ...
    def TestOptionalDouble(self) -> Any: ...
    def TestOptionalFloat(self) -> Any: ...
    def TestOptionalInt(self) -> Any: ...
    def TestOptionalLong(self) -> Any: ...
    def TestOptionalShort(self) -> Any: ...
    def TestOptionalString(self) -> Any: ...
    def TestOptionalStringVector(self) -> Any: ...
    def TestOptionalUChar(self) -> Any: ...
    def TestOptionalUInt(self) -> Any: ...
    def TestOptionalULong(self) -> Any: ...
    def TestOptionalUShort(self) -> Any: ...

class Type(Boost.Python.instance):
    Unknown: ClassVar[Type] = ...
    __instance_size__: ClassVar[int] = ...
    @overload
    def __init__(self, arg2: Type) -> None: ...
    @overload
    def __init__(self) -> None: ...
    @classmethod
    def AddAlias(cls, arg1: Type, arg2: Type, arg3: str | pxr.Ar.ResolvedPath) -> None: ...
    @classmethod
    def Define(cls, arg1: object) -> Type: ...
    @classmethod
    def Find(cls, arg1: object) -> Type: ...
    @classmethod
    def FindByName(cls, arg1: str | pxr.Ar.ResolvedPath) -> Type: ...
    @classmethod
    def FindDerivedByName(cls, arg1: Type, arg2: str | pxr.Ar.ResolvedPath) -> Type: ...
    def GetAliases(self, arg2: Type) -> tuple: ...
    def GetAllAncestorTypes(self) -> tuple: ...
    def GetAllDerivedTypes(self) -> tuple: ...
    @classmethod
    def GetRoot(cls) -> Type: ...
    def IsA(self, arg2: Type) -> bool: ...
    @overload
    def _DumpTypeHierarchy(self, TfType) -> typing.Any: ...
    @overload
    def _DumpTypeHierarchy(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __hash__(self) -> int: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def baseTypes(self) -> list[Type]: ...
    @property
    def derivedTypes(self): ...
    @property
    def isEnumType(self) -> bool: ...
    @property
    def isPlainOldDataType(self) -> bool: ...
    @property
    def isUnknown(self) -> bool: ...
    @property
    def pythonClass(self) -> PyObjWrapper: ...
    @property
    def sizeof(self) -> int: ...
    @property
    def typeName(self) -> str: ...

class Warning(_DiagnosticBase):
    def __init__(self, *args, **kwargs) -> None: ...

class WindowsImportWrapper:
    __enter__: ClassVar[Callable] = ...
    __exit__: ClassVar[Callable] = ...

class _ClassWithClassMethod(Boost.Python.instance):
    Test: ClassVar[method] = ...
    __instance_size__: ClassVar[int] = ...
    def __init__(self) -> None: ...

class _ClassWithVarArgInit(Boost.Python.instance):
    def __init__(self) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def allowExtraArgs(self): ...
    @property
    def args(self): ...
    @property
    def expired(self): ...
    @property
    def kwargs(self): ...

class _DiagnosticBase(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def commentary(self): ...
    @property
    def diagnosticCode(self): ...
    @property
    def diagnosticCodeString(self): ...
    @property
    def sourceFileName(self): ...
    @property
    def sourceFunction(self): ...
    @property
    def sourceLineNumber(self): ...

class _Enum(Boost.Python.instance):
    class TestEnum2(Tf_PyEnumWrapper):
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...

    class TestKeywords(Tf_PyEnumWrapper):
        False_: ClassVar[TestKeywords] = ...
        None_: ClassVar[TestKeywords] = ...
        True_: ClassVar[TestKeywords] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        global_: ClassVar[TestKeywords] = ...
        import_: ClassVar[TestKeywords] = ...
        print_: ClassVar[TestKeywords] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...

    class TestScopedEnum(Tf_PyEnumWrapper):
        Alef: ClassVar[TestScopedEnum] = ...
        Bet: ClassVar[TestScopedEnum] = ...
        Gimel: ClassVar[TestScopedEnum] = ...
        _baseName: ClassVar[str] = ...
        allValues: ClassVar[tuple] = ...
        def __init__(self, *args, **kwargs) -> None: ...
        def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...
    One: ClassVar[TestEnum2] = ...
    Three: ClassVar[TestEnum2] = ...
    Two: ClassVar[TestEnum2] = ...
    def __init__(self, *args, **kwargs) -> None: ...

class _TestBase(Boost.Python.instance):
    def __init__(self) -> None: ...
    def TestCallVirtual(self) -> str: ...
    @overload
    def Virtual(self) -> str: ...
    @overload
    def Virtual(self) -> None: ...
    def Virtual2(self) -> None: ...
    def Virtual3(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def Virtual4(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class _TestDerived(_TestBase):
    def __init__(self) -> None: ...
    def Virtual(self) -> str: ...
    def Virtual2(self) -> None: ...
    def Virtual3(self, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
    def __bool__(self) -> bool: ...
    def __eq__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    @property
    def expired(self): ...

class _TestEnum(Tf_PyEnumWrapper):
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...

class _TestScopedEnum(Tf_PyEnumWrapper):
    Beryllium: ClassVar[_TestScopedEnum] = ...
    Boron: ClassVar[_TestScopedEnum] = ...
    Hydrogen: ClassVar[_TestScopedEnum] = ...
    Lithium: ClassVar[_TestScopedEnum] = ...
    _baseName: ClassVar[str] = ...
    allValues: ClassVar[tuple] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def GetValueFromName(self, name: str | pxr.Ar.ResolvedPath) -> Any: ...

class _TestStaticMethodError(Boost.Python.instance):
    def __init__(self, *args, **kwargs) -> None: ...
    def Error(self) -> None: ...

class _TestStaticTokens(Boost.Python.instance):
    Fuji: ClassVar[str] = ...
    McIntosh: ClassVar[str] = ...
    Pippin: ClassVar[str] = ...
    orange: ClassVar[str] = ...
    pear: ClassVar[str] = ...
    def __init__(self, *args, **kwargs) -> None: ...

class _testStaticTokens(Boost.Python.instance):
    Fuji: ClassVar[str] = ...  # read-only
    McIntosh: ClassVar[str] = ...  # read-only
    Pippin: ClassVar[str] = ...  # read-only
    orange: ClassVar[str] = ...  # read-only
    pear: ClassVar[str] = ...  # read-only
    def __init__(self, *args, **kwargs) -> None: ...

def DictionaryStrcmp(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath) -> int: ...
def DumpTokenStats() -> None: ...
def FindLongestAccessiblePrefix(arg1: str | pxr.Ar.ResolvedPath) -> int: ...
def GetAppLaunchTime() -> int: ...
def GetCurrentScopeDescriptionStack() -> list[str]: ...
def GetEnvSetting(arg1: str | pxr.Ar.ResolvedPath) -> T: ...
@overload
def GetStackTrace() -> str: ...
@overload
def GetStackTrace() -> typing.Any: ...
def InstallTerminateAndCrashHandlers() -> None: ...
def InvokeWithErrorHandling(tupleargs, dictkwds) -> typing.Any: ...
def IsValidIdentifier(arg1: str | pxr.Ar.ResolvedPath) -> bool: ...
def LogStackTrace(reason: str | pxr.Ar.ResolvedPath, logToDb: bool = ...) -> None: ...
def MakeValidIdentifier(arg1: str | pxr.Ar.ResolvedPath) -> str: ...
@overload
def PrintStackTrace(file: typing.TextIO, str: str | pxr.Ar.ResolvedPath) -> typing.Any: ...
@overload
def PrintStackTrace(arg1: FILE, arg2: str | pxr.Ar.ResolvedPath) -> None: ...
def RealPath(path: str | pxr.Ar.ResolvedPath, allowInaccessibleSuffix: bool = ..., raiseOnError: bool = ...) -> str: ...
def ReportActiveErrorMarks() -> None: ...
def RepostErrors(exception: object) -> bool: ...
def SetPythonExceptionDebugTracingEnabled(enabled: bool) -> None: ...
def StringSplit(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath) -> list[str]: ...
def StringToDouble(arg1: str | pxr.Ar.ResolvedPath) -> float: ...
def StringToLong(arg1: str | pxr.Ar.ResolvedPath) -> int: ...
def StringToULong(arg1: str | pxr.Ar.ResolvedPath) -> int: ...
def TouchFile(fileName: str | pxr.Ar.ResolvedPath, create: bool = ...) -> bool: ...
def _CallThrowTest(arg1: object) -> None: ...
def _ConvertByteListToByteArray(arg1: list) -> Any: ...
def _DerivedFactory() -> _TestDerived: ...
def _DerivedNullFactory() -> _TestDerived: ...
def _Fatal(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int) -> None: ...
def _GetLongMax() -> int: ...
def _GetLongMin() -> int: ...
def _GetULongMax() -> int: ...
def _RaiseCodingError(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int) -> None: ...
def _RaiseRuntimeError(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int) -> None: ...
def _ReturnsBase(arg1: object) -> Any: ...
def _ReturnsBaseRefPtr(arg1: object) -> Any: ...
def _ReturnsConstBase(arg1: object) -> Any: ...
def _RoundTripWrapperCallTest(arg1: object) -> Any: ...
def _RoundTripWrapperIndexTest(arg1: object, arg2: int) -> Any: ...
def _RoundTripWrapperTest(arg1: object) -> Any: ...
def _Status(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int) -> None: ...
def _TakesBase(arg1: object) -> tuple: ...
def _TakesConstBase(arg1: object) -> str: ...
def _TakesDerived(arg1: object) -> str: ...
def _TakesReference(arg1: object) -> None: ...
def _TakesVecVecString(arg1: object) -> int: ...
def _TestAnnotatedBoolResult(arg1: bool, arg2: str | pxr.Ar.ResolvedPath) -> Tf_TestAnnotatedBoolResult: ...
def _ThrowCppException() -> str: ...
def _ThrowTest(arg1: str | pxr.Ar.ResolvedPath) -> None: ...
def _Warn(arg1: str | pxr.Ar.ResolvedPath, arg2: str | pxr.Ar.ResolvedPath, arg3: str | pxr.Ar.ResolvedPath, arg4: str | pxr.Ar.ResolvedPath, arg5: int) -> None: ...
def __SetErrorExceptionClass(arg1: object) -> None: ...
def _callUnboundInstance(arg1: object, arg2: str | pxr.Ar.ResolvedPath) -> str: ...
def _callback(arg1: object) -> None: ...
def _doErrors() -> None: ...
def _invokeTestCallback() -> str: ...
def _mightRaise(arg1: bool) -> None: ...
def _registerInvalidEnum(arg1: object) -> None: ...
def _returnsTfEnum(arg1: object) -> Any: ...
def _sendTfNoticeWithSender(arg1: object) -> None: ...
def _setTestCallback(arg1: object) -> None: ...
def _stringCallback(arg1: object) -> str: ...
def _stringStringCallback(arg1: object) -> str: ...
def _takesTestEnum(arg1: object) -> None: ...
def _takesTestEnum2(arg1: object) -> None: ...
def _takesTfEnum(arg1: object) -> None: ...
