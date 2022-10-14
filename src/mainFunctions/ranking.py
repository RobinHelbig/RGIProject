from math import log10
from typing import List, Dict

from src.data.document import Document
from src.data.index import IndexEntry
from src.helper.textProcessingHelper import getSentences, getTerms
from src.mainFunctions.indexing import indexing


def get_tf_or_tfidf_scores(terms: [str], inverted_index_pos: int, inverted_index: {str: IndexEntry}, corpus_idfs: {str: float}):
    scores: {str: float} = {}

    for term in terms:
        if term in scores:
            continue

        i = inverted_index[term]

        if inverted_index_pos != -1:
            inverted_index_entry = list(filter(lambda o: o.document_id == inverted_index_pos, i.occurrences))
            if len(inverted_index_entry) == 0:
                continue

            tf = inverted_index_entry[0].frequency
        else:  # -1 -> get tf/tfidf for whole document
            tf = 0.0
            for inverted_index_entry in i.occurrences:
                tf += inverted_index_entry.frequency

        if tf != 0:
            tf = 1 + log10(tf)

        score = tf
        if corpus_idfs:  # if inverted document frequencies of the terms in the corpus are passed, calculcate tfidf
            score = score * corpus_idfs[term]
        scores.update({term: score})

    length = 0.0
    for term in scores:
        length += pow(scores[term], 2)

    length = pow(length, 0.5)

    if length != 0:
        for term in scores:
            scores.update({term: scores[term] / length})

    return scores


def get_tfs(terms: [str], inverted_index_pos: int, inverted_index: {str: IndexEntry}) -> {str: float}:
    return get_tf_or_tfidf_scores(terms, inverted_index_pos, inverted_index, None)


def get_tfidfs(terms: [str], inverted_index_pos: int, inverted_index: {str: IndexEntry}, corpus_idfs: {str: float}) -> {str: float}:
    return get_tf_or_tfidf_scores(terms, inverted_index_pos, inverted_index, corpus_idfs)


def get_BM25(document_terms: [str], inverted_index_pos: int, sentence_length: float, avg_sentence_length: float,
             inverted_index: {str: IndexEntry}, corpus_idfs: {str: float}) -> float:
    bm25_score: float = 0.0
    k = 1.2
    b = 0.75

    for document_term in document_terms:
        i = inverted_index[document_term]
        idf = corpus_idfs[document_term]

        inverted_index_entry = list(filter(lambda o: o.document_id == inverted_index_pos, i.occurrences))
        if len(inverted_index_entry) == 0:
            continue

        tf = inverted_index_entry[0].frequency
        if tf != 0:
            tf = 1 + log10(tf)

        bm25_score += idf * ((k + 1) * tf) / (tf + k * (1 - b + b * sentence_length / avg_sentence_length))

    return bm25_score


def mmr_next_sentence(current_document: list[(int, list[str])], current_summary: list[(int, list[str])],
                      corpus_idfs: {str: float}) -> (int, [str]):
    lam = 0.5
    document_terms: list[str] = []
    sentence_terms_current_document: list[list[str]] = []
    for sentence in current_document:
        sentence_terms_current_document.append(sentence[1])
        document_terms += sentence[1]

    sentence_terms_current_summary: list[list[str]] = []
    for sentence in current_summary:
        sentence_terms_current_summary.append(sentence[1])

    inverted_index_current_document = indexing(sentence_terms_current_document)
    inverted_index_current_summary = indexing(sentence_terms_current_summary)

    document_tfidfs = get_tfidfs(document_terms, -1, inverted_index_current_document, corpus_idfs)
    current_summary_tfidfs: list[{str: float}] = list()

    for inverted_index_pos, sentence in enumerate(current_summary, start=0):
        tfidfs = get_tfidfs(sentence[1], inverted_index_pos, inverted_index_current_summary, corpus_idfs)
        current_summary_tfidfs.append(tfidfs)

    sentence_scores = list[(int, int)]()
    for inverted_index_pos, sentence in enumerate(current_document, start=0):
        tfidfs = get_tfidfs(sentence[1], inverted_index_pos, inverted_index_current_document, corpus_idfs)

        sim_sentence_document = 0.0
        for term in tfidfs:
            score = tfidfs[term]
            doc_score = document_tfidfs[term]
            sim_sentence_document += (score * doc_score)

        sum_sim_sentence_summary = 0.0
        for summary_sentence_tfidfs in current_summary_tfidfs:
            for term in tfidfs:
                score = tfidfs[term]
                summary_sentence_score = summary_sentence_tfidfs[term] if term in summary_sentence_tfidfs else 0.0
                sum_sim_sentence_summary += (score * summary_sentence_score)

        mmr = (1 - lam) * sim_sentence_document - lam * sum_sim_sentence_summary
        sentence_scores.append((sentence[0], mmr))  # sentence_index, terms

    best_sentence = sorted(sentence_scores, key=lambda x: x[1], reverse=True)[0]
    best_sentence_index = best_sentence[0]
    best_sentence = list(filter(lambda d: d[0] == best_sentence_index, current_document))[0]

    return best_sentence


def rank_sentences(document: Document, corpus_idfs: {str: float}, rank_option: str) -> list[(int, str, int)]:
    sim_scores: list[(int, str, int)] = list()

    if rank_option != "rrf":
        sentence_terms = document.text_sentence_terms  # sentence terms including bigrams, noun phrases, ...
        inverted_index = indexing(sentence_terms)
        document_tfs = get_tfs(document.text_terms, -1, inverted_index)
        document_tfidfs = get_tfidfs(document.text_terms, -1, inverted_index, corpus_idfs)

        for sentence_terms_index, sentence_terms in enumerate(sentence_terms, start=0):
            sentence = document.text_sentences[sentence_terms_index]  # real sentence string

            if rank_option == "tf":  # normalized over sentence length
                tf_score = 0.0
                tfs = get_tfs(sentence_terms, sentence_terms_index, inverted_index)
                for term in tfs:
                    score = tfs[term]
                    doc_score = document_tfs[term]
                    tf_score += (score * doc_score)

                sim_scores.append((sentence_terms_index, sentence, tf_score))

            if rank_option == "tf-idf":  # normalized over sentence length
                tfidf_score = 0.0
                tfidfs = get_tfidfs(sentence_terms, sentence_terms_index, inverted_index, corpus_idfs)
                for term in tfidfs:
                    score = tfidfs[term]
                    doc_score = document_tfidfs[term]
                    tfidf_score += (score * doc_score)

                sim_scores.append((sentence_terms_index, sentence, tfidf_score))

            if rank_option == "bm25":  # normalized over sentence length
                bm25_score = get_BM25(document.text_terms, sentence_terms_index, len(sentence),
                                      document.text_sentences_avg_length, inverted_index, corpus_idfs)

                sim_scores.append((sentence_terms_index, sentence, bm25_score))

        # print("ran", rank_option, sim_scores)
    else:
        ranked_sentences_tf = sorted(rank_sentences(document, corpus_idfs, "tf"), key=lambda x: x[2], reverse=True)
        ranked_sentences_tfidf = sorted(rank_sentences(document, corpus_idfs, "tf-idf"), key=lambda x: x[2], reverse=True)
        ranked_sentences_bm25 = sorted(rank_sentences(document, corpus_idfs, "bm25"), key=lambda x: x[2], reverse=True)

        for tf_rank, sentence_rank_tf_entry in enumerate(ranked_sentences_tf):
            sentence_index = sentence_rank_tf_entry[0]
            sentence_text = sentence_rank_tf_entry[1]

            #  find position of sentence in each ranking (+1 so calculation would work for my = 0 too)
            tf_rank = tf_rank + 1
            tfidf_rank = [i for i, sentence in enumerate(ranked_sentences_tfidf) if sentence[0] == sentence_index][0] + 1
            bm25_rank = [i for i, sentence in enumerate(ranked_sentences_bm25) if sentence[0] == sentence_index][0] + 1

            my = 5
            rrf_score = (1 / (my + tf_rank)) + (1 / (my + tfidf_rank)) + (1 / (my + bm25_rank))
            sim_scores.append((sentence_index, sentence_text, rrf_score))

    return sim_scores

def ranking(document: Document, max_sentences: int, max_chars: int, order_ranked: bool, corpus_idfs: {str: float},
            args: {str: any}) -> list[str]:
    rank_option = args["rank_option"] if "rank_option" in args else "tf-idf"  # "tf", "tf-idf", "bm25", "rrf"
    mmr = args["mmr"] if "mmr" in args else False  # True, False

    summary = list[(int, str)]()  # additionally saves pos of sentence in document to help with order, is removed before return
    summary_char_count = 0.0

    if mmr is False:
        ranked_sentences = sorted(rank_sentences(document, corpus_idfs, rank_option), key=lambda x: x[2], reverse=True)

        while True:
            if len(ranked_sentences) == 0:
                break
            if len(summary) == max_sentences:
                break

            next_sentence = ranked_sentences[0]
            ranked_sentences.remove(next_sentence)

            next_sentence_index = next_sentence[0]
            next_sentence_text = next_sentence[1]

            if max_chars:
                if summary_char_count + len(next_sentence_text) > max_chars:
                    break

            if order_ranked:
                summary.append((next_sentence_index, next_sentence_text))
            else:
                pos = 0
                for s in summary:
                    if s[0] < next_sentence_index:
                        pos += 1
                    else:
                        break

                summary.insert(pos, (next_sentence_index, next_sentence_text))
                summary_char_count += len(next_sentence_text)

    if mmr is True:
        current_document_terms: list[(int, list[str])] = list()
        current_summary_terms: list[(int, list[str])] = list()

        for sentence_terms_index, sentence_terms in enumerate(document.text_sentence_terms, start=0):
            current_document_terms.append((sentence_terms_index, sentence_terms))

        while True:
            if len(current_document_terms) == 0:
                break
            if len(summary) == max_sentences:
                break

            next_sentence = mmr_next_sentence(current_document_terms, current_summary_terms, corpus_idfs)
            next_sentence_index = next_sentence[0]
            next_sentence_text = document.text_sentences[next_sentence_index]
            next_sentence_terms = next_sentence[1]

            if max_chars:
                if summary_char_count + len(next_sentence_text) > max_chars:
                    break

            current_summary_terms.append((next_sentence_index, next_sentence_terms))
            current_document_terms.remove((next_sentence_index, next_sentence_terms))

            if order_ranked:
                summary.append((next_sentence_index, next_sentence_text))
            else:
                pos = 0
                for s in summary:
                    if s[0] < next_sentence_index:
                        pos += 1
                    else:
                        break

                summary.insert(pos, (next_sentence_index, next_sentence_text))
                summary_char_count += len(next_sentence_text)

    return [s[1] for s in summary]
