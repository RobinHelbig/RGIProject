import nltk

from src.data.document import Document
from src.data.index import IndexEntry, Occurrence


def indexing(documents: [Document]):
    print("indexing")
    inverted_index: {str: IndexEntry} = {}
    for document in documents:
        document_word_dict = getWordDict(document)
        for document_word in document_word_dict:
            document_word_count = document_word_dict[document_word]

            index_entry = IndexEntry(0, [])
            if document_word in inverted_index:
                index_entry = inverted_index[document_word]

            index_entry.document_frequency += 1
            index_entry.documents.append(Occurrence(document.id, document_word_count))

            inverted_index.update({document_word: index_entry})

    return inverted_index


def getWordDict(document: Document) -> {str: int}:
    word_dict = {str: int}
    for word in nltk.word_tokenize(document.text):
        count = 1
        if word in word_dict:
            count = word_dict.get(word) + 1
        word_dict.update({word: count})

    return word_dict
