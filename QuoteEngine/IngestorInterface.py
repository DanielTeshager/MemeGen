"""
This is an Abstract class.

this class has two class method one of
them is also an abstract method.

parse: an abstract method that needs
to be implemented by all ingestor class
is used to parse 4 types of files.

['.csv','.txt','.docx','.pdf']

"""

from typing import List
from .QuoteModel import QuoteModel
from abc import ABC, abstractmethod


class IngestorInterface(ABC):
    """Abstract Interface class."""

    supported_files = []

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Check if the data is ingestable."""
        ext = path.split('.')[-1]
        return ext in cls.supported_files

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Attempt to parse list of quotes."""
