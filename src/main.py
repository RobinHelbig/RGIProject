
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

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

documents: [Document]

def ranking():
    print("ranking")


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
documents = read_files()
index = indexing(map(attrgetter('text'), documents), False)
print("Test")

test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
evaluation(test_doc)