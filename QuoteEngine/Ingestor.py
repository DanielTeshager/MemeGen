"""
This class choses Ingestors based on ext.

Ingestor class realizes IngestorInterface
and deligates file ingestion to classes
based on the extension of the file it received.
"""
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .PDFIngestor import PDFIngestor
from .DocxIngestor import DocxIngestor


class Ingestor(IngestorInterface):
    """Handles file engestion based on extension."""

    ingestors = [DocxIngestor, CSVIngestor, PDFIngestor, TXTIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Feed Ingestors based on file type."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
