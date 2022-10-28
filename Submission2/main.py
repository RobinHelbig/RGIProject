from helper.documentHelper import read_files
from mainFunctions.clustering.clustering import clustering
from mainFunctions.clustering.evaluate import evaluate, plot_dendrogram
from mainFunctions.clustering.interpret import interpret

args = {'n_clusters': 5, 'max_df': 0.2, 'criteria': 'mean'}

text_processing = True
documents = read_files(text_processing)
cluster_model = clustering(documents, args)
cluster_data = cluster_model.labels_

relevant_terms = interpret(cluster_data, documents, args)
evaluation = evaluate(cluster_data, documents, args)
plot_dendrogram(cluster_model, truncate_mode='level', p=3)
