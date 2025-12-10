from .datatype_parser import DatatypeParser
from typing import TypeVar
from dacite import from_dict

T = TypeVar("T")

class DefaultDatatypeParser(DatatypeParser[T]):
    @staticmethod
    def parse(datatype, response, object_name):
        return from_dict(datatype, response.json()[object_name][0])

    @staticmethod
    def parse_list(datatype, response, list_name):
        return [from_dict(datatype, object) for object in response.json()[list_name]]