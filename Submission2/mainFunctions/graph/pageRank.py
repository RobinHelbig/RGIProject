from data.document import Document
from helper.pageRankEvaluation import calculate_true_pos
from helper.pageRankEvaluation import calculate_accuracy
from helper.evaluationHelper import calculate_precision_recall
from helper.evaluationHelper import calculate_fbeta_measure
from helper.evaluationHelper import calculate_precision_recall_tables_and_MAP_param
from helper.evaluationHelper import draw_precision_recall_curve
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import numpy as np
from typing import List


def build_graph(sentences: List[str], threshold: float, use_idf: bool) -> [[float]]:
    matrix = [[0 for i in range(len(sentences))] for j in range(len(sentences))]
    for index_a, sentence_a in enumerate(sentences):
        for index_b, sentence_b in enumerate(sentences):
            tfIdfVectorizer = TfidfVectorizer(use_idf=use_idf)
            tfIdfSentence1 = tfIdfVectorizer.fit_transform([sentence_a])
            tfIdfSentence2 = tfIdfVectorizer.transform([sentence_b])
            value = cosine_similarity(tfIdfSentence1, tfIdfSentence2)[0][0]
            if index_a == index_b:
                matrix[index_a][index_b] = 0.0
                continue
            if value <= threshold:
                matrix[index_a][index_b] = 0.0
            else:
                matrix[index_a][index_b] = value
    return matrix

def get_page_rank_summary(sentences: List[str], p: int, scores: dict):
    top_sentence = {sentence: scores[index] for index, sentence in enumerate(sentences)}
    top = dict(sorted(top_sentence.items(), key=lambda x: x[1], reverse=True)[:p])
    for key, value in top.items():
        print(key, value)
    return top

def get_page_rank_sentences(sentences: List[str], top: dict):
    summary_list = []
    for sent in sentences:
        if sent in top.keys():
            summary_list.append(sent)

    return summary_list

def evaluate_page_rank(document, threshold, p):
    print("DOCUMENT")
    similarity_matrix = np.array(build_graph(document.text_sentences, threshold, True))
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph, alpha=0.85, max_iter=50)

    print("top news sentences")
    news_top = get_page_rank_summary(document.text_sentences, p, scores)

    news_sentences_length = len(document.text_sentences)

    news_sentences_pr = get_page_rank_sentences(document.text_sentences, news_top)

    print("news length")
    print(news_sentences_length)

    similarity_matrix_reference_summary = np.array(build_graph(document.referenceSummary, threshold, True))
    nx_graph_reference_summary = nx.from_numpy_array(similarity_matrix_reference_summary)
    scores_reference_summary = nx.pagerank(nx_graph_reference_summary, alpha=0.85, max_iter=50)
    print("top summary sentences")
    summary_top = get_page_rank_summary(document.referenceSummary, p, scores_reference_summary)
    summary_sentences_length = len(document.referenceSummary)

    summary_sentences_pr = get_page_rank_sentences(document.referenceSummary, summary_top)

    print("summary length")
    print(summary_sentences_length)

    # evaluation

    true_pos = calculate_true_pos(summary_sentences_pr, news_sentences_pr)
    precision_recall_tuple = calculate_precision_recall(summary_sentences_pr, news_sentences_pr, true_pos)
    fbeta = calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1])
    precision_recall_tab_and_MAP = calculate_precision_recall_tables_and_MAP_param(news_sentences_pr, true_pos)
    draw_precision_recall_curve(precision_recall_tab_and_MAP)

    accuracy = calculate_accuracy(document, news_sentences_pr, summary_sentences_pr)
    MAP = precision_recall_tab_and_MAP[2]

    precision = precision_recall_tuple[0]
    recall = precision_recall_tuple[1]
    print("fbeta: ")
    print(fbeta)
    print("precison: ")
    print(precision)
    print("recall: ")
    print(recall)
    print("accuarcy: ")
    print(accuracy)
    print("MAP: ")
    print(MAP)

    return MAP

def undirected_page_rank(documents: list[Document], threshold, p):
    for document in documents:
        similarity_matrix = np.array(build_graph(document, threshold, True))
        nx_graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(nx_graph, alpha=0.85, max_iter=50)
        news_top = get_page_rank_summary(document, p, scores)
        get_page_rank_sentences(document.text_sentences, news_top)

    similarity_matrix = np.array(build_graph(documents[0], threshold, True))
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph, alpha=0.85, max_iter=50)
    news_top = get_page_rank_summary(documents[0], p, scores)
    get_page_rank_sentences(documents[0].text_sentences, news_top)






