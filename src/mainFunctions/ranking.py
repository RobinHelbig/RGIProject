from math import log10
from data.document import Document
from data.index import IndexEntry
from helper.textProcessingHelper import getSentences, getTokens
from mainFunctions.indexing import indexing
from typing import List, Dict

def get_tfs(terms: List[str], inverted_index: Dict[str: IndexEntry]) -> Dict[str: float]:
    tfs: Dict[str: float] = {}

    for term_index, term in enumerate(terms, start=0):
        if tfs[term] is not None:
            continue

        i = inverted_index[term]

        tf = next(filter(lambda x: x.document_id == term_index, i.documents)).frequency
        if tf != 0:
            tf = 1 + log10(tf)

        tfs.update({term: tf})

    return tfs


def get_tfidfs(terms: List[str], inverted_index: Dict[str: IndexEntry], corpus_inverted_index: Dict[str: IndexEntry]) -> Dict[str: float]:
    tfidfs: Dict[str: float] = {}

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


def rank_sentences(sentences: List[str], preprocessing: bool, corpus_inverted_index: Dict[str: IndexEntry], rank_option: str, current_summary: List[str]) -> List[(str, int)]:
    inverted_index = indexing(sentences, preprocessing)

    for sentence in sentences:
        tokens = getTokens(sentence, preprocessing)

        tfs = get_tfs(tokens, inverted_index)

        tfidfs = get_tfidfs(tokens, inverted_index, corpus_inverted_index)

    #return sentence : score ordered by position in text

def ranking(document: Document, max_sentences: int, max_chars: int, order_ranked: bool, corpus_inverted_index: Dict[str: IndexEntry], args: {str: any}):
    rank_option = args["rank_option"] if args["rank_option"] is not None else "tf-idf" #"tf", "tf-idf", "bm25", "RRF"
    preprocessing = args["preprocessing"] if args["preprocessing"] is not None else False #True, False
    mmr = args["mmr"] if args["mmr"] is not None else False #True, False

    summary = list[str]()

    if not mmr:
        #retrieve ranked sentences
        ranked_sentences = rank_sentences()
        while True:
            if len(summary) == max_sentences:
                break

            next_sentence: str  #sentence highest score

            if max_chars is not None:
                char_count = 0
                for sentence in summary:
                    char_count += len(sentence)
                if char_count + len(next_sentence) > max_chars:
                    break

            #summary append next highest scored sentence with order_ranked parameter in mind

            if mmr:
                #if mmr rank sentences again
                ranked_sentences = rank_sentences()



    print("HI")