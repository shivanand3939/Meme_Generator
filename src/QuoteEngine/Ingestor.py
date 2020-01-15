from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .DocxImporter import DocxImporter
from .CsvImporter import CsvImporter
from .PdfImporter import PdfImporter
from .TxtImporter import TxtImporter


class Ingestor(IngestorInterface):
    importers = [DocxImporter, CsvImporter, PdfImporter, TxtImporter]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for importer in cls.importers: 
            if importer.can_ingest(path):
                return importer.parse(path)
