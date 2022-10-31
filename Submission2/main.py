from helper.documentHelper import read_files
from mainFunctions.clustering.clustering import clustering
from mainFunctions.clustering.evaluate import evaluate, plot_dendrogram
from mainFunctions.clustering.interpret import interpret
from mainFunctions.relevance.extraction import feature_extraction_tf_idf

"""
clusters
"""
args = {'n_clusters': 5, 'max_df': 0.2, 'criteria': 'mean'}

text_processing = True
documents = read_files(text_processing)
cluster_model = clustering(documents, args)
cluster_data = cluster_model.labels_

relevant_terms = interpret(cluster_data, documents, args)
evaluation = evaluate(cluster_data, documents, args)
plot_dendrogram(cluster_model, truncate_mode='level', p=3)


""" relevance feedback """
documents = read_files(text_processing)
print(documents[1].text_sentences)
feature_extraction_tf_idf("Worries about the deficit concerns about China do, however, remain.", d=documents[1], use_idf=True)


