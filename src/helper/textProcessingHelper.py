import nltk
from typing import List

def getSentences(text: str) -> List[str]:
    return nltk.sent_tokenize(str)


def getTokens(text: str, preprocessing: bool) -> List[str]:
    words = nltk.word_tokenize(text)

    if preprocessing:
        #bigrams
        bigrams = nltk.bigrams(words)
        words.append(bigrams)

        #noun phrases

    return words
