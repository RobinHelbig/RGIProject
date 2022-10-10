
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4')

# from src.mainFunctions.evaluation import calcualte_true_pos
from src.mainFunctions.evaluation import calculate_precision_recall
from src.mainFunctions.evaluation import calculate_fbeta_measure
from src.mainFunctions.evaluation import draw_precision_recall_curve
from src.mainFunctions.evaluation import get_MAP_avg_by_cat_and_standard_deviation
from src.mainFunctions.evaluation import draw_MAP_chart

from data.document import Document

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

#def evaluation(documents: [Document]):

def evaluation(documents: List[Document]):
    print("evaluation")

    # true_pos = calcualte_true_pos(test_doc)
    # precision_recall_tuple = calculate_precision_recall(test_doc, true_pos)
    # calculate_fbeta_measure(precision_recall_tuple[0], precision_recall_tuple[1])
    draw_precision_recall_curve()

    draw_MAP_chart()


print("Start")
# visualize("VisualizeOutput1.txt", mockData(), 1)
# visualize("VisualizeOutput2.txt", mockData(), 2)
# visualize("VisualizeOutput3.txt", mockData(), 3)

# documents_no_preprocessing = read_files(False)
# documents_preprocessing = read_files(True)

order_ranked = True
text_processing = True
documents = read_files(text_processing)
index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in index:
    corpus_idfs[v] = index[v].inverted_document_frequency

for document in documents:
    document.summary = ranking(document, 7, None, order_ranked, corpus_idfs, {"rank_option": "rrf", "mmr": False})
    # print(document.id, document.summary)

    document_sentences = document.text_sentences
    summary_sentences = document.summary
    reference_summary_sentences = document.referenceSummary
    # visualize
    # evaluate


# test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
# evaluation(test_doc)