"""
CSVIngestor class handles parsing of .csv files.

when Ingestor class finds a csv it will deligate
parsing taks to this class. This class then takes
the file pars it and create QuoteModel object.

this class relies on third party library called
pandas. pands has to be installed before running
this applicaton.

"""
from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """Handles parsing of csv files."""

    supported_files = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Parse comma separated files."""
        if not cls.can_ingest(path):
            raise Exception(f'cannot ingest {path}')

        quotes = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)

        return quotes
