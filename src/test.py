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

#code, statistics and/or charts here
order_ranked = True
text_processing = False
max_sent = 8
max_chars = 500
documents = read_files(text_processing)

corpus_index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}

for v in corpus_index:
    corpus_idfs[v] = corpus_index[v].inverted_document_frequency

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "tf", "mmr": False})

business_docs = list(filter(lambda d: d.category == "business", documents))
business = get_MAP_avg_by_cat_and_standard_deviation(business_docs)
entertainment_docs = list(filter(lambda d: d.category == "entertainment", documents))
entertainment = get_MAP_avg_by_cat_and_standard_deviation(entertainment_docs)
politics_docs = list(filter(lambda d: d.category == "politics", documents))
politics = get_MAP_avg_by_cat_and_standard_deviation(politics_docs)
sport_docs = list(filter(lambda d: d.category == "sport", documents))
sport = get_MAP_avg_by_cat_and_standard_deviation(sport_docs)
tech_docs = list(filter(lambda d: d.category == "tech", documents))
tech = get_MAP_avg_by_cat_and_standard_deviation(tech_docs)

print(business, entertainment, politics, sport, tech)
draw_MAP_chart(business, entertainment, politics, sport, tech)

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

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "bm25", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### BM25 ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "rrf", "mmr": False})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### RRF ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": True})

precision_avg, recall_avg, fbeta_avg, MAP_avg = calculate_statistics(documents)
print("### MMR ###")
print("Average Precision: ", precision_avg)
print("Average Recall: ", recall_avg)
print("Average F-Beta: ", fbeta_avg)
print("Average MAP: ", MAP_avg)
print("##########")