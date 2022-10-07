# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from src.mainFunctions.evaluation import draw_precision_recall_curve

from src.data.document import Document

documents: [Document]


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
    draw_precision_recall_curve()


print("Start")
test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
evaluation(test_doc)
