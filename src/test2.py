from IPython.core.display import HTML

#imports

from mainFunctions.ranking import ranking
from operator import attrgetter
from helper.documentHelper import read_files
from mainFunctions.indexing import indexing
from src.helper.mockDataVisualize import transfer_function_output_ranking
from src.mainFunctions.evaluation import calculate_true_pos, calculate_precision_recall, calculate_fbeta_measure, \
    calculate_precision_recall_tables_and_MAP_param, draw_precision_recall_curve, \
    get_MAP_avg_by_cat_and_standard_deviation, draw_MAP_chart, calculate_statistics
from src.mainFunctions.visualize import visualize

# code, statistics and/or charts here
order_ranked = True
max_sent = 8
max_chars = 1080
documents = read_files(False)

corpus_index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}

for v in corpus_index:
    corpus_idfs[v] = corpus_index[v].inverted_document_frequency

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "tf", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### TF ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### TF-IDF ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")

order_ranked = True
max_sent = 8
max_chars = 1080
documents = read_files(True)

corpus_index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}

for v in corpus_index:
    corpus_idfs[v] = corpus_index[v].inverted_document_frequency

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs,
                               {"rank_option": "tf", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### TF ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs,
                               {"rank_option": "tf-idf", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### TF-IDF ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")
