# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from src.mainFunctions.evaluation import calculate_true_pos
from src.mainFunctions.evaluation import calculate_precision_recall
from src.mainFunctions.evaluation import calculate_fbeta_measure
from src.mainFunctions.evaluation import calculate_precision_recall_tables_and_MAP_param
from src.mainFunctions.evaluation import draw_precision_recall_curve
from src.mainFunctions.evaluation import draw_MAP_chart
from src.mainFunctions.evaluation import get_MAP_avg_by_cat_and_standard_deviation

from operator import attrgetter
from turtle import title
from typing import List

import nltk

from data.document import Document

from src.mainFunctions.indexing import indexing
from src.helper.documentHelper import read_files
from src.mainFunctions.ranking import ranking

documents: [Document]

"""pass every document you want to evaluate (for example just one document or all of a certain category"""

"""pass every document you want to evaluate (for example just one document or all of a certain category"""


# def evaluation(documents: [Document]):

def evaluation(documents: List[Document]):
    print("evaluation")
    business = []
    entertainment = []
    politics = []
    sport = []
    tech = []

    for document in documents:
        true_pos = calculate_true_pos(document)
        precision_recall_tuple = calculate_precision_recall(document.referenceSummary, document.summary, true_pos)
        calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1])
        precision_recall_tuple = calculate_precision_recall_tables_and_MAP_param(document.referenceSummary,
                                                                                       true_pos)
        # it will draw chart for every document, so I added condition
        if document.id == 2:
            draw_precision_recall_curve(precision_recall_tuple)

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


print("Start")


order_ranked = True
text_processing = True
documents = read_files(text_processing)
index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in index:
    corpus_idfs[v] = index[v].inverted_document_frequency

for document in documents:
    document.summary = ranking(document, 7, None, order_ranked, corpus_idfs, {"rank_option": "rrf", "mmr": False})
#     #print(document.id, document.summary)
#
#     document_sentences = document.text_sentences
#     summary_sentences = document.summary
#     reference_summary_sentences = document.referenceSummary

# visualize
# evaluate
#     if "Air Jamaica" in document.text:
#         document.summary = ranking(document, 3, None, order_ranked, corpus_idfs, {"rank_option": "tf", "mmr": False})
#         # print(document.id, document.summary)
#
#         document_sentences = document.text_sentences
#         summary_sentences = document.summary
#         reference_summary_sentences = document.referenceSummary
#         print("tf", summary_sentences)
#
#         summary2 = ranking(document, 3, None, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": False})
#         print("tfidf", summary2)
#
#         summary3 = ranking(document, 3, None, order_ranked, corpus_idfs, {"rank_option": "bm25", "mmr": False})
#         print("bm25",summary3)
#
#         summary4 = ranking(document, 3, None, order_ranked, corpus_idfs, {"rank_option": "rrf", "mmr": False})
#         print("rrf",summary4)
#
#         summary5 = ranking(document, 3, None, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": True})
#         print("mmr",summary5)

evaluation(documents)
