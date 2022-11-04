from Submission2.data.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.neighbors import KNeighborsClassifier
import re
from sklearn import metrics


class FeatureVector():
    def __init__(self, position: int, similarity: float, is_in_summary: bool):
        self.position = position
        self.similarity = similarity
        self.is_in_summary = is_in_summary

    def to_string(self):
        return "Position: " + str(self.position) + " " + "Similarity: " + str(self.similarity) + " " + "In summary: " + str(self.is_in_summary)

def extraction_for_many(d: [Document], use_idf: bool):
    list_of_feature_extractions = []
    for index, doc in enumerate(d):
        list_of_feature_extractions.append(feature_extraction_tf_idf(doc, use_idf))
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
        summary_alpha = [re.sub(r'[^a-zA-Z]', '', sentence).lower() for sentence in d.referenceSummary]
        #print(summary_alpha)
        is_in_summary = sentence_alpha in summary_alpha
        #print(sentence_alpha)
        vector_array.append(FeatureVector(position, value, is_in_summary))
        #print(position, value[0][0], is_in_summary)
    return vector_array

def map_vectors_to_data_frame(vectors: [FeatureVector]):
    data = [[vector.position, vector.similarity] for vector in vectors]
    output = [vector.is_in_summary for vector in vectors]
    return (data, output)
    # df = pd.DataFrame(data, columns=["position", "similarity"])
def map_vectors_to_data_frame_just_position(vectors: [FeatureVector]):
    data = [[vector.position] for vector in vectors]
    output = [vector.is_in_summary for vector in vectors]
    return (data, output)
def map_vectors_to_data_frame_just_cosine(vectors: [FeatureVector]):
    data = [[vector.similarity] for vector in vectors]
    output = [vector.is_in_summary for vector in vectors]
    return (data, output)


def naive_bayes(data, output):
    X_train, X_test, y_train, y_test = train_test_split(data, output, test_size=0.3)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)
    return gnb, X_train, X_test, y_train, y_test


def knn_model(data, output):
    X_train, X_test, y_train, y_test = train_test_split(data, output, test_size=0.3)
    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(X_train, y_train)
    return knn, X_train, X_test, y_train, y_test


def check_accuracy(model, X_test, y_test):
    y_pred = model.predict(X_test)
    return metrics.accuracy_score(y_test, y_pred)

def connect_everything_bayes(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame(vectors)
    bayes_received_model, X_train, X_test, y_train, y_test = naive_bayes(data_idf, output_idf)
    return check_accuracy(bayes_received_model, X_test, y_test)
def connect_everything_knn(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame(vectors)
    knn_received_model, X_train, X_test, y_train, y_test = knn_model(data_idf, output_idf)
    return check_accuracy(knn_received_model, X_test, y_test)

def check_accuracy_documents_bayes_idf(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes(d, True))
    average_bayes_idf = sum(accuracies)/len(accuracies)
    print("Bayes idf average: " + str(average_bayes_idf))
def check_accuracy_documents_bayes_no_idf(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes(d, False))
    average_bayes_no_idf = sum(accuracies)/len(accuracies)
    print("Bayes no idf average: " + str(average_bayes_no_idf))

def check_accuracy_documents_knn_idf(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_knn(d, True))
    average_knn_idf = sum(accuracies)/len(accuracies)
    print("Knn idf average: " + str(average_knn_idf))
def check_accuracy_documents_knn_no_idf(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_knn(d, True))
    average_knn_no_idf = sum(accuracies)/len(accuracies)
    print("Knn no idf average: " + str(average_knn_no_idf))


def check_if_sentence_in_summary(d: Document, sentence: str) -> bool:
    b = re.sub(r'[^a-zA-Z]', '', sentence.lower())
    return b in d.referenceSummary



# question 3 methods


def connect_everything_knn_position(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame_just_position(vectors)
    knn_received_model, X_train, X_test, y_train, y_test = knn_model(data_idf, output_idf)
    return check_accuracy(knn_received_model, X_test, y_test)

def connect_everything_knn_cosine(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame_just_cosine(vectors)
    knn_received_model, X_train, X_test, y_train, y_test = knn_model(data_idf, output_idf)
    return check_accuracy(knn_received_model, X_test, y_test)

def connect_everything_bayes_position(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame_just_position(vectors)
    bayes_received_model, X_train, X_test, y_train, y_test = naive_bayes(data_idf, output_idf)
    return check_accuracy(bayes_received_model, X_test, y_test)
def connect_everything_bayes_cosine(d: Document, idf):
    vectors = feature_extraction_tf_idf(d, idf)
    (data_idf, output_idf) = map_vectors_to_data_frame(vectors)
    bayes_received_model, X_train, X_test, y_train, y_test = naive_bayes(data_idf, output_idf)
    return check_accuracy(bayes_received_model, X_test, y_test)


def check_accuracy_documents_bayes_idf_position(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes_position(d, True))
    average_bayes_idf = sum(accuracies)/len(accuracies)
    print("Bayes idf average position: " + str(average_bayes_idf))
def check_accuracy_documents_bayes_idf_cosine(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes_cosine(d, True))
    average_bayes_no_idf = sum(accuracies)/len(accuracies)
    print("Bayes no idf average cosine: " + str(average_bayes_no_idf))

def check_accuracy_documents_bayes_no_idf_position(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes_position(d, False))
    average_bayes_idf = sum(accuracies)/len(accuracies)
    print("Bayes idf average position: " + str(average_bayes_idf))
def check_accuracy_documents_bayes_no_idf_cosine(docs: [Document]):
    accuracies = []
    for d in docs:
        accuracies.append(connect_everything_bayes_cosine(d, False))
    average_bayes_no_idf = sum(accuracies)/len(accuracies)
    print("Bayes no idf average cosine: " + str(average_bayes_no_idf))