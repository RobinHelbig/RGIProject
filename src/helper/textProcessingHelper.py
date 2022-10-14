import re
import string

import nltk
from nltk import pos_tag, Tree
from nltk.corpus import stopwords

def getSentences(text: str) -> [str]:
    sentences = nltk.sent_tokenize(text)
    return sentences


def extract_np(psent):
    for subtree in psent.subtrees():
        if subtree.label() == 'NP':
            yield ' '.join(word for word, tag in subtree.leaves())


def getTerms(text: str, preprocessing: bool) -> list[str]:
    words = nltk.word_tokenize(text)

    if preprocessing:
        regexp = re.compile(r'[a-zA-Z0-9]')
        # print("before", words)
        # remove punctuation
        words = list(filter(lambda word: regexp.search(word), words))

        # noun phrases
        noun_phrases = list()
        cp = nltk.RegexpParser("NP: {(<V\w+>|<NN\w?>)+.*<NN\w?>}")
        chunked = cp.parse(pos_tag(words))

        leaves = list()
        for subtree in chunked.subtrees(filter=lambda t: t.label() == 'NP'):
            leaves.append(subtree.leaves())

        for leaf in leaves:
            term = " ".join([w for w, t in leaf])
            noun_phrases.append(term)

        # bigrams
        bigrams = list(nltk.bigrams(words))
        words += [' '.join(e) for e in bigrams]

        words += noun_phrases

        # make words lower case
        for i in range(len(words)):
            words[i] = words[i].lower()
    return words
