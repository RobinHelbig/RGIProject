from Submission2.data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import cosine_similarity
import re
from sklearn import metrics


class FeatureVector():
    def __init__(self, position: int, similarity: float, is_in_summary: bool):
        self.position = position
        self.similarity = similarity
        self.is_in_summary = is_in_summary

def feature_extraction_tf_idf_many(d: [Document], use_idf: bool):
    list_of_feature_extractions = []
    for index,doc in enumerate(d):
        list_of_feature_extractions.append(feature_extraction_tf_idf(doc[index], use_idf))
    return list_of_feature_extractions



def feature_extraction_tf_idf(d: Document, use_idf: bool) -> [FeatureVector]:
    tfIdfVectorizer = TfidfVectorizer(use_idf=use_idf)
    tfIdf = tfIdfVectorizer.fit_transform([d.text])
    vector_array = []
    for sentence in d.text_sentences:
        position = -1
        sentence_alpha = re.sub(r'[^a-zA-Z]', '', sentence.lower())
        for index, doc_sentence in enumerate(d.text_sentences):
            a = re.sub(r'[^a-zA-Z]', '', doc_sentence.lower())
            if a == sentence_alpha:
                position = index + 1
        tfIdfSentence = tfIdfVectorizer.transform([sentence])
        value = cosine_similarity(tfIdf, tfIdfSentence)
        summary_alpha = [re.sub(r'[^a-zA-Z]', '', sentence) for sentence in d.referenceSummary]
        is_in_summary = sentence_alpha in summary_alpha
        vector_array.append(FeatureVector(position, value, is_in_summary))
    return vector_array


def map_vectors_to_data_frame(vectors: [FeatureVector]):
    data = [[vector.position, vector.similarity] for vector in vectors]
    output = [[vector.is_in_summary] for vector in vectors]
    return (data, output)
    # df = pd.DataFrame(data, columns=["position", "similarity"])


def naive_bayes(data, output):
    X_train, X_test, y_train, y_test = train_test_split(data, output, test_size=0.3)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb


def check_accuracy(gnb, X_test, y_test):
    y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))



def check_if_sentence_in_summary(d: Document, sentence: str) -> bool:
    b = re.sub(r'[^a-zA-Z]', '', sentence.lower())
    return b in d.referenceSummary


def training(d_train, r_train):
    model = GaussianNB()
    model.fit(d_train, r_train)
