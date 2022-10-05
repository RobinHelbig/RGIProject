from math import log10

import nltk

from src.data.document import Document
from src.data.index import IndexEntry, Occurrence
from src.helper.textProcessingHelper import getTokens


def indexing(corpus: [str], preprocessing: bool) -> {str: IndexEntry}:
    print("indexing")
    inverted_index: {str: IndexEntry} = {}

    text_id = 0

    for text in corpus:
        text_word_dict = getWordDict(text, preprocessing)
        for text_word in text_word_dict:
            text_word_count = text_word_dict[text_word]

            index_entry = IndexEntry(0, 0, [])
            if text_word in inverted_index:
                index_entry = inverted_index[text_word]

            index_entry.document_frequency += 1
            index_entry.documents.append(Occurrence(text_id, text_word_count))

            inverted_index.update({text_word: index_entry})

            text_id += 0

    for entry in inverted_index:
        inverted_index[entry].inverted_document_frequency = log10(inverted_index[entry].document_frequency/len(corpus))

    return inverted_index


def getWordDict(text: str, preprocessing: bool) -> {str: int}:
    word_dict = {str: int}
    for word in getTokens(text, preprocessing):
        count = 1
        if word in word_dict:
            count = word_dict.get(word) + 1
        word_dict.update({word: count})

    return word_dict
