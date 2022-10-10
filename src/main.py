
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

from mainFunctions.evaluation import draw_precision_recall_curve

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
    draw_precision_recall_curve()

print("Start")
# visualize("VisualizeOutput1.txt", mockData(), 1)
# visualize("VisualizeOutput2.txt", mockData(), 2)
# visualize("VisualizeOutput3.txt", mockData(), 3)
documents = read_files(True)
index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in index:
    corpus_idfs[v] = index[v].inverted_document_frequency

for document in documents:
    summary_test = ranking(document, 7, None, True, corpus_idfs, {"rank_option": "rrf", "mmr": False})
    print(document.id, summary_test)


#map to term -> idf
#ranking
# print("Test")
#
# test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
# evaluation(test_doc)