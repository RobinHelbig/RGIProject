from src.helper.documentHelper import read_files
from matplotlib import pyplot as plt
from collections import Counter
import numpy

documents_without_preprocessing = read_files(False)
documents_with_preprocessing = read_files(True)

without_array = []
with_array = []
enum1 = []
enum_number = 0

for d in documents_without_preprocessing:
    enum_number += 1
    terms_without_preprocessing = d.text_terms
    # ["Cats" "are" black or white and eat mickey mouse]
    without_array.append(len(terms_without_preprocessing))
    enum1.append(enum_number)

enum_number = 0
for d in documents_with_preprocessing:
    terms_with_preprocessing = d.text_terms
    # ["Cats", black, white, mickey, mouse, Cats black, black white, white mickey, mickey mouse]
    with_array.append(len(terms_with_preprocessing))

with_array_mod = []
without_array_mod = []
for value in with_array:
    with_array_mod.append(int(value/100))
for value in without_array:
    without_array_mod.append(int(value / 100))

c1_counted = Counter(with_array_mod)
c2_counted = Counter(without_array_mod)



plt.bar(c1_counted.keys(), c1_counted.values(), label = "with processing")
plt.bar(c2_counted.keys(), c2_counted.values(), label = "without processing")
plt.xlabel('words * 10^-2')
plt.ylabel('number of documents')
plt.legend()
plt.show()