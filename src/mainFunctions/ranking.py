from math import log10

from src.data.document import Document
from src.data.index import IndexEntry
from src.helper.textProcessingHelper import getSentences, getTokens
from src.mainFunctions.indexing import indexing


def get_tfs(terms: [str], inverted_index: {str: IndexEntry}) -> {str: float}:
    tfs: {str: float} = {}

    for term_index, term in enumerate(terms, start=0):
        if tfs[term] is not None:
            continue

        i = inverted_index[term]

        tf = next(filter(lambda x: x.document_id == term_index, i.documents)).frequency
        if tf != 0:
            tf = 1 + log10(tf)

        tfs.update({term: tf})

    return tfs


def get_tfidfs(terms: [str], inverted_index: {str: IndexEntry}, corpus_inverted_index: {str: IndexEntry}) -> {str: float}:
    tfidfs: {str: float} = {}

    for term_index, term in enumerate(terms, start=0):
        if tfidfs[term] is not None:
            continue

        i = inverted_index[term]
        ci = corpus_inverted_index[term]

        tf = next(filter(lambda x: x.document_id == term_index, i.documents)).frequency
        if tf != 0:
            tf = 1 + log10(tf)

        idf = ci.inverted_document_frequency

        tfidfs.update({term: tf * idf})

    length = 0.0
    for term in tfidfs:
        length += pow(tfidfs[term], 2)

    length = pow(length, 0.5)

    for term in tfidfs:
        tfidfs.update({term: tfidfs[term] / length})

    return tfidfs


def ranking(document: Document, max_sentences: int, max_chars: int, order_ranked: bool, corpus_inverted_index: {str: IndexEntry}, args: {str: any}):
    sum_option = args["sum_option"] if args["sum_option"] is not None else "tf-idf" #"tf", "tf-idf", "bm25", "RRF"
    preprocessing = args["preprocessing"] if args["preprocessing"] is not None else False #True, False
    mmr = args["mmr"] if args["mmr"] is not None else False #True, False

    inverted_index = indexing(document.text_sentences, preprocessing)

    for sentence in document.text_sentences:
        tokens = getTokens(sentence, preprocessing)

        tfs = get_tfs(tokens, inverted_index)

        tfidfs = get_tfidfs(tokens, inverted_index, corpus_inverted_index)








    print("HI")