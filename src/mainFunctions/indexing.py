from math import log10

import nltk

from src.data.document import Document
from src.data.index import IndexEntry, Occurrence
from src.helper.textProcessingHelper import getTerms


def indexing(corpus: list[list[str]]) -> {str: IndexEntry}:
    print("indexing")
    inverted_index: {str: IndexEntry} = {}

    document_id = 0

    for document in corpus:
        term_dict = getTermDict(document)
        for term in term_dict:
            term_count = term_dict[term]

            index_entry = IndexEntry(0, 0, [])
            if term in inverted_index:
                index_entry = inverted_index[term]

            index_entry.document_frequency += 1
            index_entry.occurrences.append(Occurrence(document_id, term_count))

            inverted_index.update({term: index_entry})

            document_id += 0

    for entry in inverted_index:
        inverted_index[entry].inverted_document_frequency = log10(inverted_index[entry].document_frequency/len(corpus))

    return inverted_index


def getTermDict(text: list[str]) -> {str: int}:
    word_dict = {str: int}
    for word in text:
        count = 1
        if word in word_dict:
            count = word_dict.get(word) + 1
        word_dict.update({word: count})

    return word_dict
