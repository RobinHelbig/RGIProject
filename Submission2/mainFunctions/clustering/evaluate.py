import numpy as np
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.metrics.cluster import contingency_matrix

from data.document import Document


def purity(cluster_labels, true_labels):
    cm = contingency_matrix(true_labels, cluster_labels)

    # divide sum of maximum document amount for category per cluster by total documents
    return np.sum(np.amax(cm, axis=0)) / np.sum(cm)

def getTrueLabels(cluster: list[int], documents: list[Document]) -> list[int]:

def evaluate(cluster: list[int], documents: list[Document]):
    sil_score = silhouette_score(vectorspace, cluster_labels, metric='cosine')

    ran_score = adjusted_rand_score(cluster_labels, true_labels)

    pur_score = purity(cluster_labels, true_labels)
