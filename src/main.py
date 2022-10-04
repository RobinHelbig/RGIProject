import string

import nltk
import re
from nltk import PunktSentenceTokenizer
from nltk.tokenize.punkt import PunktParameters

#nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from helper import helper


from src.data.document import Document

documents : [Document]

def readDocuments():
    print("read documents")

def indexing():
    print("indexing")


def ranking():
    print("ranking")

"""pass every document you want to evaluate (for example just one document or all of a certain category"""
def visualize(documents: [Document]):
    print("visualize")


"""pass every document you want to evaluate (for example just one document or all of a certain category"""
def evaluation(documents: [Document]):
    print("evaluation")

def calculateRecall(documents):
    reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    summary = helper.extract_sentences(summary_path)
    for t in reference_summary:
        print(t)
    print('***')
    for t in summary:
        print(t)


print("Start")
test_doc = Document(1,'bussines', 'some text', 'referenceSummary', 'summary')
#evaluation(test_doc)
calculateRecall(test_doc)