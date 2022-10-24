import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.metrics.cluster import contingency_matrix

from data.document import Document
from helper.documentHelper import categoryToInt


def purity(cluster_labels, true_labels):
    cm = contingency_matrix(true_labels, cluster_labels)

    # divide sum of maximum document amount for category per cluster by total documents
    return np.sum(np.amax(cm, axis=0)) / np.sum(cm)


def getTrueLabels(documents: list[Document]) -> list[int]:
    true_labels = list[int]()
    for document in documents:
        true_labels.append(categoryToInt(document.category))

    return true_labels

def evaluate(cluster: list[int], documents: list[Document], args: {str: any}):
    n_clusters = args["n_clusters"] if "n_clusters" in args else 5

    document_texts = list[str]()
    for document in documents:
        document_texts.append(document.text)

    vectorizer = TfidfVectorizer(use_idf=True)
    # vectorizer = TfidfVectorizer(use_idf=True, max_df=0.2)
    vectorspace = vectorizer.fit_transform(document_texts)
    vectorspace = vectorspace.toarray()

    sil_score = silhouette_score(vectorspace, cluster, metric='cosine')

    true_labels = getTrueLabels(documents)

    ran_score = adjusted_rand_score(cluster, true_labels)

    pur_score = purity(cluster, true_labels)
