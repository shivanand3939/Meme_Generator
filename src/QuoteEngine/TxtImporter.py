
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess, os, random


class TxtImporter(IngestorInterface):

    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Incorrect file type')

        quotes = []

        with open(path, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    quotes.append(QuoteModel(parsed[0], parsed[1]))

        return quotes
