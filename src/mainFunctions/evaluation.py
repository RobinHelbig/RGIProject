import numpy as np
import matplotlib.pyplot as plt
import math

BETA = 0.5
CATEGORIES = ['business', 'entertainment', 'politics', 'sport', 'tech']


def calculate_true_pos(document):
    true_pos = []
    for t1 in document.referenceSummary:
        for t2 in document.summary:
            # remove not same
            if t1 == t2:
                true_pos.append(t2)
    return true_pos


def calculate_precision_recall(reference_summary, summary, true_pos):
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

    return precision, recall


def calculate_fbeta_measure(precision, recall):
    if (math.pow(BETA, 2) * precision + recall) == 0:
        Fbeta = 0
    else:
        Fbeta = ((1 + math.pow(BETA, 2)) * precision * recall) / (math.pow(BETA, 2) * precision + recall)
    return Fbeta


def calculate_precision_recall_tables_and_MAP_param(summary, true_pos):
    recall_table = [0.0]
    true_pos_counter = 0
    recall_denominator = len(true_pos)
    map_precision = []

    precision_table = [0.0]
    precision_denominator = 0

    for t in summary:
        incremented = False
        if t in true_pos:
            true_pos_counter = true_pos_counter + 1
            incremented = True
        recall_table.append(true_pos_counter / recall_denominator)
        precision_denominator = precision_denominator + 1
        precision_table.append(true_pos_counter / precision_denominator)
        if incremented:
            map_precision.append(true_pos_counter / precision_denominator)

    MAP = sum(map_precision) / len(map_precision)

    return recall_table, precision_table, MAP


def draw_precision_recall_curve(precision_recall_tuple):
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    r = np.array(precision_recall_tuple[0])
    p = precision_recall_tuple[1]

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
    plt.title('Precision-recall curve')
    plt.xlabel('recall')
    plt.ylabel('precision')
    plt.show()


def get_MAP_avg_by_cat_and_standard_deviation(category_doc):
    reference_MAP = []
    score_deviation_from_mean = []

    for d in category_doc:
        true_pos = calculate_true_pos(d)
        reference_MAP.append(calculate_precision_recall_tables_and_MAP_param(d.summary, true_pos)[2])

    reference_MAP_avg = sum(reference_MAP) / len(reference_MAP)

    for i in range(len(reference_MAP)):
        score_deviation_from_mean.append(pow(reference_MAP[i] - reference_MAP_avg, 2))

    if len(reference_MAP) == 0:
        standard_deviation = 0
    else:
        standard_deviation = pow(sum(score_deviation_from_mean) / len(reference_MAP), 0.5)

    return reference_MAP_avg, standard_deviation


def draw_MAP_chart(business, entertainment, politics, sport, tech):

    fig, ax = plt.subplots()

    ax.bar(x=CATEGORIES,
           height=[business[0], entertainment[0], politics[0], sport[0],
                   tech[0]],
           yerr=[business[1], entertainment[1], politics[1], sport[1],
                 tech[1]],
           capsize=4)

    plt.title('MAP - comparision')
    plt.xlabel('Category')
    plt.ylabel('MAP value')
    plt.show()
