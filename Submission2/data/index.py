from dataclasses import dataclass


@dataclass
class Occurrence:
    document_id: int
    frequency: int

@dataclass
class IndexEntry:
    document_frequency: int
    inverted_document_frequency: float
    occurrences: list[Occurrence]


