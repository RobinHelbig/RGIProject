import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.metrics.cluster import contingency_matrix
from scipy.cluster.hierarchy import dendrogram

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


def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


def evaluate(cluster: list[int], documents: list[Document], args: {str: any}):
    document_texts = list[str]()
    for document in documents:
        document_texts.append(document.text)

    vectorizer = TfidfVectorizer(use_idf=True)
    vectorspace = vectorizer.fit_transform(document_texts)
    vectorspace = vectorspace.toarray()

    true_labels = getTrueLabels(documents)

    sil_score = silhouette_score(vectorspace, cluster, metric='cosine')

    ran_score = adjusted_rand_score(cluster, true_labels)

    pur_score = purity(cluster, true_labels)

    return sil_score, ran_score, pur_score
