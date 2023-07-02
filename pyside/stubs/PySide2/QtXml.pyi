from typing import overload
import PySide2.QtCore
import shiboken2
import typing
T = typing.TypeVar('T')

class QDomAttr(QDomNode):
    @overload
    def __init__(self, x: QDomAttr) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def name(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def ownerElement(self) -> QDomElement: ...
    def setValue(self, arg__1: str) -> None: ...
    def specified(self) -> bool: ...
    def value(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomCDATASection(QDomText):
    @overload
    def __init__(self, x: QDomCDATASection) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def __copy__(self) -> None: ...

class QDomCharacterData(QDomNode):
    @overload
    def __init__(self, x: QDomCharacterData) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendData(self, arg: str) -> None: ...
    def data(self) -> str: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def insertData(self, offset: int, arg: str) -> None: ...
    def length(self) -> int: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def replaceData(self, offset: int, count: int, arg: str) -> None: ...
    def setData(self, arg__1: str) -> None: ...
    def substringData(self, offset: int, count: int) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomComment(QDomCharacterData):
    @overload
    def __init__(self, x: QDomComment) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def __copy__(self) -> None: ...

class QDomDocument(QDomNode):
    @overload
    def __init__(self, doctype: QDomDocumentType) -> None: ...
    @overload
    def __init__(self, name: str) -> None: ...
    @overload
    def __init__(self, x: QDomDocument) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def createAttribute(self, name: str) -> QDomAttr: ...
    def createAttributeNS(self, nsURI: str, qName: str) -> QDomAttr: ...
    def createCDATASection(self, data: str) -> QDomCDATASection: ...
    def createComment(self, data: str) -> QDomComment: ...
    def createDocumentFragment(self) -> QDomDocumentFragment: ...
    def createElement(self, tagName: str) -> QDomElement: ...
    def createElementNS(self, nsURI: str, qName: str) -> QDomElement: ...
    def createEntityReference(self, name: str) -> QDomEntityReference: ...
    def createProcessingInstruction(self, target: str, data: str) -> QDomProcessingInstruction: ...
    def createTextNode(self, data: str) -> QDomText: ...
    def doctype(self) -> QDomDocumentType: ...
    def documentElement(self) -> QDomElement: ...
    def elementById(self, elementId: str) -> QDomElement: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def implementation(self) -> QDomImplementation: ...
    def importNode(self, importedNode: QDomNode, deep: bool) -> QDomNode: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    @overload
    def setContent(self, dev: PySide2.QtCore.QIODevice, namespaceProcessing: bool) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, reader: PySide2.QtCore.QXmlStreamReader, namespaceProcessing: bool) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, source: QXmlInputSource, namespaceProcessing: bool) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, source: QXmlInputSource, reader: QXmlReader) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, text: typing.Union[PySide2.QtCore.QByteArray,bytes], namespaceProcessing: bool) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, text: str, namespaceProcessing: bool) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, dev: PySide2.QtCore.QIODevice) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, text: typing.Union[PySide2.QtCore.QByteArray,bytes]) -> typing.Tuple[bool,str,int,int]: ...
    @overload
    def setContent(self, text: str) -> typing.Tuple[bool,str,int,int]: ...
    def toByteArray(self, arg__1: int = ...) -> PySide2.QtCore.QByteArray: ...
    def toString(self, arg__1: int = ...) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomDocumentFragment(QDomNode):
    @overload
    def __init__(self, x: QDomDocumentFragment) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomDocumentType(QDomNode):
    @overload
    def __init__(self, x: QDomDocumentType) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def entities(self) -> QDomNamedNodeMap: ...
    def internalSubset(self) -> str: ...
    def name(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def notations(self) -> QDomNamedNodeMap: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomElement(QDomNode):
    @overload
    def __init__(self, x: QDomElement) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def attribute(self, name: str, defValue: str = ...) -> str: ...
    def attributeNS(self, nsURI: str, localName: str, defValue: str = ...) -> str: ...
    def attributeNode(self, name: str) -> QDomAttr: ...
    def attributeNodeNS(self, nsURI: str, localName: str) -> QDomAttr: ...
    def attributes(self) -> QDomNamedNodeMap: ...
    def elementsByTagName(self, tagname: str) -> QDomNodeList: ...
    def elementsByTagNameNS(self, nsURI: str, localName: str) -> QDomNodeList: ...
    def hasAttribute(self, name: str) -> bool: ...
    def hasAttributeNS(self, nsURI: str, localName: str) -> bool: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def removeAttribute(self, name: str) -> None: ...
    def removeAttributeNS(self, nsURI: str, localName: str) -> None: ...
    def removeAttributeNode(self, oldAttr: QDomAttr) -> QDomAttr: ...
    @overload
    def setAttribute(self, name: str, value: str) -> None: ...
    @overload
    def setAttribute(self, name: str, value: float) -> None: ...
    @overload
    def setAttribute(self, name: str, value: int) -> None: ...
    @overload
    def setAttributeNS(self, nsURI: str, qName: str, value: str) -> None: ...
    @overload
    def setAttributeNS(self, nsURI: str, qName: str, value: float) -> None: ...
    @overload
    def setAttributeNS(self, nsURI: str, qName: str, value: int) -> None: ...
    def setAttributeNode(self, newAttr: QDomAttr) -> QDomAttr: ...
    def setAttributeNodeNS(self, newAttr: QDomAttr) -> QDomAttr: ...
    def setTagName(self, name: str) -> None: ...
    def tagName(self) -> str: ...
    def text(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomEntity(QDomNode):
    @overload
    def __init__(self, x: QDomEntity) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def notationName(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomEntityReference(QDomNode):
    @overload
    def __init__(self, x: QDomEntityReference) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomImplementation(shiboken2.Object):
    class InvalidDataPolicy:
        AcceptInvalidChars: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
        DropInvalidChars: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
        ReturnNullNode: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __and__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __rand__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __rmul__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __ror__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __rsub__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __rxor__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __sub__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
        def __xor__(self, other: typing.SupportsInt) -> QDomImplementation.InvalidDataPolicy: ...
    AcceptInvalidChars: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
    DropInvalidChars: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
    ReturnNullNode: typing.ClassVar[QDomImplementation.InvalidDataPolicy] = ...
    @overload
    def __init__(self, arg__1: QDomImplementation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def createDocument(self, nsURI: str, qName: str, doctype: QDomDocumentType) -> QDomDocument: ...
    def createDocumentType(self, qName: str, publicId: str, systemId: str) -> QDomDocumentType: ...
    def hasFeature(self, feature: str, version: str) -> bool: ...
    @classmethod
    def invalidDataPolicy(cls) -> QDomImplementation.InvalidDataPolicy: ...
    def isNull(self) -> bool: ...
    @classmethod
    def setInvalidDataPolicy(cls, policy: QDomImplementation.InvalidDataPolicy) -> None: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QDomNamedNodeMap(shiboken2.Object):
    @overload
    def __init__(self, arg__1: QDomNamedNodeMap) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def contains(self, name: str) -> bool: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index: int) -> QDomNode: ...
    def length(self) -> int: ...
    def namedItem(self, name: str) -> QDomNode: ...
    def namedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def removeNamedItem(self, name: str) -> QDomNode: ...
    def removeNamedItemNS(self, nsURI: str, localName: str) -> QDomNode: ...
    def setNamedItem(self, newNode: QDomNode) -> QDomNode: ...
    def setNamedItemNS(self, newNode: QDomNode) -> QDomNode: ...
    def size(self) -> int: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QDomNode(shiboken2.Object):
    class EncodingPolicy:
        EncodingFromDocument: typing.ClassVar[QDomNode.EncodingPolicy] = ...
        EncodingFromTextStream: typing.ClassVar[QDomNode.EncodingPolicy] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __and__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __rand__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __rmul__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __ror__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __rsub__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __rxor__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __sub__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...
        def __xor__(self, other: typing.SupportsInt) -> QDomNode.EncodingPolicy: ...

    class NodeType:
        AttributeNode: typing.ClassVar[QDomNode.NodeType] = ...
        BaseNode: typing.ClassVar[QDomNode.NodeType] = ...
        CDATASectionNode: typing.ClassVar[QDomNode.NodeType] = ...
        CharacterDataNode: typing.ClassVar[QDomNode.NodeType] = ...
        CommentNode: typing.ClassVar[QDomNode.NodeType] = ...
        DocumentFragmentNode: typing.ClassVar[QDomNode.NodeType] = ...
        DocumentNode: typing.ClassVar[QDomNode.NodeType] = ...
        DocumentTypeNode: typing.ClassVar[QDomNode.NodeType] = ...
        ElementNode: typing.ClassVar[QDomNode.NodeType] = ...
        EntityNode: typing.ClassVar[QDomNode.NodeType] = ...
        EntityReferenceNode: typing.ClassVar[QDomNode.NodeType] = ...
        NotationNode: typing.ClassVar[QDomNode.NodeType] = ...
        ProcessingInstructionNode: typing.ClassVar[QDomNode.NodeType] = ...
        TextNode: typing.ClassVar[QDomNode.NodeType] = ...
        values: typing.ClassVar[dict] = ...
        name: typing.Any
        @classmethod
        def __init__(cls, *args, **kwargs) -> None: ...
        def __add__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __and__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __bool__(self) -> bool: ...
        def __eq__(self, other: object) -> bool: ...
        def __ge__(self, other: object) -> bool: ...
        def __gt__(self, other: object) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> typing.Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other: object) -> bool: ...
        def __lt__(self, other: object) -> bool: ...
        def __mul__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __ne__(self, other: object) -> bool: ...
        def __or__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __pos__(self) -> typing.Any: ...
        def __radd__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __rand__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __rmul__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __ror__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __rsub__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __rxor__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __sub__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
        def __xor__(self, other: typing.SupportsInt) -> QDomNode.NodeType: ...
    AttributeNode: typing.ClassVar[QDomNode.NodeType] = ...
    BaseNode: typing.ClassVar[QDomNode.NodeType] = ...
    CDATASectionNode: typing.ClassVar[QDomNode.NodeType] = ...
    CharacterDataNode: typing.ClassVar[QDomNode.NodeType] = ...
    CommentNode: typing.ClassVar[QDomNode.NodeType] = ...
    DocumentFragmentNode: typing.ClassVar[QDomNode.NodeType] = ...
    DocumentNode: typing.ClassVar[QDomNode.NodeType] = ...
    DocumentTypeNode: typing.ClassVar[QDomNode.NodeType] = ...
    ElementNode: typing.ClassVar[QDomNode.NodeType] = ...
    EncodingFromDocument: typing.ClassVar[QDomNode.EncodingPolicy] = ...
    EncodingFromTextStream: typing.ClassVar[QDomNode.EncodingPolicy] = ...
    EntityNode: typing.ClassVar[QDomNode.NodeType] = ...
    EntityReferenceNode: typing.ClassVar[QDomNode.NodeType] = ...
    NotationNode: typing.ClassVar[QDomNode.NodeType] = ...
    ProcessingInstructionNode: typing.ClassVar[QDomNode.NodeType] = ...
    TextNode: typing.ClassVar[QDomNode.NodeType] = ...
    @overload
    def __init__(self, arg__1: QDomNode) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def appendChild(self, newChild: QDomNode) -> QDomNode: ...
    def attributes(self) -> QDomNamedNodeMap: ...
    def childNodes(self) -> QDomNodeList: ...
    def clear(self) -> None: ...
    def cloneNode(self, deep: bool = ...) -> QDomNode: ...
    def columnNumber(self) -> int: ...
    def firstChild(self) -> QDomNode: ...
    def firstChildElement(self, tagName: str = ...) -> QDomElement: ...
    def hasAttributes(self) -> bool: ...
    def hasChildNodes(self) -> bool: ...
    def insertAfter(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode: ...
    def insertBefore(self, newChild: QDomNode, refChild: QDomNode) -> QDomNode: ...
    def isAttr(self) -> bool: ...
    def isCDATASection(self) -> bool: ...
    def isCharacterData(self) -> bool: ...
    def isComment(self) -> bool: ...
    def isDocument(self) -> bool: ...
    def isDocumentFragment(self) -> bool: ...
    def isDocumentType(self) -> bool: ...
    def isElement(self) -> bool: ...
    def isEntity(self) -> bool: ...
    def isEntityReference(self) -> bool: ...
    def isNotation(self) -> bool: ...
    def isNull(self) -> bool: ...
    def isProcessingInstruction(self) -> bool: ...
    def isSupported(self, feature: str, version: str) -> bool: ...
    def isText(self) -> bool: ...
    def lastChild(self) -> QDomNode: ...
    def lastChildElement(self, tagName: str = ...) -> QDomElement: ...
    def lineNumber(self) -> int: ...
    def localName(self) -> str: ...
    def namedItem(self, name: str) -> QDomNode: ...
    def namespaceURI(self) -> str: ...
    def nextSibling(self) -> QDomNode: ...
    def nextSiblingElement(self, taName: str = ...) -> QDomElement: ...
    def nodeName(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def nodeValue(self) -> str: ...
    def normalize(self) -> None: ...
    def ownerDocument(self) -> QDomDocument: ...
    def parentNode(self) -> QDomNode: ...
    def prefix(self) -> str: ...
    def previousSibling(self) -> QDomNode: ...
    def previousSiblingElement(self, tagName: str = ...) -> QDomElement: ...
    def removeChild(self, oldChild: QDomNode) -> QDomNode: ...
    def replaceChild(self, newChild: QDomNode, oldChild: QDomNode) -> QDomNode: ...
    def save(self, arg__1: PySide2.QtCore.QTextStream, arg__2: int, arg__3: QDomNode.EncodingPolicy = ...) -> None: ...
    def setNodeValue(self, arg__1: str) -> None: ...
    def setPrefix(self, pre: str) -> None: ...
    def toAttr(self) -> QDomAttr: ...
    def toCDATASection(self) -> QDomCDATASection: ...
    def toCharacterData(self) -> QDomCharacterData: ...
    def toComment(self) -> QDomComment: ...
    def toDocument(self) -> QDomDocument: ...
    def toDocumentFragment(self) -> QDomDocumentFragment: ...
    def toDocumentType(self) -> QDomDocumentType: ...
    def toElement(self) -> QDomElement: ...
    def toEntity(self) -> QDomEntity: ...
    def toEntityReference(self) -> QDomEntityReference: ...
    def toNotation(self) -> QDomNotation: ...
    def toProcessingInstruction(self) -> QDomProcessingInstruction: ...
    def toText(self) -> QDomText: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lshift__(self, arg__1: PySide2.QtCore.QTextStream) -> PySide2.QtCore.QTextStream: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __rlshift__(self, other) -> typing.Any: ...

class QDomNodeList(shiboken2.Object):
    @overload
    def __init__(self, arg__1: QDomNodeList) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def at(self, index: int) -> QDomNode: ...
    def count(self) -> int: ...
    def isEmpty(self) -> bool: ...
    def item(self, index: int) -> QDomNode: ...
    def length(self) -> int: ...
    def size(self) -> int: ...
    def __copy__(self) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __ge__(self, other: object) -> bool: ...
    def __gt__(self, other: object) -> bool: ...
    def __le__(self, other: object) -> bool: ...
    def __lt__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...

class QDomNotation(QDomNode):
    @overload
    def __init__(self, x: QDomNotation) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomProcessingInstruction(QDomNode):
    @overload
    def __init__(self, x: QDomProcessingInstruction) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def data(self) -> str: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def setData(self, d: str) -> None: ...
    def target(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __copy__(self) -> None: ...

class QDomText(QDomCharacterData):
    @overload
    def __init__(self, x: QDomText) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def nodeType(self) -> QDomNode.NodeType: ...
    def splitText(self, offset: int) -> QDomText: ...
    def __copy__(self) -> None: ...

class QXmlAttributes(shiboken2.Object):
    @overload
    def __init__(self, arg__1: QXmlAttributes) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def append(self, qName: str, uri: str, localPart: str, value: str) -> None: ...
    def clear(self) -> None: ...
    def count(self) -> int: ...
    @overload
    def index(self, uri: str, localPart: str) -> int: ...
    @overload
    def index(self, qName: str) -> int: ...
    def length(self) -> int: ...
    def localName(self, index: int) -> str: ...
    def qName(self, index: int) -> str: ...
    def swap(self, other: QXmlAttributes) -> None: ...
    @overload
    def type(self, uri: str, localName: str) -> str: ...
    @overload
    def type(self, index: int) -> str: ...
    @overload
    def type(self, qName: str) -> str: ...
    def uri(self, index: int) -> str: ...
    @overload
    def value(self, uri: str, localName: str) -> str: ...
    @overload
    def value(self, index: int) -> str: ...
    @overload
    def value(self, qName: str) -> str: ...
    def __copy__(self) -> None: ...

class QXmlContentHandler(shiboken2.Object):
    def __init__(self) -> None: ...
    def characters(self, ch: str) -> bool: ...
    def endDocument(self) -> bool: ...
    def endElement(self, namespaceURI: str, localName: str, qName: str) -> bool: ...
    def endPrefixMapping(self, prefix: str) -> bool: ...
    def errorString(self) -> str: ...
    def ignorableWhitespace(self, ch: str) -> bool: ...
    def processingInstruction(self, target: str, data: str) -> bool: ...
    def setDocumentLocator(self, locator: QXmlLocator) -> None: ...
    def skippedEntity(self, name: str) -> bool: ...
    def startDocument(self) -> bool: ...
    def startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool: ...
    def startPrefixMapping(self, prefix: str, uri: str) -> bool: ...

class QXmlDTDHandler(shiboken2.Object):
    def __init__(self) -> None: ...
    def errorString(self) -> str: ...
    def notationDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def unparsedEntityDecl(self, name: str, publicId: str, systemId: str, notationName: str) -> bool: ...

class QXmlDeclHandler(shiboken2.Object):
    def __init__(self) -> None: ...
    def attributeDecl(self, eName: str, aName: str, type: str, valueDefault: str, value: str) -> bool: ...
    def errorString(self) -> str: ...
    def externalEntityDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def internalEntityDecl(self, name: str, value: str) -> bool: ...

class QXmlDefaultHandler(QXmlContentHandler, QXmlErrorHandler, QXmlDTDHandler, QXmlEntityResolver, QXmlLexicalHandler, QXmlDeclHandler):
    def __init__(self) -> None: ...
    def attributeDecl(self, eName: str, aName: str, type: str, valueDefault: str, value: str) -> bool: ...
    def characters(self, ch: str) -> bool: ...
    def comment(self, ch: str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def endDTD(self) -> bool: ...
    def endDocument(self) -> bool: ...
    def endElement(self, namespaceURI: str, localName: str, qName: str) -> bool: ...
    def endEntity(self, name: str) -> bool: ...
    def endPrefixMapping(self, prefix: str) -> bool: ...
    def error(self, exception: QXmlParseException) -> bool: ...
    def errorString(self) -> str: ...
    def externalEntityDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def fatalError(self, exception: QXmlParseException) -> bool: ...
    def ignorableWhitespace(self, ch: str) -> bool: ...
    def internalEntityDecl(self, name: str, value: str) -> bool: ...
    def notationDecl(self, name: str, publicId: str, systemId: str) -> bool: ...
    def processingInstruction(self, target: str, data: str) -> bool: ...
    def resolveEntity(self, publicId: str, systemId: str, ret: QXmlInputSource) -> bool: ...
    def setDocumentLocator(self, locator: QXmlLocator) -> None: ...
    def skippedEntity(self, name: str) -> bool: ...
    def startCDATA(self) -> bool: ...
    def startDTD(self, name: str, publicId: str, systemId: str) -> bool: ...
    def startDocument(self) -> bool: ...
    def startElement(self, namespaceURI: str, localName: str, qName: str, atts: QXmlAttributes) -> bool: ...
    def startEntity(self, name: str) -> bool: ...
    def startPrefixMapping(self, prefix: str, uri: str) -> bool: ...
    def unparsedEntityDecl(self, name: str, publicId: str, systemId: str, notationName: str) -> bool: ...
    def warning(self, exception: QXmlParseException) -> bool: ...

class QXmlEntityResolver(shiboken2.Object):
    def __init__(self) -> None: ...
    def errorString(self) -> str: ...
    def resolveEntity(self, publicId: str, systemId: str, ret: QXmlInputSource) -> bool: ...

class QXmlErrorHandler(shiboken2.Object):
    def __init__(self) -> None: ...
    def error(self, exception: QXmlParseException) -> bool: ...
    def errorString(self) -> str: ...
    def fatalError(self, exception: QXmlParseException) -> bool: ...
    def warning(self, exception: QXmlParseException) -> bool: ...

class QXmlInputSource(shiboken2.Object):
    @overload
    def __init__(self, dev: PySide2.QtCore.QIODevice) -> None: ...
    @overload
    def __init__(self) -> None: ...
    def data(self) -> str: ...
    def fetchData(self) -> None: ...
    def fromRawData(self, data: typing.Union[PySide2.QtCore.QByteArray,bytes], beginning: bool = ...) -> str: ...
    def next(self) -> str: ...
    def reset(self) -> None: ...
    @overload
    def setData(self, dat: typing.Union[PySide2.QtCore.QByteArray,bytes]) -> None: ...
    @overload
    def setData(self, dat: str) -> None: ...

class QXmlLexicalHandler(shiboken2.Object):
    def __init__(self) -> None: ...
    def comment(self, ch: str) -> bool: ...
    def endCDATA(self) -> bool: ...
    def endDTD(self) -> bool: ...
    def endEntity(self, name: str) -> bool: ...
    def errorString(self) -> str: ...
    def startCDATA(self) -> bool: ...
    def startDTD(self, name: str, publicId: str, systemId: str) -> bool: ...
    def startEntity(self, name: str) -> bool: ...

class QXmlLocator(shiboken2.Object):
    def __init__(self) -> None: ...
    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...

class QXmlNamespaceSupport(shiboken2.Object):
    def __init__(self) -> None: ...
    def popContext(self) -> None: ...
    def prefix(self, arg__1: str) -> str: ...
    @overload
    def prefixes(self, arg__1: str) -> typing.List[str]: ...
    @overload
    def prefixes(self) -> typing.List[str]: ...
    def processName(self, arg__1: str, arg__2: bool, arg__3: str, arg__4: str) -> None: ...
    def pushContext(self) -> None: ...
    def reset(self) -> None: ...
    def setPrefix(self, arg__1: str, arg__2: str) -> None: ...
    def splitName(self, arg__1: str, arg__2: str, arg__3: str) -> None: ...
    def uri(self, arg__1: str) -> str: ...

class QXmlParseException(shiboken2.Object):
    @overload
    def __init__(self, name: str = ..., c: int = ..., l: int = ..., p: str = ..., s: str = ...) -> None: ...
    @overload
    def __init__(self, other: QXmlParseException) -> None: ...
    def columnNumber(self) -> int: ...
    def lineNumber(self) -> int: ...
    def message(self) -> str: ...
    def publicId(self) -> str: ...
    def systemId(self) -> str: ...

class QXmlReader(shiboken2.Object):
    def __init__(self) -> None: ...
    def DTDHandler(self) -> QXmlDTDHandler: ...
    def contentHandler(self) -> QXmlContentHandler: ...
    def declHandler(self) -> QXmlDeclHandler: ...
    def entityResolver(self) -> QXmlEntityResolver: ...
    def errorHandler(self) -> QXmlErrorHandler: ...
    def feature(self, name: str) -> typing.Tuple[bool,bool]: ...
    def hasFeature(self, name: str) -> bool: ...
    def hasProperty(self, name: str) -> bool: ...
    def lexicalHandler(self) -> QXmlLexicalHandler: ...
    def parse(self, input: QXmlInputSource) -> bool: ...
    def property(self, name: str) -> typing.Tuple[int,bool]: ...
    def setContentHandler(self, handler: QXmlContentHandler) -> None: ...
    def setDTDHandler(self, handler: QXmlDTDHandler) -> None: ...
    def setDeclHandler(self, handler: QXmlDeclHandler) -> None: ...
    def setEntityResolver(self, handler: QXmlEntityResolver) -> None: ...
    def setErrorHandler(self, handler: QXmlErrorHandler) -> None: ...
    def setFeature(self, name: str, value: bool) -> None: ...
    def setLexicalHandler(self, handler: QXmlLexicalHandler) -> None: ...
    def setProperty(self, name: str, value: int) -> None: ...

class QXmlSimpleReader(QXmlReader):
    def __init__(self) -> None: ...
    def DTDHandler(self) -> QXmlDTDHandler: ...
    def contentHandler(self) -> QXmlContentHandler: ...
    def declHandler(self) -> QXmlDeclHandler: ...
    def entityResolver(self) -> QXmlEntityResolver: ...
    def errorHandler(self) -> QXmlErrorHandler: ...
    def feature(self, name: str) -> typing.Tuple[bool,bool]: ...
    def hasFeature(self, name: str) -> bool: ...
    def hasProperty(self, name: str) -> bool: ...
    def lexicalHandler(self) -> QXmlLexicalHandler: ...
    @overload
    def parse(self, input: QXmlInputSource, incremental: bool) -> bool: ...
    @overload
    def parse(self, input: QXmlInputSource) -> bool: ...
    def parseContinue(self) -> bool: ...
    def property(self, name: str) -> typing.Tuple[int,bool]: ...
    def setContentHandler(self, handler: QXmlContentHandler) -> None: ...
    def setDTDHandler(self, handler: QXmlDTDHandler) -> None: ...
    def setDeclHandler(self, handler: QXmlDeclHandler) -> None: ...
    def setEntityResolver(self, handler: QXmlEntityResolver) -> None: ...
    def setErrorHandler(self, handler: QXmlErrorHandler) -> None: ...
    def setFeature(self, name: str, value: bool) -> None: ...
    def setLexicalHandler(self, handler: QXmlLexicalHandler) -> None: ...
    def setProperty(self, name: str, value: int) -> None: ...