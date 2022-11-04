from helper.documentHelper import read_files
from mainFunctions.graph.pageRank import evaluate_page_rank
from Submission2.helper.pageRankEvaluation import draw_MAP_chart

# from math import log10
# from operator import attrgetter
#
# from data.index import IndexEntry
# from helper.documentHelper import read_files
# from mainFunctions.indexing import indexing
#
# def get_BM25(document_terms: [str], sentence_length: float, avg_sentence_length: float,
#              inverted_index: {str: IndexEntry}, inverted_index_pos: int, corpus_idfs: {str: float}) -> float:
#     bm25_score: float = 0.0
#     k = 1.2
#     b = 0.75
#
#     for document_term in document_terms:
#         i = inverted_index[document_term]
#         idf = corpus_idfs[document_term]
#
#         inverted_index_entry = list(filter(lambda o: o.document_id == inverted_index_pos, i.occurrences))
#         if len(inverted_index_entry) == 0:
#             continue
#
#         tf = inverted_index_entry[0].frequency
#         if tf != 0:
#             tf = 1 + log10(tf)

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
# text_processing = True
# documents = read_files(text_processing)
# print(documents[1].text_sentences)
# print(feature_extraction_tf_idf(d=documents[1], use_idf=True))

"""bm25"""
#         bm25_score += idf * ((k + 1) * tf) / (tf + k * (1 - b + b * sentence_length / avg_sentence_length))
#
#     return bm25_score
#
# order_ranked = True
# text_processing = True
# documents = read_files(text_processing, ["business"])
#
# corpus_index = indexing(list(map(attrgetter('text_terms'), documents)))
# corpus_idfs: {str: float} = {}
#
# for v in corpus_index:
#     corpus_idfs[v] = corpus_index[v].inverted_document_frequency
#
#
# document_you_want_to_look_at = documents[0]
# sentence_terms = document_you_want_to_look_at.text_sentence_terms
# inverted_index = indexing(sentence_terms)
#
# for sentence_index, sentence_terms in enumerate(sentence_terms, start=0):
#     sentence = document_you_want_to_look_at.text_sentences[sentence_index]
#     bm25_score = get_BM25(document_you_want_to_look_at.text_terms, len(sentence),
#                           document_you_want_to_look_at.text_sentences_avg_length, inverted_index, sentence_index, corpus_idfs)
#
#     print("score of sentence " + str(sentence_index) + ": " + str(bm25_score))

DOCUMENTS = ['doc0', 'doc50', 'doc100']

text_processing = True
threshold = 0.2
p = 7
documents = read_files(text_processing)

#undirected_page_rank(documents, threshold, p)
doc0_ev = evaluate_page_rank(documents[0], threshold, p)
doc1_ev = evaluate_page_rank(documents[50], threshold, p)
doc2_ev = evaluate_page_rank(documents[100], threshold, p)

draw_MAP_chart(doc0_ev, doc1_ev, doc2_ev, DOCUMENTS)