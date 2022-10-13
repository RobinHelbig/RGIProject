# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

from src.mainFunctions.evaluation import calcualte_true_pos_final
from src.mainFunctions.evaluation import calculate_precision_recall_final
from src.mainFunctions.evaluation import calculate_fbeta_measure
from src.mainFunctions.evaluation import calculate_precision_recall_tables_and_MAP_param_final
from src.mainFunctions.evaluation import draw_precision_recall_curve_final
from src.mainFunctions.evaluation import draw_MAP_chart_final

from src.mainFunctions.evaluation import get_MAP_avg_by_cat_and_standard_deviation_final

from operator import attrgetter
from turtle import title
from typing import List

import nltk

from data.document import Document
from helper.mockDataVisualize import mockData

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
        true_pos = calcualte_true_pos_final(document)
        precision_recall_tuple = calculate_precision_recall_final(document.referenceSummary, document.summary, true_pos)
        #warunek 0
        #calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1])
        precision_recall_tuple = calculate_precision_recall_tables_and_MAP_param_final(document.referenceSummary,
                                                                                       true_pos)
        # it will draw chart for every document
        # draw_precision_recall_curve_final(precision_recall_tuple)

        # get_all_category_docs from reference dir and from 'our' dir ???

    #get_MAP_avg_by_cat_and_standard_deviation('../BBC News Summary/Summaries/business', '../BBC News Summary/Test Summaries/business/')
    business_docs = list(filter(lambda d: d.category == "business", documents))
    business = get_MAP_avg_by_cat_and_standard_deviation_final(business_docs)

    entertainment_docs = list(filter(lambda d: d.category == "entertainment", documents))
    entertainment = get_MAP_avg_by_cat_and_standard_deviation_final(entertainment_docs)

    politics_docs = list(filter(lambda d: d.category == "politics", documents))
    politics = get_MAP_avg_by_cat_and_standard_deviation_final(politics_docs)

    sport_docs = list(filter(lambda d: d.category == "sport", documents))
    sport = get_MAP_avg_by_cat_and_standard_deviation_final(sport_docs)

    tech_docs = list(filter(lambda d: d.category == "tech", documents))
    tech = get_MAP_avg_by_cat_and_standard_deviation_final(tech_docs)

    draw_MAP_chart_final(business, entertainment, politics, sport, tech)


print("Start")
# visualize("VisualizeOutput1.txt", mockData(), 1)
# visualize("VisualizeOutput2.txt", mockData(), 2)
# visualize("VisualizeOutput3.txt", mockData(), 3)

# documents_no_preprocessing = read_files(False)
# documents_preprocessing = read_files(True)
#
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


# test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
evaluation(documents)
