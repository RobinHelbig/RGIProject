from dataclasses import dataclass
from typing import List
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
    text_terms: List[str] #terms of the whole text
    text_sentences: List[str] #actual text content of document from "News Articles" directory divided in sentences
    text_sentence_terms: List[List[str]] #terms of the whole text split by sentence
    text_sentences_avg_length: float #average text sentence length
    referenceSummary: List[str] #reference summary from "Summaries Folder"
    summary: List[str] #our own summary generated by our IR system
