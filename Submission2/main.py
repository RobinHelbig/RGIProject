from math import log10
from operator import attrgetter

from data.index import IndexEntry
from helper.documentHelper import read_files
from mainFunctions.indexing import indexing

def get_BM25(document_terms: [str], sentence_length: float, avg_sentence_length: float,
             inverted_index: {str: IndexEntry}, inverted_index_pos: int, corpus_idfs: {str: float}) -> float:
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
from mainFunctions.relevance.extraction import check_accuracy_documents_knn_idf, check_accuracy_documents_knn_no_idf, \
    check_accuracy_documents_bayes_no_idf, check_accuracy_documents_bayes_idf, feature_extraction_tf_idf, \
    map_vectors_to_data_frame, naive_bayes, knn_model, check_accuracy, check_accuracy_documents_bayes_no_idf_position, \
    check_accuracy_documents_bayes_idf_position, check_accuracy_documents_bayes_idf_cosine, check_accuracy_documents_bayes_no_idf_cosine
import numpy as np

"""
clusters
"""
# args = {'n_clusters': 5, 'max_df': 0.2, 'criteria': 'mean'}
#
# text_processing = True
# documents = read_files(text_processing)
# cluster_model = clustering(documents, args)
# cluster_data = cluster_model.labels_
#
# relevant_terms = interpret(cluster_data, documents, args)
# evaluation = evaluate(cluster_data, documents, args)
# plot_dendrogram(cluster_model, truncate_mode='level', p=3)
#

""" relevance feedback """
text_processing = True
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
documents = read_files(text_processing)
print(documents[1].text_sentences)
print(feature_extraction_tf_idf(d=documents[1], use_idf=True))


vectors = feature_extraction_tf_idf(documents[0], True)
vectors_no_idf = feature_extraction_tf_idf(documents[0], False)
print(vectors[0].to_string() + "\n" + vectors[1].to_string() + "\n" + vectors[2].to_string())
print(vectors_no_idf[0].to_string() + "\n" + vectors_no_idf[1].to_string() + "\n" + vectors_no_idf[2].to_string())
(data_bayes_idf, output_bayes_idf) = map_vectors_to_data_frame(vectors)
(data_bayes_no_idf, output_bayes_no_idf) = map_vectors_to_data_frame(vectors_no_idf)
(data_knn_idf, output_knn_idf) = map_vectors_to_data_frame(vectors)
(data_knn_no_idf, output_knn_no_idf) = map_vectors_to_data_frame(vectors_no_idf)
bayes_idf_model, X_train1, X_test1, y_train1, y_test1 = naive_bayes(data_bayes_idf, output_bayes_idf)
bayes_no_idf_model, X_train2, X_test2, y_train2, y_test2 = naive_bayes(data_bayes_no_idf, output_bayes_no_idf)
knn_received_model, X_train3, X_test3, y_train3, y_test3 = knn_model(data_knn_no_idf, output_knn_no_idf)
knn_idf_model, X_train4, X_test4, y_train4, y_test4 = knn_model(data_knn_idf, output_knn_idf)
print(check_accuracy(bayes_idf_model, X_test1, y_test1))
print(check_accuracy(bayes_no_idf_model, X_test2, y_test2))
print(check_accuracy(knn_received_model, X_test3, y_test3))
print(check_accuracy(knn_idf_model, X_test4, y_test4))
check_accuracy_documents_bayes_no_idf(documents)
check_accuracy_documents_bayes_idf(documents)
check_accuracy_documents_knn_idf(documents)
check_accuracy_documents_knn_no_idf(documents)


check_accuracy_documents_bayes_idf_position(documents)
check_accuracy_documents_bayes_idf_cosine(documents)
check_accuracy_documents_bayes_no_idf_cosine(documents)
check_accuracy_documents_bayes_no_idf_position(documents)