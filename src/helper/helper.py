import nltk
import re
import csv



def extract_sentences(original_text):
    text = re.sub(r'(\d+\.\d+|\b[A-Z](?:\.[A-Z])*\b\.?)|([.,;:!?)])\s*', lambda x: x.group(1) or f'{x.group(2)} ',
                  original_text)
    tokens = nltk.sent_tokenize(text)
    return tokens

def write_to_csv(file_name, header, data):
    with open(f'${file_name}', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)

        writer.writerows(data)