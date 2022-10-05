import numpy as np
import matplotlib.pyplot as plt

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

from helper import helper

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


def calculate_precision_recall(documents):
    reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    summary = helper.extract_sentences(summary_path)
    true_pos = []
    # for i, t1 in enumerate(reference_summary):
    #     print(i, t1)
    #
    # print('***')
    #
    # for i, t2 in enumerate(summary):
    #     print(i, t2)
    #
    # print('***')
    for t1 in reference_summary:
        for t2 in summary:
            # remove not same
            if t1 == t2:
                true_pos.append(t2)

    # print("true pos")
    # for i, t2 in enumerate(true_pos):
    #     print(i, t2)
    #
    # print('***')

    TP = len(true_pos)
    FP = len(summary) - TP
    FN = len(reference_summary) - TP

    try:
        precision = TP / (TP + FP)
    except:
        precision = 1

    try:
        recall = TP / (TP + FN)
    except:
        recall = 1

    recall_table = [0.0]
    true_pos_counter = 0
    recall_denominator = len(reference_summary)
    map_precision = []

    precision_table = [0.0]
    precision_denominator = 0

    for t in reference_summary:
        incremented = False
        if t in true_pos:
            true_pos_counter = true_pos_counter + 1
            incremented = True
        recall_table.append(true_pos_counter / recall_denominator)
        precision_denominator = precision_denominator + 1
        precision_table.append(true_pos_counter / precision_denominator)
        if incremented:
            map_precision.append(true_pos_counter / precision_denominator)

    MAP = sum(map_precision)/len(reference_summary)
    print(map_precision)
    print(MAP)
    return recall_table, precision_table



def draw_precision_recall_curve():
    test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
    precision_recall_tuple = calculate_precision_recall(test_doc)
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    # how draw recall (interpolation)?? it's needed?
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    recall_length = len(precision_recall_tuple[0])
    r = np.array(precision_recall_tuple[0])
    p = precision_recall_tuple[1]

    # r = np.linspace(precision_recall_tuple[0][0], precision_recall_tuple[0][recall_length - 1], num=recall_length)
    # p = precision_recall_tuple[1] * (1. - r)
    dup_p = p.copy()
    i = r.shape[0] - 2

    while i >= 0:
        if p[i + 1] > p[i]:
            p[i] = p[i + 1]
        i = i - 1

    fig, ax = plt.subplots()

    for i in range(r.shape[0] - 1):
        ax.plot((r[i],
                 r[i]), (p[i], p[i + 1]), 'k-', label='', color='red')
        ax.plot((r[i], r[i + 1]), (p[i + 1], p[i + 1]), 'k-', label='', color='red')

    ax.plot(r, dup_p, 'k--', color='blue')
    plt.show()


print("Start")
test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
# evaluation(test_doc)
# print(calculate_precision_recall(test_doc))
draw_precision_recall_curve()
# print(get_precision_recall_table())
