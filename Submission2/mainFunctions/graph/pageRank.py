from data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def build_graph(document):
    # print(document)
    # print("***")
    # print(document.text)
    # n_clusters = args["n_clusters"] if "n_clusters" in args else 5
    # max_df = args["max_df"] if "max_df" in args else None
    #
    # document_texts = list[str]()
    # for document in documents:
    #     document_texts.append(document.text)
    #
    vectorizer = TfidfVectorizer(use_idf=True)
    #
    # if max_df is not None:
    #     vectorizer = TfidfVectorizer(use_idf=True, max_df=max_df)
    #
    #document_text = [document.text]
    vectorspace = vectorizer.fit_transform(document.text_sentences)
    #print(vectorspace)
    #vectorspace = vectorspace.toarray()
    # print(document.text_sentences)
    # print(len(document.text_sentences))
    # number_of_sentences = []
    # tfidf_df = pd.DataFrame(vectorspace.toarray(), index=number_of_sentences, columns=vectorspace.get_feature_names())

    similarity = cosine_similarity(vectorspace)
    print(similarity)
    print("***********************************************************")



def undirected_page_rank(documents: list[Document]):
    for document in documents:
        build_graph(document)
