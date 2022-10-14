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

def calculate_avg_precision_recall_for_category(category_docs, p, l):
    precision_table = []
    recall_table = []
    for document in category_docs:
        document.summary = ranking(document, p, l, order_ranked, corpus_idfs,
                                   {"rank_option": "tf-idf", "mmr": False})
        true_pos = calculate_true_pos(document)
        precision_recall_tuple = calculate_precision_recall(document.referenceSummary, document.summary, true_pos)
        precision_table.append(precision_recall_tuple[0])
        recall_table.append(precision_recall_tuple[1])

    precision_avg = sum(precision_table) / len(recall_table)
    recall_avg = sum(recall_table) / len(recall_table)
    return precision_avg, recall_avg

print('Start')

order_ranked = True
text_processing = True
documents = read_files(text_processing)
index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in index:
    corpus_idfs[v] = index[v].inverted_document_frequency

row1 = [6, 800]
row2 = [6, 1010]
row3 = [6, 1200]
row4 = [8, 800]
row5 = [8, 1010]
row6 = [8, 1200]
row7 = [10, 800]
row8 = [10, 1010]
row9 = [10, 1200]


all_documents_6_800 = calculate_avg_precision_recall_for_category(documents, 6, 800)
precision_avg_6_800 = all_documents_6_800[0]
recall_avg_6_800 = all_documents_6_800[1]
row1.append(precision_avg_6_800)
row1.append(recall_avg_6_800)

all_documents_6_1010 = calculate_avg_precision_recall_for_category(documents, 6, 1010)
precision_avg_6_1010 = all_documents_6_1010[0]
recall_avg_6_1010 = all_documents_6_1010[1]
row2.append(precision_avg_6_1010)
row2.append(recall_avg_6_1010)

all_documents_6_1200 = calculate_avg_precision_recall_for_category(documents, 6, 1200)
precision_avg_6_1200 = all_documents_6_1200[0]
recall_avg_6_1200 = all_documents_6_1200[1]
row3.append(precision_avg_6_1200)
row3.append(recall_avg_6_1200)

all_documents_8_800 = calculate_avg_precision_recall_for_category(documents, 8, 800)
precision_avg_8_800 = all_documents_8_800[0]
recall_avg_8_800 = all_documents_8_800[1]
row4.append(precision_avg_8_800)
row4.append(recall_avg_8_800)

all_documents_8_1010 = calculate_avg_precision_recall_for_category(documents, 8, 1010)
precision_avg_8_1010 = all_documents_8_1010[0]
recall_avg_8_1010 = all_documents_8_1010[1]
row5.append(precision_avg_8_1010)
row5.append(recall_avg_8_1010)

all_documents_8_1200 = calculate_avg_precision_recall_for_category(documents, 8, 1200)
precision_avg_8_1200 = all_documents_8_1200[0]
recall_avg_8_1200 = all_documents_8_1200[1]
row6.append(precision_avg_8_1200)
row6.append(recall_avg_8_1200)

all_documents_10_800 = calculate_avg_precision_recall_for_category(documents, 10, 800)
precision_avg_10_800 = all_documents_10_800[0]
recall_avg_10_800 = all_documents_10_800[1]
row7.append(precision_avg_10_800)
row7.append(recall_avg_10_800)

all_documents_10_1010 = calculate_avg_precision_recall_for_category(documents, 10, 1010)
precision_avg_10_1010 = all_documents_10_1010[0]
recall_avg_10_1010 = all_documents_10_1010[1]
row8.append(precision_avg_10_1010)
row8.append(recall_avg_10_1010)

all_documents_10_1200 = calculate_avg_precision_recall_for_category(documents, 10, 1200)
precision_avg_10_1200 = all_documents_10_1200[0]
recall_avg_10_1200 = all_documents_10_1200[1]
row9.append(precision_avg_10_1200)
row9.append(recall_avg_10_1200)

business_docs = list(filter(lambda d: d.category == "business", documents))

business_6_800 = calculate_avg_precision_recall_for_category(business_docs, 6, 800)
business_precision_avg_6_800 = business_6_800[0]
business_recall_avg_6_800 = business_6_800[1]
row1.append(business_precision_avg_6_800)
row1.append(business_precision_avg_6_800)

business_6_1010 = calculate_avg_precision_recall_for_category(business_docs, 6, 1010)
business_precision_avg_6_1010 = business_6_1010[0]
business_recall_avg_6_1010 = business_6_1010[1]
row2.append(business_precision_avg_6_1010)
row2.append(business_recall_avg_6_1010)

business_6_1200 = calculate_avg_precision_recall_for_category(business_docs, 6, 1200)
business_precision_avg_6_1200 = business_6_1200[0]
business_recall_avg_6_1200 = business_6_1200[1]
row3.append(business_precision_avg_6_1200)
row3.append(business_recall_avg_6_1200)

business_8_800 = calculate_avg_precision_recall_for_category(business_docs, 8, 800)
business_precision_avg_8_800 = business_8_800[0]
business_recall_avg_8_800 = business_8_800[1]
row4.append(business_precision_avg_8_800)
row4.append(business_recall_avg_8_800)

business_8_1010 = calculate_avg_precision_recall_for_category(business_docs, 8, 1010)
business_precision_avg_8_1010 = business_8_1010[0]
business_recall_avg_8_1010 = business_8_1010[1]
row5.append(business_precision_avg_8_1010)
row5.append(business_recall_avg_8_1010)

business_8_1200 = calculate_avg_precision_recall_for_category(business_docs, 8, 1200)
business_precision_avg_8_1200 = business_8_1200[0]
business_recall_avg_8_1200 = business_8_1200[1]
row6.append(business_precision_avg_8_1200)
row6.append(business_recall_avg_8_1200)

business_10_800 = calculate_avg_precision_recall_for_category(business_docs, 10, 800)
business_precision_avg_10_800 = business_10_800[0]
business_recall_avg_10_800 = business_10_800[1]
row7.append(business_precision_avg_10_800)
row7.append(business_recall_avg_10_800)

business_10_1010 = calculate_avg_precision_recall_for_category(business_docs, 10, 1010)
business_precision_avg_10_1010 = business_10_1010[0]
business_recall_avg_10_1010 = business_10_1010[1]
row8.append(business_precision_avg_10_1010)
row8.append(business_recall_avg_10_1010)

business_10_1200 = calculate_avg_precision_recall_for_category(business_docs, 10, 1200)
business_precision_avg_10_1200 = business_10_1200[0]
business_recall_avg_10_1200 = business_10_1200[1]
row9.append(business_precision_avg_10_1200)
row9.append(business_recall_avg_10_1200)

entertainment_docs = list(filter(lambda d: d.category == "entertainment", documents))

entertainment_6_800 = calculate_avg_precision_recall_for_category(entertainment_docs, 6, 800)
entertainment_precision_avg_6_800 = entertainment_6_800[0]
entertainment_recall_avg_6_800 = entertainment_6_800[1]
row1.append(entertainment_precision_avg_6_800)
row1.append(entertainment_precision_avg_6_800)

entertainment_6_1010 = calculate_avg_precision_recall_for_category(entertainment_docs, 6, 1010)
entertainment_precision_avg_6_1010 = entertainment_6_1010[0]
entertainment_recall_avg_6_1010 = entertainment_6_1010[1]
row2.append(entertainment_precision_avg_6_1010)
row2.append(entertainment_recall_avg_6_1010)

entertainment_6_1200 = calculate_avg_precision_recall_for_category(entertainment_docs, 6, 1200)
entertainment_precision_avg_6_1200 = entertainment_6_1200[0]
entertainment_recall_avg_6_1200 = entertainment_6_1200[1]
row3.append(entertainment_precision_avg_6_1200)
row3.append(entertainment_recall_avg_6_1200)

entertainment_8_800 = calculate_avg_precision_recall_for_category(entertainment_docs, 8, 800)
entertainment_precision_avg_8_800 = entertainment_8_800[0]
entertainment_recall_avg_8_800 = entertainment_8_800[1]
row4.append(entertainment_precision_avg_8_800)
row4.append(entertainment_recall_avg_8_800)

entertainment_8_1010 = calculate_avg_precision_recall_for_category(entertainment_docs, 8, 1010)
entertainment_precision_avg_8_1010 = entertainment_8_1010[0]
entertainment_recall_avg_8_1010 = entertainment_8_1010[1]
row5.append(entertainment_precision_avg_8_1010)
row5.append(entertainment_recall_avg_8_1010)

entertainment_8_1200 = calculate_avg_precision_recall_for_category(entertainment_docs, 8, 1200)
entertainment_precision_avg_8_1200 = entertainment_8_1200[0]
entertainment_recall_avg_8_1200 = entertainment_8_1200[1]
row6.append(entertainment_precision_avg_8_1200)
row6.append(entertainment_recall_avg_8_1200)

entertainment_10_800 = calculate_avg_precision_recall_for_category(entertainment_docs, 10, 800)
entertainment_precision_avg_10_800 = entertainment_10_800[0]
entertainment_recall_avg_10_800 = entertainment_10_800[1]
row7.append(entertainment_precision_avg_10_800)
row7.append(entertainment_recall_avg_10_800)

entertainment_10_1010 = calculate_avg_precision_recall_for_category(entertainment_docs, 10, 1010)
entertainment_precision_avg_10_1010 = entertainment_10_1010[0]
entertainment_recall_avg_10_1010 = entertainment_10_1010[1]
row8.append(entertainment_precision_avg_10_1010)
row8.append(entertainment_recall_avg_10_1010)

entertainment_10_1200 = calculate_avg_precision_recall_for_category(entertainment_docs, 10, 1200)
entertainment_precision_avg_10_1200 = entertainment_10_1200[0]
entertainment_recall_avg_10_1200 = entertainment_10_1200[1]
row9.append(entertainment_precision_avg_10_1200)
row9.append(entertainment_recall_avg_10_1200)

politics_docs = list(filter(lambda d: d.category == "politics", documents))
politics_6_800 = calculate_avg_precision_recall_for_category(politics_docs, 6, 800)
politics_precision_avg_6_800 = politics_6_800[0]
politics_recall_avg_6_800 = politics_6_800[1]
row1.append(politics_precision_avg_6_800)
row1.append(politics_precision_avg_6_800)

politics_6_1010 = calculate_avg_precision_recall_for_category(politics_docs, 6, 1010)
politics_precision_avg_6_1010 = politics_6_1010[0]
politics_recall_avg_6_1010 = politics_6_1010[1]
row2.append(politics_precision_avg_6_1010)
row2.append(politics_recall_avg_6_1010)

politics_6_1200 = calculate_avg_precision_recall_for_category(politics_docs, 6, 1200)
politics_precision_avg_6_1200 = politics_6_1200[0]
politics_recall_avg_6_1200 = politics_6_1200[1]
row3.append(politics_precision_avg_6_1200)
row3.append(politics_recall_avg_6_1200)

politics_8_800 = calculate_avg_precision_recall_for_category(politics_docs, 8, 800)
politics_precision_avg_8_800 = politics_8_800[0]
politics_recall_avg_8_800 = politics_8_800[1]
row4.append(politics_precision_avg_8_800)
row4.append(politics_recall_avg_8_800)

politics_8_1010 = calculate_avg_precision_recall_for_category(politics_docs, 8, 1010)
politics_precision_avg_8_1010 = politics_8_1010[0]
politics_recall_avg_8_1010 = politics_8_1010[1]
row5.append(politics_precision_avg_8_1010)
row5.append(politics_recall_avg_8_1010)

politics_8_1200 = calculate_avg_precision_recall_for_category(politics_docs, 8, 1200)
politics_precision_avg_8_1200 = politics_8_1200[0]
politics_recall_avg_8_1200 = politics_8_1200[1]
row6.append(politics_precision_avg_8_1200)
row6.append(politics_recall_avg_8_1200)

politics_10_800 = calculate_avg_precision_recall_for_category(politics_docs, 10, 800)
politics_precision_avg_10_800 = politics_10_800[0]
politics_recall_avg_10_800 = politics_10_800[1]
row7.append(politics_precision_avg_10_800)
row7.append(politics_recall_avg_10_800)

politics_10_1010 = calculate_avg_precision_recall_for_category(politics_docs, 10, 1010)
politics_precision_avg_10_1010 = politics_10_1010[0]
politics_recall_avg_10_1010 = politics_10_1010[1]
row8.append(politics_precision_avg_10_1010)
row8.append(politics_recall_avg_10_1010)

politics_10_1200 = calculate_avg_precision_recall_for_category(politics_docs, 10, 1200)
politics_precision_avg_10_1200 = politics_10_1200[0]
politics_recall_avg_10_1200 = politics_10_1200[1]
row9.append(politics_precision_avg_10_1200)
row9.append(politics_recall_avg_10_1200)

sport_docs = list(filter(lambda d: d.category == "sport", documents))
sport_6_800 = calculate_avg_precision_recall_for_category(sport_docs, 6, 800)
sport_precision_avg_6_800 = sport_6_800[0]
sport_recall_avg_6_800 = sport_6_800[1]
row1.append(sport_precision_avg_6_800)
row1.append(sport_precision_avg_6_800)

sport_6_1010 = calculate_avg_precision_recall_for_category(sport_docs, 6, 1010)
sport_precision_avg_6_1010 = sport_6_1010[0]
sport_recall_avg_6_1010 = sport_6_1010[1]
row2.append(sport_precision_avg_6_1010)
row2.append(sport_recall_avg_6_1010)

sport_6_1200 = calculate_avg_precision_recall_for_category(sport_docs, 6, 1200)
sport_precision_avg_6_1200 = sport_6_1200[0]
sport_recall_avg_6_1200 = sport_6_1200[1]
row3.append(sport_precision_avg_6_1200)
row3.append(sport_recall_avg_6_1200)

sport_8_800 = calculate_avg_precision_recall_for_category(sport_docs, 8, 800)
sport_precision_avg_8_800 = sport_8_800[0]
sport_recall_avg_8_800 = sport_8_800[1]
row4.append(sport_precision_avg_8_800)
row4.append(sport_recall_avg_8_800)

sport_8_1010 = calculate_avg_precision_recall_for_category(sport_docs, 8, 1010)
sport_precision_avg_8_1010 = sport_8_1010[0]
sport_recall_avg_8_1010 = sport_8_1010[1]
row5.append(sport_precision_avg_8_1010)
row5.append(sport_recall_avg_8_1010)

sport_8_1200 = calculate_avg_precision_recall_for_category(sport_docs, 8, 1200)
sport_precision_avg_8_1200 = sport_8_1200[0]
sport_recall_avg_8_1200 = sport_8_1200[1]
row6.append(sport_precision_avg_8_1200)
row6.append(sport_recall_avg_8_1200)

sport_10_800 = calculate_avg_precision_recall_for_category(sport_docs, 10, 800)
sport_precision_avg_10_800 = sport_10_800[0]
sport_recall_avg_10_800 = sport_10_800[1]
row7.append(sport_precision_avg_10_800)
row7.append(sport_recall_avg_10_800)

sport_10_1010 = calculate_avg_precision_recall_for_category(sport_docs, 10, 1010)
sport_precision_avg_10_1010 = sport_10_1010[0]
sport_recall_avg_10_1010 = sport_10_1010[1]
row8.append(sport_precision_avg_10_1010)
row8.append(sport_recall_avg_10_1010)

sport_10_1200 = calculate_avg_precision_recall_for_category(sport_docs, 10, 1200)
sport_precision_avg_10_1200 = sport_10_1200[0]
sport_recall_avg_10_1200 = sport_10_1200[1]
row9.append(sport_precision_avg_10_1200)
row9.append(sport_recall_avg_10_1200)


tech_docs = list(filter(lambda d: d.category == "tech", documents))
tech_6_800 = calculate_avg_precision_recall_for_category(tech_docs, 6, 800)
tech_precision_avg_6_800 = tech_6_800[0]
tech_recall_avg_6_800 = tech_6_800[1]
row1.append(tech_precision_avg_6_800)
row1.append(tech_precision_avg_6_800)

tech_6_1010 = calculate_avg_precision_recall_for_category(tech_docs, 6, 1010)
tech_precision_avg_6_1010 = tech_6_1010[0]
tech_recall_avg_6_1010 = tech_6_1010[1]
row2.append(tech_precision_avg_6_1010)
row2.append(tech_recall_avg_6_1010)

tech_6_1200 = calculate_avg_precision_recall_for_category(tech_docs, 6, 1200)
tech_precision_avg_6_1200 = tech_6_1200[0]
tech_recall_avg_6_1200 = tech_6_1200[1]
row3.append(tech_precision_avg_6_1200)
row3.append(tech_recall_avg_6_1200)

tech_8_800 = calculate_avg_precision_recall_for_category(tech_docs, 8, 800)
tech_precision_avg_8_800 = tech_8_800[0]
tech_recall_avg_8_800 = tech_8_800[1]
row4.append(tech_precision_avg_8_800)
row4.append(tech_recall_avg_8_800)

tech_8_1010 = calculate_avg_precision_recall_for_category(tech_docs, 8, 1010)
tech_precision_avg_8_1010 = tech_8_1010[0]
tech_recall_avg_8_1010 = tech_8_1010[1]
row5.append(tech_precision_avg_8_1010)
row5.append(tech_recall_avg_8_1010)

tech_8_1200 = calculate_avg_precision_recall_for_category(tech_docs, 8, 1200)
tech_precision_avg_8_1200 = tech_8_1200[0]
tech_recall_avg_8_1200 = tech_8_1200[1]
row6.append(tech_precision_avg_8_1200)
row6.append(tech_recall_avg_8_1200)

tech_10_800 = calculate_avg_precision_recall_for_category(tech_docs, 10, 800)
tech_precision_avg_10_800 = tech_10_800[0]
tech_recall_avg_10_800 = tech_10_800[1]
row7.append(tech_precision_avg_10_800)
row7.append(tech_recall_avg_10_800)

tech_10_1010 = calculate_avg_precision_recall_for_category(tech_docs, 10, 1010)
tech_precision_avg_10_1010 = tech_10_1010[0]
tech_recall_avg_10_1010 = tech_10_1010[1]
row8.append(tech_precision_avg_10_1010)
row8.append(tech_recall_avg_10_1010)

tech_10_1200 = calculate_avg_precision_recall_for_category(tech_docs, 10, 1200)
tech_precision_avg_10_1200 = tech_10_1200[0]
tech_recall_avg_10_1200 = tech_10_1200[1]
row9.append(tech_precision_avg_10_1200)
row9.append(tech_recall_avg_10_1200)


header = ["p", "l", "all_docs_precision", "all_docs_recall", "business_precision", "business_recall","entertainment_precision", "entertainment_recall","politics_precision", "politics_recall","sport_precision", "sport_recall","tech_precision", "tech_recall"]
data = [row1, row2, row3, row4, row5, row6, row7, row8, row9]
write_to_csv('precision_recall.csv', header, data)
print('end')