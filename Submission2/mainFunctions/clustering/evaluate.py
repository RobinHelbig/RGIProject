import numpy as np
from sklearn.metrics import silhouette_score, adjusted_rand_score
from sklearn.metrics.cluster import contingency_matrix

from data.document import Document
from helper.documentHelper import categoryToInt


def purity(cluster_labels, true_labels):
    cm = contingency_matrix(true_labels, cluster_labels)

    # divide sum of maximum document amount for category per cluster by total documents
    return np.sum(np.amax(cm, axis=0)) / np.sum(cm)


def getTrueLabels(cluster: list[int], documents: list[Document], n_cluster: int) -> list[int]:

    # count how many times each cluster is
    # per cluster one dictionary is created that has the categories as keys and the number of occurrences as the value
    category_cluster_dictionary_list = list[{str: int}]()
    for document_index, document in enumerate(documents, start=0):
        category = document.category
        cluster = cluster[document_index]
        cluster_category_dictionary = cluster_category_dictionary_list[cluster]

        if category in cluster_category_dictionary:
            cluster_category_dictionary[category] += 1
        else:
            cluster_category_dictionary[category] = 1

    # for every cluster assign the category
    categories_for_clusters = list[str]()
    for cluster_category_dictionary in cluster_category_dictionary_list:
        sorted_categories = dict(sorted(cluster_category_dictionary.items(), key=lambda item: item[1]))
        first_category = list(sorted_categories.keys())[0]
        categories_for_clusters.append(first_category)

    true_labels = list[int]()

    for document_index, document in enumerate(documents, start=0):
        category = document.category
        cluster = categories_for_clusters.index(category)
        true_labels.append(cluster)

    return true_labels

def evaluate(cluster: list[int], documents: list[Document], args: {str: any}):
    n_clusters = args["n_clusters"] if "n_clusters" in args else 5

    sil_score = silhouette_score(vectorspace, cluster_labels, metric='cosine')

    ran_score = adjusted_rand_score(cluster_labels, true_labels)

    pur_score = purity(cluster_labels, true_labels)
