"""Models the datastructure of quotes."""


class QuoteModel():
    """Handles quote creation."""

    def __init__(self, body: str, author: str):
        """Initialize QuoteModel object."""
        self.body = body
        self.author = author

    def __repr__(self):
        """Object representation."""
        return f'<{self.body}, {self.author}>'
