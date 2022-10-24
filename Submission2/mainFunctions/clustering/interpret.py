# t1t2t3t4t5
#
# c1:
# d1 -> [1, 2, 3, 4, 5]
# d2 -> [1, 2, 3, 4, 5]
# c1 -> [median, median, median, median, median] -> sort -> most relevant terms
#
# c2:
# d3 -> [1, 2, 3, 4, 5]
# d4 -> [1, 2, 3, 4, 5]
# c2 -> [median, median, median, median, median] -> sort -> most relevant terms
from statistics import median

from sklearn.feature_extraction.text import TfidfVectorizer

from data.document import Document


def interpret(cluster: list[int], documents: list[Document], args: {str: any}) -> list[(str, int)]:
    n_clusters = args["n_clusters"] if "n_clusters" in args else 5

    cluster_relevant_terms = list[(str, int)]()

    document_texts = list[str]()
    for document in documents:
        document_texts.append(document.text)

    vectorizer = TfidfVectorizer(use_idf=True)
    # vectorizer = TfidfVectorizer(use_idf=True, max_df=0.2)
    vectorspace = vectorizer.fit_transform(document_texts)
    vectorspace = vectorspace.toarray()
    termNames = vectorizer.get_feature_names_out()
    termCount = len(termNames)

    for cluster_index in range(0, n_clusters):
        term_tfidf_list = list[list[float]]()  # term list -> tdidf per document
        for i in range(0, termCount):
            term_tfidf_list[i] = list[int]()

        for document_index, document_tfidfs in enumerate(vectorspace, start=0):
            if cluster[document_index] == cluster_index:
                for term_index, term_tfidf in enumerate(document_tfidfs, start=0):
                    term_tfidf_list[term_index].append(term_tfidf)

        term_median_tdidfs = list[(str, int)]()
        for i in range(0, termCount):
            term_tfidfs = term_tfidf_list[i]

            term_name = termNames[i]
            median_term_tdidf = median(term_tfidfs)

            term_median_tdidfs.append((term_name, median_term_tdidf))

        cluster_relevant_terms.append(sorted(term_median_tdidfs, key=lambda x: x[1], reverse=True))

    return cluster_relevant_terms
