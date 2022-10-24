from helper.documentHelper import read_files
from mainFunctions.clustering.clustering import clustering

text_processing = True
documents = read_files(text_processing)
clustering(documents, {})
