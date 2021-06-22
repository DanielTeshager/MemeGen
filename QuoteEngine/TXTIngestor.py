"""
TXTIngestor class handles parsing of .txt files.

when Ingestor class finds a .txt it will deligate
parsing taks to this class.
This class then takes the file pars it and creates
QuoteModel objects.

No third party library is required for this class

"""

from typing import List
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTIngestor(IngestorInterface):
    """Handles .txt files."""

    supported_files = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .txt files."""
        if not cls.can_ingest(path):
            raise Exception(f'cannot ingest {path}')
        temp_file = open(path)
        quotes = []
        for line in temp_file.readlines():
            line = line.strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        temp_file.close()
        return quotes
