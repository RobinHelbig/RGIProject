import numpy as np
import matplotlib.pyplot as plt
from src.helper import helper
from src.data.document_old import Document
import math
from typing import List
import csv

import os

BETA = 0.5
CATEGORIES = ['business', 'entertainment', 'politics', 'sport', 'tech']
FBETA_HEADER = ['doc', 'fbeta']


# helper
def get_all_category_docs(directory):
    category_list = []

    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f):
            category_list.append(f)

    return category_list


def get_MAP_avg_by_cat_and_standard_deviation(reference_dir, dir):
    # business

    reference_category = get_all_category_docs(reference_dir)
    category = get_all_category_docs(dir)

    true_pos = []

    for i in range(len(reference_category)):
        for j in range(len(category)):
            if i == j:
                true_pos.append(calcualte_true_pos_cat(reference_category[i], category[j]))

    reference_MAP = []
    score_deviation_from_mean = []

    for i in range(len(reference_category)):
        reference_MAP.append(
            calculate_precision_recall_tables_and_MAP_param_cat(reference_category[i], true_pos[i])[2])

    reference_MAP_avg = sum(reference_MAP) / len(true_pos)

    for i in range(len(reference_MAP)):
        score_deviation_from_mean.append(pow(reference_MAP[i] - reference_MAP_avg, 2))

    business_standard_deviation = sum(score_deviation_from_mean) / len(reference_MAP)

    return reference_MAP_avg, business_standard_deviation


def draw_MAP_chart():
    reference_business_dir = '../BBC News Summary/Summaries/business'
    business_dir = '../BBC News Summary/Test Summaries/business/'
    reference_entertainment_dir = '../BBC News Summary/Summaries/entertainment'
    entertainment_dir = '../BBC News Summary/Test Summaries/entertainment/'
    reference_politics_dir = '../BBC News Summary/Summaries/politics'
    politics_dir = '../BBC News Summary/Test Summaries/politics/'
    reference_sport_dir = '../BBC News Summary/Summaries/sport'
    sport_dir = '../BBC News Summary/Test Summaries/sport/'
    reference_tech_dir = '../BBC News Summary/Summaries/tech'
    tech_dir = '../BBC News Summary/Test Summaries/tech/'

    business_category = get_MAP_avg_by_cat_and_standard_deviation(reference_business_dir, business_dir)
    entertainment_category = get_MAP_avg_by_cat_and_standard_deviation(reference_entertainment_dir, entertainment_dir)
    politics_category = get_MAP_avg_by_cat_and_standard_deviation(reference_politics_dir, politics_dir)
    sport_category = get_MAP_avg_by_cat_and_standard_deviation(reference_sport_dir, sport_dir)
    tech_category = get_MAP_avg_by_cat_and_standard_deviation(reference_tech_dir, tech_dir)

    fig, ax = plt.subplots()

    ax.bar(x=CATEGORIES,
           height=[business_category[0], entertainment_category[0], politics_category[0], sport_category[0],
                   tech_category[0]],
           yerr=[business_category[1], entertainment_category[1], politics_category[1], sport_category[1],
                 tech_category[1]],
           capsize=4)

    plt.title('MAP - comparision')
    plt.xlabel('Category')
    plt.ylabel('MAP value')
    plt.show()


def calcualte_true_pos(documents):
    reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    summary = helper.extract_sentences(summary_path)
    true_pos = []
    for t1 in reference_summary:
        for t2 in summary:
            # remove not same
            if t1 == t2:
                true_pos.append(t2)
    return true_pos


def calculate_precision_recall(documents, true_pos):
    reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    summary = helper.extract_sentences(summary_path)

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


def calculate_precision_recall_tables_and_MAP_param(documents, true_pos):
    reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    summary = helper.extract_sentences(summary_path)

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

    MAP = sum(map_precision) / len(reference_summary)

    return recall_table, precision_table, MAP


def calcualte_true_pos_cat(reference_summary_path, summary_path):
    reference_summary = helper.extract_sentences(reference_summary_path)
    summary = helper.extract_sentences(summary_path)
    true_pos = []

    for t1 in reference_summary:
        for t2 in summary:
            # remove not same
            if t1 == t2:
                true_pos.append(t2)
    return true_pos


def calculate_precision_recall_tables_and_MAP_param_cat(reference_summary_path, true_pos):
    # reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    reference_summary = helper.extract_sentences(reference_summary_path)
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

    MAP = sum(map_precision) / len(reference_summary)

    return recall_table, precision_table, MAP
def draw_precision_recall_curve():
    test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
    true_pos = calcualte_true_pos(test_doc)
    precision_recall_tuple = calculate_precision_recall_tables_and_MAP_param(test_doc, true_pos)
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

#final
def calcualte_true_pos_final(documents: List[Document]):
    # reference_summary = helper.extract_sentences(reference_summary_path)
    # summary = helper.extract_sentences(summary_path)
    true_pos = []
    for document in documents:
        for t1 in document.referenceSummary:
            for t2 in document.summary:
                # remove not same
                if t1 == t2:
                    true_pos.append(t2)
    return true_pos


def calculate_precision_recall_final(reference_summary, summary, true_pos):
    # reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    # reference_summary = helper.extract_sentences(reference_summary_path)
    # summary_path = '../BBC News Summary/Test Summaries/business/001.txt'
    # summary = helper.extract_sentences(summary_path)

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
    Fbeta = ((1 + math.pow(BETA, 2)) * precision * recall) / (math.pow(BETA, 2) * precision + recall)
    print("Fbeta: " + str(Fbeta))
    return Fbeta


def calculate_precision_recall_tables_and_MAP_param_final(reference_summary, true_pos):
    # reference_summary_path = '../BBC News Summary/Summaries/business/001.txt'
    # reference_summary = helper.extract_sentences(reference_summary_path)
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

    MAP = sum(map_precision) / len(reference_summary)

    return recall_table, precision_table, MAP

def draw_precision_recall_curve_final(precision_recall_tuple):
    # test_doc = Document(1, 'bussines', 'some text', 'referenceSummary', 'summary')
    # true_pos = calcualte_true_pos(test_doc)
    # precision_recall_tuple = calculate_precision_recall_tables_and_MAP_param(test_doc, true_pos)
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

def get_MAP_avg_by_cat_and_standard_deviation_final(reference_dir, dir):
    # business

    reference_category = get_all_category_docs(reference_dir)
    category = get_all_category_docs(dir)

    true_pos = []

    for i in range(len(reference_category)):
        for j in range(len(category)):
            if i == j:
                true_pos.append(calcualte_true_pos_cat(reference_category[i], category[j]))

    reference_MAP = []
    score_deviation_from_mean = []

    for i in range(len(reference_category)):
        reference_MAP.append(
            calculate_precision_recall_tables_and_MAP_param_cat(reference_category[i], true_pos[i])[2])

    reference_MAP_avg = sum(reference_MAP) / len(true_pos)

    for i in range(len(reference_MAP)):
        score_deviation_from_mean.append(pow(reference_MAP[i] - reference_MAP_avg, 2))

    business_standard_deviation = sum(score_deviation_from_mean) / len(reference_MAP)

    return reference_MAP_avg, business_standard_deviation