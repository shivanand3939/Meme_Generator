from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

class IngestorInterface(ABC):

    allowed_extensions = []

    @classmethod
    def can_ingest(cls, path) -> bool:
        ext = path.split('.')[-1]
        if ext in cls.allowed_extensions:
            return True
        else:
            return False


    @classmethod
    @abstractmethod
    def parse(cls, path:str) -> List[QuoteModel]:
        pass
