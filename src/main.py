
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

from src.mainFunctions.evaluation import draw_precision_recall_curve

from src.data.document import Document

from operator import attrgetter
from turtle import title
from typing import List, Optional, Dict

import nltk

from data.document import Document
from helper.mockDataVisualize import mockData
import os

from src.mainFunctions.indexing import indexing
from src.helper.documentHelper import read_files
from src.mainFunctions.ranking import ranking

documents: [Document]


"""pass every document you want to evaluate (for example just one document or all of a certain category"""


def visualize(documents: [Document]):
    print("visualize")

# (document: [str], ranking: [str]) document -> all sentences in order they appear in article, ranking -> all sentences of summary orderd by rank
def visualize(name: str, ranking: Dict[str, int], option: int):
    # Creating the HTML file
    cur_dir = os.getcwd()
    with open(cur_dir+"/" + name +".html", "w") as file_html:
        file_html.write('''<html>
    <head>
    <title>''')
    
        file_html.write(name)
    
        file_html.write(
        '''</title>
    </head> 
    <body>
    <p>''')
        if option == 1:
            for sentence, importance in ranking.items():
                if importance>3:
                    write_just_strong(sentence, file_html)
                elif importance>1:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 2:
            for sentence, importance in ranking.items():
                if importance>3:
                    write_bold_big(sentence, file_html)
                if importance>2:
                    write_just_strong(sentence, file_html)
                elif importance>1:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        if option == 3:
            for sentence, importance in ranking.items():
                if importance>3:
                    write_just_bold_red(sentence, file_html)
                elif importance>2:
                    write_just_bold_orange(sentence, file_html)
                elif importance>1:
                    write_just_bold(sentence, file_html)
                else:
                    write_plain(sentence, file_html)
        
        
        
        
        file_html.write('''</p> 
    </body>
    </html>''')

def write_just_strong(sentence: str, file_html):
    file_html.write("<strong>" + sentence + "</strong>")

def write_just_bold(sentence: str, file_html):
    file_html.write("<b>" + sentence + "</b>")
    
def write_bold_big(sentence: str, file_html):
    file_html.write("<b><big>" + sentence + "</big></b>")

def write_just_bold_red(sentence: str, file_html):
    file_html.write('<b> <span style="color:red;">' + sentence + "</span></b>")

def write_just_bold_orange(sentence: str, file_html):
    file_html.write('<b> <span style="color:orange;">' + sentence + "</span></b>")

def write_plain(sentence:str, file_html):
    file_html.write(sentence)
    

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

summary_test = ranking(documents[0], 5, None, False, corpus_idfs, {"rank_option": "rrf", "mmr": True})
print(summary_test)
#map to term -> idf
#ranking
# print("Test")
#
# test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
# evaluation(test_doc)