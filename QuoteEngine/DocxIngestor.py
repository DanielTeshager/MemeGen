"""
DocXIngestor class handles parsing of .docx files.

when Ingestor class finds a .docx it will deligate
parsing taks to this class. This class then takes
the file pars it and create QuoteModel object.
this class relies on a third part library called
python-docx, and it must be installed before running
this applicaiton.

"""

from typing import List
import docx
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """Handles ms-word document."""

    supported_files = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse .docx files and return QuoteModel objects."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        doc = docx.Document(path)

        for para in doc.paragraphs:
            if para.text != "":
                parse = para.text.split('-')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)

        return quotes
