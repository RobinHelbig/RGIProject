import nltk
import re


def extract_sentences(original_text):
    text = re.sub(r'(\d+\.\d+|\b[A-Z](?:\.[A-Z])*\b\.?)|([.,;:!?)])\s*', lambda x: x.group(1) or f'{x.group(2)} ',
                  original_text)
    tokens = nltk.sent_tokenize(text)
    return tokens
