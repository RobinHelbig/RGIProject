from data.document import Document
from sklearn.cluster import AgglomerativeClustering
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups


def clustering(documents: list[Document], args: {str: any}):
    n_clusters = args["n_clusters"] if "n_clusters" in args else 5
    max_df = args["max_df"] if "max_df" in args else None

    document_texts = list[str]()
    for document in documents:
        document_texts.append(document.text)

    vectorizer = TfidfVectorizer(use_idf=True)

    if max_df is not None:
        vectorizer = TfidfVectorizer(use_idf=True, max_df=max_df)

    vectorspace = vectorizer.fit_transform(document_texts)
    vectorspace = vectorspace.toarray()
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='average', affinity='cosine', compute_distances=True).fit(vectorspace)
    return clustering