import nltk


def getSentences(text: str) -> [(int, str)]:
    indexed_sentences = list()
    sentences = nltk.sent_tokenize(text)
    for i in range(0, len(sentences)):
        indexed_sentences.append((i, sentences[i]))

    return indexed_sentences


def getTerms(text: str, preprocessing: bool) -> list[str]:
    words = nltk.word_tokenize(text)

    if preprocessing:
        #bigrams
        bigrams = nltk.bigrams(words)
        words.append(bigrams)

        #noun phrases

    return words
