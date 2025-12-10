from .datatype_parser import DatatypeParser
from .parse_error import DatatypeParseError
from typing import TypeVar
from dacite import from_dict

T = TypeVar("T")

class DefaultDatatypeParser(DatatypeParser[T]):
    @staticmethod
    def parse(datatype, response, object_name):
        try:
            return from_dict(datatype, response.json()[object_name][0])
        
        except Exception as e:
            raise DatatypeParseError().with_traceback(e.__traceback__)

    @staticmethod
    def parse_list(datatype, response, list_name):
        try:
            return [from_dict(datatype, object) for object in response.json()[list_name]]
        
        except Exception as e:
            raise DatatypeParseError().with_traceback(e.__traceback__)