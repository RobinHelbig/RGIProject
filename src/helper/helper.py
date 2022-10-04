import nltk
import re


def extract_sentences(path):
    with open(path) as doc:
        file = doc.read()
        text = re.sub(r'(\d+\.\d+|\b[A-Z](?:\.[A-Z])*\b\.?)|([.,;:!?)])\s*', lambda x: x.group(1) or f'{x.group(2)} ',
                      file)
        tokens = nltk.sent_tokenize(text)
    return tokens
