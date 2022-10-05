from dataclasses import dataclass
from enum import Enum


# class Category(Enum):
#     business = 'business',
#     entertainment = 'entertainment',
#     politics = 'politics',
#     sport = 'sport',
#     tech = 'tech'


@dataclass
class Document:
    """Class for storing documents, their reference summaries and the generated summaries from the IR system """
    id: int
    category: str
    text: str #actual text content of document from "News Articles" directory
    text_sentences: [str] #actual text content of document from "News Articles" directory divided in sentences
    referenceSummary: str #reference summary from "Summaries Folder"
    summary: list[str] #our own summary generated by our IR system
