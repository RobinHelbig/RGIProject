from operator import attrgetter

from src.mainFunctions.indexing import indexing
from src.helper.documentHelper import read_files
from src.mainFunctions.ranking import ranking

from src.mainFunctions.evaluation import calculate_true_pos
from src.mainFunctions.evaluation import get_MAP_avg_by_cat_and_standard_deviation
from src.mainFunctions.evaluation import draw_MAP_chart
from src.mainFunctions.evaluation import calculate_precision_recall_tables_and_MAP_param
from src.mainFunctions.evaluation import draw_precision_recall_curve
from src.mainFunctions.evaluation import calculate_precision_recall
from src.mainFunctions.evaluation import calculate_fbeta_measure

from src.helper.helper import write_to_csv

print('Start')

order_ranked = True
text_processing = True
documents = read_files(text_processing)
index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in index:
    corpus_idfs[v] = index[v].inverted_document_frequency
fbeta_list_tf = []
# MAP_avg_by_cat_and_standard_deviation, interpolated recall-and-precision curve for doc 2 - tf
for document in documents:
    document.summary = ranking(document, 8, 1010, order_ranked, corpus_idfs, {"rank_option": "tf", "mmr": False})
    true_pos = calculate_true_pos(document)
    precision_recall_tuple = calculate_precision_recall(document.referenceSummary, document.summary, true_pos)
    fbeta_list_tf.append(calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1]))
    precision_recall_tuple_table = calculate_precision_recall_tables_and_MAP_param(document.summary,
                                                                             true_pos)
    if document.id == 2:
        draw_precision_recall_curve(precision_recall_tuple_table)

avg_fbeta_tf = sum(fbeta_list_tf) / len(fbeta_list_tf)
print(avg_fbeta_tf)

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

draw_MAP_chart(business, entertainment, politics, sport, tech)

fbeta_list_tf_idf = []
# MAP_avg_by_cat_and_standard_deviation, interpolated recall-and-precision curve for doc 2 - tf-idf
for document in documents:
    document.summary = ranking(document, 8, 1010, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": False})
    true_pos = calculate_true_pos(document)
    precision_recall_tuple = calculate_precision_recall(document.referenceSummary, document.summary, true_pos)
    fbeta_list_tf_idf.append(calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1]))
    precision_recall_tuple_table = calculate_precision_recall_tables_and_MAP_param(document.summary,
                                                                                   true_pos)
    if document.id == 2:
        draw_precision_recall_curve(precision_recall_tuple_table)

avg_fbeta_tf_idf = sum(fbeta_list_tf_idf) / len(fbeta_list_tf_idf)
print(avg_fbeta_tf_idf)

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

draw_MAP_chart(business, entertainment, politics, sport, tech)

fbeta_list_bm25 = []
# MAP_avg_by_cat_and_standard_deviation, interpolated recall-and-precision curve for doc 2 - bm25
for document in documents:
    document.summary = ranking(document, 8, 1010, order_ranked, corpus_idfs, {"rank_option": "bm25", "mmr": False})
    true_pos = calculate_true_pos(document)
    precision_recall_tuple = calculate_precision_recall(document.referenceSummary, document.summary, true_pos)
    fbeta_list_bm25.append(calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1]))
    precision_recall_tuple_table = calculate_precision_recall_tables_and_MAP_param(document.summary,
                                                                                   true_pos)
    if document.id == 2:
        draw_precision_recall_curve(precision_recall_tuple_table)

avg_fbeta_bm25 = sum(fbeta_list_bm25) / len(fbeta_list_bm25)
print(avg_fbeta_bm25)

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

draw_MAP_chart(business, entertainment, politics, sport, tech)

fbeta_header = ['all_docs_tf', 'all_docs_tf_idf', 'all_docs_bm25']
fbeta_data = [avg_fbeta_tf, avg_fbeta_tf_idf, avg_fbeta_bm25]
write_to_csv('fbeta.csv', fbeta_header, [fbeta_data])

print('end')
