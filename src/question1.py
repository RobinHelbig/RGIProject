from src.helper.documentHelper import read_files
from matplotlib import pyplot as plt


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


plt.plot(enum1, with_array, label="with processing")
plt.plot(enum1, without_array, label="without processing")
plt.xlabel('document')
plt.ylabel('number of words')
plt.legend()
plt.show()