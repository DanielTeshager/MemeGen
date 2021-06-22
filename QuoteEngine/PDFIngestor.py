"""
PDFIngestor class handles parsing of .pdf files.

when Ingestor class finds a .pdf it will deligate
parsing taks to this class.
This class then takes the file pars it and creates
QuoteModel objects.
This class relies on a third part executable called
'pdftotext', and it must be installed before running
this applicaiton.

"""

import subprocess
import os
from datetime import datetime as dt
from typing import List
import random
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """Handles .pdf files."""

    supported_files = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .pdf files."""
        if not cls.can_ingest(path):
            raise Exception(f'cannot ingest {path}')
        temp = f"./_data/DogQuotes/temp/"\
               f"{str(dt.now().timestamp()).split('.')[0]}.txt"
        call = subprocess.call(['pdftotext', path, temp])
        temp_file = open(temp)
        quotes = []

        for line in temp_file.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)
        temp_file.close()
        os.remove(temp)
        return quotes
