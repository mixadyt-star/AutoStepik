from abc import ABC, abstractmethod
from typing import Dict, Any

class Base(ABC):
    @abstractmethod
    def build(self) -> Dict[str, Any]: ...