
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import subprocess, os, random



class PdfImporter(IngestorInterface):

    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Incorrect file type')

        quotes = []
        if not os.path.exists('tmp'):
            os.mkdir('tmp')
        tmp = f'./tmp/{random.randint(0,1000000)}.txt'
        print(path, tmp)
        subprocess.call(['pdftotext', path, tmp])

        with open(tmp, 'r') as f:
            for line in f.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    quotes.append(QuoteModel(parsed[0], parsed[1]))
        os.remove(tmp)
        return quotes
