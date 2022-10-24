from data.document import Document
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups


def clustering(documents: list[Document], args: {str: any}) -> [int]:
    n_clusters = args["n_clusters"] if "n_clusters" in args else 5

    document_texts = list[str]()
    for document in documents:
        document_texts.append(document.text)

    vectorizer = TfidfVectorizer(use_idf=True)
    # vectorizer = TfidfVectorizer(use_idf=True, max_df=0.2)
    vectorspace = vectorizer.fit_transform(document_texts)
    vectorspace = vectorspace.toarray()
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='average', affinity='cosine', compute_distances=False).fit(vectorspace)
    return clustering.labels_