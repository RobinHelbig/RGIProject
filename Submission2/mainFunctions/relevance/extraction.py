from Submission2.data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
import re
from sklearn import metrics


class FeatureVector():
    def __init__(self, position: int, similarity: float, is_in_summary: bool):
        self.position = position
        self.similarity = similarity
        self.is_in_summary = is_in_summary
    def give_info(self):
        return [self.position, self.similarity]

def feature_extraction_tf_idf(sentence: str, d: Document, use_idf: bool):
    position = -1
    sentence_alpha = re.sub(r'[^a-zA-Z]', '', sentence.lower())
    for index, doc_sentence in enumerate(d.text_sentences):
        a = re.sub(r'[^a-zA-Z]', '', doc_sentence.lower())
        if a == sentence_alpha:
            position = index + 1
    data = [sentence] + d.text_sentences
    tfIdfVectorizer = TfidfVectorizer(use_idf=use_idf)
    tfIdf = tfIdfVectorizer.fit_transform(data)
    df = pd.DataFrame(tfIdf[0].T.todense(), index=tfIdfVectorizer.get_feature_names(), columns=["TF-IDF"])
    df = df.sort_values('TF-IDF', ascending=False)
    df = df.replace(0, np.NaN)
    value = df.iloc[:, 0].mean()
    print(value)
    summary_alpha = [re.sub(r'[^a-zA-Z]', '', sentence) for sentence in d.referenceSummary]
    is_in_summary = sentence_alpha in summary_alpha
    return FeatureVector(position, value, is_in_summary)


def naive_bayes(data, output):
    X_train, X_test, y_train, y_test = train_test_split(data, output, test_size=0.3, random_state=109)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb
def check_accuracy(gnb, X_test, y_test):
    y_pred = gnb.predict(X_test)
    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

def map_vectors_to_data_frame(vectors: [FeatureVector]):
    data = [[vector.position, vector.similarity]for vector in vectors]
    output = [[vector.is_in_summary] for vector in vectors]
    return (data, output)
    # df = pd.DataFrame(data, columns=["position", "similarity"])


def check_if_sentence_in_summary(d: Document, sentence: str) -> bool:
    b = re.sub(r'[^a-zA-Z]', '', sentence.lower())
    return b in d.referenceSummary
def training(d_train, r_train):
    model = GaussianNB()
    model.fit(d_train, r_train)

