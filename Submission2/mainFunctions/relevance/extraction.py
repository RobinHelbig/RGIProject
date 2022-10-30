from Submission2.data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB, MultinomialNB


class FeatureVector():
    def __init__(self, position: int, similarity: float, type: str):


def feature_extraction_tf_idf(sentence: str, d: Document, use_idf: bool):
    sentences = d.text_sentences
    position = 0
    for index, doc_sentence in enumerate(d.text_sentences):
        if doc_sentence.lower().strip(" ") == sentence.lower().strip(" "):
            position = index + 1
    if position == 0:
        raise Exception("Sentence in the document not found")
    _model = "sentence-transformers/bert-base-nli-mean-tokens"
    model = SentenceTransformer(_model)
    embedings = model.encode(sentences)
    similarity = list(cosine_similarity([embedings[0:1]], embedings[1:]))
    average = sum(similarity)/len(similarity)
    return FeatureVector(position, average, "tf-idf")

def training(d_train, r_train):
    model = GaussianNB()
    model.fit(d_train, r_train)

