from src.mainFunctions.evaluation import calculate_accuracy, calculate_redundancy
import time
import sys

from IPython.core.display import HTML

#imports

from mainFunctions.ranking import ranking
from operator import attrgetter
from helper.documentHelper import read_files
from mainFunctions.indexing import indexing
from src.helper.mockDataVisualize import transfer_function_output_ranking
from src.mainFunctions.evaluation import calculate_true_pos, calculate_precision_recall, calculate_fbeta_measure, \
    calculate_precision_recall_tables_and_MAP_param, draw_precision_recall_curve, \
    get_MAP_avg_by_cat_and_standard_deviation, draw_MAP_chart, calculate_statistics
from src.mainFunctions.visualize import visualize
from src.helper.documentHelper import read_files
from matplotlib import pyplot as plt
from collections import Counter
import numpy

#rare, most common terms

#%%
order_ranked = True
max_sent = 8
max_chars = 1010
text_processing = True
start = time.time()
documents = read_files(text_processing)
end = time.time()
print("load time: ", end - start)


#code, statistics and/or charts here
start = time.time()

corpus_index = indexing(list(map(attrgetter('text_terms'), documents)))
corpus_idfs: {str: float} = {}
for v in corpus_index:
    corpus_idfs[v] = corpus_index[v].inverted_document_frequency

end = time.time()
print("corpus index time: ", end - start)
print("corpus index size: ", sys.getsizeof(corpus_index))
print("corpus idfs size: ", sys.getsizeof(corpus_idfs))



accuracy_avg = 0.0
redundancy_avg = 0.0
document_count = len(documents)

for document in documents:
    document.summary = ranking(document, max_sent, max_chars, order_ranked, corpus_idfs, {"rank_option": "tf-idf", "mmr": True, "lam": 0.9})

print("generated summaries")

for document in documents:
    accuracy_avg += calculate_accuracy(document)
    redundancy_avg += calculate_redundancy(document.summary, text_processing)

accuracy_avg = accuracy_avg / document_count
redundancy_avg = redundancy_avg / document_count
print("accuracy_avg: ", accuracy_avg)
print("redundancy_avg: ", redundancy_avg)

