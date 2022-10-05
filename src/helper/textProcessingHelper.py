import nltk


def getSentences(text: str) -> [str]:
    return nltk.sent_tokenize(str)


def getTokens(text: str, preprocessing: bool) -> [str]:
    words = nltk.word_tokenize(text)

    if preprocessing:
        #bigrams
        bigrams = nltk.bigrams(words)
        words.append(bigrams)

        #noun phrases

    return words
