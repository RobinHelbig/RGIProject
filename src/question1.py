from src.helper.documentHelper import read_files

documents_without_preprocessing = read_files(False)
documents_with_preprocessing = read_files(True)

for d in documents_without_preprocessing:
    terms_without_preprocessing = d.text_terms
    # ["Cats" "are" black or white and eat mickey mouse]
    length = len(terms_without_preprocessing)

for d in documents_with_preprocessing:
    terms_with_preprocessing = d.text_terms
    # ["Cats", black, white, mickey, mouse, Cats black, black white, white mickey, mickey mouse]
    length = len(terms_with_preprocessing)