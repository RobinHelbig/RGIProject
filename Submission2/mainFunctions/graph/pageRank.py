from data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import networkx as nx
import numpy as np


def build_graph(d: Document, threshold: float, use_idf: bool) -> [[float]]:
    matrix = [[0 for i in range(len(d.text_sentences))] for j in range(len(d.text_sentences))]
    for index_a, sentence_a in enumerate(d.text_sentences):
        for index_b, sentence_b in enumerate(d.text_sentences):
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


def get_page_rank_summary(d: Document, p: int, scores: dict):
    top_sentence = {sentence: scores[index] for index, sentence in enumerate(d.text_sentences)}
    top = dict(sorted(top_sentence.items(), key=lambda x: x[1], reverse=True)[:p])

    summary_list = []
    for sent in d.text_sentences:
        if sent in top.keys():
            summary_list.append(sent)
    return summary_list


def undirected_page_rank(documents: list[Document], threshold, p):
    for document in documents:
        similarity_matrix = np.array(build_graph(document, threshold, True))
        nx_graph = nx.from_numpy_array(similarity_matrix)
        scores = nx.pagerank(nx_graph, alpha=0.85, max_iter=50)
        get_page_rank_summary(documents[0], p, scores)

    similarity_matrix = np.array(build_graph(documents[0], threshold, True))
    nx_graph = nx.from_numpy_array(similarity_matrix)
    scores = nx.pagerank(nx_graph, alpha=0.85, max_iter=50)
    print(get_page_rank_summary(documents[0], p, scores))
