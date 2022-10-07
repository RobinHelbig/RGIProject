
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from mainFunctions.evaluation import draw_precision_recall_curve

from data.document import Document

from operator import attrgetter
from turtle import title
from typing import List

import nltk

from data.document import Document
from helper.mockDataVisualize import mockData

# from mainFunctions.indexing import indexing
from helper.documentHelper import read_files
from mainFunctions.visualize import run_visualize
documents: List[Document]

def ranking():
    print("ranking")

def visualize():
    run_visualize("lorem_ipsum4", mockData(), 4)
"""pass every document you want to evaluate (for example just one document or all of a certain category"""

"""pass every document you want to evaluate (for example just one document or all of a certain category"""

#def evaluation(documents: [Document]):

def evaluation(documents: List[Document]):
    print("evaluation")
    draw_precision_recall_curve()

print("Start")
# visualize("VisualizeOutput1.txt", mockData(), 1)
# visualize("VisualizeOutput2.txt", mockData(), 2)
# visualize("VisualizeOutput3.txt", mockData(), 3)
#documents = read_files()
#index = indexing(map(attrgetter('text'), documents), False)
print("Test")
#test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
#evaluation(test_doc)
visualize()