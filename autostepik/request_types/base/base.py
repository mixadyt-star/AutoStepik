from abc import ABC, abstractmethod
from typing import Dict, Any

class RequestBase(ABC):
    @abstractmethod
    def build(self) -> Dict[str, Any]: ...