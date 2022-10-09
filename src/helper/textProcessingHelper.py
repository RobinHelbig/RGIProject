import string

import nltk
from nltk import pos_tag, Tree
from nltk.corpus import stopwords

def getSentences(text: str) -> [str]:
    sentences = nltk.sent_tokenize(text)
    return sentences


def getTerms(text: str, preprocessing: bool) -> list[str]:
    words = nltk.word_tokenize(text)

    if preprocessing:
        #remove punctuation
        words = list(filter(lambda token: token not in string.punctuation, words))
        #noun phrases
        cp = nltk.RegexpParser("NP: {(<V\w+>|<NN\w?>)+.*<NN\w?>}")
        chunked = cp.parse(pos_tag(words))

        continuous_chunk = []
        current_chunk = []

        for subtree in chunked:
            if type(subtree) == Tree:
                current_chunk.append(" ".join([token for token, pos in subtree.leaves()]))
            elif current_chunk:
                named_entity = " ".join(current_chunk)
                if named_entity not in continuous_chunk:
                    continuous_chunk.append(named_entity)
                    current_chunk = []
            else:
                continue

        #remove stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w.lower() in stop_words]

        #bigrams
        bigrams = list(nltk.bigrams(words))
        words += [' '.join(e) for e in bigrams]

        words += continuous_chunk
    return words
