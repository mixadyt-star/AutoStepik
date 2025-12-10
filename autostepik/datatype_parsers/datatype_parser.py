from typing import TypeVar, Generic, Type, List
from abc import ABC, abstractmethod
from requests import Response

T = TypeVar("T")

class DatatypeParser(ABC, Generic[T]):
    @staticmethod
    @abstractmethod
    def parse(datatype: Type[T], response: Response, object_name: str) -> T: ...

    @staticmethod
    @abstractmethod
    def parse_list(datatype: Type[T], response: Response, list_name: str) -> List[T]: ...